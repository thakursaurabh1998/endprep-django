# EndPrep

> This is a personal project to use django for endprep

### How to run?

1. Clone this repository.
1. Install django with command `pip install django` (make sure you are using Python 3.6)
1. Also postgresql server needs to be running.
1. Go to the directory and run command `python manage.py migrate` and `python manage.py makemigrations`.
1. Then populate the database with the command `python manage.py loaddata populate_db`.
1. Run the server with the command `python manage.py runserver`. The server is up and running on port `8000`.

[Original Project Here](https://github.com/EndPrep/endprep)