import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ss import *


# Function to send an email
def send_email(subject, message, to_email):
    # Set up SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # # Update with your Gmail credentials
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach message
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Log in to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, to_email, msg.as_string())
        print("Email sent successfully!")

        # Close connection
        server.quit()
    except Exception as e:
        print("Error sending email:", str(e))

# Example usage
# subject = "Test Email"
# message = "This is a test email sent from the voice assistant."
# to_email = "xyz@gmail.com"  # Update with recipient's email address

# Call the function to send the email
# send_email(subject, message, to_email)
