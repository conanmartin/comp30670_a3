import argparse
from name.main import *
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input help')
args = parser.parse_args()

filename = args.input


def read_url_execute(uri):

    req = urllib.request.urlopen(uri)

    buffer = req.read().decode('utf-8')

    for line in buffer.split('\n'):
            if len(line.split()) == 0:
                print("Input ended")
                map_and_count(size)
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
                        x1, y1 = line.split()[2].split(',')
                        x2, y2 = line.split()[4].split(',')
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        turn_on(x1, y1, x2, y2, size)

                    elif line.split()[1] == "off":
                        x1, y1 = line.split()[2].split(',')
                        x2, y2 = line.split()[4].split(',')
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        turn_off(x1, y1, x2, y2, size)

                elif line.split()[0] == "switch":
                    x1, y1 = line.split()[1].split(',')
                    x2, y2 = line.split()[3].split(',')
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    switch(x1, y1, x2, y2, size)

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
                        #turn_on(x1,y1,x2,y2)

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



