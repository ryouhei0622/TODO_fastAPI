import yaml

from api.main import app

# yaml_schema = yaml.dump(app.openapi(), Dumper=yaml.CDumper)
# with open("openapi_schema.yaml", "w") as file:
#     file.write(yaml_schema)

# これで行けた
with open("openapi_schema.yaml", "w") as file:
    yaml.dump(app.openapi(), file, Dumper=yaml.CDumper)
