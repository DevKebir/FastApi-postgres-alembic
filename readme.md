# Users API

This is a simple Users RESTful API built with Python and the FastAPI framework. It uses SQLAlchemy ORM for interacting with the PostgreSQL database, and Alembic for data migration.

## Usage

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/abkebir/FastApi-postgres-alembic.git
    cd your-repository
    ```

2. Install the dependencies:

    ```bash
    pip freeze > requirements.txt
    pip install -r requirements.txt
    ```

### Configuration

1. Configure the PostgreSQL database connection in the `database.py` file.

### Database Migrations with Alembic

Database migrations are managed using Alembic commands. Follow these steps after making changes to your models:

1. Initialize Alembic:

    ```bash
    alembic init alembic
    ```

2. Edit the generated `alembic.ini` file to set your database connection string.

3. Create an initial migration:

    ```bash
    alembic revision --autogenerate -m "initial"
    ```

4. Apply migrations to the database:

    ```bash
    alembic upgrade head
    ```

5. For each subsequent change to the models, generate a new migration:

    ```bash
    alembic revision --autogenerate -m "description_of_change"
    ```

6. Apply the new migration to the database:

    ```bash
    alembic upgrade head
    ```

Make sure to run these commands in the terminal after making any changes to your models to keep the database schema updated. Adjust the migration descriptions accordingly.

### API Endpoints

- **GET /get-users**: Get a list of all users.
- **GET /get-users/{user_id}**: Get user details by user ID.
- **GET /get-by-username**: Get user details by username.
- **POST /create-user**: Create a new user.
- **PUT /update-user**: Update an existing user.
- **DELETE /delete-user**: Delete a user by user ID.

### How to Run
- Run the FastAPI application with :
  ```bash
   uvicorn main:app --reload.
   ```
- Access the API at http://127.0.0.1:8000.
