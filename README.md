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
- **LangChain & LangGraph** (LLM Orchestration)
- **Google Gemini 1.5 Flash** (Generative AI Model)
- **SQLAlchemy** (Database Abstraction for AI)

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

---

## 🔐 Manual Data Cryptography (AES-256)

Rather than relying on high-level plugins, this project implements a **custom symmetric encryption layer** using the industry-standard `cryptography` (Fernet) library. This ensures that sensitive product data is protected throughout its entire lifecycle.

### The Security Workflow

1.  **Encryption at Rest**: Sensitive fields (`supplier_cost_encrypted` and `internal_notes_encrypted`) are intercepted within the Django Model's `save()` method. They are converted to ciphertext before being written to the SQLite database.
2.  **Role-Based Access Control (RBAC)**: 
    * **Standard Users**: The API automatically masks sensitive fields, returning `********` or `Restricted`.
    * **Staff/Admins**: Authorized administrators can view decrypted data, which is handled securely through the Serializer's `to_representation` logic.
3.  **Zero-Leak Policy**: Sensitive information is never stored in plaintext. Even if the database file (`db.sqlite3`) is compromised, the sensitive fields remain unreadable without the `FIELD_ENCRYPTION_KEY`.
4.  **On-Demand Decryption**: The React frontend features a "Decrypt/Hide" toggle, allowing admins to selectively reveal sensitive data using their JWT credentials.



---

## 🛡️ Key Security Features Demonstrated

* **Manual Fernet Implementation**: Deep-dive into AES-256 encryption and secure key management using environment variables.
* **API Data Masking**: Practical application of data minimization by hiding sensitive fields at the endpoint level.
* **Defense in Depth**: Security is enforced at three levels: the Database (Encryption), the API (RBAC), and the UI (Masking).
* **JWT Integration**: Full authentication flow where user roles directly dictate data visibility.
The encryption key is stored securely in a `.env` file and never committed to GitHub.
* **AI Prompt Injection Mitigation**: Use of SQLDatabase.from_uri constraints and custom PromptTemplates to prevent the LLM from accessing sensitive authentication tables or performing unauthorized database writes.

---

## 🔑 Environment Variables
Create a `.env` file in the project root:

```env
FIELD_ENCRYPTION_KEY=your_fernet_key_here
SECRET_KEY=your_django_secret_key
The encryption key is generated using Fernet and must be a valid 32-byte base64 string.
GOOGLE_API_KEY=your_gemini_api_key_here

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

## 🤖 AI-Powered Natural Language Analytics
Integrates an **Intelligent Database Assistant** using **LangChain** and **Google Gemini 1.5 Flash** to translate plain-English queries into real-time SQL insights.

### 🛡️ Security & AI Guardrails
Built with a "Security-First" approach to prevent SQL injection and data leakage:
* **Read-Only Enforcement:** Uses `sqlite:///db.sqlite3?mode=ro` to physically prevent destructive operations (`DELETE`, `DROP`).
* **Schema Masking:** AI is restricted via `include_tables` to the `products_product` table, hiding sensitive system and user tables.
* **Encryption Awareness:** Custom `PromptTemplates` instruct the LLM to ignore `_encrypted` fields, preventing logic errors on ciphertext.
* **Output Sanitization:** Engineered prompts to enforce raw SQL returns, neutralizing Markdown syntax errors in the SQLite engine.

## 🧪 Admin Panel

Django Admin is enabled to:

- View products
- Verify encrypted fields
- Manage users

### Create admin user:
python manage.py createsuperuser

## 🎯 What This Project Demonstrates

- **AI Orchestration**: Integration of LLMs with structured relational databases using LangChain.
- **Defensive AI Architecture**: Implementing "Least Privilege" access and read-only database connections for AI agents.
- **Real-world REST API Design**: Building scalable, production-ready endpoints with Django & DRF.
- **Advanced Data Security**: Manual AES-256 encryption at the model level and role-based data masking.
- **Full-Stack Integration**: Bridging a React frontend with a complex backend featuring JWT Auth, filtering, and AI analytics.
- **Clean Architecture**: Strict separation of concerns across Models, Serializers, Views, and AI Utility layers.
