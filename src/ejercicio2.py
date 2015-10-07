
__author__ = "TERLY"
__date__ = "$07/10/2015 02:52:38 PM$"

if __name__ == "__main__":
    print "Hello World"
    
ht = input('Introduzca horas trabajadas: ')
if ht > 40:
    he = ht - 40
    ss = he * 20 + 40 * 16
else:
    ss = ht*16
    
    
print ((' el salario semanal es :'), ss)    
