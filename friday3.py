'''#syntax4    import module_name as alias_name
import friday4 as f4
print(f4.y)
f4.funn()
import funs as gg
print(gg.iseven(8))
import Recursion as R
print(R.fact(7))

#syntax5 "from module_name import identifier as alias name"
from friday4 import funn as fi
fi()
from Recursion import main as m
m()'''


#When files are in diiferent locations
import sys
sys.path.append("C:/Users/TEMP.601SV2.006/Desktop")
import diff
diff.countt()
#when they are all saved in the same folder
sys.path.append("C:/Users/TEMP.601SV2.006/Desktop/pact")
import abc
import plusABC
import powers
print(powers.ispower(9,2))