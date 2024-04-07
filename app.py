from flask import Flask, render_template, request

app = Flask(__name__)

# List of private email domains to deny
private_domains = ["gmail.com", "yahoo.com", "hotmail.com"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        if any(email.endswith(domain) for domain in private_domains):
            return render_template('error.html', message='Private email domains are not allowed.')
        else:
            # Process the form data (e.g., save to a database)
            # Here, we're just printing it for demonstration
            print(f"Received form data: First Name: {first_name}, Last Name: {last_name}, Email: {email}")
            return render_template('success.html', first_name=first_name)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
