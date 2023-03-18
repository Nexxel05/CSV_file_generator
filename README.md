# CSV file generator

Simple app to generate csv file with different data types of any length

## Check it out!

[http://nexxel05.pythonanywhere.com/](http://nexxel05.pythonanywhere.com/)

Login credentials:

User: admin   
Password: 1qazcde3

## Installation

Python3 must be already installed

```shell
git clone https://github.com/Nexxel05/CSV_file_generator.git
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Create .env file in root directory and store there your SECRET_KEY like shown in .env_sample 
```
python manage.py migrate
python manage.py runserver
```
