'''print("HELLO MISS...")
print("YOU DONT KNOW WHERE I AM")
print("OOOooOOooOOoooooo")'''

import time

def countdown_timer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)

        timer=f"{mins}:{secs}"
        print(timer)
        time.sleep(1)
        seconds-=1

    print("TIMES UP BOZOSSSSS")

seconds=input("Enter the time in seconds. NOT min or hours cus otherwise you clearly cant read:   ")       

countdown_timer(int(seconds))