from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "hearme-secret"

@app.route("/")
def index():
    exit_flag = request.args.get("exit")
    role = request.args.get("role")
    return render_template(
        "index.html",
        exit=exit_flag,
        role=role,
        logged_in=session.get("logged_in", False)
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["logged_in"] = True
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/role")
def role():
    if not session.get("logged_in"):
        return redirect("/login")
    return render_template("role.html")

@app.route("/wait")
def wait():
    role = request.args.get("role")
    if role not in ["talker", "listener"]:
        return redirect("/")
    return render_template("wait.html", role=role)

@app.route("/chat")
def chat():
    role = request.args.get("role")
    private = request.args.get("private")
    return render_template("chat.html", role=role, private=private)

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    role = request.args.get("role")
    feeling = request.args.get("feeling")
    return render_template("feedback.html", role=role, feeling=feeling)

if __name__ == "__main__":
    app.run(debug=True)