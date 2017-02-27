import urllib.request




def read_url_execute(uri):

    req = urllib.request.urlopen(uri)

    buffer = req.read().decode('utf-8')

    for line in buffer.split('\n'):
            if len(line.split()) == 0:
                print("Finished calculating!")
                map_and_count(size, new_map, uri)
            else:
                if len(line.split()) == 1:
                    if 0 >= int(line) > 999999:
                        print("Grid size out of range")
                    else:
                        print("Running...")
                        size = (int(line))
                        map1 = []
                        new_map = create(size, map1)

                elif line.split()[0] == "turn":
                    if line.split()[1] == "on":
                        line = line.replace(',', ' ')
                        x1, y1 = line.split()[2], line.split()[3]
                        x2, y2 = line.split()[5], line.split()[6]
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        if x2 >= x1 and y2 >= y1:
                            turn_on(x1, y1, x2, y2, size, new_map)

                    elif line.split()[1] == "off":
                        line = line.replace(',', ' ')
                        x1, y1 = line.split()[2], line.split()[3]
                        x2, y2 = line.split()[5], line.split()[6]
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        if x2 >= x1 and y2 >= y1:
                            turn_off(x1, y1, x2, y2, size, new_map)

                elif line.split()[0] == "switch":
                    line = line.replace(',', ' ')
                    x1, y1 = line.split()[1], line.split()[2]
                    x2, y2 = line.split()[4], line.split()[5]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    if x2 >= x1 and y2 >= y1:
                        switch(x1, y1, x2, y2, size, new_map)

def read_url_count(uri):
    req = urllib.request.urlopen(uri)

    buffer = req.read().decode('utf-8')
    count = 0
    for line in buffer.split('\n'):
        count += 1

    print ("Number of lines read:", count)

def read_url_commands(uri):

    req = urllib.request.urlopen(uri)

    buffer = req.read().decode('utf-8')

    for line in buffer.split('\n'):
            if len(line.split()) == 0:
                print("Input ended")
            else:
                print(line)
                print(len(line.split()))
                for i in range(len(line.split())):
                    print(line.split()[i])
                if len(line.split()) == 1:
                    if 0 > int(line) > 999999:
                        print("Grid size out of range")

                elif line.split()[0] == "turn":
                    if line.split()[1] == "on":
                        '''turn on()'''
                        print("Command is turn on")
                        x1, y1 = line.split()[2].split(',')
                        print("x1 is:", x1, ", y1 is:", y1)
                        x2, y2 = line.split()[4].split(',')
                        print("x2 is:", x2, ", y2 is:", y2)
                        print("")

                    elif line.split()[1] == "off":
                        '''turn off()'''
                        print("Command is turn off")
                        x1, y1 = line.split()[2].split(',')
                        print("x1 is:", x1, ", y1 is:", y1)
                        x2, y2 = line.split()[4].split(',')
                        print("x2 is:", x2, ", y2 is:", y2)
                        print("")

                elif line.split()[0] == "switch":
                    '''switch()'''
                    print("Command is switch")

                    x1, y1 = line.split()[1].split(',')
                    print("x1 is:", x1, ", y1 is:", y1)
                    x2, y2 = line.split()[3].split(',')
                    print("x2 is:", x2, ", y2 is:", y2)

                    print("")




def read_file(filename):
    buffer = open(filename).read()
    print(len(buffer.split()))
    for line in buffer.split('\n'):
        print(line)
        print(len(line.split()))
        for i in range(len(line.split())):
            print(line.split()[i])
        if len(line.split()) == 1:
            if 0 > int(line) > 999999:
                print("Grid size out of range")
            else:
                size = (int(line))
                map1 = []
                create(size, map1)
        elif line.split()[0] == "turn":
            if line.split()[1] == "on":
                command = line.split()[0]
                print("Command is", command)
            elif line.split()[1] == "off":
                '''turn off()'''
                command = line.split()[0]
                print("Command is", command)
        elif line.split()[0] == "switch":
            '''switch()'''
        command = line.split()[0]
        print("Command is", command)


def read_file_execute(filename):
    buffer = open(filename).read()
    for line in buffer.split('\n'):
        if len(line.split()) == 0:
            print("Input ended")
            map_and_count(size, new_map, filename)
        else:
            if len(line.split()) == 1:
                if 0 > int(line) > 999999:
                    print("Grid size out of range")
                else:
                    size = (int(line))
                    map1 = []
                    new_map = create(size, map1)

            elif line.split()[0] == "turn":
                if line.split()[1] == "on":
                    line = line.replace(',', ' ')
                    x1, y1 = line.split()[2], line.split()[3]
                    x2, y2 = line.split()[5], line.split()[6]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    turn_on(x1, y1, x2, y2, size, new_map)

                elif line.split()[1] == "off":
                    line = line.replace(',', ' ')
                    x1, y1 = line.split()[2], line.split()[3]
                    x2, y2 = line.split()[5], line.split()[6]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    turn_off(x1, y1, x2, y2, size, new_map)

            elif line.split()[0] == "switch":
                line = line.replace(',', ' ')
                x1, y1 = line.split()[1], line.split()[2]
                x2, y2 = line.split()[4], line.split()[5]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                switch(x1, y1, x2, y2, size, new_map)

def create(size, map1):
    '''Creates list in map1 to the size specified by input'''

    #print("Creating map of size", size, "*", size)
    for x in range(size):
        for y in range(size):
            map1 += False,
            new_map = map1
    return new_map

def turn_on(x1, y1, x2, y2, size, new_map):
    '''Turns on lights in range defined.'''
    x1 = coord_check(x1, size)
    x2 = coord_check(x2, size)
    y1 = coord_check(y1, size)
    y2 = coord_check(y2, size)

    #print("Turning on", x1, ",", y1, "to", x2, ",", y2)

    for i in range(size * y1, size * y2 + 1, size):
        for j in range(x1 + i, x2 + i + 1):
            new_map[j] = True
    return new_map

def turn_off(x1, y1, x2, y2, size, new_map):
    '''Turns off lights in range defined'''
    x1 = coord_check(x1, size)
    x2 = coord_check(x2, size)
    y1 = coord_check(y1, size)
    y2 = coord_check(y2, size)


    #print("Turning off", x1, ",", y1, "to", x2, ",", y2)

    for i in range(size * y1, size * y2 + 1, size):
        for j in range(x1 + i, x2 + i + 1):
            new_map[j] = False
    return new_map

def switch(x1, y1, x2, y2, size, new_map):
    '''for range defined, switches lights from off to on and vice versa'''
    x1 = coord_check(x1, size)
    x2 = coord_check(x2, size)
    y1 = coord_check(y1, size)
    y2 = coord_check(y2, size)
    #print("Switching", x1, ",", y1, "to", x2, ",", y2)

    for i in range(size * y1, size * y2 + 1, size):
        for j in range(x1 + i, x2 + i + 1):
            if not new_map[j]:
                new_map[j] = True
            else:
                new_map[j] = False
    return new_map

def map_and_count(size, new_map, uri):
    '''Visualistation of LED grid'''
    '''
    for j in range(len(new_map)):
        if new_map[j]:
            print("X", " ", end="")
        else:
            print("-", " ", end="")
        if (j + 1) % (size) == 0:
            print("")
    '''
    print("File executed:", uri)
    print("Lights on:", sum(new_map))

def coord_check(n, size):
    '''checks if coordinates are within range of grid. If not, makes them so.'''
    if n < 0:
        return 0
    elif n >= size:
        return size - 1
    else:
        return n

