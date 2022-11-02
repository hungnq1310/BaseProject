# test

# --------------------------------------------------------
# dictionary
counts = dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for lines in handle:
    lines.strip()
    if not lines.startswith("From "): continue
    words = lines.split()
    counts[words[1]] = counts.get(words[1], 0) + 1

bigCount = None
bigWord = None
for word, count in counts.items():
    if bigWord is None or count > bigCount:
        bigWord = word
        bigCount = count

print(bigWord, bigCount)

# ver2:
# DNS
count_country = dict()

for line in fh:
    if not line.startswith("Location:"):
        continue
    spiece = line.rstrip().split(":")
    country = spiece[1]
    count_country[country] = count_country.get(country, 0) + 1
    count_country.

print("Country\tCount")
for k, v in count_country.items():
    print(k, v)

# -------------------------------------------------------
'''
- Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day 
for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then
splitting the string a second time using a colon.
(From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008)
- Once you have accumulated the counts for each hour, print out the counts, sorted by hour'''
# count gio
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
list_count = list()
counts = dict()
for lines in handle:
    lines.strip()
    if not lines.startswith("From "): continue
    words = lines.split()
    list_count.append(words[5])

list_count.sort()
for name in list_count:
    counts[name[:2]] = counts.get(name[:2], 0) + 1

for k, v in counts.items():
    print(k, v)

# bai 2: count email
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
list_count = list()
counts = dict()
for lines in handle:
    lines.strip()
    if not lines.startswith("From "): continue
    words = lines.split()
    list_count.append(words[1])

list_count.sort()
for name in list_count:
    counts[name] = counts.get(name, 0) + 1

print("{:30}{:^20}".format("Email", "Count"))
for k, v in counts.items():
    print("{:30}{:^20}".format(k, v))

# --------------------------------------------------------------
# file
# input file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
tong = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(':')
    num = float(line[pos + 1:])
    tong += num
    count += 1
    # print(line)
    # print(sum)
    # print(count)
print("Average spam confidence:", tong / count)
# print("Done")

# ------------------------------------------------------------------
# SOCKET
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()

# --------------------------------------------------------------------
# BeautifulSOUP
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

# -------------------------------------------------------------------
# XML

import urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)

# ---------------------------------------------------------
# json

# 1
import json

data = '''
    [
      { "id" : "001",
        "x" : "2",
        "name" : "Chuck"
      } ,
      { "id" : "009",
        "x" : "7",
        "name" : "Brent"
      }
    ]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

    # 2:

import urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

# -----------------------------------------------------------------------
# database

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
    CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                    VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()


# ------------------------------------------------------------------
# isPrime

def is_prime_basic(number):
    if number < 2:
        return False
    for value in range(2, number):
        if number % value == 0:
            return False
    return True


def prime_num(numb):
    prime_list = list()
    i = 1
    while i < numb:
        if is_prime_basic(i): prime_list.append(i)
        i = i + 1
    print(prime_list)


# ----------------------------------------------------------
# Perfectnumber

def isPerfectNum(num):
    if (num == ListDiviser(num)):
        return True
    else:
        return False


def ListDiviser(number):
    lst = list()
    sum_div = 0
    for x in range(1, number):
        if (number % x) == 0: lst.append(x)
    # print(lst)
    for i in lst:
        sum_div += i
    return sum_div


while True:
    try:
        num = int(input("Enter the number: "))
        if (num < 0):
            print("The number must be positive")
            continue
        break
    except:
        print("The number must be a positive number")

print("The prime number from 0 to ", num)
for i in range(1, num):
    if isPerfectNum(i):
        print(i)

# -------------------------------------
# min max

num_list = list()


def min_max():
    min = None
    max = None
    for numb in num_list:
        if min is None or min < numb:
            min = numb
        if max is None or max > numb:
            max = numb
    print("Maximun is ", max)
    print("Minimum is ", min)


while True:
    try:
        line = input("Enter the number: ")
        if (line == "done"):
            break
        num = int(line);
        num_list.append(num)
    except:
        print("Invalid number")

min_max()


# -------------------------------------
# format + class

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def toString(self):
        return "{:^20}{:^10}{:^10}".format(self.name, self.age, self.score)


student_list = list()
while True:
    try:
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        score = int(input("Enter student's core: "))
    except:
        print("Invalid information!")
        continue
    student = Student(name, age, score)
    student_list.append(student)
    req = input("Do you want to exit?: ").lower()
    if req.startswith('y'): break


def sort_list(list_name):
    leng = len(list_name)
    for i in range(leng):
        for j in range(leng - 1):
            if list_name[j].get_name() > list_name[j + 1].get_name():
                list_name[j], list_name[j + 1] = list_name[j + 1], list_name[j]


def print_list(lst):
    print("{:^20}{:^10}{:^10}".format("Name", "Age", "Scores"))
    for i in lst:
        print(i.toString())


print_list(student_list)
sort_list(student_list)
print_list(student_list)

# -------------------------------------------------------------------------
# exmp1

import sqlite3

conn = sqlite3.connect('DNSList.sqlite')
cur = conn.cursor()

cur.executescript('''
        DROP TABLE IF EXISTS DNS;
        CREATE TABLE DNS(
            IP TEXT,
            Reliability INTEGER,
            Description TEXT
        )
    ''')

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "DNSList.txt"

fh = open(fname)
for line in fh:
    if not line.startswith("IP Address"):
        continue
    spieces = line.rstrip().split(":")
    # insert in table
    IP = spieces[1]
    reliability = int(spieces[2])
    if reliability >= 50:
        descript = "Normal"
    else:
        descript = "Low"
    cur.execute('''
            INSERT OR IGNORE INTO DNS (IP, Reliability, Description) VALUES (?,?,? ) '''
                , (IP, reliability, descript))
    conn.commit()

# Extract SQL
sqlstr = '''
        SELECT IP,Reliability,Description
        FROM DNS
        ORDER BY Reliability DESC;
        '''

print("{:^30}{:^20}{:^20}".format("IP", "Reliability", "Description"))
for row in cur.execute(sqlstr):
    print("{:^30}{:^20}{:^20}".format(row[0], row[1], row[2]))

cur.close()


# -----------------------------------------------------------
# fibo
def isFibo(num):
    n = 0
    n1 = 0
    n2 = 1
    for i in range(0, num):
        print(n1, sep=" ")
        n = n1 + n2
        n1 = n2
        n2 = n


# -------------------------------------------------------
# cube perfect

def percube(num):
    n = 1
    for i in range(2, num):
        n = i * i * i
        if (n > num): break
        print(n)


# -----------------------------------------------------
# count_even
def count_even(list_num):
    sum = 0
    count = 0
    for numb in list_num:
        if (numb % 2) == 0:
            sum = sum + numb
            count += 1
    print(str(sum) + ", " + str(count))
    return float(sum / count)


# class object
# -------------------------------------

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def toString(self):
        return "{:^20}{:^10}{:^10}".format(self.name, self.age, self.score)


student_list = list()
while True:
    try:
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        score = int(input("Enter student's core: "))
    except:
        print("Invalid information!")
        continue
    student = Student(name, age, score)
    student_list.append(student)
    req = input("Do you want to exit?: ").lower()
    if req.startswith('y'): break


def sort_list(list_name):
    leng = len(list_name)
    for i in range(leng):
        for j in range(leng - 1):
            if list_name[j].get_name() > list_name[j + 1].get_name():
                list_name[j], list_name[j + 1] = list_name[j + 1], list_name[j]


def print_list(lst):
    print("{:^20}{:^10}{:^10}".format("Name", "Age", "Scores"))
    for i in lst:
        print(i.toString())


print_list(student_list)
sort_list(student_list)
print_list(student_list)
