# import yaml
from ruamel.yaml import YAML

from api.main import app

# yaml_schema = yaml.dump(app.openapi(), Dumper=yaml.CDumper)
# with open("openapi_schema.yaml", "w") as file:
#     file.write(yaml_schema)

# これで行けた
yaml = YAML()
# with open("openapi_schema_random.yaml", "w") as file:
# yaml.dump(
#     app.openapi(), file, Dumper=yaml.CDumper, default_flow_style=False, encoding=("utf-8"), allow_unicode=True
# )
# yaml.dump(app.openapi(), file)
with open("openapi_schema.yaml", "w") as file:
    yaml.dump(app.openapi(), file)
    # yaml.dump({"a": [1, 2]}, file)

# versionの明記があるはず
# エンコードがうまくいかない

# なければデフォルトにする
# openapi: "3.0.3"
# info:
#   version: 0.1.0
#   title: FastPCD
#   description: A cloud server that helps akari members' developments

#
# import json

# schema = json.dumps(app.openapi())
# yaml_schema = yaml.dump(schema)
# # yaml_schema = yaml.dump(app.openapi(), Dumper=yaml.CDumper)
# with open("openapi_schema_raw.yaml", "w") as file:
#     file.write(yaml_schema)
