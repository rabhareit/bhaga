# Bhaga (DEPRECATED)

This is slackbot which I had been using(needs python `3.6.7` or higher).

## How to use

1. Clone this repository.

```shell
git clone https://github.com/rabhareit/bhaga.git
```

2. Install required packages.

If you use poetry, run below.
```shell
poetry install
```

If not, see `pyproject.toml` or `requirements.txt`.

3. Prepare Database. Table structure is defined in `static/sql/init.sql`

4. Make configure file of your sql as `mysql.ini` on root of this project.

```mysql.ini
[sql]
host={host address}
port={port}
user={username}
password={password}
database={database name}
```

5. Configure your slack workspace info to `config.ini` on root of this project.

```config.ini
[slack]
verification_token={your verification token}
BOT_USER_OAUTH_ACCESS_TOKEN={your access token}
```

6. Run main script.

```shell
python run.py
```
