theList = ["apple", "banana", "orange"]
theList.sort()

for index, item in enumerate(theList):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)