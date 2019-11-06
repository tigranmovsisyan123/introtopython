import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", type=str)
args = parser.parse_args()
odd = int(len(args.text)-1)
mid = int(odd/2)
mid_three = args.text[mid-1:mid+2]
new = args.text.replace(mid_three, mid_three.upper())
print("the old string", args.text)
print("middle three characters", mid_three)
print("the new string", new)