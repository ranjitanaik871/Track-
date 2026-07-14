# Meeting Room Booking Logger

bookings = [("Room A", "09:00", "10:00"),
    ("Room B", "10:30", "11:30"),
    ("Room C", "01:00", "02:00"),
    ("Room D", "03:00", "04:00")
]

print("Meeting Room Schedule")

for booking in bookings:
    #using unpacking method ,we can print the values assigned in bookings
    room, start, end = booking
    print("Room name:", room)
    print("Start Time:", start)
    print("End Time:", end)
    