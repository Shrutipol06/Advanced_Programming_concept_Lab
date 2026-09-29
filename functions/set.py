s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print("SET:", s1)

# 1. add() - adds an element
s1.add(50)
print("1. add:", s1)

# 2. remove() - removes an element
s1.remove(20)
print("2. remove:", s1)

# 3. discard() - removes an element safely
s1.discard(10)
print("3. discard:", s1)

# 4. pop() - removes a random element
s1.pop()
print("4. pop:", s1)

# 5. union() - combines two sets
print("5. union:", s1.union(s2))

# 6. intersection() - common elements
print("6. intersection:", s1.intersection(s2))

# 7. difference() - elements only in first set
print("7. difference:", s1.difference(s2))

# 8. symmetric_difference() - elements not common
print("8. symmetric difference:",
      s1.symmetric_difference(s2))

# 9. issubset() - checks if one set is subset
print("9. issubset:", s1.issubset(s2))

# 10. issuperset() - checks if one set contains another
print("10. issuperset:", s1.issuperset(s2))