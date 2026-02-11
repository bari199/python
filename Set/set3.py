def find_intersection(set1,set2):
    result = set1.intersection(set2)
    return result

a={1,2,3,4,5}
b={4,5,6,7,8}

common = find_intersection(a,b)
print("Intersection:", common)
