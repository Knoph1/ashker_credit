from flask import Flask, render_template, request

app = Flask(__name__)

# Example route for GET and POST methods
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle POST request here
        return "POST request received"
    else:
        # Handle GET request here
        return "GET request received"

if __name__ == '__main__':
    app.run(debug=True)
