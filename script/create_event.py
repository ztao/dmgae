import json

with open('event_template.json', 'r+') as event_file:
	event = json.loads(event_file.read())