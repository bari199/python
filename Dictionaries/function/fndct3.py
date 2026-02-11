def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

print(merge_dicts(dict1, dict2))
