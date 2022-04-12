from pymprog import *
begin('WYNDOR GLASS CO. ')
verbose(True) 
x, y = var('x, y') # variables
#Objetivo
maximize(3000 * x + 5000 * y)
#restrições
x<=4 #disponibilidade de tempo fábrica 1
2*y <= 12 # disponibilidade de tempo fábrica 2
3*x+2*y<=18 #disponibilidade de tempo fábrica 3

solve()
print("###>Objective value: %f"%vobj())
sensitivity() # sensitivity report
end()
