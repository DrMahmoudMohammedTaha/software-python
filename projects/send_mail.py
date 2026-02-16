
# Here's how to create an App Password for your Gmail account:

# Go to your Google Account security settings (https://myaccount.google.com/security)
# Make sure 2-Step Verification is turned on for your account
# Scroll down to "App passwords" (or search for it)
# Select "Mail" as the app and "Other" or "Custom" as the device
# Give it a name like "Python Email Script"
# Google will generate a 16-character password (with spaces) for you to use
# Copy this password and use it in your Python script where it says "your-app-password-here"

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    # Your Gmail credentials
    sender_email = "mahmoudaboahmed6@gmail.com"
    sender_password = "your-app-password-here"  # Use an App Password, not your regular password
    receiver_email = "mahmoud.aboayaad@ejust.edu.eg"
    
    # Create the email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Email from Python Script"
    
    # Email body
    body = "This is a test email sent from Python."
    message.attach(MIMEText(body, "plain"))
    
    try:
        # Create SMTP session
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Enable security
        
        # Login to your Gmail account
        server.login(sender_email, sender_password)
        
        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
        print("Email sent successfully!")
        
        # Close the SMTP session
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email()