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

def smth(filename):
    file = open(filename,"r")
    file_ori = open('ori_' + filename, "w")
    bla = ""
    for line in file:
        file_ori.write(line)
        tmp = re.match(r'(.*)\/\*lapsap\*\/"(.*)"\/\*lapsap\*\/(.*)', line)
        if tmp:
            bla += tmp.group(1) + salt(tmp.group(2)) + tmp.group(3) + '\n'
        else:
            bla += line
    file.close()
    file_ori.close()
    file = open(filename,"w")
    file.write(bla)
    file.close()

for i in range(1,len(sys.argv)):
    print ('editing ', sys.argv[i])
    smth (sys.argv[i])


