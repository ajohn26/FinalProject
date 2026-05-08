# Import Flask so we can make a website
# Import request so we can get information from the URL
from flask import Flask, request

# Import random so we can make a random confirmation number
import random


# Create the Flask app
app = Flask(__name__)


# This is a list of contracted clinics
# Each clinic has a name, distance, claim types, appointment times, and a soonest number
# The soonest number helps us sort clinics by earliest appointment
clinics = [
    {
        "name": "OPTUM Serve Downtown Medical Center",
        "distance": 2.1,
        "claim_types": ["General Medical", "Mental Health", "Vision"],
        "times": ["9:00 AM", "11:00 AM", "2:00 PM"],
        "soonest": 9
    },
    {
        "name": "OPTUM Serve Lawrenceville Exam Center",
        "distance": 3.4,
        "claim_types": ["Mental Health", "Audio or Tinnitus", "Musculoskeletal"],
        "times": ["10:00 AM", "1:00 PM", "4:00 PM"],
        "soonest": 10
    },
    {
        "name": "OPTUM Serve Gwinnett Outpatient Clinic",
        "distance": 4.2,
        "claim_types": ["General Medical", "Respiratory / Sleep Apnea", "Mental Health"],
        "times": ["8:30 AM", "12:00 PM", "3:00 PM"],
        "soonest": 8.5
    },
    {
        "name": "OPTUM Serve Norcross",
        "distance": 9.8,
        "claim_types": ["Respiratory / Sleep Apnea", "Musculoskeletal", "General Medical"],
        "times": ["8:00 AM", "10:30 AM", "2:00 PM"],
        "soonest": 8
    },
    {
        "name": "OPTUM Serve Hearing and Vision Clinic",
        "distance": 6.5,
        "claim_types": ["Audio or Tinnitus", "Vision"],
        "times": ["9:30 AM", "1:30 PM", "3:30 PM"],
        "soonest": 9.5
    }
]


# These are the claim types the user can choose from
claim_types = [
    {"name": "General Medical", "emoji": "🩺"},
    {"name": "Mental Health", "emoji": "🧠"},
    {"name": "Audio or Tinnitus", "emoji": "👂"},
    {"name": "Respiratory / Sleep Apnea", "emoji": "🫁"},
    {"name": "Musculoskeletal", "emoji": "🦴"},
    {"name": "Vision", "emoji": "👁️"}
]


# This function makes a random confirmation number
def make_confirmation_number():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    number = "CONF-"

    for i in range(6):
        number = number + random.choice(letters)

    return number


# This function returns the CSS styles for the whole website
def get_styles():
    return """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #eaf4fb;
            margin: 0;
            padding: 30px 20px;
        }

        .container {
            max-width: 700px;
            margin: 0 auto;
        }

        .header {
            background-color: #1a6fa8;
            color: white;
            padding: 22px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        .header h1 {
            margin: 0;
        }

        .header p {
            margin-bottom: 0;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
        }

        .button-card {
            background-color: white;
            border: 2px solid #d0e8f7;
            border-radius: 12px;
            padding: 18px;
            color: #1a6fa8;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
        }

        .button-card:hover {
            background-color: #f2f9fd;
            border-color: #1a6fa8;
        }

        .card {
            background-color: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }

        .card h3 {
            color: #1a6fa8;
            margin-top: 0;
        }

        .badge {
            display: inline-block;
            background-color: #e8f4fd;
            color: #1a6fa8;
            padding: 5px 10px;
            border-radius: 20px;
            margin: 4px 4px 10px 0;
            font-size: 14px;
            font-weight: bold;
        }

        .time-button {
            display: inline-block;
            background-color: #1a6fa8;
            color: white;
            padding: 8px 14px;
            border-radius: 8px;
            text-decoration: none;
            margin: 4px;
            font-weight: bold;
        }

        .green-button {
            display: inline-block;
            background-color: #2e7d32;
            color: white;
            padding: 12px 18px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            margin-top: 10px;
        }

        .filter-button {
            display: inline-block;
            background-color: white;
            border: 2px solid #1a6fa8;
            color: #1a6fa8;
            padding: 8px 14px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            margin-right: 8px;
            margin-bottom: 14px;
        }

        .back-link {
            display: inline-block;
            margin-top: 10px;
            color: #1a6fa8;
            text-decoration: none;
            font-weight: bold;
        }

        .message-box {
            background-color: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 16px;
        }
    </style>
    """


# This function makes the beginning of every page
# This keeps us from copying the same HTML over and over
def start_page(title, subtitle):
    page = "<html><head><title>SchedulingPro</title>"
    page = page + get_styles()
    page = page + "</head><body><div class='container'>"
    page = page + "<div class='header'>"
    page = page + "<h1>🏥 SchedulingPro</h1>"
    page = page + "<p>" + subtitle + "</p>"
    page = page + "</div>"
    return page


# This function ends every page
def end_page():
    return "</div></body></html>"


# This is the home page
@app.route("/")
def home():
    page = start_page("Home", "What is your type of claim?")

    page = page + "<div class='grid'>"

    for claim in claim_types:
        page = page + "<a class='button-card' href='/location?claim=" + claim["name"] + "'>"
        page = page + claim["emoji"] + " " + claim["name"]
        page = page + "</a>"

    page = page + "</div>"
    page = page + end_page()

    return page


# This page pretends to use location services
# For this beginner project, we are not using real GPS yet
@app.route("/location")
def location():
    claim = request.args.get("claim")

    if claim is None:
        page = start_page("Error", "Something went wrong")
        page = page + "<div class='message-box'>No claim type was selected.</div>"
        page = page + "<a class='back-link' href='/'>← Go back</a>"
        page = page + end_page()
        return page

    page = start_page("Use Location", "Use location services")

    page = page + "<div class='card'>"
    page = page + "<h3>📍 Find clinics near you</h3>"
    page = page + "<p>This demo will use your location to show the nearest contracted clinics.</p>"
    page = page + "<a class='green-button' href='/results?claim=" + claim + "&sort=distance'>Use my location</a>"
    page = page + "</div>"

    page = page + "<a class='back-link' href='/'>← Go back</a>"
    page = page + end_page()

    return page


# This page shows the clinics that match the claim type
@app.route("/results")
def results():
    claim = request.args.get("claim")
    sort = request.args.get("sort")

    if claim is None:
        page = start_page("Error", "Something went wrong")
        page = page + "<div class='message-box'>No claim type was selected.</div>"
        page = page + "<a class='back-link' href='/'>← Go back</a>"
        page = page + end_page()
        return page

    matching_clinics = []

    for clinic in clinics:
        if claim in clinic["claim_types"]:
            matching_clinics.append(clinic)

    if sort == "soonest":
        matching_clinics.sort(key=lambda clinic: clinic["soonest"])
    else:
        matching_clinics.sort(key=lambda clinic: clinic["distance"])

    page = start_page("Results", "Contracted clinics for: " + claim)

    page = page + "<a class='filter-button' href='/results?claim=" + claim + "&sort=distance'>Filter: Distance</a>"
    page = page + "<a class='filter-button' href='/results?claim=" + claim + "&sort=soonest'>Filter: Soonest Available</a>"

    if len(matching_clinics) == 0:
        page = page + "<div class='message-box'>No clinics were found for this claim type.</div>"

    for clinic in matching_clinics:
        earliest_time = clinic["times"][0]

        page = page + "<div class='card'>"
        page = page + "<h3>🏨 " + clinic["name"] + "</h3>"
        page = page + "<span class='badge'>📍 " + str(clinic["distance"]) + " miles away</span>"
        page = page + "<span class='badge'>⭐ Contracted clinic</span>"
        page = page + "<p><b>Earliest appointment:</b> " + earliest_time + "</p>"
        page = page + "<p>Pick a time:</p>"

        for time in clinic["times"]:
            page = page + "<a class='time-button' href='/review?claim=" + claim + "&clinic=" + clinic["name"] + "&time=" + time + "'>"
            page = page + "🕐 " + time
            page = page + "</a>"

        page = page + "</div>"

    page = page + "<a class='back-link' href='/'>← Start over</a>"
    page = page + end_page()

    return page


# This page lets the user review before confirming
@app.route("/review")
def review():
    claim = request.args.get("claim")
    clinic = request.args.get("clinic")
    time = request.args.get("time")

    page = start_page("Review", "Review your appointment")

    page = page + "<div class='card'>"
    page = page + "<h3>📋 Appointment Details</h3>"
    page = page + "<p><b>Claim Type:</b> " + claim + "</p>"
    page = page + "<p><b>Clinic:</b> " + clinic + "</p>"
    page = page + "<p><b>Time:</b> " + time + "</p>"
    page = page + "<a class='green-button' href='/confirm?claim=" + claim + "&clinic=" + clinic + "&time=" + time + "'>Confirm appointment</a>"
    page = page + "</div>"

    page = page + "<a class='back-link' href='/results?claim=" + claim + "'>← Go back</a>"
    page = page + end_page()

    return page


# This page confirms the appointment
@app.route("/confirm")
def confirm():
    claim = request.args.get("claim")
    clinic = request.args.get("clinic")
    time = request.args.get("time")
    confirmation_number = make_confirmation_number()

    page = start_page("Confirmed", "Your appointment is booked")

    page = page + "<div class='card'>"
    page = page + "<h3>✅ Appointment Confirmed!</h3>"
    page = page + "<p><b>Claim Type:</b> " + claim + "</p>"
    page = page + "<p><b>Clinic:</b> " + clinic + "</p>"
    page = page + "<p><b>Time:</b> " + time + "</p>"
    page = page + "<p><b>Confirmation Number:</b> " + confirmation_number + "</p>"
    page = page + "</div>"

    page = page + "<a class='back-link' href='/'>← Book another appointment</a>"
    page = page + end_page()

    return page


# This starts the app
# debug=True helps show errors while coding
app.run(debug=True)