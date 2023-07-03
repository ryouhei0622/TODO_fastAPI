import json

import requests
import yaml

from api.main import app

# response = requests.get("http://localhost:8000/openapi.json")
# schema = response.json()
# print(response)
# print("##########################################################################################")
# print(schema)

# yaml_schema = yaml.dump(schema)
# with open("openapi_schema.yaml", "w") as file:
#     file.write(yaml_schema)

# print(type(app.openapi()))
# schema = json.dumps(app.openapi(), indent=2, ensure_ascii=False)
# print(schema)
# yaml_schema = yaml.dump(schema)
yaml_schema = yaml.dump(app.openapi(), Dumper=yaml.CDumper)
with open("openapi_schema_raw.yaml", "w") as file:
    file.write(yaml_schema)
