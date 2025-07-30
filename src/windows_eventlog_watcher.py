import win32evtlog

server = 'localhost'
log_type = 'Security'

hand = win32evtlog.OpenEventLog(server, log_type)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

print("Watching Windows Security log...")

events = win32evtlog.ReadEventLog(hand, flags, 0)
for event in events:
    if event.EventID in [4625, 4624]:  # 4625 = Failed login, 4624 = Success login
        print(f"[ALERT] Event ID {event.EventID}: {event.StringInserts}")
