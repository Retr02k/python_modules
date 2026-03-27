def ft_water_reminder():
    days_passed = int(input("Days since last watering: "))
    if days_passed > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
