data = {'name': 'sisi', 'age': 22, 'sex': '0', 'address': '22', 'school': 'ww:hasnk:ad', 'experience': 'wwe',
        'evaluation': 'ee', 'user_id': 10}
list = []
for k,v in data.items():
        list.append("'%s'"%k+'='+"'%s'"%v)

print(list)
