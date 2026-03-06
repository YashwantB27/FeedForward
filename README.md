# 🍽️ FeedForward

> A web platform to reduce food waste, connect food donors with those in need, and help users live healthier lives through personalized diet & workout planning.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![HTML](https://img.shields.io/badge/Frontend-HTML%2FCSS-orange?logo=html5)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 About

**FeedForward** is a community-driven platform built with Flask that does more than just fight food waste. It bridges the gap between food donors (restaurants, households, events) and recipients (NGOs, individuals in need) — while also empowering users to take charge of their health with built-in **Diet Planning** and **Workout Planning** tools.

Whether you're donating surplus food or planning your next meal and fitness routine, FeedForward has you covered. 🥗💪

---

## ✨ Features

### 🍽️ Food Donation
- 🔐 User Authentication (Login / Register)
- 📦 Food Listing & Donation Management
- 📥 Inbox & Messaging System
- 🌍 Multi-language Support (Translations)
- 🥜 Allergy Information Tracking
- 📊 Role-based Access (Donor / Recipient)

### 🥗 Diet Planner
- 📋 Personalized meal plans based on dietary goals
- 🔢 Calorie & nutrient tracking per meal
- 🥦 Support for dietary preferences (Veg, Vegan, Keto, etc.)
- 🧾 Daily & weekly meal schedule builder
- ⚠️ Allergy-aware meal suggestions

### 💪 Workout Planner
- 🏋️ Customized workout routines (Beginner / Intermediate / Advanced)
- 📅 Weekly workout schedule planning
- 🎯 Goal-based plans (Weight Loss / Muscle Gain / Stamina)
- 🗂️ Exercise library with instructions
- 📈 Progress tracking & activity logs

---

## 🗂️ Project Structure

```
FeedForward/
│
├── app.py                  # Main Flask application entry point
├── extensions.py           # Flask extensions (db, login manager, etc.)
├── translations.py         # Language/translation utilities
├── requirements.txt        # Python dependencies
│
├── models/                 # Database models (User, Food, Message, etc.)
├── routes/                 # Flask Blueprints / route handlers
├── templates/              # Jinja2 HTML templates
├── static/                 # CSS, JS, Images
└── instance/               # SQLite database (auto-generated)
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YashwantB27/FeedForward.git
cd FeedForward
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
Create a `.env` file in the root directory:
```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///feedforward.db
```

### 5. Run the Application
```bash
python app.py
```

Visit: **http://localhost:5000**

---

## 🥗 Diet Planner

FeedForward's Diet Planner helps users maintain a healthy and balanced lifestyle by providing personalized meal recommendations tailored to their health goals.

**How it works:**
1. User sets their goal (Weight Loss / Muscle Gain / Maintenance)
2. Enter dietary preferences and any food allergies
3. Get a **personalized daily & weekly meal plan**
4. Track calories and nutrients for each meal
5. Plans auto-adjust based on allergy settings from your profile

**Supported Diet Types:**
| Diet Type | Description |
|-----------|-------------|
| 🥦 Vegetarian | Plant-based with dairy & eggs |
| 🌱 Vegan | Fully plant-based |
| 🥩 Keto | High fat, low carb |
| 💪 High Protein | For muscle building |
| ⚖️ Balanced | General healthy eating |

---

## 💪 Workout Planner

The Workout Planner provides structured fitness routines to help users achieve their personal health and fitness goals — no gym membership required!

**How it works:**
1. User selects their fitness goal (Weight Loss / Muscle Gain / Stamina / Flexibility)
2. Choose experience level (Beginner / Intermediate / Advanced)
3. Get a **customized weekly workout schedule**
4. Browse the exercise library with step-by-step instructions
5. Log completed workouts and track your progress over time

**Workout Categories:**
| Category | Examples |
|----------|---------|
| 🏃 Cardio | Running, Cycling, Jump Rope |
| 🏋️ Strength | Push-ups, Squats, Deadlifts |
| 🧘 Flexibility | Yoga, Stretching Routines |
| 🔥 HIIT | High-Intensity Interval Training |
| 🏠 Home Workouts | No-equipment exercises |

---

## 🚀 Deployment (Render)

1. Push code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Add environment variables in Render dashboard

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| Database | SQLite (dev), PostgreSQL (prod) |
| Frontend | HTML, CSS, Jinja2 |
| Auth | Flask-Login |
| ORM | Flask-SQLAlchemy |

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Yashwant B** — [@YashwantB27](https://github.com/YashwantB27)

> *"Don't waste food — forward it. Eat right, train smart, live well!"* 🌱💪
