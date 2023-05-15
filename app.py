#mentorapp.py

# from flask import Flask, render_template, request

# app = Flask(__name__)
# # app = Flask("Mentor App")

# @app.route('/')
# def landing_page():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit_email():
#     email = request.form.get('email')
#     # Save the email to your database or perform any desired action
#     return 'Email submitted successfully!'

# if __name__ == '__main__':
#     # app.debug = True
#     app.run(port = 5988)
###Test 1^

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def landing_page():
    if request.method == 'POST':
        email = request.form['email']
        with open('emails.txt', 'a') as file:
            file.write(email + '\n')
        return 'Thank you for submitting your email!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5988)
