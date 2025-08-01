dict3 = {
    'c': 19,
    'b': 76,
    'h': {'f': [12, 67, 667, 88]},
    'a': {'c': 71, 'a': 100, 'b': 98, 'd': 87, 'k': 50},
    'p': {'o': 100}
}


def contains_value(d, target):
    if isinstance(d, dict):
        for value in d.values():
            if contains_value(value, target):
                return True
    elif isinstance(d, list):
        for item in d:
            if contains_value(item, target):
                return True
    else:
        return d == target
    return False


print(contains_value(dict3, 88))  # Output: True

def contains_value1(data, target):
    # If it's a dictionary, go through all its values
    if type(data) is dict:
        for value in data.values():
            if contains_value1(value, target):
                return True

    # If it's a list, go through all its items
    elif type(data) is list:
        for item in data:
            if contains_value1(item, target):
                return True

    # If it's not a dict or list, check the value directly
    else:
        if data == target:
            return True

    return False
print(contains_value1(dict3, 88))

def contains_value2(d,target):
    if isinstance(d,dict):
        for i in d.values():
            if contains_value2(i,target):
                return True

    elif isinstance(d,list):
        for i in d:
            if contains_value2(i,target):
                return True
    else:
        if d == target:
            return True
    return False


print(contains_value2(dict3, 88))

