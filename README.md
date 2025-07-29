# 🎯 Number Guessing Game – Flask App

A fun, interactive number guessing game built with **Flask**, **HTML**, **CSS**, and **Vanilla JS**. The game challenges users to guess a number between 1 and 100, providing real-time feedback and an elegant, responsive UI.

---

## 🚀 Features

- 🔢 Random number guessing logic (1–100)
- 🎯 Feedback for high/low guesses
- 🎉 Victory animation and stats
- 🧠 Session-based game state
- 💡 Error handling and input validation
- 📱 Fully responsive and mobile-friendly UI

---

## 📸 Preview

<img width="400" height="350" alt="Screenshot 2025-07-29 195303" src="https://github.com/user-attachments/assets/0fea6f87-d1a9-44fc-86fe-4b8c92303da3" />
<img width="400" height="600" alt="Screenshot 2025-07-29 195056" src="https://github.com/user-attachments/assets/17cb10e8-f9be-49d3-ba4c-454406e363ca" />



---


## 🛠️ Tech Stack

- **Backend**: Python, Flask  
- **Frontend**: HTML5, CSS3, JavaScript  
- **Styling**: Custom responsive CSS with animations

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/number-guessing-game.git
cd number-guessing-game
````

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install flask
```

4. **Run the app**

```bash
python app.py
```

5. **Open in browser**

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

* A random number between 1 and 100 is generated and stored in the session.
* Users enter their guess through the input form.
* The server compares the guess to the target number and responds with:

  * "Too high"
  * "Too low"
  * or "Correct! 🎉"
* The game can be restarted once completed.

---
