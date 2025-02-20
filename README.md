
---

# **Django Project Setup Guide** 🚀  

This guide explains how to set up and run the Django project. Follow the steps below to install dependencies, configure the environment, and start the project.  

## **1. Clone the Repository**  

```bash
git clone https://github.com/abdullokhonz/itproger.git
cd itproger
```

## **2. Create a Virtual Environment**  

Before installing dependencies, create and activate a virtual environment:  

- **Windows:**  
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **Mac/Linux:**  
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

## **3. Install Dependencies**  

Once the virtual environment is activated, install the required packages:  

```bash
pip install -r requirements.txt
```

## **4. Configure Environment Variables**  

Create a `.env` file in the project's root directory and add the following variables:  

```ini
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

## **5. Apply Migrations**  

Before running the project, apply database migrations:  

```bash
python manage.py migrate
```

## **6. Create a Superuser (Optional, for Admin Panel)**  

If you need access to the Django admin panel, create a superuser:  

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username, email, and password.  

## **7. Run the Development Server**  

Start the Django development server with:  

```bash
python manage.py runserver
```

The project will be available at:  
➡️ **http://127.0.0.1:8000/**  

## **8. Additional Commands**  

- **Collect static files (for production):**  
  ```bash
  python manage.py collectstatic
  ```

- **Run tests:**  
  ```bash
  python manage.py test
  ```

## **9. Deactivating the Virtual Environment**  

When you're done, deactivate the virtual environment:  

```bash
deactivate
```

---
