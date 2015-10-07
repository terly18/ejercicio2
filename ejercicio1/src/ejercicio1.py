# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "TERLY"
__date__ = "$07/10/2015 03:16:35 PM$"

if __name__ == "__main__":
    print "Hello World"
ht = input('Introduzca horas trabajadas: ')
if ht > 40:
    he = ht - 40
    ss = he * 20 + 40 * 16
else:
    ss = ht*16
    
    
print ((' el salario semanal es :'), ss)    