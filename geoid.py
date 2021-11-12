f = open('1000_largest_cities.txt', 'r')

print(type(f))


content = f.read()

print(type(content))
cities = content.split(',')[1::4]
state = content.split(',')[2::4]

index = 0


print(set(cities))


def listOfDuplicates(list):
    duplicates = []
    for i in range(0,len(list)):
        if(list[i].count(list[i]) > 1):
            duplicates.append(list[i])
    return duplicates

print(listOfDuplicates(cities))