import json

f = open('../1000_largest_cities.txt', 'r')
content = f.read()
# print(content)

cities = content.split(',')[1::4]
states = content.split(',')[2::4]

# print(cities)


g = open('export2/data.json', 'r')
export = json.load(g)


print(type(export))


# cities_exported = export.split