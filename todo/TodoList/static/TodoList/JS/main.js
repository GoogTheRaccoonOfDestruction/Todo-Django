
// Get all delete buttons
const deleteButtons = document.querySelectAll('.task-delete-btn')

// Attach event listener to each delete button
deleteButtons.forEach(button=>{
button.addEventListener("click", function(event){
        // Prevent the dfault form submisson
        event.preventDefault();

        // Prompt the user for conformation
        const confirmed = confirm("You are about to delete this task, are you sure you want to continue?");

        // If user confirms deletion, submit the form
        if (confirmed) {
            // Find the form associated with the delete button
            const form = button.closest('form');

            // Submit the form
            form.submit();
        }
});
});

// Get all save buttons
const deleteButtons = document.querySelectAll('.task-save-btn')

// Attach event listener to each save button
saveButtons.forEach(button=>{
button.addEventListener("click", function(event){
        // Prevent the dfault form submisson
        event.preventDefault();

        // Prompt the user for conformation
        const confirmed = confirm("Are you certain you have completed your task");

        // If user confirms deletion, submit the form
        if (confirmed) {
            // Find the form associated with the save button
            const form = button.closest('form');

            // Submit the form
            form.submit();
        }
});
});


