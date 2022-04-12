from numpy import minimum
from pymprog import *
begin('bike production')
verbose(True) 
x, y = var('x, y') # variables
maximize(4 * x + 6 * y)
2*x+y <=8 # mountain bike limit
-x+y <= 3 # racer production limit
-2*x-y<=4
# metal finishing limit

solve()
print("###>Objective value: %f"%vobj())
sensitivity() # sensitivity report
end()
