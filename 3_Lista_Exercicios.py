from pymprog import *
begin('Fábrica de Móveis. ')
verbose(True) 
x, y , z, w = var('x, y, z, w') # variables
#Objetivo
maximize(100 * x + 80 * y + 120 * z + 20 * w)
#restrições
x + y + z + 4 * w<= 250 #disponibilidade de tábua
y + z + 2*w <= 600 # disponibilidade de prancha
3*x + 2*y + 4*z <=500 #disponibilidade de tempo fábrica 3

solve()
print("###>Z: %f"%vobj())
sensitivity() # sensitivity report
end()
