import datetime
import winsound

def alaram (Timing):
    alttime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
    alttime = alttime [11:-3]
    print(alttime)
    Horeal = alttime[:2]    
    Horeal = int(Horeal)
    Mireal = alttime[3:5]
    Mireal = int(Mireal)

    print(f"reminder is set for {Timing}")


    while True:
        if Horeal == datetime.datetime.now().hour:
            if Mireal == datetime.datetime.now().minute:
                print(f"Reminder is Running")
                winsound.PlaySound('abc',winsound.SND_LOOP)
            elif Mireal < datetime.datetime.now().minute:
                break


if __name__ == '__main__':
    alaram('2:40 AM')