from ruamel.yaml import YAML

from api.main import app

yaml = YAML()
with open("openapi_schema_test.yaml", "w") as file:
    yaml.dump(app.openapi(), file)
