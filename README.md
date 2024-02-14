# Lab - Class 27 

## Project: Django CRUD and Forms

### Author: [Immanuel Shin](https://github.com/ImmanuelShin)

### Setup

#### Requirements

**How to initialize/run your application:**
  1. Clone the repository.
   ```bash
   git clone
   ```
  2. Navigate to the project directory.
   ```bash
   cd [name-of-directory]
   ```
  3. Activate your virtual environment (if applicable).
   ```bash
   `python3 -m venv .venv`

   `source .venv/bin/activate` (Linux/Mac)

   `source .venv/Scripts/activate` (Windows)
   ```
  4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
  5. Apply migrations:
  ```bash
  python manage.py migrate
  ```
  6. Run server:
  ```bash
  python manage.py runserver
  ```
  7. Navigate to provided URL  
    - Sould be similar to http://127.0.0.1:8000/

### Tests

Run tests with:
```bash
python manage.py test
```