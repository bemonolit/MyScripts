#!/usr/bin/python

import sqlite3
import os
from sqlite3 import Error

wordlist_Path = "/Users/andreas/Documents/scripts/wordlists/"
responderdb_Path = "./Responder.db"
format = "netntlmv2"
rules = "Jumbo"
hash = "hash.txt"


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_hashes(conn):

    cur = conn.cursor()
    cur.execute("SELECT fullhash FROM responder")

    rows = cur.fetchall()

    for row in rows:
        #print(row[0])
        f = open(hash, "a")
        f.write(row[0]+'\n')
        f.close()

def run_john(wordlists):
    f = open(hash, "r")
    f.close()
    for x in wordlists:
        print('Running wordlist: ' + x +' \n')
        os.system('john ' + hash + ' -w=' + wordlist_Path + x + ' --rules:' + rules + '--format:' + format)

def wordlists(path):
    mylist = os.listdir(path)
    return mylist

def main():
    database = responderdb_Path
    try:
        os.remove(hash)

    except:
        print('Error deleting old hash. No biggy')


    # create a database connection
    conn = create_connection(database)
    with conn:


        #Getting hashes
        select_all_hashes(conn)

    run_john(wordlists(wordlist_Path))
    os.system('john ' + hash + ' --show')


if __name__ == '__main__':
    main()
