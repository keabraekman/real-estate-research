import pickle


geoid_array = pickle.load(open('geoid-array.pickle', 'rb'))
place_array = pickle.load(open('place-array.pickle', 'rb'))
state_array = pickle.load(open('state-array.pickle', 'rb'))
url_array = pickle.load(open('url-array.pickle', 'rb'))

# We want to get the unique indices in url since it's our partition key
# then transform all the arrays based on this list

def unique_indices(list):
    indices = []
    for i in range(len(list)):
        if(list[i] not in indices):
            indices.append(i)
    return indices

indices_to_keep = unique_indices(url_array)

def list_without_duplicates(list, indices_to_keep):
    new_list = []
    for i in range(len(indices_to_keep)):
        new_list.append(list[i])
    return new_list

def export_new_list_to_pickle(filename, new_list):
    print('exporting : ', filename)
    pickle.dump(new_list, open(filename, 'wb'))


export_new_list_to_pickle('url-array.pickle', list_without_duplicates(url_array, indices_to_keep))
export_new_list_to_pickle('state-array.pickle', list_without_duplicates(state_array, indices_to_keep))
export_new_list_to_pickle('place-array.pickle', list_without_duplicates(place_array, indices_to_keep))
export_new_list_to_pickle('geoid-array.pickle', list_without_duplicates(geoid_array, indices_to_keep))

