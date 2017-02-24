from name.reader import read
from nose.tools import *
from name.main import *
from name.reader import *

def test_read():
    #Are files and they're lines being read?
    read("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")


def test_parse():
    '''Test is parsing'''

def test_count():
    '''test if correct amount of lights are on for given input'''