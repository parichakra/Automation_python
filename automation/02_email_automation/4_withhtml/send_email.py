import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define your SMTP server details from environment variables
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_SERVER_PORT = os.getenv("SMTP_SERVER_PORT")

# Define your sender email address and password from environment variables
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")
SENDER_EMAIL_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD")

# Define the receiver email address from environment variables
RECEIVER_EMAIL_ADDRESS = os.getenv("RECEIVER_EMAIL_ADDRESS")

# Define your subject for the email
subject = "Congratulations on Completing the Workshop!"

# Read the HTML content from the email.html file
with open("email.html", "r") as file:
    email_html = file.read()

# Define the email body content directly in Python
email_body = """
<p>Hello,</p>
<p>I hope this message finds you well. It's a pleasure to reach out to you.</p>
<blockquote>
  <p>"The journey of a thousand miles begins with one step."</p>
  <footer>- Lao Tzu</footer>
</blockquote>
<p>Best regards,<br>Parichakra</p>
<p><img src="cid:profile_bikram" alt="parichakra" style="width:100px;height:auto;"></p>
"""

# Inject the dynamic content into the email HTML structure
email_html = email_html.replace('{{ email_body }}', email_body)

# Create a multipart message and set headers
message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = SENDER_EMAIL_ADDRESS
message["To"] = RECEIVER_EMAIL_ADDRESS

# Attach the HTML part to the message
part2 = MIMEText(email_html, "html")
message.attach(part2)

# Attach the profile_bikram.jpg image
with open("profile_bikram.jpg", "rb") as image_file:
    image = MIMEImage(image_file.read())
    image.add_header('Content-ID', '<profile_bikram>')
    message.attach(image)

# Attach schedule.pdf file
file_path = "schedule.pdf"
with open(file_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(file_path)}",
    )
    message.attach(part)

print("Initializing SMTP server connection...")

# Initialize the SMTP server connection
smtp = smtplib.SMTP(SMTP_SERVER, int(SMTP_SERVER_PORT))
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
smtp.sendmail(SENDER_EMAIL_ADDRESS, RECEIVER_EMAIL_ADDRESS, message.as_string())
print("Email sent successfully!")

print("Closing the SMTP server connection...")
# Close the SMTP server connection
smtp.quit()
print("SMTP server connection closed.")
