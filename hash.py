#!user/bin/python3
from hashlib import *
import sys
import os
from time import *
#md5(32), sha1(40), sha224(56), sha256(64), sha384(86), and sha512(128)

os.system('clear')

try:
    class hash(object):
        def __init__(self,v1,v2,v3,v4,v5,v6):
            self.v1 =v1 ; self.v2=v2 ; self.v3=v3 ;self.v4=v4
            self.v5=v5 ; self.v6=v6

        def encryp(self,op):
            #encryp
            self.op=op
            if self.op == "1":
                sleep(0.3)
                e = """
                md5 and sha1 and sha244 and sha256 and sha384 and sha512
                example

                |mode hash| ======> md5 or sha1  .......
                |encrypt|====> hellow

                """
                print(e)
                try:

                    self.hh = input("|mode hash| ======> ")
                    sleep(0.3)
                    self.to = input("|encrypt|====> ")
                    sleep(0.3)
                    if self.hh == self.v1:
                        return md5(self.to.encode()).hexdigest()
                    elif self.hh == self.v2:
                        return sha1(self.to.encode()).hexdigest()
                    elif self.hh == self.v3:
                        return sha224(self.to.encode()).hexdigest()
                    elif self.hh == self.v4:
                        return sha256(self.to.encode()).hexdigest()
                    elif self.hh == self.v5:
                        return sha384(self.to.encode()).hexdigest()
                    elif self.hh == self.v5:
                        return  sha512(self.io.encode()).hexdigest()
                except AttributeError:
                    print("")
                except KeyboardInterrupt:
                    print()
                else:
                    return "NOT Found"
        def decod(self,y,n):
            #decrypt
            self.y=y
            self.n=n

            try:
                if self.op == "2":
                    self.font = input("your Decrypt < y/n >=====> ")
                    if self.font == "y" or self.font == "Y":
                        sleep(0.3)
                        ran = """
                        her Decrytp  example

                        |hash decrypt |======>>>> 296ab79bb0e6b305a21f964bd2ac8531
                               and

                        |file|===>>>>> wordlist.txt

                        """
                        print(ran)
                        self.hash11 = input("|hash decrypt |======>>>>  ")
                        self.file = input("|file|===>>>>> ")
                        sleep(0.3)
                        with open(self.file,mode="r") as f:
                            for line in f:
                                line =line.strip()
                                if md5(line.encode()).hexdigest() == self.hash11:
                                    return self.v1+"    "+line
                                elif sha1(line.encode()).hexdigest() == self.hash11:
                                    return "  {}  ".format(self.v2),line
                                elif sha224(line.encode()).hexdigest() == self.hash11:
                                    return "  {}  ".format(self.v3),line
                                elif sha256(line.encode()).hexdigest() == self.hash11:
                                    return "  {}  ".format(self.v4),line
                                elif sha384(line.encode()).hexdigest() == self.hash11:
                                    return "  {}  ".format(self.v5),line
                                elif sha512(line.encode()).hexdigest() == self.hash11:
                                    return "  {}  ".format(self.v6),line
                    elif self.font == "n" or self.font == "N":
                        sleep(0.2)
                        print(sys.exit())
                    else:
                        return ""
            except  FileNotFoundError:
                return("Not Found")


except KeyboardInterrupt:
    print()
