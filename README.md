# Fantasy Cricket Game

A desktop-based fantasy cricket application built using Python, PyQt5, and SQLite.

---

## Features

- Create fantasy cricket teams
- Select players by category
- Calculate match points
- Store player and team data using SQLite
- GUI built with PyQt5

---

## Technologies Used

- Python
- PyQt5
- SQLite3

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python Main.py
```

---

## Project Structure

```text
FantasyCricketGame/
│
├── database/
│   └── FantasyCricketGame.db
│
├── modules/
│   ├── match.py
│   ├── matches.py
│   ├── stats.py
│   └── teams.py
│
├── ui/
│   ├── Main.ui
│   ├── EvaluateTeam.ui
│   ├── Main.py
│   └── EvaluateTeam.py
│
├── screenshots/
│   ├── home.png
│   ├── evaluate_team.png
│   └── team_selection.png
│
├── data/
│   ├── players.csv
│   └── matches.csv
│
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
```

---

## Screenshots

### Main Window
![Main Window](screenshots/main_window.png)

### Team Evaluation
![Evaluation](screenshots/evaluate_score.png)

---

## Future Improvements

- Live cricket API integration
- Better UI design
- Player statistics visualization
- Online multiplayer support

---

## Author

Artham Siri
