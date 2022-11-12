import time
# the countdown fuction is defined below
def countdown(t):
    while t:
        mins,secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t-=1
        print('lift off!')

#ask the user to enter the countdown period in seconds
t=input("enter the time in seconds:")
# function call
countdown(int(t))        