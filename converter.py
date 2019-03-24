import json
import sys

file_open = open(r'source/source.json', mode='r', encoding='Latin-1')
json_data = json.load(file_open)


def json_to_html():
    dict_tags = []  # Create an empty dictionary
    for tag in json_data:  # Appending to dictionary formatted data from json file
        if tag['title']:
            dict_tags.append('<h1>' + str(tag["title"]) + '</h1>')
        if tag['body']:
            dict_tags.append('<p>' + str(tag["body"]) + '</p>')

    output_data = (''.join(dict_tags))  # Merging formatted items into a string

    sys.stdout.write(output_data)  # Output to stdout

    return str(output_data)  # This needs for test because without what line function returns none


json_to_html()
