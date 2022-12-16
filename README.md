# erdos

### quickstart:

```bash
npm run build # from ./frontend/
docker compose up
```

swagger is @ hostname/docs

### todo remove: dirty hack to populate db
- put .csv file next to erdos/backend/app/dataloader.py
- docker compose up --build
- connect to backend container and start dataloader.py

### dependency workflow:

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
