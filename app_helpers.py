import json
import datetime
import app_utils
from pprint import pprint


def get_data(input, city):
    if 'https' in input:
        temp = app_utils.fetch_data(input)
    else:
        temp = get_input(f'./raw_results/{input}')
    results = parse_results(temp)
    output(results, city)
    return results


def get_input(file):
    with open(file, encoding='utf-8-sig') as f:
        data = json.load(f)
    return data


def output(dic, city):
    now = datetime.datetime.now()
    suffix = f'{now.hour}{now.minute}'
    with open(f'./parsed_results/data_{city}_{suffix}.json', 'w') as outfile:
        json.dump(dic, outfile, sort_keys=True, indent=4)


def parse_results(input_json):
    new_results = []
    temp = input_json['areaResults']
    for item in temp:
        for k,v in item.items():
            new_dict = {}
            new_dict['id'] = k
            new_dict['statistics'] = v['statistics']
            new_dict['results'] = v['contestResults'][0]
            new_dict['race'] = new_dict['results']['contestName']
            new_results.append(new_dict)
    new_dict = {'stats': input_json['statistics'], 'races': new_results}
    return new_dict


# {
#   'stats' : xxxx
#   'races': [
#     {
#       'results': [],
#       'statistics' : {}
#       'id' : 'x',
#       'race': 'xxxxx'
#     },
#     {},
#     {},
#   ]
# }

races = {
    '1': 'Mayor',
    '3': 'Ward 1',
    '4': 'Ward 2',
    '5': 'Ward 3',
    '6': 'Ward 4',
    '7': 'Ward 5',
    '8': 'Ward 6',
    '9': 'Ward 7',
    '10': 'Ward 8',
    '11': 'Ward 9',
    '12': 'Ward 10',
    '13': 'Ward 11',
    '14': 'Ward 12',
    '15': 'Ward 13',
    '16': 'Ward 14',
    '17': 'Ward 15',
    '18': 'Trustee, Hamilton-Wentworth District School Board Wards 1 & 2',
    '19': 'Trustee, Hamilton-Wentworth District School Board Ward 3',
    '20': 'Trustee, Hamilton-Wentworth District School Board Ward 4',
    '21': 'Trustee, Hamilton-Wentworth District School Board Ward 5',
    '22': 'Trustee, Hamilton-Wentworth District School Board Ward 6',
    '23': 'Trustee, Hamilton-Wentworth District School Board Ward 7',
    '24': 'Trustee, Hamilton-Wentworth District School Board Wards 8 & 14',
    '25': 'Trustee, Hamilton-Wentworth District School Board Ward 9 & 10',
    '26': 'Trustee, Hamilton-Wentworth District School Board Ward 11 & 12',
    '27': 'Trustee, Hamilton-Wentworth District School Board Ward 13',
    '28': 'Trustee, Hamilton-Wentworth District School Board Ward 15',
    '29': 'Trustee, Hamilton-Wentworth Catholic District School Board Wards 1, 2 & 15',
    '30': 'Trustee, Hamilton-Wentworth Catholic District School Board Wards 3 & 4',
    '31': 'Trustee, Hamilton-Wentworth Catholic District School Board Ward 5',
    '32': 'Trustee, Hamilton-Wentworth Catholic District School Board Ward 6',
    '33': 'Trustee, Hamilton-Wentworth Catholic District School Board Ward 7',
    '34': 'Trustee, Hamilton-Wentworth Catholic District School Board Wards 8 & 14',
    '35': 'Trustee, Hamilton-Wentworth Catholic District School Board Wards 9 & 11',
    '36': 'Trustee, Hamilton-Wentworth Catholic District School Board Ward 10',
    '37': 'Trustee, Hamilton-Wentworth Catholic District School Board Wards 12 & 13',
    '38': 'Trustee, Conseil scolaire catholique MonAvenir - French Catholic'
}