
from datetime import datetime
from pygame import mixer

mixer.init()
while True:
    alarm_hour = input("What hour do you want the alarm to ring : ")
    print()
    if not (alarm_hour.isnumeric()) or int(alarm_hour) < 0 or int(alarm_hour) > 13:
        print("Invalid HOUR ! Try again...")
        print()
    else:
        break

while True:
    alarm_min = input("What minute do you want the alarm to ring : ")
    print()
    if not (alarm_min.isnumeric()) or int(alarm_min) < 0 or int(alarm_min) > 59:
        print("Invalid MINUTE ! Try again...")
        print()
    else:
        break

while True:
    alarm_sec = input("What second do you want the alarm to ring : ")
    print()
    if not (alarm_sec.isnumeric()) or int(alarm_sec) < 0 or int(alarm_sec) > 59:
        print("Invalid SECOND ! Try again...")
        print()
    else:
        break

while True:
    alarm_period = input("AM or PM ? ").upper()
    print()
    if alarm_period != 'AM' and alarm_period != 'PM':
        print("Invalid input ! Try again...")
        print()
    else:
        break

print(f"Setting up alarm at  {alarm_hour}:{alarm_min}:{alarm_sec}  {alarm_period}")

while True:
    current_time = datetime.now()

    current_hour = current_time.strftime("%I")
    current_min = current_time.strftime("%M")
    current_sec = current_time.strftime("%S")
    current_period = current_time.strftime("%p")

    if alarm_hour == current_hour and alarm_min == current_min and alarm_sec == current_sec and alarm_period == current_period:
        print("It is now the time !!!")

        mixer.music.load("fantasy_alarm_clock.mp3")

        # Setting the volume
        mixer.music.set_volume(100)

        # Start playing the song
        mixer.music.play()

        while True:

            print()
            query = input("Press 't' to stop the alarm : ")

            if query == 't':

                # Stop the mixer
                mixer.music.stop()
                break
            else:
                print("Invalid input !")

        break

