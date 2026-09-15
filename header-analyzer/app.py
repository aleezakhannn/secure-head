from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from analyzer import check_headers, calculate_score

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
)

@app.route("/", methods=["GET", "POST"])
@limiter.limit("10 per minute")
def index():
    results = None
    score = None
    grade = None
    error = None

    if request.method == "POST":
        url = request.form["url"].strip()

        if not url:
            error = "Please enter a website URL."
        else:
            results = check_headers(url)

            if results == "unsafe":
                error = "This URL is blocked for security reasons (internal/private address)."
                results = None
            elif results == "error":
                error = "Couldn't reach that website. Check the URL and try again."
                results = None
            else:
                score, grade = calculate_score(results)

    return render_template("index.html", results=results, score=score, grade=grade, error=error)

if __name__ == "__main__":
    app.run(debug=False)