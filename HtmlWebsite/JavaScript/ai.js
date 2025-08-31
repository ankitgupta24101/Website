// Get elements
const chatBox = document.getElementById('chat-box');
const input = document.getElementById('command');
const sendBtn = document.getElementById('send-btn');

// Get URL and CSRF from HTML data attributes
const aiUrl = input.dataset.url;
const csrfToken = input.dataset.csrf;

// Add a chat bubble
function addBubble(message, sender, typing=false) {
    const div = document.createElement('div');
    div.classList.add('bubble', sender);
    if (typing) {
        div.textContent = 'Kitty is typing...';
        div.classList.add('typing');
    } else {
        div.innerHTML = `<div class="avatar"></div><div>${message}</div>`;
    }
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
    return div;
}

// Send command to server
function sendCommand() {
    const command = input.value.trim();
    if (!command) return;

    addBubble(command, 'user'); // User bubble
    input.value = '';

    const typingBubble = addBubble('', 'bot', true); // Bot typing

    fetch(aiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken
        },
        body: `command=${encodeURIComponent(command)}`
    })
    .then(res => res.json())
    .then(data => {
        typingBubble.innerHTML = `<div class="avatar"></div><div>${data.message}</div>`;
        typingBubble.classList.remove('typing');
    })
    .catch(err => {
        console.error(err);
        typingBubble.textContent = 'Error sending command';
        typingBubble.classList.remove('typing');
    });
}

// Event listeners
sendBtn.addEventListener('click', sendCommand);
input.addEventListener('keyup', e => { if (e.key === 'Enter') sendCommand(); });
