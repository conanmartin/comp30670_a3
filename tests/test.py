from nose.tools import *
from name.reader import *

def test_read(input):
    #Are files and their lines being read?
    read_url_count(input)


def test_commands(input):
    #are commands and coordinates being separated properly?
    read_url_commands(input)


def test_count(input):
    #test if correct amount of lights are on for given input
    #read_url_execute(input)
    read_file_execute(input)


#test_read("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")

#test_commands("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")

#test_count("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")

test_count("test_input")
