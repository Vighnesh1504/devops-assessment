# A simple Flask web application
from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def hello():
    return '<h1>Hello, World! This is my DevOps assessment!</h1>'

# Run the application
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
