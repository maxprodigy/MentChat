const chatBox = document.querySelector('.box');
const inputField = document.querySelector('.input-field input');
const sendButton = document.querySelector('.input-field button');

const BACKEND_URL = 'http://127.0.0.1:5000/chat';

sendButton.addEventListener('click', sendMessage);
inputField.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function appendMessage(message, sender) {
    const itemDiv = document.createElement('div');
    itemDiv.classList.add('item');
    if (sender === 'user') {
        itemDiv.classList.add('right');
    } else {
        const iconDiv = document.createElement('div');
        iconDiv.classList.add('icon');
        const icon = document.createElement('i');
        // Using a robot icon for the chatbot
        icon.classList.add('fa', 'fa-robot');
        iconDiv.appendChild(icon);
        itemDiv.appendChild(iconDiv);
    }

    const msgDiv = document.createElement('div');
    msgDiv.classList.add('msg');
    const p = document.createElement('p');
    p.textContent = message;
    msgDiv.appendChild(p);
    itemDiv.appendChild(msgDiv);
    chatBox.appendChild(itemDiv);

    const br = document.createElement('br');
    br.clear = 'both';
    chatBox.appendChild(br);

    chatBox.scrollTop = chatBox.scrollHeight;
}

function showTypingIndicator() {
    // This can be expanded to show a "Bot is typing..." message
    // For now, it just serves as a placeholder for future enhancements
    console.log("Bot is typing...");
}

async function sendMessage() {
    const userInput = inputField.value.trim();
    if (userInput === '') return;

    appendMessage(userInput, 'user');
    inputField.value = '';

    showTypingIndicator();

    try {
        const response = await fetch(BACKEND_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        appendMessage(data.response, 'bot');

    } catch (error) {
        console.error('Error:', error);
        appendMessage('Sorry, something went wrong. Please try again.', 'bot');
    }
} 