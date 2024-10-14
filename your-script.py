import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "rishavi08072002@gmail.com"  # Replace with your email
sender_password = "hgze qqqv bzoi ixcq"  # Replace with your email password or app password
receiver_email = "avinash9588@gmail.com"

# Create the email content
def create_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg

# Send the email
def send_email():
    subject = "Script Update"
    body = "Hello Avinash, the script is working fine."

    msg = create_email(subject, body)

    try:
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Log in to the email account

        # Send the email
        server.send_message(msg)
        print(f"Email sent to {receiver_email}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()  # Terminate the server

# Main loop to send email every 2 minutes
if __name__ == "__main__":
    while True:
        send_email()
        time.sleep(120)  # Sleep for 2 minutes (120 seconds)
