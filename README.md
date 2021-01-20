# MarketGenius

This project is the backend part built with Django REST of an e-commerce application.

## Build Setup

This project use Python 3.8.6

``` bash
# It is best to use the python virtualenv tool to build locally:

sudo pip3 install virtualenv

# Then in your project folder:

virtualenv newenv
source newenv/bin/activate
pip3 install -r requirements.txt
python3 manage.py runserver

```

## Database

This project works with a sqlite database.

### Database schema


## API REST

This project API is built with Django REST framework.

API routes endpoints :

> Products

``` bash
# GET  - return all the products
http://localhost:8000/products/
# POST  - create new product
http://localhost:8000/products/
# PUT  - edit an existant product
http://localhost:8000/products/{id}/
# DELETE  - delete an existant product
http://localhost:8000/products/{id}/

````

> Tickets

``` bash
# GET  - return all the tickets
http://localhost:8000/tickets/
# POST  - create new ticket
http://localhost:8000/tickets/
# DELETE  - delete an existant product
http://localhost:8000/tickets/{id}/

````

## Front repository

You can find the back-end project built with Django Rest here : https://github.com/lebiscuithd/MarketGenius-FrontEnd
