#import math

def clock():
    i = False
    while i == False:
        clockin = str(input("What time did you clock in? "))
        clockin1 = clockin.strip()
        clockinampm = clockin1[len(clockin1)-1]
        clockin1 = clockin.split(":")
        clockinhour = clockin1[0]
        if clockinampm == "p" and int(clockinhour) < 12:
            clockinhour = int(clockinhour) + 12
            i = True
        elif clockinampm =="a" and int(clockinhour) == 12:
            i = True
            clockinhour = int(0)
        elif clockinampm == "a" and int(clockinhour) < 12:
            i = True
        elif clockinampm == "p" and int(clockinhour) == 12:
            i = True
        clockinminute = clockin1[1]
        clockinminute = clockinminute.replace('a', ' ')
        clockinminute = clockinminute.replace('p', ' ')
        clockinminute = clockinminute.strip()
        if clockinminute != 0:
            clockinminreal = int(clockinminute) / 60
            clockinminreal = round(clockinminreal, 3)
        clock.clockintotal = float(clockinhour) + float(clockinminreal)
    o = False
    while o == False:
        clockout = str(input("What time did you clock out? "))
        clockout1 = clockout.strip()
        clockoutampm = clockout1[len(clockout1)-1]
        clockout1 = clockout1.split(":")
        clockouthour = clockout1[0]
        if clockoutampm == "p" and int(clockouthour) < 12:
            clockouthour = int(clockouthour) + 12
            o = True
        elif clockoutampm == "a" and int(clockouthour) == 12:
            o = True
            clockouthour = int(0)
        elif clockoutampm == "a" and int(clockouthour) < 12:
            o = True
        elif clockoutampm == "p" and int(clockouthour) == 12:
            o = True
        clockoutminute = clockout1[1]
        clockoutminute = clockoutminute.replace('a', ' ')
        clockoutminute = clockoutminute.replace('p', ' ')
        clockoutminute = clockoutminute.strip()
        if clockoutminute != 0:
            clockoutminreal = int(clockoutminute) / 60
            clockoutminreal = round(clockoutminreal, 3)
        clock.clockouttotal = float(clockouthour) + float(clockoutminreal)
    
x=False
while x == False:
    try:
        dayz = int(input("How many days did you work in this 7 day period? "))
        x = True
    except:
        print("Must use an integer amount")

y = False
while y == False:
    try:
        hourrate = float(input("How much is your per hour rate of pay? "))
        y = True
    except:
        print("Must use a number, floating point values are allowed")

weektimetotal = 0
d = 0
while d < dayz:
    print("For day", d+1, "in your work week. Use format 01:23a when recording time." )
    clock()
    if clock.clockouttotal > clock.clockintotal:
        totalhours = clock.clockouttotal - clock.clockintotal
        if totalhours < 0:
            totalhours = totalhours + 12
        if totalhours > 6: totalhourswithout = totalhours - 0.5
        else: totalhourswithout = totalhours
        totalhourswithout = totalhours - 0.5
        print("Total hours for this day are", round(totalhourswithout, 3))
        weektimetotal = weektimetotal + totalhours
        d = d + 1
    else:
        totalhours = (clock.clockouttotal + 24) - clock.clockintotal
        if totalhours < 0:
            totalhours = totalhours + 12
        if totalhours > 6: totalhourswithout = totalhours - 0.5
        else: totalhourswithout = totalhours
        totalhourswithout = totalhours - 0.5
        print("Total hours for this day are", round(totalhourswithout, 3))
        weektimetotal = weektimetotal + totalhours
        d = d + 1

print("Total clock time is " + str(weektimetotal))

if weektimetotal < 40.00:
    grosspay = round(hourrate * weektimetotal, 3)
    print("Gross pay for this week is " + str(grosspay))
elif weektimetotal > 40.00:
    overtimehours = weektimetotal - 40.00
    overtimepay = round(overtimehours * 0.5 * hourrate, 3)
    grosspay = round(hourrate * weektimetotal + overtimepay, 3)
    print("Gross pay for this week is " + str(grosspay) + " this total includes overtime pay.")
else:
    print("Something went wrong")