import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", type=str)
args=parser.parse_args()
list4 = ["a","s","d","f","1","2","3"]
print(list4)
list4.remove(args.text)
print(list4)