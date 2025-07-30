# Access Permission Alert System 🔐

Monitors permission changes across:
- ✅ MySQL (GRANT / REVOKE)
- ✅ Linux (`/var/log/auth.log`)
- ✅ Windows Event Logs

Sends **real-time email alerts** and shows a **web dashboard** of changes.

---

## 📁 Features

- 📬 Email alerts when DB or system permissions change
- 📊 Live dashboard (Flask) to view historical changes
- 🐧 Linux + 🪟 Windows support
- 🪪 Secrets stored in `.env`

---

## 🏁 How to Run

1. Clone repo  
   `git clone https://github.com/YOUR_USERNAME/access-permission-alert-system.git`

2. Set up Python env  
   `pip install -r requirements.txt`

3. Create `.env`  
   (copy from `.env.example` and fill in your credentials)

4. Run it (choose what you need):
   ```bash
   python src/monitor.py                # MySQL alert
   python src/authlog_watcher.py        # Linux auth log
   python src/windows_eventlog_watcher.py # Windows logs
   python src/dashboard.py              # Dashboard
