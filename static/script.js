// static/script.js
document.addEventListener('DOMContentLoaded', function() {
    // Example: Add client-side form validation
    document.querySelector('form').addEventListener('submit', function(event) {
        var name = document.querySelector('input[name="name"]').value.trim();
        var age = document.querySelector('input[name="age"]').value.trim();
        var grade = document.querySelector('input[name="grade"]').value.trim();
        if (name === '' || age === '' || grade === '') {
            alert('Please fill in all fields');
            event.preventDefault();
        }
    });
});
