const signupForm = document.getElementById("signup-form");
signupForm.addEventListener("submit", (event) => {
  event.preventDefault(); // Prevent default form submission

  const fullname = document.getElementById("fullname").value;
  const phone = document.getElementById("phone").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirm-password").value;

  // Validation checks:
  let errorMessage = "";

  // Validate full name (example):
  if (!/^[a-zA-Z\s]+$/.test(fullname)) {
    errorMessage += "Full name must only contain letters and spaces.\n";
  }

  // Validate phone number (example):
  if (!/^\d{10}$/.test(phone)) {
    errorMessage += "Invalid phone number format.\n";
  }

  // Validate email format:
  if (!validateEmail(email)) {
    errorMessage += "Please enter a valid email address.\n";
  }

  // Validate password length:
  if (password.length < 8) {
    errorMessage += "Password must be at least 8 characters long.\n";
  }

  // Validate password confirmation:
  if (password !== confirmPassword) {
    errorMessage += "Passwords do not match.\n";
  }

  // If there are errors, display them:
  if (errorMessage !== "") {
    alert(errorMessage);
    return; // Stop the function from proceeding
  }

  // If validation passes, send data to server (replace with your actual logic):
  console.log("Sending signup data to server:", fullname, phone, email, password);
  // ... (Perform server-side signup logic)

  // Clear form fields and display success message:
  signupForm.reset();
  alert("Signup successful!");
});

// Helper function to validate email format:
function validateEmail(email) {
  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}
