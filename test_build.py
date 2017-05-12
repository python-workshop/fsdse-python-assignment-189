import sys
from build import is_prime

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
test(is_prime(21) == False) #non prime number
test(is_prime(11) == True) #prime number

