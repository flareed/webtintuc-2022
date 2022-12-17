# THE23POST

## Installation

### Install all library to support for program

```bash
pip install -r requirements.txt
```
## Virtual Environment

### Work on virtual environment

```bash
myEnv\Scripts\activate
```

## Connect and update database

### First, we need create a new database
    Open MySQL --> Create a new database, set:
        Name database: article_website
        Charset: utf8mb4
        Collation: utf8bm4_unicode

### Next, grant to program access your database
 ##### Step 1    
    Go to DATABASE var in ./article_website/settings.py
 ##### Step 2  
    At USER and PASSWORD fields, change to mySQL's user and password


### Then, return to terminal, type:

```bash
py manage.py makemigrations myApp
py manage.py migrate
```

## Compile and Run server

```bash
python manage.py runserver
```


## License 
THE 23 GROUP

