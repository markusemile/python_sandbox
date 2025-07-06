import json
file_path = "json_file_test.json"
with open(file_path, "w+") as f:
    a = {
        "users": [
            {"id": 1, "name": "patrick"},
            {"id": 2, "name": "patrice"},
            {"id": 3, "name": "paul"},

            ]
    }
    # dump() options
    #   - indent = num
    json.dump(a, f, indent=4)
    f.seek(0)
    t = json.load(f)
    print(t)
    print(type(t))

