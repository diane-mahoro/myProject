from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    username = request.form['username']
    message = request.form['message']
    messages.append(f'<strong>{username}:</strong> {message}')
    return jsonify({'message': 'Message received!'})

@app.route('/get_messages')
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)