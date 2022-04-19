from pymprog import *
begin('O Problema das Ligas Metalicas')
verbose(True) 
x, y = var('x, y') # variables
#Objetivo
maximize(3000 * x + 5000 * y)
#restrições
0.5*x+0.2*y <=16 #disponibilidade de cobre (toneladas)
0.25*x+0.3*y <= 11 # disponibilidade de zinco (tonelada)
0.25*x+0.5*y<=15 # disponibilidade de Chumbo (tonelada)
# metal finishing limit

solve()
print("Z: %f"%vobj())
sensitivity() # sensitivity report
end()
