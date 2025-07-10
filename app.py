from flask import Flask, request, render_template, redirect, url_for, session
from core.header_checker import check_headers
from core.xss_scanner import test_xss
from core.sqli_scanner import test_sqli
from core.csrf_scanner import detect_csrf_forms
from core.dir_bruteforce import brute_force_paths
from utils.export_pdf import export_pdf
from utils.export_csv import export_csv

app = Flask(__name__)
app.secret_key = 'changeme_secret_key'

USERNAME = "admin"
PASSWORD = "pass123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/scanner", methods=["GET", "POST"])
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    results = []
    if request.method == "POST" and "url" in request.form:
        url = request.form["url"]
        headers, header_issues = check_headers(url)
        for issue in header_issues:
            results.append({"type": "Header", "details": issue})
        if test_xss(url):
            results.append({"type": "XSS", "details": "Possible reflected XSS vulnerability."})
        if test_sqli(url):
            results.append({"type": "SQL Injection", "details": "Possible SQL injection vulnerability."})
        csrf_forms = detect_csrf_forms(url)
        for form in csrf_forms:
            results.append({"type": "CSRF", "details": "Form without CSRF token."})
        found = brute_force_paths(url)
        for path in found:
            results.append({"type": "Directory", "details": f"Found path: {path}"})
        if request.form.get("export") == "pdf":
            export_pdf(results)
        elif request.form.get("export") == "csv":
            export_csv(results)
    return render_template("index.html", results=results)

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)