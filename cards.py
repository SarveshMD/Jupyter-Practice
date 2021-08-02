# Importing required modules #
import random
import time

# Defining required class #
# =============================================================== #

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'
# =============================================================== #

# Setting it up #
sets = ['Heart', 'Diamond', 'Spade', 'Club']
numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = []
for set in sets:
	for number in numbers:
		cards.append(f"{set} {number}")

shuffledCards = list()
shuffledCards.extend(cards)
random.shuffle(shuffledCards)
shuffledCards1 = shuffledCards[:21]
for card in shuffledCards1:
	print(color.BLUE + card + color.END)

print(color.CYAN + "\nChoose a card from the listed cards and remember it or write it down somewhere !")
print("I am going to find what card you chose :)")
print("Hit enter when you're ready !" + color.END)
input()
print("\n")
random.shuffle(shuffledCards1)


# Defining required functions #
# =============================================================== #

def splitIntoThree(deck):
	num = 0
	deck1 = list()
	deck2 = list()
	deck3 = list()
	for card in deck :
		num += 1
		if num == 1:
			deck1.append(card)
		if num == 2:
			deck2.append(card)
		if num == 3:
			deck3.append(card)
		if num > 3:
			num = 1
			deck1.append(card)
	print("  {}Deck 1     {}|   {}Deck 2      {}|    {}Deck 3 ".format(color.RED, color.END, color.GREEN, color.END, color.BLUE))
	for card1, card2, card3 in zip(deck1, deck2, deck3):
		print(color.RED + card1, " "* (15-len(card1)), color.GREEN + card2, " " *(15-len(card2)), color.BLUE + card3 + color.END)
	return deck1, deck2, deck3
# =============================================================== #

def whereIs(splitNDeck1, splitNDeck2, splitNDeck3):
	n = 1
	while True:
		while True:
			if n>1:
				print(color.RED + "Invalid deck number ! (re-enter deck number)")
			else:
				print()
				print(color.GREEN + "Which deck the card you chose is ?\n(Enter the deck number)")
			deckNo = input()
			if deckNo == "1" or deckNo == "2" or deckNo == "3":
				deckNo = int(deckNo)
				break
			else:
				n += 1
				continue
		print()
		print(color.PURPLE + "Are you sure that the card you chose is in this deck ?")

		if deckNo == 1:
			for card in splitNDeck1:
				print(color.RED + card)
		elif deckNo == 2:
			for card in splitNDeck2:
				print(color.GREEN + card)
		elif deckNo == 3:
			for card in splitNDeck3:
				print(color.BLUE + card)

		while True:
			print()
			confirm = input(color.END + "({}y{}/{}n{})\n".format(color.GREEN,color.END,color.RED,color.END))
			print()
			if confirm.lower() == "y" or confirm.lower() == "n":
				break
			else:
				continue
		if confirm.lower() == "n":
			continue
		else:
			break
	return deckNo
# =============================================================== #

def orderDecks(shuffledCardsN, splitNDeck1, splitNDeck2, splitNDeck3, deckNo):
	if deckNo == 1:
		shuffledCardsN.extend(splitNDeck2)
		shuffledCardsN.extend(splitNDeck1)
		shuffledCardsN.extend(splitNDeck3)
	if deckNo == 2:
		shuffledCardsN.extend(splitNDeck1)
		shuffledCardsN.extend(splitNDeck2)
		shuffledCardsN.extend(splitNDeck3)
	if deckNo == 3:
		shuffledCardsN.extend(splitNDeck2)
		shuffledCardsN.extend(splitNDeck3)
		shuffledCardsN.extend(splitNDeck1)

	return shuffledCardsN

# =============================================================== #

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-  Round 1  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
split1 = splitIntoThree(shuffledCards1)
split1Deck1 = split1[0]
split1Deck2 = split1[1]
split1Deck3 = split1[2]

deckNo = whereIs(split1Deck1, split1Deck2, split1Deck3)

shuffledCards2 = list()
shuffledCards2 = orderDecks(shuffledCards2, split1Deck1, split1Deck2, split1Deck3, deckNo)

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-  Round 2  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
split2 = splitIntoThree(shuffledCards2)
split2Deck1 = split2[0]
split2Deck2 = split2[1]
split2Deck3 = split2[2]

deckNo = whereIs(split2Deck1, split2Deck2, split2Deck3)

shuffledCards3 = list()
shuffledCards3 = orderDecks(shuffledCards3, split2Deck1, split2Deck2, split2Deck3, deckNo)


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-  Round 3  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
split3 = splitIntoThree(shuffledCards3)
split3Deck1 = split3[0]
split3Deck2 = split3[1]
split3Deck3 = split3[2]

deckNo = whereIs(split3Deck1, split3Deck2, split3Deck3)

shuffledCards4 = list()
shuffledCards4 = orderDecks(shuffledCards4, split3Deck1, split3Deck2, split3Deck3, deckNo)

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

print(color.YELLOW + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(color.BLUE + "The card you chose is :\n")

heart = [
	color.RED,
	'        00000000000           000000000000',
	'      00000000     00000   000000     0000000',
	'    0000000             000              00000',
	'   0000000               0                 0000',
	'  000000                                    0000',
	'  00000                                      0000',
	' 00000                                      00000',
	f' 00000{((37-len(shuffledCards4[10]))//2)*" "}{color.CYAN}{shuffledCards4[10]}{color.END}{color.RED}{((37-len(shuffledCards4[10]))//2)*" "}000000',
	'  000000                                 0000000',
	'   0000000                              0000000',
	'     000000                            000000',
	'       000000                        000000',
	'          00000                     0000',
	'             0000                 0000',
	'               0000             000',
	'                 000         000',
	'                    000     00',
	'                      00  00',
	'                        00',
	f'{color.END}\n'
	]

for line in heart:
	time.sleep(0.02)
	print(line)
