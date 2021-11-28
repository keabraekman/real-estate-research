states_abbreviations = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'dc', 'fl', 'ga', 
'hi', 'ia', 'id', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'me', 'mi', 
'mn', 'mo', 'ms', 'mt', 'nc', 'nd', 'ne', 'nh', 'nj', 'nm', 'nv', 'ny', 'oh', 
'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'va',
'vt', 'wa', 'wi', 'wv', 'wy']

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 
'Connecticut', 'Delaware', 'district-of-columbia', 'Florida', 'Georgia', 
'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 
'Louisiana', 'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 
'Missouri', 'Mississippi', 'Montana', 'North-Carolina', 'North-Dakota', 
'Nebraska', 'New-Hampshire', 'New-Jersey', 'New-Mexico', 'Nevada', 'New-York', 
'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode-Island', 'South-Carolina', 
'South-Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont',
'Washington', 'Wisconsin', 'West-Virginia', 'Wyoming']

# states_abbreviations = ['al']

url_segments = []
for i in range(len(states_abbreviations)):
    file_name = states_abbreviations[i] + '.txt'
    geoid_open = open(file_name,'r')
    geoid = geoid_open.read()
    geoid_split = geoid.split('|')

    places = geoid_split[3::6]
    state_ids = geoid_split[1::6]
    place_ids = geoid_split[2::6]
    state = states[i]

    for j in range(len(places)):
        url_segments.append('https://www.homearea.com/place/' + places[j].replace(' ', '-') + '-' + state + '/' + state_ids[j] + place_ids[j])

# https://www.homearea.com/place/yoder-town-wyoming/5686665/

print("\n".join(url_segments))
print(len(url_segments))
    


# content2 = open('ak.txt','r')
# content = content2.read()
# print(content)