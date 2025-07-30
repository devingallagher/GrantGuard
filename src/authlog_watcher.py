import time

AUTH_LOG = "/var/log/auth.log"
ALERT_WORDS = ['Failed password', 'Accepted password', 'authentication failure']

def watch_auth_log():
    print("Watching /var/log/auth.log for suspicious logins...")
    with open(AUTH_LOG, 'r') as file:
        file.seek(0, 2)  # Move to EOF
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                continue
            if any(word in line for word in ALERT_WORDS):
                print("[ALERT] Suspicious login detected:", line.strip())

if __name__ == "__main__":
    watch_auth_log()
