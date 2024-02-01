# Library Management System

## Description

This is a simple Library Management System implemented using Django and Django REST Framework.

## Project Setup

### Prerequisites

- Python 3.x
- Django REST Framework
- PostgreSQL

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/sthsuyash/library-management-system.git library-management-system && cd library-management-system
   ```

2. Create a virtual environment

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment

   ```bash
   source venv/bin/activate
   ```

   or

   ```powershell
   .\venv\Scripts\activate
   ```

4. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

5. Create a PostgreSQL database

   ```bash
   psql -c "CREATE DATABASE library;"
   ```

6. Update the database credentials in `libraryManagementSystem/settings.py`

   Example:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'library',
           'USER': 'postgres',
           'PASSWORD': 'postgres',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

   You should also copy the .env.example file to .env and update the values in it.

7. Run the migrations

   ```bash
   python manage.py migrate
   ```

8. Create a superuser to access the admin panel

   ```bash
    python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser.

9. Run the development server

   ```bash
   python manage.py runserver
   ```

   The development server should be up and running at [http://localhost:8000](http://localhost:8000).

10. You can access the admin panel at [http://localhost:8000/admin](http://localhost:8000/admin).

11. To run the tests. This includes all the tests for the models, views and the API endpoints.

    ```bash
    python manage.py test library.tests
    ```

## API Documentation

### Swagger

The API documentation is available at [http://localhost:8000/swagger/](http://localhost:8000/swagger/).

OR

### Manual documentations

The API documentation is as follows:

#### 1. User API

1. Create a New User

   - Endpoint: `/api/users/create/`
   - Method: POST
   - Request Body:

   ```json
   {
     "name": "Sam Smith",
     "email": "sam@example.com",
     "membership_date": "2022-01-01"
   }
   ```

2. List All Users

   - Endpoint: `/api/users/list/`
   - Method: GET

3. Get User by ID

   - Endpoint: `/api/users/<int:id>/`
   - Method: GET

#### 2. Book API

1. Add a New Book

   - Endpoint: `/api/books/add/`
   - Method: POST
   - Request Body:

   ```json
   {
     "title": "Sample Book",
     "isbn": "1234567890123",
     "published_date": "2022-01-01",
     "genre": "Fiction"
   }
   ```

2. List All Books

   - Endpoint: /api/books/list/
   - Method: GET

3. Get Book by ID

   - Endpoint: /api/books/<int:id>/
   - Method: GET

4. Assign/Update Book Details

   - Endpoint: /api/books/details/assign/
   - Method: PUT
   - Request Body:

   ```json
   {
     "book_id": 1,
     "number_of_pages": 300,
     "publisher": "Publisher Name",
     "language": "English"
   }
   ```

#### 3. Borrowed Books API

1. Borrow a Book

   - Endpoint: /api/borrow/
   - Method: POST
   - Request Body:

   ```json
   {
     "user": 1,
     "book": 1,
     "borrow_date": "2022-02-01"
   }
   ```

2. Return a Book

   - Endpoint: /api/return/<int:id>/
   - Method: PUT
   - Request Body:

   ```json
   {
     "return_date": "2022-03-01"
   }
   ```

3. List All Borrowed Books

   - Endpoint: /api/list/borrowed/
   - Method: GET

## Additional Notes

- The API endpoints are available at [http://localhost:8000/api/](http://localhost:8000/api/).
- The project assumes the use of PostgreSQL as the database. Adjust database settings in settings.py if using a different database.
- The date format used is YYYY-MM-DD. Ensure that the date is in this format when making requests.
