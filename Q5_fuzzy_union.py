# Question 5: Consider a universe representing room temperature in degree C and 
# other universe representing relative humidity given by:
# T = 0.4/16 + 0.8/18 + 1.0/20 + 1.0/22 + 0.8/24 + 0.5/26
# H = 0.2/0 + 0.8/20 + 1.0/40 + 0.6/60 + 0.2/80
# Calculate the membership of "Acceptable Temperature OR Acceptable Humidity"

T = {16: 0.4, 18: 0.8, 20: 1.0, 22: 1.0, 24: 0.8, 26: 0.5}
H = {0: 0.2, 20: 0.8, 40: 1.0, 60: 0.6, 80: 0.2}

print("Acceptable Temperature OR Acceptable Humidity (Union)")
print("-" * 55)
print(f"{'Temperature':<15} {'Humidity':<15} {'Union Membership (max)'}")
print("-" * 55)

for t_val, t_mu in T.items():
    for h_val, h_mu in H.items():
        union_mu = max(t_mu, h_mu)
        print(f"T={t_val:<13} H={h_val:<13} {union_mu}")
