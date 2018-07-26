import json

with open('quote.json') as data_file:
    data = json.load(data_file)
feedsjson = open('modified.json', 'w')

obj = []
for i in range(len(data)):
    entry = {}
    set1 = []
    for j in range(len(data[i]['title'])):
        entry['title'] = data[i]['title'][j]
        entry['updatetime'] = data[i]['updatetime'][j]
        entry['price'] = data[i]['price'][j]
        entry['photocount'] = data[i]['photocount'][j]
        entry['bedroom'] = data[i]['bedroom'][j] + data[i]['bedroom'][j + 1]
        entry['bathroom'] = data[i]['bathroom'][j] + data[i]['bathroom'][j + 1] + data[i]['bathroom'][j + 2] + \
                            data[i]['bathroom'][j + 3]
        # entry['cityaddress'] = data[i]['add1'][j]
        # entry['squareroot'] = data[i]['squareroot'][j]
        obj.append(entry)

json.dumps(obj, feedsjson)
print obj
