import yaml
data = '''
goals:
  daily:
  - routine:
    - morning review: done
    - brush and floss 2 times: changing to "after every meal"
    - do the exercise routine: done
    - eat no more than one meal: done
    - evening plan: done
  - tasks:
    - task1: in progress
    - task2: not started
    - task3: completed
'''
parsed_data = yaml.safe_load(data)
table = []
for item in parsed_data['goals']['daily']:
    if isinstance(item, dict):
        for key, value in item.items():
            if isinstance(value, list):
                first = True
                for sub_dict in value:
                   for sub_key, sub_value in sub_dict.items():
                        pk = ''
                        if first:
                            op = " ." + str(len(list(value))) + "+"
                            first = False                            
                        table.append([op, key, sub_key, sub_value])
                        op = ''
                        key= ''
print()                        
print ("|===")
for row in table:
    if row[0]:
        print("{}|{}|{}|{}".format(row[0], row[1], row[2], row[3]))
    else:
         print("|{}|{}".format(row[2], row[3]))
print ("|===")