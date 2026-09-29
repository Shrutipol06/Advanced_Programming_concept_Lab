f1 = frozenset([10, 20, 30, 40])
f2 = frozenset([30, 40, 50, 60])

print("\nFROZEN SET:", f1)

# 1. union()
print("1. union:", f1.union(f2))

# 2. intersection()
print("2. intersection:", f1.intersection(f2))

# 3. difference()
print("3. difference:", f1.difference(f2))

# 4. symmetric_difference()
print("4. symmetric difference:",
      f1.symmetric_difference(f2))

# 5. issubset()
print("5. issubset:", f1.issubset(f2))

# 6. issuperset()
print("6. issuperset:", f1.issuperset(f2))

# 7. isdisjoint() - checks if no common elements
print("7. isdisjoint:", f1.isdisjoint(f2))

# 8. len() - number of elements
print("8. length:", len(f1))

# 9. in - checks if element exists
print("9. 20 exists:", 20 in f1)

# 10. not in - checks if element does not exist
print("10. 100 does not exist:", 100 not in f1)
