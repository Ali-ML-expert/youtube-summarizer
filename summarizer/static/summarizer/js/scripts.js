// Add any JavaScript functionality here
console.log("Scripts loaded");

// Add smooth scrolling to all links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Form validation
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        let inputs = this.querySelectorAll('input[required]');
        inputs.forEach(input => {
            if (!input.value) {
                e.preventDefault();
                input.classList.add('error');
            } else {
                input.classList.remove('error');
            }
        });
    });
});