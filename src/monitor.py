import os
import pymysql
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')

LAST_SEEN_FILE = 'last_seen.txt'

if os.path.exists(LAST_SEEN_FILE):
    with open(LAST_SEEN_FILE, 'r') as f:
        last_seen = f.read().strip()
else:
    last_seen = '1970-01-01 00:00:00'

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='P@ssw0rd1!',
    database='mysql'
)

cursor = conn.cursor()
cursor.execute("""
    SELECT event_time, argument 
    FROM general_log 
    WHERE (argument LIKE 'GRANT%%' OR argument LIKE 'REVOKE%%') 
    AND event_time > %s 
    ORDER BY event_time ASC;
""", (last_seen,))

rows = cursor.fetchall()
if rows:
    entries = []
    for time, cmd in rows:
        cmd_clean = cmd.decode('utf-8') if isinstance(cmd, bytes) else cmd
        entries.append(f"[{time}] {cmd_clean}")

    # Save audit log
    with open('audit_log.txt', 'a') as log:
        for entry in entries:
            log.write(entry + '\n')

    # Email
    msg = EmailMessage()
    msg['Subject'] = 'MySQL Permission Changes Detected'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_RECEIVER
    msg.set_content("The following GRANT/REVOKE changes were detected:\n\n" + "\n".join(entries))

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print("Email sent.")
    
    # Update last seen
    with open(LAST_SEEN_FILE, 'w') as f:
        f.write(str(rows[-1][0]))
else:
    print("ℹ️ No new GRANT/REVOKE detected.")

conn.close()

#              & "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p
#runs through task schedruler, runs as soon as pc starts 
