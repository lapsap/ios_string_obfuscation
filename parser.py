#!/usr/bin/env python3

import sys
import re

cipher = "[String_ob.AppDelegate, NSObject, NSString]"

def salt(input):
    list = []
    offset = 0
    for t in input:
        list.append( ord(t) ^ ord(cipher[offset % len(cipher)]) )
        offset = offset + 1
    encrypted = "o.reveal(key: [" + str(list[0])
    for i in range(1,len(list)):
        encrypted += ", " + str(list[i])
    encrypted += "] )"
    return encrypted
def check_str(input):
    tmp = re.match(r'(.*)\/\*lapsap\*\/"(.*)"\/\*lapsap\*\/(.*)', input)
    if tmp:
        return tmp.group(1) + salt(tmp.group(2)) + tmp.group(3) + '\n'
    else:
        return input

def smth(filename):
    file = open(filename,"r")
    file_ori = open('ori_' + filename, "w")
    bla = ""
    for line in file:
        file_ori.write(line)
        t1 = t2 = line
        t1 = check_str(line)
        while ( t1 != t2 ):
            t2 = t1 
            t1 = check_str(t1)
        bla += t1
    file.close()
    file_ori.close()
    file = open(filename,"w")
    file.write(bla)
    file.close()

for i in range(1,len(sys.argv)):
    print ('editing ', sys.argv[i])
    smth (sys.argv[i])


