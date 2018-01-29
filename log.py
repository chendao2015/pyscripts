#!/usr/bin/env python3
import sys
import re

def prePos(seekfile):
    global curpos
    try:
        cf = open(seekfile)
    except IOError:
        curpos = 0
        return curpos
    except FileNotFoundError:
        curpos = 0
        return curpos
    else:
        try:
            curpos = int(cf.readline().strip())
        except ValueError:
            curpos = 0
            cf.close()
            return curpos
        cf.close()
    return curpos

def lastPos(filename):
    with open(filename) as lfile:
        if lfile.readline():
            lfile.seek(0,2)
        else:
            return 0
        lastPos = lfile.tell()
    return lastPos

def getSeekFile():
    try:
        seekfile = sys.argv[2]
    except IndexError:
        seekfile = '/tmp/logseek'
    return seekfile

def getKey():
    try:
        tagKey = str(sys.argv[3])
    except IndexError:
        tagKey = 'Error'
    return tagKey

def getResult(filename,seekfile,tagkey):
    destPos = prePos(seekfile)
    curPos = lastPos(filename)

    if curPos < destPos:
        curpos = 0

    try:
        f = open(filename)
    except IOError:
        print('Could not open file: %s' % filename)
    except FileNotFoundError:
        print('Could not open file: %s' % filename)
    else:
        f.seek(destPos)

        while curPos != 0 and f.tell() < curPos:
            rresult = f.readline().strip()
            global result
            if re.search(tagkey, rresult):
                result = 1
                break
            else:
                result = 0

        with open(seekfile,'w') as sf:
            sf.write(str(curPos))
    finally:
        f.close()
    return result

if __name__ == "__main__":
    result = 0
    curpos = 0
    tagkey = getKey()
    seekfile = getSeekFile()
    result = getResult(sys.argv[1],seekfile,tagkey)
    print(result)
