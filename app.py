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
    app.run(host='0.0.0.0', port=5988)
