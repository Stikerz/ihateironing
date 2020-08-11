## Getting Started

This project was written using python3.7. A pip requirements.txt
 file is
 included to install the dependencies

## Running with Docker
- A Docker Compose file is provided that will run the application in an
 isolated environment

- Make sure you have `docker & docker-compose` installed and that the Docker
 daemon is running
 
- Build & Run the image: `docker-compose up --build`

- Start using web app: `http://http://127.0.0.1:8000/`

## Project Structure Notes

- The Backend Django Rest Framework  are stored in the `winterfell/drycleaning
` folder
- Project uses Postgres with DB info hardcoded  in `winterfell/settings` for
 dev purposes only ( store sensitive data are either with environment
  variables or via a json file in production)
- Currently API is for retrieving only as instructed with task
- Django server 'runserver' for dev purposes only, server such a gunicorn for
 prod
 - fixtures to load database with initial data (use tool such celery for prod) 

## API Endpoints
- Retrieve Orders : /drycleaning/orders/ 
- Retrieve Items : /drycleaning/items/
- Retrieve LineItems : /drycleaning/lineitems/?search=<order_id>

## Testing
- Run python manage.py test winterfell.tests drycleaning/tests/ # Run test


## Coverage 

```

Name                              Stmts   Miss  Cover   Excluded
---------------------------------------------------------------
drycleaning/__init__.py	              0	     0	 100%    0
drycleaning/admin.py	              1	     0	 100%    0
drycleaning/models.py	              33     0	 100%    4
drycleaning/serializers.py	      19     0	 100%    0
drycleaning/tests/test_models.py      34     0	 100%    0
drycleaning/tests/test_views.py	      52     0	 100%    0
drycleaning/urls.py	              3	     0	 100%    0
drycleaning/views.py	              15     0	 100%    0
winterfell/__init__.py	              0	     0	 100%    0
winterfell/settings.py	              18     0	 100%    0
winterfell/tests.py	              7      0	 100%    0
winterfell/urls.py	              4	     0	 100%    0
winterfell/views.py	              4	     0	 100%    0
---------------------------------------------------------------
TOTAL                               190      0   100%   4

```
