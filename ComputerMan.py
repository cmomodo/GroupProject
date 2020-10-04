def checkInput(size):
	choiceArray = ["A", "B", "C", "D", "E"]
	while True:
		inp = input("What choice?")
		inp = inp.upper()
		for x in range (size):
			if (inp == choiceArray[x]):
				return (inp)
				break			
		print("Not a valid input")
				

print('The printer stumbled as it tried to stand and after a few tries, it succeeded. That’s when it grew two, muscular arms.\n\
        A - Look at arms.\n\
        B - Do not look at arms')
choice = checkInput(2)
if (choice == "A"):
        #choice = checkInput(1)
	print("they were big enough to crush the average gaming mouse, big vascous veins littered the skin.\n")
elif (choice == "B"):
        pass
if (choice == "A" or "B"):
        print("It struts towards Mac in a gorilla-like fashion,the floorboards creak as it’s monstrous limbs touched the ground.Once it was less than a meter away from Mac, it let out a call that sounded like a mix between Internet dial-up and a Lion’s roar.\nYou cover your ears in pain, trying to mute the beast's call. After it’s call, a printed piece of paper flew out from it’s back\n\
        A - Look at note.\n\
        B - Do not look at note")
        choice = checkInput(2)
        if (choice == "A"):
                print("it says “Screw You Computer Man!”")
        elif (choice == "B"):
                print("I guess you'll never know what it said")
        if (choice == "A" or "B"):
                print("Your brain’s entire system changed to mimic Von Neumann’s architecture. Your clock rate was so fast, it was enough to make Intel cower. He had more cores than AMD could ever dream of adding. Your brain now fetched, decoded, and executed every thought he had. Every emotion you now feel became a complex order of processes that were passed into your brain.\n\
        A - Try to feel emotion.\n\
        B - Do not try to feel emotion")
                choice = checkInput(2)
                if (choice == "A"):
                        print("the only emotion you feel now is an unbridled hatred towards this abomination of a printer that stood before you. You let out an enraged yell and kick the printer, sending it flying out of the window.")
                elif (choice == "B"):
                        print("you try not to but the only emotion you still have access to is your unbridled hatred towards this abomination of a printer that stood before you. You let out an enraged yell and kicked the printer, sending it flying out of the window.")
                if (choice == "A" or "B"):
                        print('you notice another slip of paper near the window \n\
                        A - Look at paper.\n\
                        B - Do not look at paper')
                        choice = checkInput(2)
                        if (choice == "A"):
                                print("the note reads “I will return with an army of peripherals Computer Man, and then you will never be able to print phishing photos again!”")
                        elif (choice == "B"):
                                print("You don't read the note")
