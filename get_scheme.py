import json

import yaml

from api.main import app

yaml_schema = yaml.dump(app.openapi(), Dumper=yaml.CDumper)
with open("openapi_schema.yaml", "w") as file:
    file.write(yaml_schema)
