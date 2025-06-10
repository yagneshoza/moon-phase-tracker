from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import requests
import os
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = os.getenv("MY_SECRET_SESSION_KEY")  # required for session to work

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        date = request.form["date"]
        location = request.form["location"]

        url = f"http://api.weatherapi.com/v1/astronomy.json?key={API_KEY}&q={location}&dt={date}"

        try:
            res = requests.get(url)
            res.raise_for_status()

            data = res.json()
            astro = data["astronomy"]["astro"]
            session["phase"] = astro["moon_phase"]
            session["illumination"] = astro["moon_illumination"]
            session["moonrise"] = astro["moonrise"]
            session["moonset"] = astro["moonset"]
            session["date"] = date
            session["location"] = location

            # Map moon phase to image
            phase_to_image = {
                "New Moon": "new_moon.jpg",
                "Full Moon": "full_moon.jpg",
                "First Quarter": "first_quarter.jpg",
                "Last Quarter": "last_quarter.jpg",
                "Waxing Crescent": "waxing_crescent.jpg",
                "Waning Crescent": "waning_crescent.jpg",
                "Waxing Gibbous": "waxing_gibbous.jpg",
                "Waning Gibbous": "waning_gibbous.jpg",
            }
            session["moon_image"] = f"/static/image/{phase_to_image.get(session['phase'], 'default.jpg')}"

        except Exception as e:
            session["error"] = str(e)

        return redirect(url_for("main"))  # Redirects to GET

    # For GET request (after redirect or initial load)
    data = {
        "phase": session.pop("phase", None),
        "illumination": session.pop("illumination", None),
        "moonrise": session.pop("moonrise", None),
        "moonset": session.pop("moonset", None),
        "date": session.pop("date", None),
        "location": session.pop("location", None),
        "error": session.pop("error", None),
        "moon_image": session.pop("moon_image", None),
    }

    return render_template("index.html", **data)

@app.route("/graph")
def graph():
    phases = []
    dates = []
    today = datetime.today()

    for i in range(30):
        date = today + timedelta(days=i)
        date_str = date.strftime("%Y-%m-%d")

        url = f"http://api.weatherapi.com/v1/astronomy.json?key={API_KEY}&q=India&dt={date_str}"
        try:
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()
            illumination = float(data["astronomy"]["astro"]["moon_illumination"])
            phases.append(illumination)
            dates.append(date_str)
        except:
            continue

    return render_template("graph.html", dates=dates, phases=phases)

if __name__ == "__main__":
    app.run(debug=True)
