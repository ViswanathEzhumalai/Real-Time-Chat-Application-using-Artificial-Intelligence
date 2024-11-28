from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from ai_utils import analyze_sentiment, translate_message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return "AI Chat App Backend is Running!"

@socketio.on('send_message')
def handle_message(data):
    message = data.get('message')
    sentiment = analyze_sentiment(message)
    translated_message = translate_message(message, 'es')  # Translate to Spanish
    enriched_message = {
        'original': message,
        'sentiment': sentiment,
        'translated': translated_message
    }
    emit('receive_message', enriched_message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)