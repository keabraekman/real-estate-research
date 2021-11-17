import json

f = open('../1000_largest_cities.txt', 'r')
content = f.read()
# print(content)

cities = content.split(',')[1::4]
states = content.split(',')[2::4]

# print(len(cities))

g = open('export3/export.json', 'r')
export = json.load(g)


exported_cities = []
for i in range(len(export['Items'])):
    print('export city = ', export['Items'][i]['city-name']['S'])
    exported_cities.append(export['Items'][i]['city-name']['S'])


result_cities = []
result_indexes = []
# for index, c in enumerate(cities):
#     print('index = ', index)
#     print(exported_cities.count(c))
    # print('c = ', c)
    # if(c not in exported_cities):
    #     result_cities.append(c)
    #     result_indexes.append(index)

for index, c in enumerate(exported_cities):
    # print('index = ', index)
    # print(cities.count(c))
    if(cities.count(c) > 1):
        print(index, ' ', c, ' ', cities.count(c))
        
# print('Missing cities = ', result_cities)
# print(len(result_cities))



# cities_exported = export.split



