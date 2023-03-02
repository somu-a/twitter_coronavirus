#!/usr/bin/env python3

# command line args
import argparse
import matplotlib
matplotlib.use('Agg')

parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# plot the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
#print(items)

top_ten = items[1:11]
countries = []
values = []
for country, value in top_ten:
    countries.append(country)
    values.append(value)

plt.bar(countries, values)

if args.input_path == "reduced.country":
    plt.xlabel("Countries")
    plt.ylabel("Number of Tweets")
    plt.title("Top 10 Countries with Tweets including: " + str(args.key))
    if args.key == '#coronavirus':
        plt.savefig('CountryCoronavirus.png')
    elif args.key == '#코로나바이러스':
        plt.savefig('Country#코로나바이러스.png')

elif args.input_path == "reduced.lang":
    plt.xlabel("Languages")
    plt.ylabel("Number of Tweets")
    plt.title("Top 10 Countries with Tweets including: " + str(args.key))
    if args.key == '#coronavirus':
        plt.savefig('LanguageCoronavirus.png')
    elif args.key == '#코로나바이러스':
        plt.savefig('Language#코로나바이러스.png')
