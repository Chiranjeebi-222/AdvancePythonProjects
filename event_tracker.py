events = set()

while True:
    event = input("Enter event (or write 'exit'): ")
    if event == "exit":
        break
    events.add(event)

print("Tracked events:", events)
