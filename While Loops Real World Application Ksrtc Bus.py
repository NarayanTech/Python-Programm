# Real Life Example : KSRTC BUS SEAT Avilable 
available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    booking = input("Do you want to book a seat? (yes/no): ").lower()
    
    if booking == "yes":
        available_seats -= 1
        print("Seat booked!")
    elif booking == "no":
        print("No booking made.")
else:
      print("All Seats Are Booked")