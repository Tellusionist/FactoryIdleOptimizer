import json

with open('component_settings.json') as f:
    settings = json.read(f)
    
print(settings)