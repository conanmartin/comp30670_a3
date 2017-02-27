'''
Author: Conan Martin
Email: conan.martin@ucdconnect.ie
Created 20th February 2017
'''

#size = 50
#map1 = []

def create(size, map1):
    '''Creates list in map1 to the size specified by input'''

    print("Creating map of size", size, "*", size)
    for x in range(size):
        for y in range(size):
            map1 += False,
            new_map = map1
            return new_map

def turn_on(x1, y1, x2, y2, size):
    '''Turns on lights in range defined.'''
    x1 = coord_check(x1, size)
    x2 = coord_check(x2, size)
    y1 = coord_check(y1, size)
    y2 = coord_check(y2, size)

    for i in range(size * y1, size * y2 + 1, size):
        for j in range(x1 + i, x2 + i + 1):
            map1[j] = True

def turn_off(x1, y1, x2, y2, size):
    '''Turns off lights in range defined'''
    x1 = coord_check(x1, size)
    x2 = coord_check(x2, size)
    y1 = coord_check(y1, size)
    y2 = coord_check(y2, size)


    print("Turning off", x1, ",", y1, "to", x2, ",", y2)

    for i in range(size * y1, size * y2 + 1, size):
        for j in range(x1 + i, x2 + i + 1):
            map1[j] = False

def switch(x1, y1, x2, y2, size):
    '''for range defined, switches lights from off to on and vice versa'''
    x1 = coord_check(x1, size)
    x2 = coord_check(x2, size)
    y1 = coord_check(y1, size)
    y2 = coord_check(y2, size)
    print("Switching", x1, ",", y1, "to", x2, ",", y2)

    for i in range(size * y1, size * y2 + 1, size):
        for j in range(x1 + i, x2 + i + 1):
            if not map1[j]:
                map1[j] = True
            else:
                map1[j] = False
def map_and_count(size):
    '''Visualistation of LED grid'''
    for j in range(len(map1)):
        if map1[j]:
            print("X", " ", end="")
        else:
            print("-", " ", end="")
        if (j + 1) % (size) == 0:
            print("")

    print("Lights on:", sum(map1))

def coord_check(n, size):
    '''checks if coordinates are within range of grid. If not, makes them so.'''
    if n < 0:
        return 0
    elif n >= size:
        return size - 1
    else:
        return n


#create(size, map1)

#turn_on(1,1,11,11)

#turn_off(6,1,8,5)

#switch(9,9,59,54)

#print_map()

#print("Lights on:", sum(map1))







