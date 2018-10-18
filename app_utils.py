import json
from pprint import pprint

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


def parse_results(file):
    with open(file, encoding='utf-8-sig') as f:
        data = json.load(f)

    new_results = []
    temp = data['areaResults']

    for item in temp:
        for k,v in item.items():
            new_dict = {}
            new_dict['id'] = k
            new_dict['statistics'] = v['statistics']
            new_dict['results'] = v['contestResults'][0]
            new_dict['race'] = new_dict['results']['contestName']
            new_results.append(new_dict)

    this_object = {'stats': data['statistics'], 'races': new_results}
    # pprint(this_object)
    with open('data.json', 'w') as outfile:
        json.dump(this_object, outfile, sort_keys=True, indent=4)

    return this_object

