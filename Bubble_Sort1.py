myList = [6, 5, 3, 1, 8, 7, 2, 4]

def BubbleSort(x):
    for counter in range(0, len(x)):
        negcounter = len(x)
        negcounter -= counter
        if negcounter == 0:
            break
        for z in range(0, (len(x)-1-counter)):
            temp = x[z]
            x[z] = x[z+1]
            x[z+1] = temp
            print x

BubbleSort(myList)
