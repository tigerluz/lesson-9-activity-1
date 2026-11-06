print("Step 1: pick your vehicle")
print("  1 - Bike")
print("  2 - Car")
print()
choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:

    print("Step 2: Pick your bike type")
    print("  1 - Scooty")
    print("  2 - Mountain Bike")
    print()
  
    bike_type = int(input("Enter 1 or 2: "))
    print()

    if bike_type == 1:
     print("You have selected Scooty")
     print("Top speed: 80 km/h")
     print("best for: city roads")
    else:
     print("You picked mountain bike")
     print("Top speed   : 40 km/h")
     print("Best for    : Off-road trails")
elif choice ==2: 
     print("Step 2: Pick your car type")
     print("  1 - Sedan")
     print("  2 - SUV")
     print()
  
     car_type = int(input("Enter 1 or 2: "))
     print()

     if car_type == 1:
      print("You have selected Sedan")
      print("Top speed: 200 km/h")
      print("Best for: City and highway driving")
     else:
        print("You picked SUV")
        print("Top speed   : 180 km/h")
        print("Best for    : Off-road and family trips")
else:
 print("Invalid choice. Please restart the program and select either 1 or 2.")
 print("Please enter 1 or 2 to select your vehicle type.")
 print("========================================")
 print("   Your custom ride is ready!           ")
 print("   Enjoy the journey!                   ")
 print("========================================")