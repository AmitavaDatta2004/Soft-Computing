# Question 6: Solve the Air Conditioner Controller Problem using Fuzzy Inference System.
# Frame the rules. Compare the result using Mamdani, Sugeno and Tsukamoto FIS.
#
# Rules (Temperature, Humidity -> Compressor Speed):
#  1) Very Low, Dry        -> Off       9)  High, Dry         -> Low
#  2) Very Low, Comfortable-> Off       10) High, Comfortable -> Medium
#  3) Very Low, Humid      -> Off       11) High, Humid       -> Fast
#  4) Very Low, Sticky     -> Low       12) High, Sticky      -> Fast
#  5) Low, Humid           -> Low       13) Very High, Dry    -> Medium
#  6) Low, Comfortable     -> Off       14) Very High, Comfortable -> Fast
#  7) Low, Humid           -> Low       15) Very High, Humid  -> Fast
#  8) Low, Sticky          -> Medium    16) Very High, Sticky -> Fast

import numpy as np

# ── Membership Functions ─────────────────────────────────────────────────────
def trimf(x, a, b, c):
    if x <= a or x >= c: return 0.0
    elif a < x <= b: return (x - a) / (b - a)
    else: return (c - x) / (c - b)

def trapmf(x, a, b, c, d):
    if x <= a or x >= d: return 0.0
    elif a < x <= b: return (x - a) / (b - a)
    elif b < x <= c: return 1.0
    else: return (d - x) / (d - c)

# ── Temperature MFs (0 to 50 °C) ─────────────────────────────────────────────
def temp_very_low(t): return trapmf(t, 0, 0, 10, 20)
def temp_low(t):      return trimf(t, 10, 20, 30)
def temp_high(t):     return trimf(t, 25, 35, 45)
def temp_very_high(t):return trapmf(t, 35, 45, 50, 50)

# ── Humidity MFs (0 to 100%) ──────────────────────────────────────────────────
def hum_dry(h):        return trapmf(h, 0, 0, 20, 35)
def hum_comfortable(h):return trimf(h, 25, 45, 60)
def hum_humid(h):      return trimf(h, 50, 65, 80)
def hum_sticky(h):     return trapmf(h, 70, 85, 100, 100)

# ── Fuzzify Inputs ────────────────────────────────────────────────────────────
def fuzzify(temp, hum):
    return {
        'temp': {
            'very_low': temp_very_low(temp),
            'low':      temp_low(temp),
            'high':     temp_high(temp),
            'very_high':temp_very_high(temp)
        },
        'hum': {
            'dry':         hum_dry(hum),
            'comfortable': hum_comfortable(hum),
            'humid':       hum_humid(hum),
            'sticky':      hum_sticky(hum)
        }
    }

# ── Apply Rules (Mamdani AND = min) ──────────────────────────────────────────
def apply_rules(f):
    t = f['temp']
    h = f['hum']
    rules = {
        'off':    max(min(t['very_low'], h['dry']),
                      min(t['very_low'], h['comfortable']),
                      min(t['very_low'], h['humid']),
                      min(t['low'],      h['comfortable'])),
        'low':    max(min(t['very_low'], h['sticky']),
                      min(t['low'],      h['humid']),
                      min(t['high'],     h['dry'])),
        'medium': max(min(t['low'],      h['sticky']),
                      min(t['high'],     h['comfortable']),
                      min(t['very_high'],h['dry'])),
        'fast':   max(min(t['high'],     h['humid']),
                      min(t['high'],     h['sticky']),
                      min(t['very_high'],h['comfortable']),
                      min(t['very_high'],h['humid']),
                      min(t['very_high'],h['sticky']))
    }
    return rules

# ── Output Singletons (for Sugeno / Tsukamoto) ───────────────────────────────
# Sugeno: output is a crisp singleton per rule
SINGLETONS = {'off': 0, 'low': 25, 'medium': 50, 'fast': 100}

# ── MAMDANI Defuzzification (Centroid with discrete universe) ─────────────────
def mamdani(rules):
    # Output MFs for speed (0-100)
    x = np.linspace(0, 100, 200)
    def spd_off(s):    return np.minimum(rules['off'],    np.maximum(0, 1 - np.abs(s - 0) / 12))
    def spd_low(s):    return np.minimum(rules['low'],    np.maximum(0, 1 - np.abs(s - 25) / 15))
    def spd_medium(s): return np.minimum(rules['medium'], np.maximum(0, 1 - np.abs(s - 50) / 15))
    def spd_fast(s):   return np.minimum(rules['fast'],   np.maximum(0, 1 - np.abs(s - 90) / 15))

    agg = np.maximum.reduce([spd_off(x), spd_low(x), spd_medium(x), spd_fast(x)])
    denom = np.sum(agg)
    return np.sum(x * agg) / denom if denom > 0 else 0

# ── SUGENO Defuzzification (weighted average of singletons) ──────────────────
def sugeno(rules):
    num = sum(rules[k] * SINGLETONS[k] for k in rules)
    den = sum(rules.values())
    return num / den if den > 0 else 0

# ── Main ──────────────────────────────────────────────────────────────────────
temp = float(input("Enter Temperature (0-50 °C): "))
hum  = float(input("Enter Humidity    (0-100 %): "))

f     = fuzzify(temp, hum)
rules = apply_rules(f)

print("\n--- Fuzzy Membership Values ---")
print(f"Temperature: Very Low={f['temp']['very_low']:.2f}  Low={f['temp']['low']:.2f}  High={f['temp']['high']:.2f}  Very High={f['temp']['very_high']:.2f}")
print(f"Humidity:    Dry={f['hum']['dry']:.2f}  Comfortable={f['hum']['comfortable']:.2f}  Humid={f['hum']['humid']:.2f}  Sticky={f['hum']['sticky']:.2f}")

print("\n--- Rule Firing Strengths ---")
for k, v in rules.items():
    print(f"  {k.capitalize()}: {v:.4f}")

m = mamdani(rules)
s = sugeno(rules)

print(f"\n--- Compressor Speed Output ---")
print(f"  Mamdani    : {m:.2f}  %")
print(f"  Sugeno     : {s:.2f}  %")
