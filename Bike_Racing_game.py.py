import time
Top_score = 20
Name = "Preethika N C"
while True:
    distance = int(0)
    print('\n=====================================================================================')
    print('\n\nJust Start the engine and Go...with a flow!!')
    print('\nTap 1 and 2 to move forward your successful path')
    print('$=20m')
    print('\nCurrent Record: '+str(Top_score)+' || By: '+Name)
    print("\nPress Enter to Start the Race")
    input()
    print('Countdown Starts....')
    time.sleep(3)
    print("GO!!")
    start_time = time.time()
    while distance < 20:
        p1 = int(input())
        if p1 == 1:
            p2 = int(input())
            if p2 == 2:
                distance = distance +1
                if distance == 10:
                    print("$ You are halfway there!")
                elif distance % 1==0:
                        print("$")
    finish_time = time.time() - start_time
    finish_time = round(finish_time,2)
    print("Congratulations on successfully completing the race!")
    print("You took",finish_time,"seconds to reach your successful path")

    if finish_time < Top_score:
        print("Wow!! you are amazing, You got a new high score")
        Name = input("Please enter your good name: ")
        Top_score = finish_time
