#! /usr/bin/python
import sys, math
from modulo_equal import equal 

#constantes
A = -100.0
B = 100.0
numero_test = 500
lista_identidades = [ ('(a*b)**3', '(a**3)*(b**3)'), 
                      ('a/b','1/(b/a)'), 
                      ('exp(a+b)','exp(a)*exp(b)'),
                      ('log(a**b)','b*log(a)'),
                      ('a-b','-(b-a)'),
                      ('(a*b)**4','(a**4)*(b**4)'),
                      ('(a+b)**2','(a**2)+2*a*b+(b**2)'),
                      ('(a+b)*(a-b)','(a**2)-(b**2)'),
                      ('log(a*b)','log(a)+log(b)'),
                      ('a*b','exp(log(a)+log(b))'),
                      ('1/((1/a)+(1/b))','a*b/(a+b)'), 
                      ('a*(sin(b)**2+cos(b)**2)','a'), 
                      ('sinh(a+b)','(exp(a)*exp(b)-exp(-a)*exp(-b))/2'), 
                      ('tan(a+b)','sin(a+b)/cos(a+b)'), 
                      ('sin(a+b)','sin(a)*cos(b)+sin(b)*cos(a)') 
										]

if __name__ == '__main__':
  if (len(sys.argv) == 4 ):
    min_value = float(sys.argv[1])
    max_value = float(sys.argv[2])
    numero_test = int(sys.argv[3]) 

    print "%25s %40s %15s" % ('expresion1', 'expresion2', '% de fallos')
    for i in range(len(lista_identidades)):
      print "%25s %40s %10g" % (lista_identidades[i][0], lista_identidades[i][1], equal(lista_identidades[i][0], lista_identidades[i][1], min_value, max_value, numero_test) )
  else: 
    print "La forma de uso es %s min_value max_value numero_test" %(sys.argv[0])
    print "Se usan los valores por defecto:" 
    print " %s expr1    expr2         min_value  max_value numero_test fallos" % (sys.argv[0])
    print " %s (a*b)**3 (a**3)*(b**3) -100.0     100.0     500         %g" % (sys.argv[0], equal('(a*b)**3', '(a**3)*(b**3)', A, B, numero_test))
    print " %s (a/b)    1/(b/a)       -100.0     100.0     500         %g" % (sys.argv[0], equal('(a/b)', '1/(b/a)', A, B, numero_test))
