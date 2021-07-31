import time
Top_score = 20
Name = "Preethika N C" #Top Scorer Name
while True: #Condition to start the race
    distance = int(0) #Initial distance covered by the user
    print('\n=====================================================================================')
    print('\n\nJust Start the engine and Go...with a flow!!')
    print('\nTap 1 and 2 to move forward your successful path')
    print('$=20m')
    print('\nCurrent Record: '+str(Top_score)+' || By: '+Name)  #Previous Record of the user
    print("\nPress Enter to Start the Race")
    input()
    print('Countdown Starts....')
    time.sleep(3) #CountDown
    print("GO!!")
    start_time = time.time() #starting time of the race
    while distance < 20:
        p1 = int(input()) #enter 1 to enter the next one
        if p1 == 1:
            p2 = int(input()) #enter 2 to increase the distance
            if p2 == 2:
                distance = distance +1 #distance inscreases by 1 for every 2 count
                if distance == 10: 
                    print("$ You are halfway there!")
                elif distance % 1==0:
                        print("$") #it's representing the pathway
    finish_time = time.time() - start_time #finish time of the user
    finish_time = round(finish_time,2) #rounding the finish time with 2 decimal count
    print("Congratulations on successfully completing the race!")
    print("You took",finish_time,"seconds to reach your successful path")

    if finish_time < Top_score: #It sets the new record of the user if their finish time less than the top scorer
        print("Wow!! you are amazing, You got a new high score")
        Name = input("Please enter your good name: ")
        Top_score = finish_time
