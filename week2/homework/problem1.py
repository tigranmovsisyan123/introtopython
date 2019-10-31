import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--num_y", type = int, help = "Number of years")
parser.add_argument("--num_d", type = int, help = "Number of days")

args = parser.parse_args()
tday = datetime.datetime.today()
years = datetime.timedelta(days = 0)
days = datetime.timedelta(days = 0)
if args.num_y:
    years = datetime.timedelta(days = args.num_y*365)
if args.num_d:
    days = datetime.timedelta(days = args.num_d)
print("Current date: " , tday)
print("Given years: ", args.num_y)
print("Given days: ", args.num_d)
print("Final date: ", tday + years + days)
