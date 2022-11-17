from ast import Str
import time
import os


inputanswer = 0
print("---- QUIZ ----")
print("Press Enter to Start")
input()
score = 0
posscore = 0

while True:
	
	os.system('cls')
	time.sleep(1)
	print("When was Python founded")
	x = 0
	posanswer = ["A: 1981", "B: 1984", "C: 1983", "D: 1991"]
	correctanswer = "d"
	for x in posanswer:
		time.sleep(.5)
		print(x)
	inputanswer = input()
	inputanswer = inputanswer.lower()
	inputanswer = inputanswer.strip()
	if inputanswer == correctanswer:
		score += 1
		print("Correct")
	else:
		print("Incorrect, the correct answer was", correctanswer.upper())
	posscore += 1
	print("Total Score (", score, "/" , posscore, ")")
	time.sleep(1.5)
	os.system('cls')

	
	time.sleep(1)
	print("What companies use python")
	x = 0
	posanswer = ["A: Stack Overflow", "B: Youtube", "C: Minecraft", "D: Microsoft"]
	correctanswer = "b"
	for x in posanswer:
		time.sleep(.5)
		print(x)
	inputanswer = input()
	inputanswer = inputanswer.lower()
	inputanswer = inputanswer.strip()
	if inputanswer == correctanswer:
		score += 1
		print("Correct")
	else:
		print("Incorrect, the correct answer was", correctanswer.upper())
	posscore += 1
	print("Total Score (", score, "/" , posscore, ")")
	time.sleep(1.5)
	os.system('cls')


	time.sleep(1)
	print("Where was Python founded")
	x = 0
	posanswer = ["A: The Nether", "B: South America", "C: Netherland", "D: Portugal"]
	correctanswer = "c"
	for x in posanswer:
		time.sleep(.5)
		print(x)
	inputanswer = input()
	inputanswer = inputanswer.lower()
	inputanswer = inputanswer.strip()
	if inputanswer == correctanswer:
		score += 1
		print("Correct")
	else:
		print("Incorrect, the correct answer was", correctanswer.upper())
	posscore += 1
	print("Total Score (", score, "/" , posscore, ")")
	time.sleep(1.5)
	os.system('cls')

	time.sleep(1)
	print("What is one of the main uses for Python")
	x = 0
	posanswer = ["A: Websites", "B: C++ Coding", "C: Unity", "D: Game Development"]
	correctanswer = "a"
	for x in posanswer:
		time.sleep(.5)
		print(x)
	inputanswer = input()
	inputanswer = inputanswer.lower()
	inputanswer = inputanswer.strip()
	if inputanswer == correctanswer:
		score += 1
		print("Correct")
	else:
		print("Incorrect, the correct answer was", correctanswer.upper())
	posscore += 1
	print("Total Score (", score, "/" , posscore, ")")
	time.sleep(1.5)
	os.system('cls')

	time.sleep(1)
	print("Where does the python logo come from")
	x = 0
	posanswer = ["A: It was based on a image a fan sent", "B: Mayan Snakes", "C: The Ying and Yang", "D: Colors"]
	correctanswer = "b"
	for x in posanswer:
		time.sleep(.5)
		print(x)
	inputanswer = input()
	inputanswer = inputanswer.lower()
	inputanswer = inputanswer.strip()
	if inputanswer == correctanswer:
		score += 1
		print("Correct")
	else:
		print("Incorrect, the correct answer was", correctanswer.upper())
	posscore += 1
	print("Total Score (", score, "/" , posscore, ")")
	time.sleep(1.5)
	os.system('cls')

	time.sleep(1)
	print("Who created Python")
	x = 0
	posanswer = ["A: Gong Yoo", "B: Guido Van Rossum", "C: Vando Bundsen", "D: Ben Dover"]
	correctanswer = "b"
	for x in posanswer:
		time.sleep(.5)
		print(x)
	inputanswer = input()
	inputanswer = inputanswer.lower()
	inputanswer = inputanswer.strip()
	if inputanswer == correctanswer:
		score += 1
		print("Correct")
	else:
		print("Incorrect, the correct answer was", correctanswer.upper())
	posscore += 1
	print("Total Score (", score, "/" , posscore, ")")
	time.sleep(1.5)
	os.system('cls')

	break

print("---- QUIZ ----")
print("")
print("Final Score (", score, "/" , posscore, ")")
input()
