# Secure Product Management API (Django + DRF)

## 📌 Project Overview
This project is a **secure RESTful API** built using **Django** and **Django REST Framework (DRF)** to manage product data.  
It demonstrates core backend concepts such as:

- REST API design
- Authentication & authorization (JWT)
- Pagination & filtering
- Data encryption at rest
- CSV data ingestion
- SQLite database integration

The project is intentionally kept **simple yet realistic**, making it suitable for learning, interviews, and portfolio demonstration.

---

## 🏗️ Tech Stack
- **Python**
- **Django**
- **Django REST Framework**
- **SQLite** (default Django database)
- **JWT Authentication (SimpleJWT)**
- **django-filter**
- **encrypted-model-fields**
- **python-dotenv**

---

## 📂 Project Structure
secure_product_api/
│
├── secure_product_api/
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── products/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── admin.py
│ └── ...
│
├── populate_products.py
├── products.csv
├── requirements.txt
├── .env
└── manage.py


---

## 🧾 Dataset
The project starts with a **CSV file (`products.csv`)** containing product details:

- Product ID
- Category
- Price
- Manufacturing date
- Expiry date

This CSV is used to **pre-populate the database** using a custom script.

---

## 🔐 Data Encryption
Some fields are considered **sensitive** and are encrypted before being stored in the database.

### Encrypted Fields
- `supplier_cost` → Encrypted using `EncryptedIntegerField`
- `internal_notes` → Encrypted using `EncryptedTextField`

Encryption happens **automatically at the model level**, meaning:
- Data is encrypted in the database
- Decrypted transparently when accessed via Django ORM

The encryption key is stored securely in a `.env` file and never committed to GitHub.

---

## 🔑 Environment Variables
Create a `.env` file in the project root:

```env
FIELD_ENCRYPTION_KEY=your_fernet_key_here
SECRET_KEY=your_django_secret_key
The encryption key is generated using Fernet and must be a valid 32-byte base64 string.

## 📥 Database Population

- A script (populate_products.py) is used to:
- Read product data from products.csv
- Insert records into the SQLite database
- Automatically generate dummy encrypted values for encrypted fields

Run: python populate_products.py

## 🔐 Authentication (JWT)

The API is protected using JSON Web Tokens (JWT).

### Token Endpoints

POST /api/token/ → Get access & refresh tokens

POST /api/token/refresh/ → Refresh access token

### Example request body:
{
  "username": "admin_username",
  "password": "admin_password"
}
## 📦 API Endpoints
List & Create Products
GET  /api/products/
POST /api/products/

- Requires authentication
- Supports pagination and filtering

## 📄 Pagination

Pagination is enabled globally using DRF.

### Example response:
{
  "count": 20,
  "next": "?page=2",
  "previous": null,
  "results": [...]
}
Default page size: 5 items per page

## 🔍 Filtering

Filtering allows clients to retrieve specific data using query parameters.

Examples:
/api/products/?product_category=Food
/api/products/?product_price=299.99
/api/products/?product_category=Electronics&page=2

Implemented using django-filter.

## 🛡️ Permissions

Only authenticated users can access the API

JWT tokens are required in request headers:
Authorization: Bearer <access_token>

## 🧪 Admin Panel

Django Admin is enabled to:

- View products
- Verify encrypted fields
- Manage users

### Create admin user:
python manage.py createsuperuser

## 🎯 What This Project Demonstrates

- Real-world REST API design
- Secure handling of sensitive data
- Authentication & authorization
- Scalable API features (pagination & filtering)
- Clean separation of concerns (models, serializers, views)
- Practical Django + DRF usage