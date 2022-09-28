# erdos

dependency workflow:
- if not already installed: `pip install pip-tools`
- add dependency to pyproject.toml
- run `compile.sh`
- if you need dependencies locally: `pip install -r requirements.txt`