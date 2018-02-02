Backend DRF that manages user ads

## Usage

Running as docker containers

```bash
docker-compose build
docker-compose up -d
```

## Access the admin panel

### Create a super user:
```
docker-compose exec app bash
python manage.py createsuperuser
```

login using this link: http://localhost:8000/admin/login/


## Tests

```bash
$ docker-compose run --rm app pytest
```

or, to run a single test:

```bash
docker-compose run --rm app pytest -q -s tests/test_api.py
```
to see test coverage report:

```bash
docker-compose exec app bash
py.test --cov=app tests/

```

# **API endpoints:**

[API endpoints](API.md)


# **Data Structure:**

[Data class Diagram](data-structure.png)

