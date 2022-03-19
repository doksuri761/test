import random
import os
import threading

listes = [1, 2, 3, 4]  * 5
random.shuffle(listes)
historyf = open("history", "w")
historyf.close()
historyf = open("history", "a")
history = []


def th():
	for i in range(int(input("Index: "))):
		rlist = [1, 2, 3, 4]
		rvalue = random.choice([1,2,3,4])
		rlist.remove(rvalue)
		listes.pop(random.choice(rlist))
		listes.append(rvalue)
		random.shuffle(listes)
		history.append(rvalue)
		msg = f"Index: {i + 1}, rValue: {rvalue}\n1: {round(history.count(1) / len(history) * 100, 3)}%, 2: {round(history.count(2) / len(history) * 100, 3)}%, 3: {round(history.count(3) / len(history) * 100, 3)}%, 4: {round(history.count(4) / len(history) * 100, 3)}%\n1: {history.count(1)}, 2: {history.count(2)}, 3: {history.count(3)}, 4: {history.count(4)}\nlist: {listes}\nLast List: [1: {listes.count(1)}, 2: {listes.count(2)}, 3: {listes.count(3)}, 4: {listes.count(4)}]"
		print(msg)
		historyf.write(msg)
		os.system("clear")	 
	file = open("output", "w")
	file.write(msg)
	file.close()
	historyf.close()
	print(msg)
	

th()
