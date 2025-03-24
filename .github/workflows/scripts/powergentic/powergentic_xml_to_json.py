import xmltodict
import json

# Read the XML file
with open("./_data/latest_posts_powergentic.xml", "r") as xml_file:
    xml_content = xml_file.read()

# Parse XML to a Python dictionary
data_dict = xmltodict.parse(xml_content)

# Convert the dictionary to JSON
json_data = json.dumps(data_dict, indent=4)

# Delete existing file
import os
if os.path.exists("./_data/latest_posts_powergentic.json"):
    os.remove("./_data/latest_posts_powergentic.json")

# Write JSON data to a file
with open("./_data/latest_posts_powergentic.json", "w") as json_file:
    json_file.write(json_data)

# Print the JSON output
print(json_data)