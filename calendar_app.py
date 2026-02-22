import json
import os
from datetime import datetime, timedelta

DATA_FILE = "events.json"
events = []
next_id = 1

def load_events():
    """Load events from JSON file if it exists, and set next_id safely."""
    global events, next_id

    if not os.path.exists(DATA_FILE):
        events = []
        next_id = 1
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            print("Warning: events.json has invalid format. Starting with empty events.")
            events = []
            next_id = 1
            return

        # Validate basic fields
        cleaned = []
        max_id = 0
        for item in data:
            if isinstance(item, dict) and {"id", "title", "date", "time"} <= set(item.keys()):
                cleaned.append(item)
                if isinstance(item["id"], int) and item["id"] > max_id:
                    max_id = item["id"]

        events = cleaned
        next_id = max_id + 1

    except (json.JSONDecodeError, OSError) as e:
        print(f"Warning: Could not load {DATA_FILE}: {e}")
        events = []
        next_id = 1

def save_events():
    """Save events to JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(events, f, indent=2)
    except OSError as e:
        print(f"Error: Could not save to {DATA_FILE}: {e}")

def add_event(title, date, time):
    global next_id
    event = {"id": next_id, "title": title, "date": date, "time": time}
    events.append(event)
    next_id += 1
    save_events()
    print("Event added and saved!")

def add_recurring_event(title, start_date, time, frequency, count):
    try:
        d = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    step = timedelta(days=1) if frequency == "daily" else timedelta(weeks=1)

    for i in range(count):
        date_str = d.strftime("%Y-%m-%d")
        add_event(f"{title} (#{i+1})", date_str, time)
        d += step

def delete_event_by_id(event_id):
    global events
    before = len(events)
    events = [e for e in events if e["id"] != event_id]
    if len(events) < before:
        save_events()
        print("Event deleted and saved!")
    else:
        print("No event found with that ID.")

def list_events():
    if not events:
        print("\nNo events yet.")
        return
    print("\nYour Events:")
    for e in events:
        print(f'[{e["id"]}] {e["title"]} on {e["date"]} at {e["time"]}')

def main_menu():
    load_events()

    while True:
        print("\n--- Calendar Tracker AI (V4: JSON Save/Load) ---")
        print("1) Add single event")
        print("2) Add recurring event")
        print("3) Delete event")
        print("4) List events")
        print("5) Quit")

        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            date = input("Date (YYYY-MM-DD): ").strip()
            time = input("Time (e.g., 2:00 PM): ").strip()
            add_event(title, date, time)

        elif choice == "2":
            title = input("Title: ").strip()
            start_date = input("Start date (YYYY-MM-DD): ").strip()
            time = input("Time (e.g., 2:00 PM): ").strip()
            frequency = input("Frequency (daily/weekly): ").strip().lower()
            try:
                count = int(input("How many times? ").strip())
            except ValueError:
                print("Count must be a number.")
                continue
            if frequency not in ("daily", "weekly"):
                print("Frequency must be 'daily' or 'weekly'.")
                continue
            add_recurring_event(title, start_date, time, frequency, count)

        elif choice == "3":
            try:
                event_id = int(input("Event ID to delete: ").strip())
                delete_event_by_id(event_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif choice == "4":
            list_events()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()