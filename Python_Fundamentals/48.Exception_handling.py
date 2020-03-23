# this concept is used to avoid error during run time#
import sys
list=['a',1,0]
for i in list:
    try:
        print('Entry is ',i)
        r=1/int(i)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", i, "is", r)