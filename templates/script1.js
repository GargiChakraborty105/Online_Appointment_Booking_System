fetch('doctor-details.json')
  .then(response => response.json())
  .then(data => {
    // Update doctor information
    document.getElementById('doctor-photo').src = data.photo;
    document.getElementById('doctor-photo').alt = data.name + ", " + data.specialization + " doctor"; // Alt text for accessibility
    document.getElementById('doctor-name').textContent = data.name;
    document.getElementById('doctor-specialization').textContent = data.specialization;
    document.getElementById('doctor-bio').textContent = data.bio;

    // Handle time slot button clicks and POST request
    const timeSlotButtons = document.querySelectorAll(".time-slots button");
    const selectedTimeInput = document.getElementById("selected-time");

    timeSlotButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const selectedTime = button.dataset.time;
        selectedTimeInput.value = selectedTime;

        // Submit form data via POST
        const formData = new FormData();
        formData.append('selectedTime', selectedTime);

        fetch('/book-appointment', {
          method: 'POST',
          body: formData
        })
        .then(response => response.json())
        .then(data => {
          // Handle server response, e.g., display success message or redirect
          console.log(data);
        })
        .catch(error => {
          // Handle errors
          console.error(error);
        });
      });
    });

    // Update services list
    const servicesList = document.getElementById('services-list');
    data.services.forEach(service => {
      const listItem = document.createElement('li');
      listItem.textContent = service;
      servicesList.appendChild(listItem);
    });

    // Populate testimonials
    const testimonialsContainer = document.getElementById('testimonials-container');
    data.testimonials.forEach(testimonial => {
      const testimonialDiv = document.createElement('div');
      testimonialDiv.textContent = testimonial.quote;
      testimonialDiv.appendChild(document.createElement('p')).textContent = `- ${testimonial.patientName}`;
      testimonialsContainer.appendChild(testimonialDiv);
    });
  });
