from pymprog import *
begin('Fábrica de Lâmpadas.')
verbose(True) 

y0, x1n, x1e,y1,x2n,x2e,y2,x3n,x3e,y3 = var('y0, x1n, x1e,y1,x2n,x2e,y2,x3n,x3e,y3') # variables
#objetivo
minimize(1.00 * y0 + 3.50 * x1n + 4.25 * x1e + 1.00 * y1 + 3.50 * x2n + 4.25 * x2e + 1.00 * y2 +3.50 * x3n + 4.25 * x3e + 1.00 * y3)
#restrições
y0 == 500
y0 + x1n + x1e - y1 == 2184
y1 + x2n + x2e - y2 == 4945
y2 + x3n + x3e - y3 == 2356
y3 = 0
x1n <= 2500
x2n <= 2500
x3n <= 2500
x1e <= 1250
x2e <= 1250
x3e <= 1250
solve()
print("###>Z: %f"%vobj())
sensitivity() # sensitivity report
end()
