import requests


# url = 'https://www2.census.gov/geo/docs/reference/codes/files/st01_al_places.txt'


states = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'dc', 'fl', 'ga', 'hi', 'ia', 'id', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'me', 'mh', 'mi', 'mn', 'mo', 'ms', 'mt', 'nc', 'nd', 'ne', 'nh', 'nj', 'nm', 'nv', 'ny', 'oh', 'ok', 'or', 'pa', 'pr', 'pw', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'va', 'vi', 'vt', 'wa', 'wi', 'wv', 'wy']
number = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58']

# Keeps track of numbers used
number_index = 0

# for s in states:
#     url = 'https://www2.census.gov/geo/docs/reference/codes/files/st' + number[number_index] + '_' + s + '_places.txt'
#     print('requesting : ' + url)
#     r = requests.get(url, allow_redirects=True)
#     while(r.status_code == 404):
#         number_index += 1
#         url = 'https://www2.census.gov/geo/docs/reference/codes/files/st' + number[number_index] + '_' + s + '_places.txt'
#         r = requests.get(url, allow_redirects=True)
#     text_file_name = s + '.txt'
#     open(text_file_name, 'wb').write(r.content)
#     number_index += 1




for s in states:
    for n in number:
        url = 'https://www2.census.gov/geo/docs/reference/codes/files/st' + n + '_' + s + '_places.txt'
        r = requests.get(url, allow_redirects=True)
        if not (r.status_code == 404):
            print('requesting : ' + url)
            text_file_name = s + '.txt'
            open(text_file_name, 'wb').write(r.content)
            break
