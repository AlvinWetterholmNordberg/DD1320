from array import array


class ArrayQ:
    def __init__(self):
        self.__queue = array("i")
        self.__front = 0
        self.__rear = -1
        self.__size = 0

    def __str__(self):
        if self.is_Empty():
            print("[]")
        else:
            items = []
            for i in range(self.__size):
                items.append(self.__queue[self.__front + i])
            return str(items)

    def is_Empty(self):
        return self.__size == 0

    def enqueue(self, item):
        self.__queue.append(item)
        self.__rear += 1
        self.__size += 1

    def dequeue(self):
        if self.is_Empty():
            raise Exception("Kön är tom, det finns inget element att ta bort.")

        first_obj = self.__queue[self.__front]
        self.__front += 1
        self.__size -= 1

        if self.is_Empty():
            self.__queue = array("i")
            self.__front = 0
            self.__rear = -1

        return first_obj

    def peek(self):
        if self.is_Empty():
            raise Exception("Kön är tom, det finns inget första element att kika på. ")
        else:
            return self.__queue[self.__front]

    def get_size(self):
        return self.__size


# För LinkedQ, en kö av noder (länkad lista)


"""
Själva LinkedQ-klassen ska ha två privata attribut: first som håller reda på den första noden i kön och last som pekar ut den sista. 
Använd samma gränssnitt som i uppgift 1, med enqueue, dequeue osv.

Det är extra knepigt att programmera enqueue(x) eftersom det blir två fall, 
beroende på om kön är tom eller inte. Rita upp bägge fallen (lådor med pilar) innan du skriver koden!   
"""


class Node:  # Detta är själva objektet med datan och minnesadressenadressen i next.
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedQ:
    def __init__(self):
        # p is a variable pinting at the first node object
        # q is a variable pointing at the last node object
        self.__first = None
        self.__last = None

    def __str__(self):
        onTableString = ""
        # Vi gör en egen pekare som heter current
        current = self.__first
        while current:
            onTableString += f"{str(current.data)}  "
            current = current.next
        return onTableString

    def isEmpty(self):
        return self.__first == None

    def enqueue(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.__first = newNode
            self.__last = newNode

        else:
            self.__last.next = newNode
            self.__last = newNode

    def dequeue(self):
        # returnera det sista objektet i listan
        # den kvarstående listan skall inte innehålla det dequeade elementet
        if self.isEmpty():
            raise Exception("Kön är tom. Det finns inget kö-objekt att ta bort.")
        else:
            firstObj = self.__first
            self.__first = self.__first.next
            if self.isEmpty():
                self.__last = None
            return firstObj.data


"""class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        nytt = Node(data)
        nytt.next = self.top
        self.top = nytt
"""

if __name__ == "__main__":
    # kör testkod direkt i denna modul här
    print("--- TESTKOD --- \n")

    myLinkedQ = LinkedQ()
    myLinkedQ.enqueue(5)
    myLinkedQ.enqueue(7)
    myLinkedQ.enqueue(2)
    myLinkedQ.enqueue(9)

    deqeueuatElement = myLinkedQ.dequeue()

    print(myLinkedQ)
    print(deqeueuatElement)
    myLinkedQ.enqueue(deqeueuatElement)
    print(myLinkedQ)
