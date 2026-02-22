events = []
next_id = 1

def add_event(title, date, time):
    global next_id
    event = {"id": next_id, "title": title, "date": date, "time": time}
    events.append(event)
    next_id += 1
    print("Event added!")

def delete_event_by_id(event_id):
    global events
    before = len(events)
    events = [e for e in events if e["id"] != event_id]
    if len(events) < before:
        print("Event deleted!")
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
    while True:
        print("\n--- Calendar Tracker AI (V2) ---")
        print("1) Add event")
        print("2) Delete event")
        print("3) List events")
        print("4) Quit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            date = input("Date (YYYY-MM-DD): ").strip()
            time = input("Time (e.g., 2:00 PM): ").strip()
            add_event(title, date, time)
        elif choice == "2":
            try:
                event_id = int(input("Enter event ID to delete: ").strip())
                delete_event_by_id(event_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == "3":
            list_events()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()