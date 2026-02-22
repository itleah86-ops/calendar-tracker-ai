events = []

def add_event(title, date, time):
    event = {"title": title, "date": date, "time": time}
    events.append(event)
    print("Event added!")

def delete_event(title):
    global events
    events = [e for e in events if e["title"] != title]
    print("Event deleted!")

def show_events():
    print("\nYour Calendar:")
    for e in events:
        print(f"{e['title']} on {e['date']} at {e['time']}")

# Test Version 1
add_event("Doctor Appointment", "2026-02-25", "10:00 AM")
add_event("Team Meeting", "2026-02-26", "2:00 PM")
show_events()

delete_event("Doctor Appointment")
show_events()