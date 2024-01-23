#!/usr/bin/env python
from componentes import *
#import errores
import flujo
import string
import sys
import os
from sys import argv

##########      Practica realizada por:       #########
#                                                     #
#                                                     #
#             Domingo José Caballero Navarro          #
#                Rubén Castillo Carrasco              #
#                                                     #
#                                                     #
#######################################################

class Analex:
#############################################################################
##  Conjunto de palabras reservadas para comprobar si un identificador es PR
#############################################################################

 ############################################################################
 #
 #  Funcion: __init__
 #  Tarea:  Constructor de la clase
 #  Prametros:  flujo:  flujo de caracteres de entrada
 #  Devuelve: --
 #
 ############################################################################
    def __init__(self, flujo):
        self.flujo= flujo
        self.poserror= 0
        self.nlinea=1
        # PR almacena la listra de palabras reservadas
        self.PR = frozenset(["PROGRAMA", "VAR", "ENTERO", "REAL", "BOOLEANO", "INICIO", "FIN", "SI", "ENTONCES", "SINO", "MIENTRAS", "HACER", "LEE", "ESCRIBE", "Y", "O", "NO", "CIERTO","FALSO"])



 ############################################################################
 #
 #  Funcion: TrataNum
 #  Tarea:  Lee un numero del flujo
 #  Prametros:  flujo:  flujo de caracteres de entrada
 #              ch: primera caractera tratar
 #  Devuelve: El valor numerico de la cadena leida
 #
 ############################################################################
    def TrataNum(self,flujo, ch):
        l=ch
        real = False
        ch = self.flujo.siguiente()
        #Mientras encuentre un numero o bien el primer punto, sigue iterando
        while((ord(ch)<58 and ord(ch)>47) or (ch=='.' and real==False)):
            if(ch=='.'):
                #Encuentra punto, marcamos a True la variable para que, si vuelve a enocntrar otro pare el bucle,
                #al no considerarse este ultimo como parte del numero. Además nos sirve para crear la clase
                real=True
            l=l+ch
            ch=self.flujo.siguiente()
        #Cuando encontramos un caracter que no es del numero lo devolvemos al flujo para que se trate posteriormente
        flujo.devuelve(ch)
        if(real):
            return float(l)
        else:
            return int(l)

#Completar

 ############################################################################
 #
 #  Funcion: TrataIdent
 #  Tarea:  Lee identificadores
 #  Prametros:  flujo:  flujo de caracteres de entrada
 #              ch: Primer caracter a tratar
 #  Devuelve: Devuelve una cadena de caracteres que representa un identificador
 #
 ############################################################################33
    def TrataIdent(self,flujo, ch):
        l = ch
        #Mientras que encuentre una letra, mayuscula o minuscula, o bien un numero sigue iterando
        while((ord(ch)<58 and ord(ch)>47) or (ord(ch)<90 and ord(ch)>64) or (ord(ch)<123 and ord(ch)>96)):

            ch=flujo.siguiente()
            if((ord(ch)<58 and ord(ch)>47) or (ord(ch)<90 and ord(ch)>64) or (ord(ch)<123 and ord(ch)>96)):
                l=l+ch
        #Devuelve el ultimo caracter, que no es una letra, para que sea tratado
        flujo.devuelve(ch)
        return l

  #Completar
  # return l

  ############################################################################
  #
  #  Funcion: TrataIdent
  #  Tarea:  Lee identificadores
  #  Prametros:  flujo:  flujo de caracteres de entrada
  #              ch: Primer caracter a tratar
  #  Devuelve: Devuelve una cadena de caracteres que representa un identificador
  #
  ############################################################################
    def TrataComent(self, flujo):
        ch=flujo.siguiente
        #Mientras que no encuentre el fin de linea, el comentario sigue
        while(ch!='\n'):
            ch=flujo.siguiente()
        #Devuelve el fin de linea, para que este sea tratado y se sume 1 a self.linea
        flujo.devuelve(ch)
        return

  #Completar

 ############################################################################
 #
 #  Funcion: EliminaBlancos
 #  Tarea:  Descarta todos los caracteres blancos que hay en el flujo de entrada
 #  Prametros:  flujo:  flujo de caracteres de entrada
 #  Devuelve: --
 #
 ############################################################################
    def EliminaBlancos(self,flujo):
        ch=flujo.siguiente()
        #Mientras que siga encontrando blancos, sigue iterando
        while(ch==' ' or ch =="\t"):
            ch=flujo.siguiente()
        flujo.devuelve(ch)
        return 
#Completar

 ############################################################################
 #
 #  Funcion: Analiza
 #  Tarea:  Identifica los diferentes componentes lexicos
 #  Prametros:  --
 #  Devuelve: Devuelve un componente lexico
 #
 ############################################################################
    def Analiza(self):
        l = ""
        ch = self.flujo.siguiente();
        #Si enceuntra un espacio, llama a la funcion para que elimine los consecutivos, si los hay
        if ch == " " or ch =="\t":
            self.EliminaBlancos(self.flujo)
            return self.Analiza()
        #Si encuentra el caracter \r o \r\n, incrementa el numero de lineas solo en uno en ambos casos
        elif ch == "\r" :
            ch2=self.flujo.sigueinte()
            if(ch2=='\n'):
                self.nlinea=self.nlinea+1
            else:
                self.nlinea=self.nlinea+1
                self.flujo.devuelve(ch2)
            i=0
            return self.Analiza()
        # acciones si hemos encontrado una numero, que puede ser entero o real
        elif (ch.isnumeric()):
            cad=self.TrataNum(self.flujo,ch)
            if(type(cad)==int):
                #Creamos una clase Numero de tipo int, donde almacenamos su valor o su tipo(int)
                o=Numero(cad,self.nlinea,False)
            else:
                #Creamos una clase Numero de tipo real, donde almacenamos su valor o su tipo(real)
                o=Numero(cad,self.nlinea,True)
            return o

        #Si encontramos una letra como primer caracter, estamos ante un identificador o una palabra reservada
        elif(ch.isalpha()):
            cad = self.TrataIdent(self.flujo,ch)
            #Si una vez analizado el componente coincide con el nombre completo de una palabra reservada, 
            #la guardamos como a estas
            if(cad in self.PR):
                o=PR(cad,self.nlinea)
            else:
                o=Identif(cad,self.nlinea)
            return o
        

        #Pasamos a analizar los operadores relacionales, que en este caso son >,<,<>,=
        elif ch=='<':
            ch2=self.flujo.siguiente()
            if(ch2=='>' or ch2=='='):
                o=OpRel(ch+ch2,self.nlinea)
            else:
                self.flujo.devuelve(ch2)
                o=OpRel(ch,self.nlinea)
            return o

        elif ch=='=':
            o=OpRel(ch,self.nlinea)
            return o

        elif ch=='>':
            ch2=self.flujo.siguiente()
            if(ch2=='='):
                o=OpRel(ch+ch2,self.nlinea)
            else:
                self.flujo.devuelve(ch2)
                o=OpRel(ch,self.nlinea)
            return o
        
        #Se tratan los op aritmeticos con prioridad de suma
        elif(ch=='+' or ch=='-'):
            o=OpAdd(ch,self.nlinea)
            return o

        #Se tratan los operadores aritmeticos de la prioridad de la mult, salvo el de % 
        # que se tratara de forma independiente
        elif(ch=='*' or ch=='/' ):
            o=OpMult(ch,self.nlinea)
            return o


        #Tratamos la aparicion de los simbolos ( ) ; , . , que corresponden con al categoria lexica de simbolo
        elif(ch==')' or ch=='(' or ch==';' or ch==',' or ch=='.'):
            
            return Simbolo(ch,self.nlinea)

        #Cuando tenemos como caracter ':' pasa lo siguiente
        elif ch==':':
            ch2=self.flujo.siguiente()
            #Si los dos puntos van segudos de un simbolo de igual, se trata de una asignacion 
            if(ch2=='='):
                o=OpAsigna(self.nlinea)
                
            #Si hay dos puntos seguidos de algo distinto de un igual, se trata de un simbolo
            else:
                self.flujo.devuelve(ch2)
                o=Simbolo(ch,self.nlinea)
            return o

        #Cuando tenemos como caracter '%' pasa lo siguiente
        elif ch=='%':
            ch2=self.flujo.siguiente()
            #Si hay dos simbolos % consecutivos se trata de un comentario
            if(ch2!='%'):
                o=OpMult(ch,self.nlinea)
                return o
            
            #En el caso de haber un % segudo de algo distinto de %, se trata de un operador de resto

            else:
                self.TrataComent(self.flujo)
                return self.Analiza()


        # completar aqui para todas las categorias lexicasw
        elif ch == "\n":
            ## acciones al encontrar un salto de linea
            self.nlinea = self.nlinea + 1
            return self.Analiza()
        elif ch:
            # se ha encontrado un caracter no permitido
            print ("ERROR LEXICO  Linea " + str(self.nlinea) + " ::  Caracter " + ch + " invalido ")
            self.poserror= self.poserror+1
            return self.Analiza()
        else:
            print("FIN DEL ARCHIVO")
            print("La cantidad de errores encontrados es de ", self.poserror)
            # el final de fichero
            return EOF()

############################################################################
#
#  Funcion: __main__
#  Tarea:  Programa principal de prueba del analizador lexico
#  Prametros:  --
#  Devuelve: --
#
############################################################################

if __name__=="__main__":
    script, filename=argv
    txt=open(filename)
    print ("PROGRAMA FUENTE %r"  % filename)
    i=0
    fl = flujo.Flujo(txt)
    analex=Analex(fl)
    c = analex.Analiza()
    while c.cat != "EOF":
        print (c)
        c = analex.Analiza()
        i = i + 1

