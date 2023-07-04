import yaml

from api.main import app

# yaml_schema = yaml.dump(app.openapi(), Dumper=yaml.CDumper)
# with open("openapi_schema.yaml", "w") as file:
#     file.write(yaml_schema)

# これで行けた
with open("openapi_schema.yaml", "w") as file:
    yaml.dump(app.openapi(), file, Dumper=yaml.CDumper)

# versionの明記があるはず
# エンコードがうまくいかない

# なければデフォルトにする
# openapi: "3.0.3"
# info:
#   version: 0.1.0
#   title: FastPCD
#   description: A cloud server that helps akari members' developments

#
