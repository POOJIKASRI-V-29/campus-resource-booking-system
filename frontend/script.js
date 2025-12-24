function createResource() {
  fetch("http://127.0.0.1:8000/resources", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      resource_id: document.getElementById("rid").value,
      type: document.getElementById("type").value,
      capacity: Number(document.getElementById("cap").value)
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("msg").innerText = data.message || data.detail;
  });
}
