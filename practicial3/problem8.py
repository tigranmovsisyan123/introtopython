import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", type=int)
args=parser.parse_args()
set3 = {1,2,3,4,5,6,}
if args.text > min(set3) and args.text < max(set3):
    print(True)
else:
    print(False)
    