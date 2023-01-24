
i=1
command=""
quit=True
count=0
while True:
    command=input(">").lower()
    if 'help' in command:
                    print('''>   start: Enter start to start game,
>   Stop: Enter stp to stop game,
>   Help: Enter help for any problem''')

    elif 'start' in command:
                print("Game started")
                
                while count<2:
                         print("Game already started")
                    
            

    elif  'stop' in command:
                print("Game Ended")
                count+=1
                if count<1:
                    print("Game already stopped")

    elif 'quit'  in command:
                True
                break
    
               
               

    else:
                 print("Your command is not valid , Please check command once again")
 
    i+=1

    
    