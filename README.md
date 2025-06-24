# 🏋️ Gym Class Scheduling and Membership Management System

A backend system for managing gym operations, designed with role-based access for **Admin**, **Trainer**, and **Trainee** users. It enables user registration, class schedule creation, and booking with enforced business rules (e.g., max classes and bookings per day).

---

## 📌 Project Overview

This Django-based backend system allows gym admins to create class schedules, assign trainers, and manage bookings. Trainers can view assigned schedules. Trainees can register and book available classes.

**Key Rules:**
- Max **5 classes per day**
- Each class duration: **2 hours**
- Max **10 trainees per class**
- JWT-based authentication and role-based access control

---

## 🧩 Relation Diagram

You can view the relation diagram [here](https://dbdiagram.io/d/Gym-Scheduling-68599abdf039ec6d3685961f)

---

## ⚙️ Technology Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (`djangorestframework-simplejwt`)
- **Database**: SQLite (for demo), PostgreSQL recommended for production
- **Deployment**: [Render](https://render.com)
- **API Tool**: Postman

---

## 🚀 API Endpoints

| Action                       | Method | Endpoint                           | Auth Required | Role      |
|-----------------------------|--------|------------------------------------|---------------|-----------|
| Register                    | POST   | `/api/users/register/`            | ❌            | Any       |
| Login                       | POST   | `/api/token/`                      | ❌            | Any       |
| Refresh Token               | POST   | `/api/token/refresh/`             | ❌            | Any       |
| Create Schedule             | POST   | `/api/schedules/`                 | ✅            | Admin     |
| View All Schedules          | GET    | `/api/schedules/`                 | ✅            | All       |
| Create Booking              | POST   | `/api/bookings/`                  | ✅            | Trainee   |
| View Bookings               | GET    | `/api/bookings/`                  | ✅            | All       |

> Use JWT tokens (Bearer Token) in the Authorization header.

---

## 🧮 Database Schema (Model Overview)

### 🔸 User (Extended `AbstractUser`)
- `username`, `email`, `password`
- `role`: `admin`, `trainer`, `trainee`

### 🔸 Schedule
- `date`, `start_time`, `end_time`
- `trainer` → FK to User (role = trainer)

### 🔸 Booking
- `schedule` → FK to Schedule
- `trainee` → FK to User (role = trainee)
- `booked_at` (auto-created)

---

## 📌 API Endpoints

All available API endpoints and their usage are documented here:

👉 [**Postman API Documentation**](https://documenter.getpostman.com/view/46111276/2sB2xChV45)

This documentation includes:
- Authentication (Login, Token Refresh)
- User registration and role-based access
- Schedule creation and viewing
- Booking classes by trainees
- Admin-only and role-specific actions

## 🧑‍💼 Admin Credentials

Use this to test admin-level features:

```txt
Email: admin@gmail.com  
Password: securePass123  
```

## 🖥️ Instructions to Run Locally
1. Clone the project
```python
git clone https://github.com/your-username/gym-api.git
cd gym-api
```
2. Create virtual environment
```python
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows
```
3. Install dependencies
```python
pip install -r requirements.txt
```
4. Run migrations
```python
python manage.py makemigrations
python manage.py migrate
```
5. Run the server
```python
python manage.py runserver
```
6. (Optional) Create superuser
```python
python manage.py createsuperuser
```
## 🌐 Live Hosting Link
[🔗 Live API on Render](https://gym-scheduling-1.onrender.com/)

## 📥 Download Postman Collection
You can [download the Postman collection](./postman_collection.json) and import it into Postman.
