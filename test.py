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
				

print('"MUM" Mac yelled as he scanned through boxes of wires to find his USB wire.\n\
        Mac took another quick glance around his room, hoping to find his cable.\n\
        Mac recently came back from a phishing trip with his colleagues, which he claims he enjoyed very much.\n\
        \n\
        A - Look at the poster.\n\
        B - On my desk perhaps?\n\
        C - Under the bed?')
choice = checkInput(3)
if (choice == "A"):
	print("        Mac stares at the poster of his Hyper-Advanced AI powered Turbo-Inkjet printer.\n\
              He wondered to himself why anyone would need an AI powered printer but the search for the cable was more important.\n\
              In fact who even has a poster of a printer anyway?\n\
              \n\
              A -  Frustrated he did what anyone in his situation would, MUMMMMMY.")
	choice = checkInput(1)
elif (choice == "B"):
	print("        The desk is cluttered with PC components, empty bottles of powerade and half eaten cups of instant noodles.\n\
              Unfortunately the cable is not here.\n\
              \n\
              A - There is but one option MUMMMMMY.")
	choice = checkInput(1)
elif (choice == "C"):
	print('        All his could find was dustBits under his bed, and a familiar box at the back, tucked away in secret with the words\n\
              "Private, P.S that means for you too Mom". He looked away in shame and carried on with his search.\n\
              \n\
              A - Reminded of his mother he had one choice, MUMMMMMY.')
	choice = checkInput(1)
else:
        pass
if (choice == "A"):
        print("        “Malcom, you left it under your pillow” his mother screamed up the stairs.\n\
                Of course it was, he knew that.\n\
                \n\
                A - Look under the pillow.")
        choice = checkInput(1)
else:
        pass
if (choice == "A"):
        print("        Mac flipped over his pillows to find the wire exactly there,\n\
                he desperately wanted to upload the pictures from the trip to print and frame them for the office.\n\
                Mac wasn’t the most popular at work, being one of the youngest and least experienced, but he wouldn’t give up.\n\
                \n\
                \n\
                      He grabbed his camera and started flicking through the images.\n\
                \n\
                A - Put the camera down.\n\
                B - Inspect the photos.")
        choice = checkInput(2)

if (choice == "B"):
        print("        Mac looks through the photos, hoping to find some instance of him having a good time but as he scrolled he came to the slow realisation he wasntin any of the photos.\n\
                He was always the photographer but never the photographee.\n\
                \n\
                \n\
                A - Feeling even worse than when he had started he decided to put the camera down")
        choice = checkInput(1)
else:
        pass
if (choice == "A"):
        print("        He was alone. He was unwanted. He didn’t belong.\n\
                \n\
                “Why do I bother trying, they're never going to accept me” Mac contemplated to himself.\n\
                \n\
                After a few moments he cleared his head and got back up, wire in hand ready for the next step.\n\
                \n\
                RING RING\n\
                \n\
                He looked at his phone, it was work. He stood for a moment, he knows whatever it is it can't be good.\n\
                \n\
                \n\
                A - Answer the phone, how bad could it really be.\n\
                B - Ignore it, if its important they will call back.")
        choice = checkInput(2)
else:
        pass
if (choice == "A"):
        print('        He wasnt in the mood to talk to work right now. He just wanted to be alone with his thoughts and his camera.\n\
                He may be alone but he will always have his computer to keep him company.\n\
                \n\
                At that moment a text message popped up on his phone.\n\
                \n\
                “Malcom, I hate to be the bearer of bad news but we have had multiple issues with our computers at work, rendering them nonfunctional.\n\
                To cover the cost of the new servers and computers we have had to make cuts to the team.\n\
                I am sorry Malcom, being one of the last to join it makes sense, we have to let you go. Take care. Goodbye.”\n\
                \n\
                A - ...what?')
        choice = checkInput(1)
elif (choice == "B"):
        print('        “Hello” Mac responded as he answered his phone.\n\
                \n\
                “Malcom, I hate to be the bearer of bad news but we have had multiple issues with our computers at work, rendering them nonfunctional.\n\
                To cover the cost of the new servers and computers we have had to make cuts to the team.\n\
                I am sorry Malcom, being one of the last to join it makes sense, we have to let you go. Take care. Goodbye.”\n\
                \n\
                A - ...what?')
        choice = checkInput(1)
else:
        pass
if (choice == "A"):
        print('        Mac was frozen, in shock, heart pounding like air was never going to reach his lungs and this was it for him.\n\
                \n\
                He collapsed on his GT omega racing chair trying to comprehend the phone call he had just received.\n\
                \n\
                Moments passed and he still remained in shock.\n\
                He told himself it couldn’t be real, it was just a prank, they play them on him all the time.\n\
                He decided to continue what he was doing before, acting as though the phone call never happened.\n\
                \n\
                “It was just a joke,” Mac told himself.\n\
                \n\
                A - Open Latch')
        choice = checkInput(1)
              
