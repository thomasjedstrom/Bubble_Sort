import random
import datetime

sample_list = []

def pop(x):
    for counter in range(0,100):
        random_num = random.randint(0,10000)
        x.append(random_num)
    print '\nThis is your Sample List'
    print sample_list
    
pop(sample_list)

def Bubble_Sort(a):
    startTime = datetime.datetime.now()
    for counter in range(0, (len(a)-1)):
        for z in range(0, len(a)-1):
            if a[z]>a[z+1]:
                temp = a[z]
                a[z] = a[z+1]
                a[z+1] = temp
    print '\nThis is your Selection_Sort'
    print a
    endTime = datetime.datetime.now()
    calcdTime = endTime - startTime
    print 'This operation took ' + str(calcdTime) + ' seconds to complete'

Bubble_Sort(sample_list)


def Selection_Sort(a):
    startTime = datetime.datetime.now()
    for x in range(0, len(a)):
        y = len(a)-1-x
        if x<y:
            for z in range(x, y+1):
                if a[z] < a[x]:
                    a[z], a[x] = a[x], a[z]
                if a[z] > a[y]:
                    a[z], a[y] = a[y], a[z]
    print '\nThis is your Selection_Sort'
    print a
    endTime = datetime.datetime.now()
    calcdTime = endTime - startTime
    print 'This operation took ' + str(calcdTime) + ' seconds to complete'
Selection_Sort(sample_list)
