document.getElementById('send-btn').addEventListener('click', sendMessage);

function appendMessage(sender, text) {
    const chatbox = document.getElementById('chatbox');
    const message = document.createElement('div');
    message.textContent = sender + ': ' + text;
    chatbox.appendChild(message);
    chatbox.scrollTop = chatbox.scrollHeight;
}

function sendMessage() {
    const userInput = document.getElementById('user-input');
    const text = userInput.value.trim();
    if (!text) return;
    appendMessage('Você', text);
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: text })
    })
    .then(response => response.json())
    .then(data => {
        if (data.reply) {
            appendMessage('Bot', data.reply);
        } else {
            appendMessage('Erro', data.error || 'Erro ao responder');
        }
    })
    .catch(err => appendMessage('Erro', err.message));
    userInput.value = '';
}
