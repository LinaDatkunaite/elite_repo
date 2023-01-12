# JSON - java script object notation
# JSON - Python: null = NONE, object - dict, array - list
# load/loads ir dump/ dumps methodai 4 loads/dumps - stringas
import json
import requests

# data = '''{
#   "student": [
#
#      {
#         "id":"01",
#         "name": "Tom",
#         "lastname": "Price"
#      },
#      {
#         "id":"02",
#         "name": "Nick",
#         "lastname": "Thameson"
#      }
#   ]
# }'''
#
# data_dict = json.loads(data)
# print(data_dict)
# print(type(data_dict))
#
#
# for student in data_dict['student']:
#     print(student)

# dump intend=2, sort_keys=Ture

import json

with open('JSON_uzduotys.json', 'r') as f:
    data = json.load(f)
color_list=[]
print(data)
new_dict={}
for item in data['colors']:
    color =item['color']
    print(color)
    rgb = item['code']['rgba']
    rgb = ', '.join(str(x) for x in rgb[0:-1])
    print(rgb)
    hex = item['code']['hex']
    print(hex)
    new_dict.update({'color': color,'rgb': rgb,'hex': hex})
    print(new_dict)
    color_list.append(new_dict)
print(color_list)
new_dict={'colors': color_list}
print(new_dict)

with open('json_done.json', 'w') as f:
    json.dump(new_dict,f ,indent=2)

