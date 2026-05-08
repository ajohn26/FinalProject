# SchedulingPro

SchedulingPro is a beginner-friendly Python and Flask web application designed to simulate a scheduling platform for veterans filing VA disability claims.

The goal of the project is to simplify the appointment scheduling process by helping users:

- Select a VA disability claim type
- Find nearby contracted clinics
- Filter clinics by distance or availability
- Choose an appointment time
- Review appointment details
- Receive a confirmation number

This project was created as a hands-on learning experience to practice healthcare workflow design, Python development, and full-stack web application concepts.

---

# Features

## Veteran Appointment Workflow

Users can:

- Select different VA disability claim exam types
- Search for nearby clinics
- View available appointment slots
- Schedule appointments
- Receive appointment confirmations

## Clinic Search Simulation

The platform simulates:

- VA-contracted clinic listings
- Distance-based filtering
- Availability filtering
- Appointment time selection

## Beginner-Friendly Architecture

The project is intentionally structured for learning and future expansion.

It is designed to help developers understand:

- Flask routing
- Frontend and backend communication
- Form handling
- Database integration concepts
- Healthcare scheduling workflows

---

# Tech Stack

## Backend
- Python
- Flask

## Frontend
- HTML5
- CSS3
- JavaScript

## Database (Planned)
- SQLite
- PostgreSQL

## Development Tools
- VS Code
- Git
- GitHub

---

# Project Structure

```bash
SchedulingPro/
│
├── app.py                 # Main Flask application
├── templates/             # HTML pages
├── static/                # CSS, JavaScript, images
├── database/              # Database files and models
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── venv/                  # Virtual environment (not uploaded)
```

---

# Installation Guide

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SchedulingPro.git
cd SchedulingPro
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a requirements.txt file yet, install Flask manually:

```bash
pip install flask
```

---

# Running the Application

Start the Flask server:

```bash
python app.py
```

You should see output similar to:

```bash
Running on http://127.0.0.1:5000/
```

Open the link in your browser.

---

# Example User Flow

1. User opens SchedulingPro
2. User selects a VA disability claim type
3. User searches for nearby clinics
4. User filters available appointments
5. User chooses an appointment time
6. User reviews appointment details
7. User receives a confirmation number

---

# Future Improvements

Planned features include:

- User authentication
- Real-time clinic database integration
- Google Maps API integration
- Email and SMS confirmations
- Veteran profile dashboard
- Appointment rescheduling
- Admin portal for clinic management
- AI-powered appointment recommendations
- Mobile responsive design

---

# Troubleshooting

## Flask Not Found

If you receive:

```bash
ModuleNotFoundError: No module named 'flask'
```

Run:

```bash
pip install flask
```

---

## Python Command Not Working

Try:

```bash
python3 app.py
```

or verify Python installation:

```bash
python --version
```

---

## Virtual Environment Not Activating

### Windows PowerShell Fix

Run:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then reactivate the virtual environment.

---

# Learning Goals

This project was built to strengthen skills in:

- Healthcare workflow analysis
- Full-stack web development
- Flask application structure
- Scheduling system logic
- Database design concepts
- User experience planning
- GitHub project management

---

# About the Project

SchedulingPro is currently a learning and portfolio project inspired by real-world healthcare scheduling workflows within VA disability examination systems.

The long-term vision is to create a streamlined scheduling experience that reduces delays and improves accessibility for veterans.
