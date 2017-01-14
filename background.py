from random import randint

def get_background():
	bg = ["#53DF83", "#47D2E9", "#44BBFF", "#FC575E", "#E7F76D", "#EAF2BB", "#F0F1F5", "#D1D6A9", "#F7BC05", "#B8959B"]
	index = randint(0, len(bg)-1)
	print("bg is:" + str(index))
	return bg[index]