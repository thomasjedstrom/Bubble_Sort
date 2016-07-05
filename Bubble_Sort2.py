import random
import datetime

sample_list = []

def pop(x):
    for counter in range(0,100):
        random_num = random.randint(0,10000)
        x.append(random_num)
    print sample_list
    
pop(sample_list)


def Bubble_Sort(x):
    startTime = datetime.datetime.now()
    for counter in range(0, (len(x)-1)):
        for z in range(0, len(x)-1):
            if x[z]>x[z+1]:
                temp = x[z]
                x[z] = x[z+1]
                x[z+1] = temp
    print x
    endTime = datetime.datetime.now()
    calcdTime = endTime - startTime
    print 'This operation took ' + str(calcdTime) + ' seconds to complete'

Bubble_Sort(sample_list)