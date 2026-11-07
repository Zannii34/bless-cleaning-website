document.addEventListener("DOMContentLoaded", function() {
    // Get today's date
    const today = new Date();
    
    // Format it as YYYY-MM-DD
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth() + 1).padStart(2, '0'); // Months start at 0!
    const dd = String(today.getDate()).padStart(2, '0');
    
    const formattedDate = `${yyyy}-${mm}-${dd}`;
    
    // Find the date input field
    const dateInput = document.getElementById("date");
    
    // Set the 'min' attribute so users can't pick a date before today
    if (dateInput) {
        dateInput.setAttribute("min", formattedDate);
    }
});