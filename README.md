# SkillPath – Training Recommendation System

A beginner-friendly web application that recommends training courses based on a learner's current skills, interests and learning level.

## Technology
- Python 3
- Flask
- HTML and CSS
- CSV dataset
- Pure-Python cosine similarity and keyword matching

**No scikit-learn is used.** The recommendation calculation is implemented in `recommender.py` using Python's built-in `math`, `re`, `csv` and `collections` modules.

## Run in VS Code (Windows)

1. Extract `Training_Recommendation_System.zip`.
2. Open the extracted `Training_Recommendation_System` folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Check Python:
   ```powershell
   py --version
   ```
5. Create a virtual environment:
   ```powershell
   py -m venv venv
   ```
6. Activate it in PowerShell:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, use Command Prompt terminal and run:
   ```cmd
   venv\\Scripts\\activate.bat
   ```
7. Install the one required package:
   ```powershell
   py -m pip install -r requirements.txt
   ```
8. Start the website:
   ```powershell
   py app.py
   ```
9. Open this address in your browser:
   `http://127.0.0.1:5000/`

Keep the terminal running while using the website. Press `Ctrl + C` in the terminal to stop it.

## Project structure

```text
Training_Recommendation_System/
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
├── data/
│   └── trainings.csv
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## How it works
1. The learner enters skills and an area of interest.
2. The app converts the text into keywords.
3. It compares the learner's keywords with each course using cosine similarity.
4. It gives a small bonus to courses matching the selected learning level.
5. It displays the five highest-scoring courses with match percentages and resource links.

## Customize
Add or edit rows in `data/trainings.csv`. Keep the same column names: `title, category, skills, level, duration, description, url`.
