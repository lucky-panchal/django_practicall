from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "404 Not Found", "message": "The requested route does not exist."}), 404

if __name__ == '__main__':
    app.run(debug=True)
