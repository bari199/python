from itertools import permutations, combinations

s = "ABC"

print("Permutations:")
for p in permutations(s):
    print("".join(p))

print("\nCombinations:")
for c in combinations(s, 2):
    print("".join(c))
