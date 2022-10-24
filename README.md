# Bank security console
This is a private repository for an undisclosed bank. Thus if you accidentally found this repository most likely you will not have a database access, and will only be able to view html templates and database requests examples.  

In case you have a database access - the script shows all id cards, their visits statistics, and who is currently in the vault. 

## How to install
Using GitHub CLI:
```bash
gh repo clone Ph0enixGh0st/django-orm-watching-storage
```

Or download and unpack ZIP file from GIT Hub repository: https://github.com/Ph0enixGh0st/django-orm-watching-storage.git

# Prerequisites
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Next step is to create a ".env" file in the same folder with the script:
```
DB_ENGINE={django database postgresql/sqlite3/etc}
DB_HOST={your host here}
DB_PORT={port #}
DB_NAME={database name}
DB_USER={username}
DB_PASSWORD={your password}
SITE_SECRET_KEY={your site secret key}
DEBUG=FALSE
```

## How to run Watch_Tower
```bash
python manage.py runserver 0.0.0.0:8000
```
The service will be available at this address: http://127.0.0.1:8000/

![watchtower_photo1](https://user-images.githubusercontent.com/108229516/194126272-3ceeab16-fd6f-4dab-b9a4-39a5862c9c43.jpg)
![watchtower_photo2](https://user-images.githubusercontent.com/108229516/194126283-f0e8ef62-8b46-4f8e-9f11-1c58fbe7d201.jpg)


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
