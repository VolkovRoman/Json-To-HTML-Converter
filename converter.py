import json
import sys

file_open = open(r'source/source.json', mode='r', encoding='Latin-1')
json_data = json.load(file_open)

def json_to_html():
    dict_tags = []  # Create an empty dictionary
    inside_item=[]  # list for 4rth task
    for element in json_data:  # Appending to dictionary formatted data from json file
        dict_tags.append('<li>')  # Adding tag '<li>' in the start of the item
        for keys in element.keys():  # Adding another 'for', that allows to use this converter with any tags
          if isinstance(element[keys], list)==True: # In case our keys are list           
            inside_item.append('<li>')  # Adding tag '<li>' in the start of the item
            for num in range(0, len(element[keys])):
              for el in element[keys][num].keys(): # 
                inside_item.append('<'+str(el)+'>' + str(element[keys][0][el]) + '</'+str(el)+'>')
              inside_item.append('</li>')  # Adding tag '</li>'in the end of the item
              #  Wrap the item in top-level tags
              inside_item.insert(0, '<ul>')
              inside_item.insert(len(inside_item), '</ul>')
              inside_item.insert(0, ('<'+str(keys)+'>'))
              inside_item.insert(len(inside_item), ('/<'+str(keys)+'>'))   
              inside_item_data = (''.join(inside_item))
              dict_tags.append(inside_item_data)  # Adding created list into the main table     
          else:
            dict_tags.append('<'+str(keys)+'>' + str(element[keys]) + '</'+str(keys)+'>')
        dict_tags.append('</li>')  # Adding tag '</li>'in the end of the item
    
    # Adding tags '<ul>' and '</ul>' in the same way
    dict_tags.insert(0, '<ul>')
    dict_tags.insert(len(dict_tags), '</ul>')

    output_data = (''.join(dict_tags))  # Merging formatted items into a string

    sys.stdout.write(output_data)  # Output to stdout

    return str(output_data)  # This needs for test because without what line function returns none


json_to_html()
