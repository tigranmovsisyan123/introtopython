import argparse

parser = argparse.ArgumentParser()
parser.add_argument("key", type = str )
parser.add_argument("value", type = str)
args=parser.parse_args()
dict1 = {1: "value1"}
print(dict1)
dict1[args.key] = args.value
print(dict1)