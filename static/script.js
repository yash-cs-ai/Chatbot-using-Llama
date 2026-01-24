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
    // 1. Create Wrapper
    const wrapper = document.createElement("div");
    // Adds class "message-wrapper" AND either "user" or "bot"
    wrapper.classList.add("message-wrapper", sender);

    // 2. Create Label
    const label = document.createElement("span");
    label.classList.add("label");
    label.textContent = sender === "user" ? "You" : "Chatbot";

    // 3. Create Bubble
    const bubble = document.createElement("div");
    bubble.classList.add("message-bubble");
    bubble.textContent = text;

    // 4. Assemble
    wrapper.appendChild(label);
    wrapper.appendChild(bubble);
    chatMessages.appendChild(wrapper);

    // 5. Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}