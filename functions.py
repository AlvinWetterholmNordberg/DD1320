from classes import LinkedQ


def print_queue(input_array):
    print(list(input_array))


def testing_ArrayQ():
    q = LinkedQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if x == 1 and y == 2:
        print("OK")
    else:
        print("FAILED")


def getCardDeck(input):
    # Converts string input into an integer list of cards
    parts = input.split()
    strCardList = list(map(str, parts))
    cardDeck = LinkedQ()
    for card in strCardList:
        cardDeck.enqueue(card)
    return cardDeck


def runMagicTrick():
    cardDeck = getCardDeck(input("Skriv in korten 1-10 i den magiska ordningen: "))
    faceUpDeck = LinkedQ()

    while not cardDeck.isEmpty():
        # Moving the first card to the back

        toRear = cardDeck.dequeue()
        cardDeck.enqueue(toRear)
        # Taking the first card from the deck and place it in the solved dekc that is shown on the table
        faceUpDeck.enqueue(cardDeck.dequeue())
        # Show the table
        # print(f"The table: {faceUpDeck}")
        # Show the skipped card
        # print(f"To the back: {toRear}")
    print(faceUpDeck)


def listLen(p):
    if p == None:
        return 0
    else:
        return 1 + listLen(p.next)


def printList(p):
    if p == None:
        pass
    else:
        print(p.data)
        printList(p.next)
