from hash import *

def main():
    try:
        send = """
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $                                                     $
        $            |       |                                $
        $            |       |                                $
        $              =====     ###################          $
        $            |       |   #                 #          $
        $            |       |   #                 #          $
        $                        #  CRACKED        #          $
        $                        #                 #          $
        $                        #                 #          $
        $                        ###################          $
        $                                                     $
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        """
        print(send)
        has  = hash('md5', 'sha1', 'sha224', 'sha256', 'sha384','sha512')
        encode1 = has.encryp(input("<$encrypt/1 and $decrypt/2 >>>>>"))


        decode1 = has.decod("y","n")
    except KeyboardInterrupt:
        print()































if __name__ == "__main__":
    main()
