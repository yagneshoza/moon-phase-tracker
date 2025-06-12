# 🌙 Moon Phase Tracker

A simple Flask web app that lets users track the moon's current phase, illumination, moonrise and moonset times for any given location and date. The app also visualizes moon illumination over the next 30 days using an interactive graph.

## 🚀 Live Demo

[Click here to view the live site](https://moon-phase-tracker-zknc.onrender.com/)

## 🚀 Features

- 🌕 Displays moon phase, illumination, moonrise, and moonset for any date/location
- 📈 Interactive graph of moon illumination over 30 days
- 🖼️ Moon phase image based on real-time phase
- 📅 Uses WeatherAPI for astronomy data
- 🎨 Styled with Bootstrap for a responsive layout
- 📁 Background image and dark theme for a modern UI

## 🔧 Tech Stack

- Python 🐍
- Flask 🌐
- HTML + CSS + Bootstrap 🎨
- Chart.js 📊
- WeatherAPI.com 🌦️

## 🛠️ Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/moon-phase-tracker.git
   cd moon-phase-tracker
2. Install dependencies
   ```bash
   pip install -r requirements.txt
3. Create a .env file
   WEATHER_API_KEY=your_weatherapi_key
   MY_SECRET_SESSION_KEY=your_secret_key
4. Run the application
   ```bash
   python app.py
Then open http://127.0.0.1:5000 in your browser.

FOLDER STRUCTURE
moon-phase-tracker/
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   │   └── moon phase images
│   └── js/
│       └── graph.js
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   └── graph.html
│
├── .env
├── app.py
├── requirements.txt
└── README.md

📌 Todo / Improvements
 Add lunar calendar view
 Add live moon webcam feed
 Add moonset/moonrise charts
 Add multiple language support

⭐ Star this repo if you like it! Pull requests are welcome 🤝

