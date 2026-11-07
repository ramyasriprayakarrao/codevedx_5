from flask import Flask, render_template, request
from recommender import recommend_trainings, get_categories

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    message = ""
    if request.method == "POST":
        skills = request.form.get("skills", "").strip()
        interest = request.form.get("interest", "").strip()
        level = request.form.get("level", "Beginner").strip()
        if not skills and not interest:
            message = "Please enter at least one skill or an area of interest."
        else:
            recommendations = recommend_trainings(skills, interest, level)
            if not recommendations:
                message = "No close matches found. Try broader skills or a different interest."
    return render_template(
        "index.html",
        recommendations=recommendations,
        message=message,
        categories=get_categories(),
        submitted=request.method == "POST",
        skills=request.form.get("skills", "") if request.method == "POST" else "",
        interest=request.form.get("interest", "") if request.method == "POST" else "",
        level=request.form.get("level", "Beginner") if request.method == "POST" else "Beginner"
    )

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
