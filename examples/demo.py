# examples/demo.py

# Note: We don't need to 'import math' here because the
# mathsym runner provides it in the execution globals.
import mathsym

print("--- Testing Math Symbols ---")

# Test 1: Area of a circle with radius 10
radius = 10
area = π * radius²
print(f"Area of a circle with r={radius}: {area}")
# Expected output should be near 314.159

# Test 2: Pythagorean theorem
a = 3
b = 4
c = √(a² + b²)
print(f"Hypotenuse for a=3, b=4: {c}")
# Expected output should be 5.0

# Test 3: Relational operators
val1 = 10
val2 = 20
if val1 ≠ val2:
    print(f"{val1} is not equal to {val2}, as expected.")
else:
    print(f"ERROR: {val1} was equal to {val2}")

print("--- Tests Complete ---") 