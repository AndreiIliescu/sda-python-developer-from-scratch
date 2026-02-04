import json

# file = open('test.txt', 'w')

# file.close()

# with open('test.txt', 'r') as file:
#     print(file.readlines())

with open('../file.json', 'w') as file:
    json.dump({'a': 1}, file)

with open('../file.json', 'r') as file:
    data = json.load(file)
    print(data)
