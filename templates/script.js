fetch('doctor-details.json')
.then(response => response.json())
.then(data => {
    // Update doctor information
    document.getElementById('doctor-photo').src = data.photo;
    document.getElementById('doctor-photo').alt = data.name + ", " + data.specialization + " doctor"; // Alt text for accessibility
    document.getElementById('doctor-name').textContent = data.name;
    document.getElementById('doctor-specialization').textContent = data.specialization;
    document.getElementById('doctor-bio').textContent = data.bio;

    // Update services list
    const servicesList = document.getElementById('services-list');
    data.services.forEach(service => {
        const listItem = document.createElement('li');
        listItem.textContent = service;
        servicesList.appendChild(listItem);
    });

    // Populate testimonials (without carousel for now)
    const testimonialsContainer = document.getElementById('testimonials-container');
    data.testimonials.forEach(testimonial => {
        const testimonialDiv = document.createElement('div');
        testimonialDiv.textContent = testimonial.quote;
        testimonialDiv.appendChild(document.createElement('p')).textContent = `- ${testimonial.patientName}`; // Add patient name
        testimonialsContainer.appendChild(testimonialDiv);
    });
});
