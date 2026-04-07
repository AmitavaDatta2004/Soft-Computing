# Question 3: Take different element of a fuzzy Set as user input and defuzzify using 
# Bisector of area, Centroid of area, Mean of Maximum and Smallest of maximum.

# Input fuzzy set
fuzzy_set = [(1, 0.2), (2, 0.5), (3, 0.9), (4, 0.7), (5, 0.3)]

# Centroid
num = sum(x * mu for x, mu in fuzzy_set)
den = sum(mu for _, mu in fuzzy_set)
centroid = num / den

# Bisector
total_area = den
half_area = total_area / 2
cum_area = 0
bisector = None

for x, mu in fuzzy_set:
    cum_area += mu
    if cum_area >= half_area:
        bisector = x
        break

# Mean of Maxima
max_mu = max(mu for _, mu in fuzzy_set)
max_x = [x for x, mu in fuzzy_set if mu == max_mu]
mom = sum(max_x) / len(max_x)

# Smallest of Maxima
som = min(max_x)

print("Centroid:", centroid)
print("Bisector:", bisector)
print("Mean of Maxima:", mom)
print("Smallest of Maxima:", som)
