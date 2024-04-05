Create a virtual environment :
-->python -m venv .venv

Activate the virtual environment on Windows :
-->source venv/Scripts/activate

To install Django :
-->pip install django

For Database setup :
-->python manage.py makemigrations

Apply the migrations :
-->python manage.py migrate

To create an superuser account, use this command : (optional)
-->python manage.py createsuperuser

Finally, run the development server :
-->python manage.py runserver