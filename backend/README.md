### FastAPI + Postgres

Simple Backend for manage blood donations.

### Installation

```
pip install -r requirements.txt
```

### DB

Set your environment variables following `.env.example` file:

```
POSTGRES_HOST=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
POSTGRES_PORT=
```

Then run:

```
docker compose up -d
```

You can access to the database using `psql`:

```
psql -U postgres -W -h localhost -p 5252 -d bloodsystem
```
