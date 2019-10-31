import argparse

parser = argparse.ArgumentParser()
parser.add_argument("str")
args = parser.parse_args()
print( args.str.upper())
print( args.str.lower())
print( args.str)