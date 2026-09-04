class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __contains__(self, value):
        # True om value finns i trädet, False annars
        return finns(self.root, value)

    def put(self, newvalue):
        # När trädobjektets put("gurka") anropas skickar trädet sin rotpekare och det nya ordet till funktionen putta som ser till att en ny nod skapas på rätt ställe.
        # Sorterar in newvalue i trädet
        self.root = putta(self.root, newvalue)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


# Hjälpfunktioner


def putta(p, newvalue):
    # Funktion som gör själva jobbet att stoppa in en ny nod

    # Om trädet är tomt
    # Om newvalue är större än
    # Om newvalue är mindre än
    if p is None:
        return Node(newvalue)
    if newvalue < p.value:
        p.left = putta(p.left, newvalue)

    if newvalue > p.value:
        p.right = putta(p.right, newvalue)

    return p


def finns(p, key):
    # Funktion för att söka efter ett värde. Returnerar true eller false.

    # Basfall 1: om listan är tom finns inte värdet i den
    if p is None:
        return False

    # Basfall 2: Om key överränsstämmer med nodens value 'p.value'
    if key == p.value:
        return True

    # Scenario (most common): Om key inte överräns stämmer med p.value.

    # Om key är mindre än nodens value
    if key < p.value:
        return finns(p.left, key)
    else:
        return finns(p.right, key)


def skriv(p):
    # Funktion som gör själva jobbet att skriva ut trädet.

    if p is not None:
        skriv(p.left)  # Skriver ut alla barn till vänster
        print(p.value, end=" ")  # Skriver ut rootnode
        skriv(p.right)  # Skriver ut alla barn till höger


if __name__ == "__main__":

    print("Testkod: ")
    # kör testkod direkt i denna modul här
    svenska = binTree()  # Skapa ett trädobjekt
    svenska.put("gurka")  # Sortera in "gurka" i trädet
    svenska.put("hallongrotta")
    svenska.put("kuk")

    if "gurka" in svenska:  # Kolla om "gurka" finns i trädet
        # (Operatorn in anropar metoden __contains__ som du ska implementera i din Bintree-klass)
        svenska.write()  # Skriver alla trädobjektets ord i bokstavsordning
