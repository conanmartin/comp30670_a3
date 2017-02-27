'''
Author: Conan Martin
Email: conan.martin@ucdconnect.ie
Created 20th February 2017
'''


from name.reader import read_url_execute

import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='Insert url for file to be run')
    args = parser.parse_args()

    file_to_execute = args.input

    read_url_execute(file_to_execute)

if __name__ == '__main__':
    main()











