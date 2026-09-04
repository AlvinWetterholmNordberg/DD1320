from bintreeFile import binTree
import re


def makeTree():
    tree = binTree()
    data = input().strip()
    while data != "#":
        tree.put(data)
        data = input().strip()
    return tree


def searches(tree):
    findme = input().strip()
    while findme != "#":
        if findme in tree:
            print(findme, "found")
        else:
            print(findme, "not found")
        findme = input().strip()


def uppg2():
    svenska = binTree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()  # Ett trebokstavsord per rad
            if ordet in svenska:
                print(ordet, end=" ")
            else:
                svenska.put(ordet)  # in i sökträdet
    print("\n")


def getWords(file_path):
    with open(file_path, "r") as file:
        for line in file:
            for word in line.split():
                yield word


def uppg3():
    # 1. Bygger det svenska sökträdet
    svenska = binTree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()  # Ett trebokstavsord per rad
            if ordet not in svenska:
                svenska.put(ordet)

    # 2. Skapar det engelska sökträdet och läs in engelska.txt
    engelska = binTree()
    with open("engelska.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # ord-splitter som rensar bort irriterande skiljetecken (som punkter, kommatecken och citattecken) från engelska.txt och ger dig en ren lista med ord redo för att sökas i trädet.
    words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text)
    for word in words:
        print(word)
    # 3. Gå igenom orden, kontrollera dubbletter och svenska ord
    for word in words:
        ordet = word.lower()
        # Om ordet inte finns i engelskaträdet så ger vi den en plats där. Detta undviker dubletter
        if ordet not in engelska:
            engelska.put(ordet)
            # Om rodet finns i det svenska ordträdet så skriver vi ut det.
            if ordet in svenska:
                print(ordet, end=" ")
    print("\n")


uppg3()
