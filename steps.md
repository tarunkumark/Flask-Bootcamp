# Prerequisites
```
    PostgreSQL
    Python >=3.7
    python venv -> pip install virtualenv
    VSCode
    (Optional)PGAdmin4 for viewing db 
```


# Setting up the app

``` mkdir flask-postgres 
    cd flask-postgres
    python -m venv env
    env/Scripts/activate(for windows)
    source env/bin/activate(for linux/macOS)
    pip install flask Flask-SQlAlchemy psycopg2
```

# Creating a database with psql

## Opening the psql CLI
### For windows
```
psql -u postgres -w
```

### For Linux/macOS
```
sudo -u postgres psql
```

# To run the server

## Create all tables in DB(linux/macOS)
```
export FLASK_APP=app
export FLASK_en=development
flask shell
```

## Create all tables in DB(linux/macOS)
```
SET FLASK_APP=app
SET FLASK_en=development
flask run
```
## Inside the shell
```
from app import db
db.create_all()
```
## Run the server
```
flask run
```
# Fetch updated code
```
git pull
```
# Push updated code
```
git commit -am "message"
git push origin main
```