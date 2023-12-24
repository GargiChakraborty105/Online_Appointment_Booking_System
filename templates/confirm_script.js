// Assuming appointment data is passed in the URL query string
const urlParams = new URLSearchParams(window.location.search);
const selectedDate = urlParams.get("date");
const selectedTime = urlParams.get("time");

// Fill in the appointment details
const appointmentDateSpan = document.getElementById("appointment-date");
const appointmentTimeSpan = document.getElementById("appointment-time");

appointmentDateSpan.textContent = selectedDate;
appointmentTimeSpan.textContent = selectedTime;
