function sendMessage() {
  const input = document.getElementById("messageInput");
  if (!input.value.trim()) return;

  const p = document.createElement("p");
  p.textContent = input.value;
  document.getElementById("messages").appendChild(p);

  input.value = "";
}
