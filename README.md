# Participant Assessment Management System

A Flask web application for managing participants and recording psychosocial assessments. Designed to track **Thoughts and Behaviours** questionnaire results with automatic scoring and visual indicators.

---

## Features

- **User authentication** with role-based access (admin / user)
- **Participant management** — create, edit, delete, and list participants
- **Assessment recording** — log dated assessment sessions per participant
- **Thoughts and Behaviours questionnaire** — 8 Likert-scale questions with automatic scoring
- **Colour-coded results** — red / yellow / green badges based on total score

---

## Prerequisites

- Python 3.8+
- pip

---

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd AgileSoftwareProject

# Install dependencies
pip install -r requirements.txt
```

---

## Database Setup

The SQLite database is created automatically on first run. To seed the database with sample participants and default user accounts:

```bash
python seed.py
```

This creates:

- 28 sample participants
- Two default accounts:

| Username | Password | Role  |
|----------|----------|-------|
| `admin`  | `admin`  | Admin |
| `user`   | `user`   | User  |

> ⚠️ Change these credentials before deploying to any shared or production environment.

---

## Running the App

```bash
python app.py
```

The app starts in debug mode and is available at: `http://127.0.0.1:5000`

---

## Usage

### Logging In

Navigate to `http://127.0.0.1:5000` — you will be redirected to the login page. Enter your credentials to continue.

### Participants

| Action | Who can do it |
| ------ | ------------- |
| View list | All logged-in users |
| Add participant | All logged-in users |
| Edit participant | All logged-in users |
| Delete participant | Admin only |

Each participant requires:

- **ID** — exactly 9 characters (e.g. a prison reference number)
- **Name** — 2–50 characters
- **Date of birth** — must be in the past; participant must be 18 or older

### Assessments

From a participant's record you can add and view assessments. Each assessment records:

- **Date** — cannot be in the future
- **Thoughts and Behaviours questionnaire** — 8 questions answered on a 5-point Likert scale (Strongly Disagree → Strongly Agree)

#### Scoring

| Score | Badge  | Meaning        |
|-------|--------|----------------|
| 0–9   | 🔴 Red    | Needs attention |
| 10–24 | 🟡 Yellow | Moderate        |
| 25+   | 🟢 Green  | Positive        |

### Registering New Users

Admin users can register new accounts via the **Register** page (accessible from the navigation menu when logged in as admin).

---

## Project Structure

```
AgileSoftwareProject/
├── app.py                  # Application entry point and configuration
├── seed.py                 # Database seeding script
├── requirements.txt        # Python dependencies
├── models/
│   ├── database.py         # SQLAlchemy instance
│   ├── user.py             # User model
│   ├── participant.py      # Participant model
│   ├── assessment.py       # Assessment model
│   └── thoughts_and_behaviours.py  # Questionnaire model
├── controllers/
│   ├── auth.py             # Authentication routes
│   ├── participants.py     # Participant routes
│   └── assessments.py      # Assessment routes
├── templates/
│   ├── base.html
│   ├── auth/
│   ├── participants/
│   └── assessments/
└── instance/
    └── data.db             # SQLite database (auto-created)
```

---

## Configuration

All configuration is in `app.py`. Key settings:

| Setting | Default | Notes |
|---------|---------|-------|
| `SECRET_KEY` | `dev-secret-key-change-in-production` | **Change this in production** |
| Database | `sqlite:///data.db` | SQLite file in the instance folder |
| Debug mode | `True` | Disable in production |

---

## Tech Stack

| Library | Purpose |
|---------|---------|
| Flask | Web framework |
| Flask-SQLAlchemy | ORM / database integration |
| Flask-Login | Session management |
| Werkzeug | Password hashing |
| Jinja2 | HTML templating |
| SQLite | Database |
