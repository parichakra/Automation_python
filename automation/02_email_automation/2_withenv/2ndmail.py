import smtplib
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define your SMTP server details from environment variables
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")  # Default to Gmail's SMTP server
SMTP_SERVER_PORT = os.getenv("SMTP_SERVER_PORT", 587)  # Default to common port for TLS

# Define your sender email address and password from environment variables
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")
SENDER_EMAIL_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD")

# Define the receiver email address from environment variables
RECEIVER_EMAIL_ADDRESS = os.getenv("RECEIVER_EMAIL_ADDRESS")

# Ensure that the environment variables are correctly loaded
if not all([SMTP_SERVER, SMTP_SERVER_PORT, SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD, RECEIVER_EMAIL_ADDRESS]):
    raise ValueError("One or more environment variables are missing.")

# Define your subject and body for the email
subject = "Meeting Reminder: Project Update"
body = """
Hi ,

I hope this email finds you well. I wanted to share some exciting news with you. Our team has just completed the final stages of our project, and the results are amazing! We're planning a small celebration this Friday at 3 PM in the main conference room, and we'd love for you to join us.

Let me know if you can make it!

Best regards,
parichakra
"""

# Construct the email message
message = f'Subject: {subject}\n\n{body}'

try:
    print("Initializing SMTP server connection...")
    # Initialize the SMTP server connection
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_SERVER_PORT)
    print("SMTP server connection initialized.")

    print("Starting TLS encryption...")
    # Start TLS encryption
    smtp.starttls()
    print("TLS encryption started.")

    print("Logging in to the SMTP server...")
    # Login to the SMTP server
    smtp.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)
    print("Logged in to the SMTP server.")

    print("Sending the email...")
    # Send the email
    smtp.sendmail(SENDER_EMAIL_ADDRESS, RECEIVER_EMAIL_ADDRESS, message)
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print("SMTP Authentication Error:", e)
except Exception as e:
    print("Error:", e)
finally:
    print("Closing the SMTP server connection...")
    # Close the SMTP server connection
    smtp.quit()
    print("SMTP server connection closed.")
