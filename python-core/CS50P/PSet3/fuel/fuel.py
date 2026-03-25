while True:
    fraction = input("Fraction: ").split("/")
    try:
        numerator = int(fraction[0])
        denominator = int(fraction[1])

        if denominator == 0:
            continue

        percentage = (numerator / denominator) * 100

        if percentage < 0 or percentage > 100:
            continue

    except (ValueError, IndexError):
        continue
    else:
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage:.0f}%")
        break