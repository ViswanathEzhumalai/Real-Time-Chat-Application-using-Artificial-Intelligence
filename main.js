const socket = io('http://localhost:5000');

const messagesDiv = document.getElementById('messages');
const input = document.getElementById('input');
const sendButton = document.getElementById('send');

sendButton.addEventListener('click', () => {
    const message = input.value;
    if (message.trim()) {
        socket.emit('send_message', { message });
        input.value = '';
    }
});

socket.on('receive_message', (data) => {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = `${data.original} (Sentiment: ${data.sentiment}, Translated: ${data.translated})`;
    messagesDiv.appendChild(messageDiv);
});