from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Stylish Login</title>

    <style>

        body{
            margin:0;
            padding:0;
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            background:linear-gradient(135deg,#667eea,#764ba2);
            font-family:Arial, sans-serif;
        }

        .login-box{
            width:320px;
            background:white;
            padding:40px;
            border-radius:15px;
            box-shadow:0 10px 25px rgba(0,0,0,0.3);
            text-align:center;
        }

        h2{
            margin-bottom:25px;
            color:#333;
        }

        input{
            width:100%;
            padding:12px;
            margin:10px 0;
            border:none;
            border-radius:8px;
            background:#f1f1f1;
            font-size:15px;
        }

        input:focus{
            outline:none;
            background:#e3e3e3;
        }

        button{
            width:100%;
            padding:12px;
            border:none;
            border-radius:8px;
            background:#667eea;
            color:white;
            font-size:16px;
            cursor:pointer;
            transition:0.3s;
        }

        button:hover{
            background:#5a67d8;
        }

        .success{
            color:green;
            font-weight:bold;
            margin-top:15px;
        }

        .error{
            color:red;
            font-weight:bold;
            margin-top:15px;
        }

    </style>
</head>

<body>

    <div class="login-box">

        <h2>🔐 Flask Login</h2>

        <form method="POST">

            <input type="text" name="username" placeholder="Enter Username" required>

            <input type="password" name="password" placeholder="Enter Password" required>

            <button type="submit">Login</button>

        </form>

        {% if message %}
            <p class="{{ category }}">{{ message }}</p>
        {% endif %}

    </div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():

    message = ""
    category = ""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            message = "✅ Login Successful"
            category = "success"
        else:
            message = "❌ Invalid Username or Password"
            category = "error"

    return render_template_string(
        HTML,
        message=message,
        category=category
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
