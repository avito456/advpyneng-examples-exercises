import json

with open('sw_templates.json') as f:
    templates = json.load(f)

#print(templates.access)
print(templates)

for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))