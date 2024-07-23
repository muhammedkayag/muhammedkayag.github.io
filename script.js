let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop -150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset +height){
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a [href*=' + id + ' ]').classList.add('active')
            })
        }
    })
}


menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}




// Get the form element
const form = document.getElementById('contact-form');

// Add an event listener to the form's submit event
form.addEventListener('submit', (e) => {
  e.preventDefault(); // Prevent the default form submission

  // Get the form data
  const formData = new FormData(form);
  const fullName = formData.get('full_name');
  const email = formData.get('email');
  const phoneNumber = formData.get('phone_number');
  const subject = formData.get('subject');
  const message = formData.get('message');

  // Make an AJAX request to the server-side script
  $.ajax({
    type: 'POST',
    url: 'send-email.php',
    data: {
      full_name: fullName,
      email: email,
      phone_number: phoneNumber,
      subject: subject,
      message: message
    },
    success: (response) => {
      console.log('Email sent successfully!');
      // Redirect to a thank-you page or display a success message
      window.location.href = 'thank-you.html';
    },
    error: (xhr, status, error) => {
      console.error('Error sending email:', error);
    }
  });
});

