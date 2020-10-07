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
				

print('It was time for a change, the electrical impulses were strong.\n\
        Mac exclaimed “Now this is epic” and turned around to quickly grab his black minecraft glasses from his desk, he was ready.\n\
        Printer Man was on a suicide mission to destroy all the code and he needed to be stopped!.\n\
        A - How he felt.\n\
        B - What changes he went through?\n\
        C - How powerful was he')
choice = checkInput(3)
if (choice == "A"):
	print("        He started to feel like his whole DNA was being re-written.\n\
              His arms began to elongate and you could start to see the 1’s and 0’s pushing through his skin and re-writing his base code..\n\
              He saw a shining light coming from his chest and creating a space in his skin glow red on his chest?\n\
              A -  To get him closer to his goal of destroying Printer Man.")
        #choice = checkInput(1)
elif (choice == "B"):
	print("        He could feel the energy pulsing through his veins, surging energy to his heart\n\
              Macs body started to physically change and a strong red armour shone through.\n\
              A - To annihilate the man from his visions “Printer Man”")
	choice = checkInput(1)
elif (choice == "C"):
	print('        Mac slammed his fist into the Yasuo poster on his wall\n\
              "his fist went straight through the wall without a scratch on his armour\n\
              A - The man from his visions, Printer-Man.')
	choice = checkInput(1)
else:
        pass
if (choice == "A"):
        print("        “Macs head was surging with energy and his heart was racing like Lightning McQueen.\n\
                He felt energized.\n\
                A - How he felt.")
        choice = checkInput(1)
