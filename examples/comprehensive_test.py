# Comprehensive test for the mathsym runner
import mathsym

print("--- Comprehensive Symbol Test ---")

# 1. Basic Math & Constants
print("\n[1] Testing Basic Math...")
radius = 7
circumference = 2 × π × radius
area = π * radius²
print(f"Circumference (r=7): {circumference}")
print(f"Area (r=7): {area}")

# 2. Relational Operators from Algebra
print("\n[2] Testing Relational Operators...")
x = 100
y = 100
z = 50
print(f"Is {x} ≠ {z}? {x ≠ z}")
print(f"Is {x} ≤ {y}? {x ≤ y}")

# 3. Set Theory
print("\n[3] Testing Set Theory...")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union_set = set_a ∪ set_b
intersection_set = set_a ∩ set_b
print(f"Union of {set_a} and {set_b}: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Is 5 ∈ union_set? {5 ∈ union_set}")
print(f"Is 10 ∉ union_set? {10 ∉ union_set}")
print(f"Is ∅ a subset of set_a? {∅ ⊆ set_a}")


print("\n--- Tests Complete ---") 