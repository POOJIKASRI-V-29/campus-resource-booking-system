function createResource() {
  fetch("https://campus-booking-backend-q3xk.onrender.com/resources", {
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
function bookResource() {
  fetch("https://campus-booking-backend-q3xk.onrender.com/bookings", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      resource_id: document.getElementById("bid").value,
      date: document.getElementById("date").value,
      start_time: document.getElementById("start").value,
      end_time: document.getElementById("end").value,
      booked_by: document.getElementById("user").value
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("msg").innerText = data.message || data.detail;
  });
}
function login() {
  const username = document.getElementById("username").value;
  const role = document.getElementById("role").value;

  if (!username) {
    document.getElementById("msg").innerText = "Enter username";
    return;
  }

  localStorage.setItem("username", username);
  localStorage.setItem("role", role);

  window.location.href = "index.html";
}
