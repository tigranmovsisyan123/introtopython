import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Name", type = str,)
args = parser.parse_args()

print("Welcome, ", args.Name)