import json

x = {
        "name": "Rixos The Palm Dubai",
        "position": [25.1212, 55.1535],
    }
    
y = json.dumps(x, indent=5)

print(y)