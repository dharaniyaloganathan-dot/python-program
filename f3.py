from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        user = request.form["username"]
        pwd = request.form["password"]

        if user == "admin" and pwd == "1234":
            return "<h2 style='color:green;'>Login Success ✅</h2>"

        else:
            return "<h2 style='color:red;'>Invalid Login ❌</h2>"

    return '''

    <html>

    <head>
        <title>Simple Login</title>
    </head>

    <body style="text-align:center; margin-top:100px; font-family:Arial;">

        <h1>Flask Login</h1>

        <form method="POST">

            <input type="text"
                   name="username"
                   placeholder="Username">

            <br><br>

            <input type="password"
                   name="password"
                   placeholder="Password">

            <br><br>

            <button type="submit">
                Login
            </button>

        </form>

    </body>

    </html>

    '''

if __name__ == "__main__":
    app.run(debug=True)
