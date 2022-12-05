import json
from pprint import pprint

def read(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)


# pprint(read('students.json'))
# OUT:
# ...
# {'birthday': '1948-11-27T00:00:00.000000',
#   'id': 9997,
#   'name': 'Dave Robinson',
#   'room': 444,
#   'sex': 'M'},
#  {'birthday': '1972-04-12T00:00:00.000000',
#   'id': 9998,
#   'name': 'Jesus Stewart',
#   'room': 789,
#   'sex': 'F'},
#  {'birthday': '1956-11-02T00:00:00.000000',
#   'id': 9999,
#   'name': 'Savannah Phelps',
#   'room': 638,
#   'sex': 'M'}]
# pprint(read('rooms.json'))
# OUT:
# ...
# {'id': 989, 'name': 'Room #989'},
# {'id': 990, 'name': 'Room #990'},
# {'id': 991, 'name': 'Room #991'},
# {'id': 992, 'name': 'Room #992'},
# {'id': 993, 'name': 'Room #993'},
# {'id': 994, 'name': 'Room #994'},
# {'id': 995, 'name': 'Room #995'},
# {'id': 996, 'name': 'Room #996'},
# {'id': 997, 'name': 'Room #997'},
# {'id': 998, 'name': 'Room #998'},
# {'id': 999, 'name': 'Room #999'}]