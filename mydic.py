getage = {"a": 24, "b":2, "x": 43, "y": 20}

ages = list(getage.values())
maxage = max(ages)
print(maxage)
for i in getage:
    if getage.get(i) == maxage:
        print(i)
