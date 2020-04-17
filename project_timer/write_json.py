import json

f_name = "first name"
l_name = "last name"

result = [{"f_name": f_name, "l_name": l_name}]

with open("file.json", "w", encoding="utf-8") as f:
    # Write it to file
    json.dump(result, f, ensure_ascii=False, indent=4)
