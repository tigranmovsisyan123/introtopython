import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text",type=int)
args=parser.parse_args()
set1 = {1,2,3,4,5,3,6}
print(set1)
set1.remove(args.text)
print(set1)