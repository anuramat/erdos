# erdos

dependency workflow:
- install pip-tools:
```bash
pip install pip-tools
```

- add dependency to `pyproject.toml`

- compile requirements:
```bash
pip-compile -o requirements.txt pyproject.toml
```

- if you need dependencies locally:
```bash
pip install -r requirements.txt
```