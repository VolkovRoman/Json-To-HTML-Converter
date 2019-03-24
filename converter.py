import json
import sys

file_open = open(r'source/source.json', mode='r', encoding='Latin-1')
json_data = json.load(file_open)


def json_to_html():
    dict_tags = []  # Create an empty dictionary
    for tag in json_data:  # Appending to dictionary formatted data from json file
        dict_tags.append('<li>')  # Adding tag '<li>' in the start of the item
        for keys in tag.keys():  # Adding another 'for', that allows to use this converter with any tags
            dict_tags.append('<'+keys+'>' + tag[keys] + '</'+keys+'>')
        dict_tags.append('</li>')  # Adding tag '</li>'in the end of the item

    # Adding tags '<ul>' and '</ul>' in the same way
    dict_tags.insert(0, '<ul>')
    dict_tags.insert(len(dict_tags), '</ul>')

    output_data = (''.join(dict_tags))  # Merging formatted items into a string

    sys.stdout.write(output_data)  # Output to stdout

    return str(output_data)  # This needs for test because without what line function returns none


json_to_html()
