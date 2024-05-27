# Eyemate Project CRUD API

This project is a CRUD (Create, Read, Update, Delete) API built using Django Rest Framework. This API will be extensively used in our Eyemate project to manage various database operations.

## Getting Started

To get the project up and running, follow these instructions.

### Prerequisites

Make sure you have the following installed on your local machine:

- Python (version 3.6 or above)
- Django
- Django Rest Framework

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Django-CRUD-API
    ```
    ```bash
    cd myapi
    ```
3. Create a virtual environment:
    ```bash
    python -m venv env
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source env/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Database Migrations

Run the following commands to set up the database:

1. Make migrations:
    ```bash
    python manage.py makemigrations
    ```
2. Apply migrations:
    ```bash
    python manage.py migrate
    ```

### Running the Server

To start the development server, navigate to the `myapi` directory and run the following command:

```bash
python manage.py runserver
```
