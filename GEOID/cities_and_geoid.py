import pickle 

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


def url_array():
    url_array = []
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
            url_array.append('https://www.homearea.com/place/' + places[j].replace(' ', '-') + '-' + state + '/' + state_ids[j] + place_ids[j])        
    with open('url-array.pickle', 'wb') as handle:
        pickle.dump(url_array, handle, protocol=pickle.HIGHEST_PROTOCOL)



url_array = pickle.load(open('url-array.pickle', 'rb'))


def place_array():
    place_array = []
    for i in range(len(states_abbreviations)):
        file_name = states_abbreviations[i] + '.txt'
        geoid_open = open(file_name,'r')
        geoid = geoid_open.read()
        geoid_split = geoid.split('|')
        places = geoid_split[3::6]
        for j in range(len(places)):
            place_array.append(places[j])
    with open('place-array.pickle', 'wb') as handle:
        pickle.dump(place_array, handle, protocol=pickle.HIGHEST_PROTOCOL)

# place_array()


def state_array():
    state_array = []
    for i in range(len(states_abbreviations)):
        file_name = states_abbreviations[i] + '.txt'
        geoid_open = open(file_name,'r')
        geoid = geoid_open.read()
        geoid_split = geoid.split('|')
        state = states[i]
        places = geoid_split[3::6]
        for j in range(len(places)):
            state_array.append(state)
    # print('state array = ', len(state_array))
    with open('state-array.pickle', 'wb') as handle:
        pickle.dump(state_array, handle, protocol=pickle.HIGHEST_PROTOCOL)

state_array()


# content2 = open('ak.txt','r')
# content = content2.read()
# print(content)