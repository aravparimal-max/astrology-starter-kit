from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        birthdate = request.form["birthdate"]
        # Later: add planetary calculations + AI here
        return f"Hello {name}, born on {birthdate}. Your horoscope will appear here soon!"
    return '''
        <form method="post">
            Name: <input name="name"><br>
            Birthdate (YYYY-MM-DD): <input name="birthdate"><br>
            <input type="submit">
        </form>
    '''

app.run(host="0.0.0.0", port=8080)
