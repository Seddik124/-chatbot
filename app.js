async function sendMessage() {
      const input = document.getElementById("message");
      const messages = document.getElementById("messages");
      const msg = input.value.trim();
      if (!msg) return;

      const userMsg = document.createElement("div");
      userMsg.className = "message user";
      userMsg.textContent = msg;
      messages.appendChild(userMsg);
      input.value = "";
      messages.scrollTop = messages.scrollHeight;

      const botTyping = document.createElement("div");
      botTyping.className = "message bot";
      botTyping.textContent = "...";
      messages.appendChild(botTyping);
      messages.scrollTop = messages.scrollHeight;

      try {
        const res = await fetch("/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: msg })
        });

        const data = await res.json();
        botTyping.remove();

        const botMsg = document.createElement("div");
        botMsg.className = "message bot";
        botMsg.textContent = data.response || "Erreur de réponse";
        messages.appendChild(botMsg);
        messages.scrollTop = messages.scrollHeight;
      } catch (e) {
        botTyping.remove();
        const errorMsg = document.createElement("div");
        errorMsg.className = "message bot";
        errorMsg.textContent = "Erreur de connexion au serveur.";
        messages.appendChild(errorMsg);
      }
    }