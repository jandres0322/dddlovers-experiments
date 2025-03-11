window.addEventListener("DOMContentLoaded", () => {
  const messages = document.getElementById("mensajes");

  if(typeof(EventSource) !== "undefined") {
    var source = new EventSource("http://localhost:8000/standard/solicitud-descarga-async");
    source.onmessage = function(event) {
      const message = document.createElement("li");
      const content = document.createTextNode(event.data);
      message.appendChild(content);
      messages.appendChild(message);
    }
  }
});