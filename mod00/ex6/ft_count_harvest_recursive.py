def ft_count_harvest_recursive():
    day_give = int(input("Days until harvest: "))

    def help(current_day: int):
        if current_day > day_give:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        help(current_day + 1)

    help(1)
