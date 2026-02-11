def separate_keys_values(data):
    keys = list(data.keys())
    values = list(data.values())
    return keys, values


details = {
    "id": 101,
    "name": "Anita",
    "dept": "CSE"
}

k, v = separate_keys_values(details)
print("Keys:", k)
print("Values:", v)
