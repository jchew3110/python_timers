#modules
import datetime
import time
#TIMER
#Enter Preferences


supported_formats = ["hrs","min","sec"]

print("\n")

def get_input():
    global unit_input
    unit_input = input("Enter the format in which you want to time yourself:{}:".format(supported_formats))
    unit_input.lower()

#Check if the format entered is valid.
get_input()

if unit_input in supported_formats:
    pass
else:
    print("Invalid Input.Please re-enter you desired format.\nThe input is case insenseitive")
    get_input()

def countdown_timer(x):
    while x >= 0 :
        x -= 1
        print("{} remaining".format(str(datetime.timedelta(seconds=x))))
        print("\n")
        time.sleep(1)


#Check for input and assign variable to determine the total amount of seconds
def IOTimer():
    while True:
        try:
            if unit_input == "hrs":
                hours  = int(input("Enter the number of hours: "))
                print("\n")
                minutes = int(input("Enter the number of minutes: "))
                print("\n")
                seconds = int(input("Enter the number of seconds: "))
                print("\n")
                break
            elif unit_input == "min":
                hours = 0
                minutes = int(input("Enter the number of minutes: "))
                print("\n")
                seconds = int(input("Enter the number of seconds: "))
                print("\n")
                break
            elif unit_input == "sec":
                hours = 0
                minutes = 0
                seconds = int(input("Enter the number of seconds: "))
                print("\n")
                break
        except:
            print("Invalid Input.Re-enter the values")
            print("\n")
            IOTimer()
    hours_in_sec = hours*3600
    minutes_in_sec = minutes*60
    total_seconds = hours_in_sec + minutes_in_sec + seconds
    print("Starting countdown for {}".format(str(datetime.timedelta(seconds=total_seconds))))
    print("\n")
    time.sleep(2)
    countdown_timer(total_seconds)

IOTimer()
