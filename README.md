# MyShop E-Commerce

Hi! Please follow these **Instructions** to get the app up and running. 


>* pip3 install -r requirements.txt
>* python manage.py makemigrations
>* python manage.py migrate
>* python manage.py createsuperuser [To access the admin located at http://localhost:8000/admin]
		Enter Username, Email, Password
>* python manage.py runserver

> **Note:** Run the celery using the command mentioned below

>* celery -A myshop worker -l info (In seperate Terminal)
>* celery -A myshop flower broker_api=http://guest:guest@localhost:15672/api/ --address=127.0.0.1 --port=5555 (In seperate Terminal)

Some Usage Instruction

>* Login to admin panel[after creating super user ]
>* Add some categories
>* Add some product in those categories
>* Now you are good to go. Browse http://localhost:8000/ 