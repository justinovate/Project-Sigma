def main():
    time = input("What time is it?  ")
    if 7.0 <= convert(time) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(time) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(time) <= 19.0:
        print("dinner time")

def convert(time):
    marker = time.split()[-1]
    time = time.replace(marker, "").strip()
    hours, minutes = map(float, time.split(":"))
    minutes /= 60
    if marker == "p.m." and hours != 12:
        hours += 12
    elif marker == "a.m." and hours == 12:
        hours = 0
    return hours + minutes
    
if __name__ == "__main__":
    main()