# Question 4: Given, following rules:
# R1: If BP is high and temperature is high then health is Poor
# R2: If BP is normal and temperature is normal then health is Good
# R3: If BP is low and temperature is normal the health is Normal
# Take the value of Blood Pressure and Temp as User input and determine health.

def trapmf(x, a, b, c, d):
    if x <= a or x >= d: return 0.0
    elif a <= x <= b: return (x - a) / (b - a)
    elif b <= x <= c: return 1.0
    elif c <= x <= d: return (d - x) / (d - c)

def trimf(x, a, b, c):
    if x <= a or x >= c: return 0.0
    elif a < x <= b: return (x - a) / (b - a)
    elif b < x < c: return (c - x) / (c - b)

bp = float(input("Enter Blood Pressure: "))
temp = float(input("Enter Temperature: "))

# Fuzzify BP
bp_low = trapmf(bp, 0, 0, 60, 90)
bp_normal = trimf(bp, 80, 110, 130)
bp_high = trapmf(bp, 120, 140, 200, 200)

# Fuzzify Temperature
temp_normal = trimf(temp, 35, 37, 38)
temp_high = trapmf(temp, 37.5, 39, 45, 45)

# Rule 1: High BP and High Temp -> Poor
rule1_poor = min(bp_high, temp_high)

# Rule 2: Normal BP and Normal Temp -> Good
rule2_good = min(bp_normal, temp_normal)

# Rule 3: Low BP and Normal Temp -> Normal
rule3_normal = min(bp_low, temp_normal)

# Simple Centroid Defuzzification (singletons: Poor=20, Normal=50, Good=80)
total_weight = rule1_poor + rule2_good + rule3_normal

if total_weight > 0:
    health_score = (rule1_poor * 20 + rule3_normal * 50 + rule2_good * 80) / total_weight
    print(f"\nRule Firing Strengths:")
    print(f"Poor: {rule1_poor}")
    print(f"Normal: {rule3_normal}")
    print(f"Good: {rule2_good}")
    print(f"\nDetermined Health Score: {health_score:.2f}")
else:
    print("Health Status is undefined for this input.")
