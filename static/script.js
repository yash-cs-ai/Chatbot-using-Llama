const form = document.getElementById("chat-form");
const input = document.getElementById("user-input");
const chatMessages = document.getElementById("chat-messages");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const message = input.value.trim();
    if (!message) return;

    addMessage("user", message);
    input.value = "";

    try {
        const formData = new FormData();
        formData.append("msg", message);

        const response = await fetch("/get", {
            method: "POST",
            body: formData
        });

        const botReply = await response.text();
        addMessage("bot", botReply);

    } catch (error) {
        console.error(error);
        addMessage("bot", "Server connection error.");
    }
});

function addMessage(sender, text) {
    const wrapper = document.createElement("div");
    wrapper.className = sender === "user"
        ? "flex justify-end"
        : "flex justify-start";

    const messageDiv = document.createElement("div");
    messageDiv.className = sender === "user"
        ? "user-message"
        : "bot-message";

    messageDiv.textContent = text;
    wrapper.appendChild(messageDiv);
    chatMessages.appendChild(wrapper);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}
