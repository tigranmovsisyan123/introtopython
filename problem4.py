import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--Age", type = int)
args = parser.parse_args()
if args.Age:
print("Happy Birthday you already", args.Age, "years old")