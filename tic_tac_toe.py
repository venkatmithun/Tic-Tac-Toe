from random import randint
dict={}
for i in range(1,10):
    dict["position_{}".format(i)]=" "
player = input("Please type in your symbol, X or O ?: ")
if player=="X":
    computer="O"
elif player=="O":
    computer="X"
if player!='X' and player!='O':
    print("Can't you read bro?")

else:
    for i in range(1,100):
        x = input("Please type in position by selecting numbers in range(1-9) row wise: ")
        if x.isdigit():
           x=int(x)
        else:
            print("Please read instructions properly and try again!")
            continue
        if x<10 and x>0:
            R = randint(1,9)
            if dict["position_{}".format(x)]==" ":
                dict["position_{}".format(x)]=player
                if " " in dict.values():            
                    if dict["position_1"]==dict["position_2"]==dict["position_3"]!=" ":
                        print(" ",dict["position_1"],"wins!")
                        print(dict["position_1"],"|",dict["position_2"],"|",dict["position_3"])
                        print("__|___|__")
                        print(dict["position_4"],"|",dict["position_5"],"|",dict["position_6"])
                        print("__|___|__")
                        print(dict["position_7"],"|",dict["position_8"],"|",dict["position_9"])
                        print("  |   |  ")
                        break
                        
                    elif dict["position_1"]==dict["position_5"]==dict["position_9"]!=" ":
                        print(" ",dict["position_1"],"wins!")
                        print(dict["position_1"],"|",dict["position_2"],"|",dict["position_3"])
                        print("__|___|__")
                        print(dict["position_4"],"|",dict["position_5"],"|",dict["position_6"])
                        print("__|___|__")
                        print(dict["position_7"],"|",dict["position_8"],"|",dict["position_9"])
                        print("  |   |  ")
                        break
                    
                    elif dict["position_1"]==dict["position_4"]==dict["position_7"]!=" ":
                        print(" ",dict["position_1"],"wins!")
                        print(dict["position_1"],"|",dict["position_2"],"|",dict["position_3"])
                        print("__|___|__")
                        print(dict["position_4"],"|",dict["position_5"],"|",dict["position_6"])
                        print("__|___|__")
                        print(dict["position_7"],"|",dict["position_8"],"|",dict["position_9"])
                        print("  |   |  ")
                        break
                    
                    elif dict["position_2"]==dict["position_5"]==dict["position_8"]!=" ":
                        print(" ",dict["position_1"],"wins!")
                        print(dict["position_1"],"|",dict["position_2"],"|",dict["position_3"])
                        print("__|___|__")
                        print(dict["position_4"],"|",dict["position_5"],"|",dict["position_6"])
                        print("__|___|__")
                        print(dict["position_7"],"|",dict["position_8"],"|",dict["position_9"])
                        print("  |   |  ")
                        break    
                        
                    elif dict["position_3"]==dict["position_6"]==dict["position_9"]!=" ":
                        print(" ",dict["position_1"],"wins!")
                        print(dict["position_1"],"|",dict["position_2"],"|",dict["position_3"])
                        print("__|___|__")
                        print(dict["position_4"],"|",dict["position_5"],"|",dict["position_6"])
                        print("__|___|__")
                        print(dict["position_7"],"|",dict["position_8"],"|",dict["position_9"])
                        print("  |   |  ")
                        break
                    
                    elif dict["position_4"]==dict["position_5"]==dict["position_6"]!=" ":
                        print(" ",dict["position_1"],"wins!")
                        print(dict["position_1"],"|",dict["position_2"],"|",dict["position_3"])
                        print("__|___|__")
                        print(dict["position_4"],"|",dict["position_5"],"|",dict["position_6"])
                        print("__|___|__")
                        print(dict["position_7"],"|",dict["position_8"],"|",dict["position_9"])
                        print("  |   |  ")
                        break
                    
                    elif dict["position_7"]==dict["position_8"]==dict["position_9"]!=" ":
                        print(" ",dict["position_1"],"wins!")
                        print(dict["position_1"],"|",dict["position_2"],"|",dict["position_3"])
                        print("__|___|__")
                        print(dict["position_4"],"|",dict["position_5"],"|",dict["position_6"])
                        print("__|___|__")
                        print(dict["position_7"],"|",dict["position_8"],"|",dict["position_9"])
                        print("  |   |  ")
                        break
                    
                    elif dict["position_3"]==dict["position_5"]==dict["position_7"]!=" ":
                        print(" ",dict["position_1"],"wins!")
                        print(dict["position_1"],"|",dict["position_2"],"|",dict["position_3"])
                        print("__|___|__")
                        print(dict["position_4"],"|",dict["position_5"],"|",dict["position_6"])
                        print("__|___|__")
                        print(dict["position_7"],"|",dict["position_8"],"|",dict["position_9"])
                        print("  |   |  ")
                        break
                              
                
                
                    if dict["position_{}".format(5)]==" ":
                        dict["position_{}".format(5)]=computer
                        print("if statement in except passed")
                        
                    else: 
                        while True:
                    
                            if dict["position_{}".format(R)]==" " and dict["position_{}".format(R)]!=player and dict["position_{}".format(R)]!=computer:
                                dict["position_{}".format(R)]=computer
                                break
                            else:
                                R=randint(1,9)
                        print("else statement in except passed")

                    print(dict["position_1"],"|",dict["position_2"],"|",dict["position_3"])
                    print("__|___|__")
                    print(dict["position_4"],"|",dict["position_5"],"|",dict["position_6"])
                    print("__|___|__")
                    print(dict["position_7"],"|",dict["position_8"],"|",dict["position_9"])
                    print("  |   |  ")
                
                    if dict["position_1"]==dict["position_2"]==dict["position_3"]!=" ":
                        print(" ",dict["position_1"],"wins!")
                        break
                    elif dict["position_1"]==dict["position_5"]==dict["position_9"]!=" ":
                        print(" ",dict["position_1"],"wins!")
                        break
                    elif dict["position_1"]==dict["position_4"]==dict["position_7"]!=" ":
                        print(" ",dict["position_1"],"wins!")
                        break
                    elif dict["position_2"]==dict["position_5"]==dict["position_8"]!=" ":
                        print(" ",dict["position_2"],"wins!")
                        break
                    elif dict["position_3"]==dict["position_6"]==dict["position_9"]!=" ":
                        print(" ",dict["position_3"],"wins!")
                        break
                    elif dict["position_4"]==dict["position_5"]==dict["position_6"]!=" ":
                        print(" ",dict["position_4"],"wins!")
                        break
                    elif dict["position_7"]==dict["position_8"]==dict["position_9"]!=" ":
                        print(" ",dict["position_7"],"wins!")
                        break
                    elif dict["position_3"]==dict["position_5"]==dict["position_7"]!=" ":
                        print(" ",dict["position_3"],"wins!")
                        break
                else: 
                    print("Match Draw")
                    break
            else:
                print("Please enter position which is empty!")
        else:
            print("Out of range")
