import argparse

parse=argparse.ArgumentParser()
parse.add_argument("input", type=str)
args = parse.parse_args()
list2 = ["a","b","c",1,1,2,3,4,5]

print(list2.count(args.input))
print(list2)