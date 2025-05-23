#syntax 1"import programme name then call
#import Recursion
#import Recursion.fact

#syntax 2"from program_name import *[ALL]
#syntax 3"from program_name import SPECIFIC_FUNCTION
from funs import iseven
#Use the a function eg main to run code outside the defined functions
def main():
    if iseven(7):
        print("even")
    else:
        print("odd")
    import math
    print(math.sqrt(9))       
main()