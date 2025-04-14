for x in range (1, 11):
    print(x)

    print('Yooh Mavo')

    #  reverse
    for x in reversed(range(1,11)): 
        print(x)
        
        # skip
        for x in range (1 , 21):
            if x ==13:
                continue 
            else:
                print(x)

                # break
                for x in range (1, 21):
                    if x ==13:
                        break
                else:
                    print(x)