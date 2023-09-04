<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the form data
    $user_name = $_POST['user_name'];
    $user_email = $_POST['user_email'];
    $user_message = $_POST['user_message'];

    // Validate the form data
    if (empty($user_name) || empty($user_email) || empty($user_message)) {
        echo "All fields are required!";
        exit();
    }

    // Process the form data 
    $to = "caleb.kwakye@richmond.edu";
    $subject = "New contact form submission";
    $message = "Name: " . $user_name . "\nEmail: " . $user_email . "\n\nMessage:\n" . $user_message;
    $headers = "From: " . $user_email;

    if (mail($to, $subject, $message, $headers)) {
        echo "Your message has been sent successfully!";
    } else {
        echo "There was a problem sending your message. Please try again.";
    }
} else {
    echo "Invalid form submission.";
}
?>
