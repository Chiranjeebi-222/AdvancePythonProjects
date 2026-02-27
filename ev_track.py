events = set()

n = int(input("Enter number of events: "))

for i in range(1, n + 1):
    event_name = input(f"Enter event {i} name: ")
    events.add((i, event_name))

print("\nAvailable Events:")
for serial, name in sorted(events):
    print(f"{serial}. {name}")

serial_no = int(input("\nEnter serial number to find event: "))
available_ids = {item[0] for item in events}

if serial_no in available_ids:
    for item in events:
        if item[0] == serial_no:
            print(f"\nEvent Name: {item[1]}")
else:
    print("\nInvalid serial number!")