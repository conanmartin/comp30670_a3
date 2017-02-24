import argparse
import urllib.request
def read(uri):

    req = urllib.request.urlopen(uri)

    buffer = req.read().decode('utf-8')

    for line in buffer.split('\n'):
        print(line)

read("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
'''
def read(filename):
    buffer = open(filename).read()
'''
