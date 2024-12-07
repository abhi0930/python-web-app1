from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint 1: Hello World
@app.route('/')
def hello_world():
    return 'Hello World'

# Endpoint 2: Error logging and Bad Request response
@app.route('/error')
def error():
    app.logger.error("This is an error message")
    return jsonify({'error': 'Bad Request'}), 400

if __name__ == '__main__':
    app.run(debug=True)
