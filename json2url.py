#!/usr/bin/python3
import os
import json
import sys

def openJson(file):
    with open(file, 'r') as myfile:
        datafile=myfile.read()
    global data
    data = json.loads(datafile)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 reddit2json.py [/path/to/reddit.json]")
        exit()

    openJson(sys.argv[1])
    outFile = "subs.txt"
    print ("\n[*] Opening "+ sys.argv[1])
    o = open(outFile, 'w')

    for sub in data["subreddits"]:
        id = sub["display_name_prefixed"]
        o.write("https://old.reddit.com/" + id + "\n")
    print ("[+] subs.json Complete!\n")

if __name__ == "__main__":
    main()
