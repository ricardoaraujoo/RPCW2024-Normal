import json

# Load the JSON data
with open('pg54190.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Write the data back to a new JSON file to decode Unicode sequences
with open('formatted_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Unicode sequences decoded and JSON formatted.")
