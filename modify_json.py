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
        entry['place'] = data[i]['place'][j]
        entry['photocount'] = data[i]['photocount'][j]
        obj.append(entry)

print (len(obj))
print obj
