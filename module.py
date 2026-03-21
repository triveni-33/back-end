import math
print(math.sqrt(25)) # Square root → 5.0
print(math.pow(2, 4))# 2^4 → 16.0
print(math.factorial(5))# 5! → 120
print(math.gcd(12, 18)) # GCD → 6
print(math.floor(3.7))# → 3
print(math.ceil(3.2))# → 4
print(math.trunc(3.9)) # → 3
print(math.log(10))   # Natural log
print(math.log10(100))  # Log base 10 → 2.0
print(math.exp(2))  # e^2
print(math.fabs(-5.6))# Absolute value → 5.6

import datetime
d = datetime.date(2025, 8, 30)
t=datetime.time(11,20,5)
print(d.year)
print(d.month)
print(d.day)
print(t.hour)
print(t.minute)
print(t.second)

a = [10, 20, 30, 40, 50]
count = 0
for i in a:
    count = count + 1

print(count)