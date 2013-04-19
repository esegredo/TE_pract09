#! /usr/bin/python
import random, sys 
from math import exp, sin, cos, log, tan, sinh

#constantes
A = -100.0
B = 100.0
numero_test = 500

def equal(expr1, expr2, A, B, n):
  i = 0
  fallos = 0
  while (i <= n): 
   a = random.uniform(A,B)
   b = random.uniform(A,B)
   if eval(expr1) != eval(expr2): 
     fallos = fallos + 1
   i = i + 1
  return (fallos*100/n)
  
if __name__ == '__main__':
  if (len(sys.argv) == 6 ):
    expr1 = sys.argv[1]
    expr2 = sys.argv[2]
    min_value = float(sys.argv[3])
    max_value = float(sys.argv[4])
    numero_test = int(sys.argv[5]) 
    print "%s %s %f %f %d" % (expr1, expr2, min_value, max_value, numero_test)
    print "Porcentaje de fallos ", equal(expr1, expr2, min_value, max_value, numero_test) 
  else: 
    print "La forma de uso es %s expr1 expr2 min_value max_value numero_test" % (sys.argv[0])
    print "Se usan los valores por defecto:" 
    print " %s expr1    expr2         min_value  max_value numero_test fallos" % (sys.argv[0])
    print " %s (a*b)**3 (a**3)*(b**3) -100.0     100.0     500         %g" % (sys.argv[0], equal('(a*b)**3', '(a**3)*(b**3)', A, B, numero_test))
    print " %s (a/b)    1/(b/a)       -100.0     100.0     500         %g" % (sys.argv[0], equal('(a/b)', '1/(b/a)', A, B, numero_test))
