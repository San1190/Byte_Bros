#import time
import timeit
def prueba_for(n):
    l = []

    for n in range(1 , n+1):
        l.append(n)

    return l


def prueba_while(n):
    l = []
    c = 1

    while c <= n:
        l.append(c)
        c += 1

    return l

#inicio = time.time()
#prueba_for(100000000)
#final = time.time()
#
#print(final- inicio)
#
#
#
#inicio = time.time()
#prueba_while(100000000)
#final = time.time()
#
#print(final- inicio)

declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(n):
    l = []

    for n in range(1 , n+1):
        l.append(n)

    return l

'''


duracion = timeit.timeit(declaracion , mi_setup, number = 100000)
print(duracion)
#print(prueba_for(15))
#print(prueba_while(15))