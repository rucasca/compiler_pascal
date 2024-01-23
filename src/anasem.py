#!/usr/bin/env python

#import arboles

import componentes
import flujo
import analex
import sys
from AST import *
from sys import argv
#import errores


class Sintactico:
#Constructor de la clase que implementa el Analizador Sintactico
#Solicita el primer compnente lexico 
    def __init__(self, lexico):
        self.lexico= lexico
        self.token=self.lexico.Analiza()
        self.lista=[]

        self.tabla_simbolos = dict()

    #Metodo que permite almacenar una nueva entrada en la tabla de simbolos
    def inserta_tabla_simbolos(self,id,tipo):
        if not(self.esta_tabla_simbolos(id)):
            if(tipo=="booleano"):
                self.tabla_simbolos[id] = (id,tipo,False)
            else:
                self.tabla_simbolos[id] = (id,"numero",0.0)
        else:
            return False
        return True

    #Metodo que permite modificar el valor de una entrada de la tabla de simbolos
    def modifica_valor_tabla(self,id,valor):
        if(self.esta_tabla_simbolos(id)):
            self.tabla_simbolos[id][2]=valor
            return True
        else:
            return False

    #Metodo que permite comprobar si hay un elemento con un id en la tabla de simbolos
    def esta_tabla_simbolos(self,id):
        return (id in self.tabla_simbolos.keys())


    ######################################################################################
    ##
    ## Mensajes de error para cuando encontramos un fallo en la sintaxis del programa
    ##
    ######################################################################################
    def Error(self, nerr, tok):
        #print("Tenemos: "+str(self.token.val))
        if nerr == 1:
            print ("Linea: " + str(self.token.linea) + "  ERROR Se espera PROGRAMA")
        elif nerr==2:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera IDENTIFICADOR")
        elif nerr==3:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera ;")
        elif nerr==4:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera .")
        elif nerr==5:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera :")
        elif nerr==6:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera ,")
        elif nerr==7:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera ENTERO")
        elif nerr==8:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera REAL")
        elif nerr==9:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera BOOLEANO")
        elif nerr==10:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera INICIO")
        elif nerr==11:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera FIN")
        elif nerr==12:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera SI")
        elif nerr==13:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera ENTONCES")
        elif nerr==14:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera SINO")
        elif nerr==15:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera MIENTRAS")

        elif nerr==16:  #Se espera decl_var
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera PR(VAR o INICIO)")
        elif nerr==17:  #Se espera decl_v
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera ID o INICIO")
        elif nerr==18:  #Se espera lista_id
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera ID")
        elif nerr==19:  #Se espera resto_lista_id
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera ; o .")
        elif nerr==20:  #Se espera tipo_std
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera PR(ENTERO REAL o BOOLEANO)")
        elif nerr==21:  #Se espera instrucciones
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera INICIO")
        elif nerr==22:  #Se espera lista_ins
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera INICIO SI ENCONCES MIENTRAS LEE ESCRIBE o FIN")
        elif nerr==23:  #Se espera instruccion
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera INICIO ID LEE ESCRIBE SI o MIENTRAS")
        elif nerr==24:  #Se espera instruccion
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera ID")
        elif nerr==25:  #Se espera ins_e_s
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera LEE o ESCRIBE")
        elif nerr==26:  #Se espera expresion
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera ID NO CIERTO FALSO  + - o ( ")
        elif nerr==27:  #Se espera expresion_aux
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera oprel ; ENTONCES SINO HACER o )")
        elif nerr==28:  #Se espera expresion_simple
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera ID NO CIERTO FALSO + - num (")
        elif nerr==29:  #Se espera resto_expr_simple
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera  ; ENTONCES SINO HACER O oposuma oprel )")
        elif nerr==30:  #Se espera termino
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera  ID NO CIERTO FALSO num (")
        elif nerr==31:  #Se espera resto_termino
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera  ; ENTONCES SINO HACER Y O opsuma opmult o )")
        elif nerr==32:  #Se espera factor
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera  ID NO CIERTO FALSO o (")
        elif nerr==33:  #Se espera signo
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera  + o -")

        #Errores para cuando el terminal no es el esperado
        elif nerr==34:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera VAR")
        elif nerr==35:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera HACER")
        elif nerr==36:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera LEE")
        elif nerr==37:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera ESCRIBE")
        elif nerr==38:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera NO")
        elif nerr==39:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera CIERTO")
        elif nerr==40:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera FALSO")
        elif nerr==41:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera Y")
        elif nerr==42:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera O")
        elif nerr==43:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera opasigna")
        elif nerr==44:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera opsuma")
        elif nerr==45:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera opmult")
        elif nerr==46:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera oprel")
        elif nerr==47:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera +")
        elif nerr==48:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera -") 
        elif nerr==49:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera num")
        elif nerr==50:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera (")
        elif nerr==51:
            print ("Linea: " + str(self.token.linea) + "  ERROR:Se espera )") 
        else:
            print("Fallo en el error, fuera de rango")

        
    #############################################################################################
    ##
    ## Lista de funciones para comprobar que el valor del siguiente es el de un terminal esperado
    ##
    ##############################################################################################
    
    def programa(self):
        if self.token.cat != "PR" or self.token.valor != "PROGRAMA":
            self.Error (1,self.token) 
            return False
        self.token = self.lexico.Analiza()
        return True

    def var(self):
        if(self.token.cat=="PR" and self.token.valor=="VAR"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (34,self.token)
            return False
        return True

    def id(self):
        if(self.token.cat=="Identif" ):
            valor = self.token.valor
            self.token = self.lexico.Analiza()
        else:
            self.Error (2,self.token)
            return False
        return True,valor
        
    def punto_coma(self):
        if(self.token.cat=="Simbolo" and self.token.valor==";"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (3,self.token)
            return False
        return True
    

    def punto(self):
        if(self.token.cat=="Simbolo" and self.token.valor=="."):
            self.token = self.lexico.Analiza()
        else:
            self.Error (4,self.token)
            return False
        return True


    def dos_puntos(self):
        if(self.token.cat=="Simbolo" and self.token.valor==":"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (5,self.token)
            return False
        return True

    def coma(self):
        if(self.token.cat=="Simbolo" and self.token.valor==","):
            self.token = self.lexico.Analiza()
        else:
            self.Error (6,self.token)
            return False
        return True


    def entero(self):
        if(self.token.cat=="PR" and self.token.valor=="ENTERO"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (7,self.token)
            return False
        return True


    def real(self):
        if(self.token.cat=="PR" and self.token.valor=="REAL"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (8,self.token)
            return False
        return True


    def booleano(self):
        if(self.token.cat=="PR" and self.token.valor=="BOOLEANO"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (9,self.token)
            return False
        return True

    def inicio(self):
        if(self.token.cat=="PR" and self.token.valor=="INICIO"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (10,self.token)
            return False
        return True

    def fin(self):
        if(self.token.cat=="PR" and self.token.valor=="FIN"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (11,self.token)
            return False
        return True

    def si(self):
        if(self.token.cat=="PR" and self.token.valor=="SI"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (12,self.token)
            return False
        return True

    def sino(self):
        if(self.token.cat=="PR" and self.token.valor=="SINO"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (14,self.token)
            return False
        return True

    def entonces(self):
        if(self.token.cat=="PR" and self.token.valor=="ENTONCES"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (13,self.token)
            return False
        return True


    def mientras(self):
        if(self.token.cat=="PR" and self.token.valor=="MIENTRAS"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (15,self.token)
            return False
        return True


    def hacer(self):
        if(self.token.cat=="PR" and self.token.valor=="HACER"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (35,self.token)
            return False
        return True


    def lee(self):
        if(self.token.cat=="PR" and self.token.valor=="LEE"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (36,self.token)
            return False
        return True

    def escribe(self):
        if(self.token.cat=="PR" and self.token.valor=="ESCRIBE"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (37,self.token)
            return False
        return True

    def no(self):
        if(self.token.cat=="PR" and self.token.valor=="NO"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (38,self.token)
            return False
        return True

    def cierto(self):
        if(self.token.cat=="PR" and self.token.valor=="CIERTO"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (39,self.token)
            return False
        return True

    def falso(self):
        if(self.token.cat=="PR" and self.token.valor=="FALSO"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (40,self.token)
            return False
        return True


    def y(self):
        if(self.token.cat=="PR" and self.token.valor=="Y"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (41,self.token)
            return False, "op_erroneo"
        return True, "Y"


    def o(self):
        if(self.token.cat=="PR" and self.token.valor=="O"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (42,self.token)
            return False, "op_erroneo"
        return True, "O"


    def opasigna(self):
        if(self.token.cat=="OpAsigna" ):
            self.token = self.lexico.Analiza()
        else:
            self.Error (43,self.token)
            return False
        return True


    def opsuma(self):
        if(self.token.cat=="OpAdd" ):
            valor =self.token.tipo
            self.token = self.lexico.Analiza()
        else:
            self.Error (44,self.token)
            return False,"op_erroneo"
        return True,valor

    def opmult(self):
        if(self.token.cat=="OpMult" ):
            valor =self.token.tipo
            self.token = self.lexico.Analiza()
        else:
            self.Error (45,self.token)
            return False,"op_erroneo"
        return True,valor


    def oprel(self):
        if(self.token.cat=="OpRel" ):
            valor =self.token.val
            self.token = self.lexico.Analiza()
        else:
            self.Error (46,self.token)
            return False,"op_erroneo"
        return True,valor

    def mas(self):
        if(self.token.cat=="Simbolo" and self.token.valor=="+"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (47,self.token)
            return False,"op_erroneo"
        return True,"+"

    def menos(self):
        if(self.token.cat=="Simbolo" and self.token.valor=="-"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (48,self.token)
            return False,"op_erroneo"
        return True,"-"


    def num(self):
        if(self.token.cat=="Numero" ):
            valor =self.token.valor
            tipo = self.token.tipo
            self.token = self.lexico.Analiza()
        else:
            self.Error (49,self.token)
            return False,"op_erroneo","op_erroneo"
        return True,valor,tipo

    def par_apertura(self):
        if(self.token.cat=="Simbolo" and self.token.valor=="("):
            self.token = self.lexico.Analiza()
        else:
            self.Error (50,self.token)
            return False
        return True


    def par_cierre(self):
        if(self.token.cat=="Simbolo" and self.token.valor==")"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (51,self.token)
            return False

        return True


    def EOF(self):
        if(self.token.cat=="EOF" ):
            return True
        else:
            return False  



    #############################################################################################################
    ##
    ## Funciones para cuando llegamos a un no terminal, saber que regla aplicar atendiendo al valor del siguiente
    ##
    ##############################################################################################################

    def decl_var(self):
        if(self.token.cat=="PR" and self.token.valor=="VAR"):
            if  not(self.decl_var_2()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="INICIO"):
            if  not(self.decl_var_3()): return False 
        else:
            self.Error (16,self.token) 
            return False
        return True

    def decl_v(self):
        if(self.token.cat=="Identif" ):
            if  not(self.decl_v_4()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="INICIO"):
            if  not(self.decl_v_5()): return False 
        else:
            self.Error (17,self.token) 
            return False             
        return True

    def lista_ids(self,lista_ids):
        if(self.token.cat=="Identif" ):
            correcto, lista = self.lista_id_6(lista_ids)
            if  not(correcto): return False, lista
        else:
            self.Error (18,self.token)
            return False ,lista_ids
        return True, lista

    def resto_listaid(self,lista_ids):
        if(self.token.cat=="Simbolo" and self.token.valor==","):
            correcto, lista = self.resto_listaid_7(lista_ids)
            if  not(correcto): return False , lista

        elif(self.token.cat=="Simbolo" and self.token.valor==":"):
            correcto, lista = self.resto_listaid_8(lista_ids)
            if  not(correcto): return False, lista
            
        else:
            self.Error (19,self.token)
            return False,lista_ids
        
        return True,lista


    def tipo_std(self):
        if(self.token.cat=="PR" and self.token.valor=="ENTERO"):
            correcto, tipo = self.tipo_std_9()
            if  not(correcto): return False ,tipo
            
        elif(self.token.cat=="PR" and self.token.valor=="REAL"):
            correcto, tipo = self.tipo_std_10()
            if  not(correcto): return False, tipo
            
        elif(self.token.cat=="PR" and self.token.valor=="BOOLEANO"):
            correcto, tipo = self.tipo_std_11()
            if  not(correcto): return False , tipo
            
        else:
            self.Error (20,self.token)
            return False, "Error"
        return True, tipo


    def instrucciones(self):
        if(self.token.cat=="PR" and self.token.valor=="INICIO"):
            correcto, arbol =self.instrucciones_12() 
            if  not(correcto): return False , arbol 
        else:
            self.Error (21,self.token)
            return False, NodoVacio(self.token.linea)
        return True, arbol

    def lista_ins(self, lista_ins):
        if(self.token.cat=="Identif" ):
            correcto, lista = self.lista_inst_13(lista_ins)
            if  not(correcto): return False , lista
        elif(self.token.cat=="PR" and self.token.valor=="INICIO"):
            correcto, lista = self.lista_inst_13(lista_ins)
            if  not(correcto): return False, lista
        elif(self.token.cat=="PR" and self.token.valor=="SI"):
            correcto, lista = self.lista_inst_13(lista_ins)
            if  not(correcto): return False, lista
        elif(self.token.cat=="PR" and self.token.valor=="ENTONCES"):
            correcto, lista = self.lista_inst_13(lista_ins)
            if  not(correcto): return False, lista
        elif(self.token.cat=="PR" and self.token.valor=="MIENTRAS"):
            correcto, lista = self.lista_inst_13(lista_ins)
            if  not(correcto): return False, lista
        elif(self.token.cat=="PR" and self.token.valor=="LEE"):
            correcto, lista = self.lista_inst_13(lista_ins)
            if  not(correcto): return False, lista
        elif(self.token.cat=="PR" and self.token.valor=="ESCRIBE"):
            correcto, lista = self.lista_inst_13(lista_ins)
            if  not(correcto): return False, lista
        elif(self.token.cat=="PR" and self.token.valor=="FIN"):
            correcto, lista = self.lista_inst_14(lista_ins)
            if  not(correcto): return False, lista
        else:
            self.Error (22,self.token)
            return False, []
        return True, lista

    def instruccion(self):
        if(self.token.cat=="Identif" ):
            correcto, arbol = self.instruccion_16()
            if  not(correcto): return False, arbol
        elif(self.token.cat=="PR" and self.token.valor=="INICIO"):
            correcto, arbol =self.instruccion_15()
            if  not(correcto): return False, arbol
        elif(self.token.cat=="PR" and self.token.valor=="SI"):
            correcto, arbol =self.instruccion_18()
            if  not(correcto): return False, arbol
        elif(self.token.cat=="PR" and self.token.valor=="LEE"):
            correcto, arbol =self.instruccion_17()
            if  not(correcto): return False, arbol
        elif(self.token.cat=="PR" and self.token.valor=="ESCRIBE"):
            correcto, arbol =self.instruccion_17()
            if  not(correcto): return False,arbol
        elif(self.token.cat=="PR" and self.token.valor=="MIENTRAS"):
            correcto, arbol =self.instruccion_19()
            if  not(correcto): return False, arbol 
        else:
            self.Error (23,self.token)
            return False, NodoVacio(self.token.linea)
        return True, arbol


    def ins_simple(self):
        if(self.token.cat=="Identif" ):
            correcto, arbol = self.inst_simple_20()
            if  not(correcto): return False , arbol
        else:
            self.Error (24,self.token)
            return False, NodoVacio(self.token.linea)
        return True, arbol

    def ins_e_s(self):
        if(self.token.cat=="PR" and self.token.valor=="LEE"):
            correcto, arbol = self.inst_e_s_21()
            if  not(correcto): return False, arbol
            
        elif(self.token.cat=="PR" and self.token.valor=="ESCRIBE"):
            correcto, arbol = self.inst_e_s_22()
            if  not(correcto): return False, arbol
            
        else:
            self.Error (25,self.token)
            return False, NodoVacio(self.token.linea)
        return True, arbol


    def expresion(self):
        if(self.token.cat=="Identif" ):
            correcto, arbol,tipo =self.expresion_23()
            if  not(correcto): return False, arbol,"numero"
        elif(self.token.cat=="PR" and self.token.valor=="NO"):
            correcto, arbol,tipo =self.expresion_23()
            if  not(correcto): return False, arbol,"numero" 
        elif(self.token.cat=="PR" and self.token.valor=="CIERTO"):
            correcto, arbol,tipo =self.expresion_23()
            if  not(correcto): return False, arbol,"numero" 
        elif(self.token.cat=="PR" and self.token.valor=="FALSO"):
            correcto, arbol,tipo = self.expresion_23()
            if  not(correcto): return False, arbol,"numero" 
        elif(self.token.cat=="Simbolo" and self.token.valor=="+"):
            correcto, arbol,tipo = self.expresion_23()
            if  not(correcto): return False, arbol,"numero" 
        elif(self.token.cat=="Simbolo" and self.token.valor=="-"):
            correcto, arbol,tipo = self.expresion_23()
            if  not(correcto): return False, arbol,"numero"
        elif(self.token.cat=="Numero"):
            correcto, arbol,tipo = self.expresion_23()
            if  not(correcto): return False, arbol,"numero"
        elif(self.token.cat=="Simbolo" and self.token.valor=="("):
            correcto, arbol,tipo = self.expresion_23()
            if  not(correcto): return False, arbol,"numero"
        else:
            self.Error (26,self.token)
            return False, NodoVacio(self.token.linea),"numero"
        return True, arbol,tipo


    def expresion_aux(self,arbol,tipo):
        if(self.token.cat=="Simbolo" and self.token.valor==";"):
            correcto, arbol, tipo = self.expresion_aux_25(arbol,tipo)
            if  not(correcto): return False , NodoVacio(self.token.linea),"numero"
        elif(self.token.cat=="PR" and self.token.valor=="ENTONCES"):
            correcto, arbol, tipo = self.expresion_aux_25(arbol,tipo)
            if  not(correcto): return False , NodoVacio(self.token.linea),"numero"
        elif(self.token.cat=="PR" and self.token.valor=="SINO"):
            correcto, arbol, tipo = self.expresion_aux_25(arbol,tipo)
            if  not(correcto): return False, NodoVacio(self.token.linea),"numero" 
        elif(self.token.cat=="PR" and self.token.valor=="HACER"):
            correcto, arbol, tipo = self.expresion_aux_25(arbol,tipo)
            if  not(correcto): return False , NodoVacio(self.token.linea),"numero"
        elif(self.token.cat=="Simbolo" and self.token.valor==")"):
            correcto, arbol, tipo = self.expresion_aux_25(arbol,tipo)
            if  not(correcto): return False , NodoVacio(self.token.linea),"numero"
        elif(self.token.cat=="OpRel" ):
            correcto, arbol, tipo = self.expresion_aux_24(arbol,tipo)
            if  not(correcto): return False , NodoVacio(self.token.linea),"numero"
        else:
            self.Error (27,self.token)
            return False, NodoVacio(self.token.linea),"numero"
        return correcto, arbol, tipo


    def expr_simple(self):
        if(self.token.cat=="Identif" ):
            correcto, arbol, tipo = self.expr_simple_26()
        elif(self.token.cat=="PR" and self.token.valor=="NO"):
            correcto, arbol, tipo = self.expr_simple_26()
        elif(self.token.cat=="PR" and self.token.valor=="CIERTO"):
            correcto, arbol, tipo = self.expr_simple_26() 
        elif(self.token.cat=="PR" and self.token.valor=="FALSO"):
            correcto, arbol, tipo = self.expr_simple_26()
        elif(self.token.cat=="Numero"):
            correcto, arbol, tipo = self.expr_simple_26()
        elif(self.token.cat=="Simbolo" and self.token.valor=="("):
            correcto, arbol, tipo = self.expr_simple_26()
        elif(self.token.cat=="Simbolo" and self.token.valor=="+"):
            correcto, arbol, tipo = self.expr_simple_27()
        elif(self.token.cat=="Simbolo" and self.token.valor=="-"):
            correcto, arbol, tipo =self.expr_simple_27() 
        else:
            self.Error (28,self.token)
            return False, NodoVacio(self.token.linea),"numero"
        return correcto, arbol, tipo


    def resto_exprsimple(self,arbol,tipo):
        if(self.token.cat=="Simbolo" and self.token.valor==";"):
            correcto, arbol, tipo = self.resto_exsimple_30(arbol,tipo)
        elif(self.token.cat=="PR" and self.token.valor=="ENTONCES"):
            correcto, arbol, tipo =self.resto_exsimple_30(arbol,tipo)
        elif(self.token.cat=="PR" and self.token.valor=="SINO"):
            correcto, arbol, tipo =self.resto_exsimple_30(arbol,tipo)
        elif(self.token.cat=="PR" and self.token.valor=="HACER"):
            correcto, arbol, tipo =self.resto_exsimple_30(arbol,tipo)
        elif(self.token.cat=="Simbolo" and self.token.valor==")"):
            correcto, arbol, tipo =self.resto_exsimple_30(arbol,tipo)
        elif(self.token.cat=="OpRel"):
            correcto, arbol, tipo =self.resto_exsimple_30(arbol,tipo)
        elif(self.token.cat=="OpAdd"):
            correcto, arbol, tipo = self.resto_exsimple_28(arbol,tipo)
        elif(self.token.cat=="PR" and self.token.valor=="O"):
            correcto, arbol, tipo =self.resto_exsimple_29(arbol,tipo)
        else:
            self.Error (29,self.token)
            return False, NodoVacio(self.token.linea),"numero"
        return correcto,arbol,tipo


    def termino(self):
        if(self.token.cat=="Identif" ):
            correcto, arbol, tipo = self.termino_31()
        elif(self.token.cat=="PR" and self.token.valor=="NO"):
            correcto, arbol, tipo = self.termino_31()
        elif(self.token.cat=="PR" and self.token.valor=="CIERTO"):
            correcto, arbol, tipo = self.termino_31()
        elif(self.token.cat=="PR" and self.token.valor=="FALSO"):
            correcto, arbol, tipo = self.termino_31()
        elif(self.token.cat=="Numero" ):
            correcto, arbol, tipo = self.termino_31()
        elif(self.token.cat=="Simbolo" and self.token.valor=="("):
            correcto, arbol, tipo = self.termino_31()
        else:
            self.Error (30,self.token)
            return False, NodoVacio(self.token.linea),"numero"
        return correcto, arbol, tipo


    def resto_term(self,arbol,tipo):
        if(self.token.cat=="Simbolo" and self.token.valor==";"):
            correcto, arbol, tipo = self.resto_term_34(arbol,tipo)
        elif(self.token.cat=="PR" and self.token.valor=="ENTONCES"):
            correcto, arbol, tipo=self.resto_term_34(arbol,tipo)
        elif(self.token.cat=="PR" and self.token.valor=="SINO"):
            correcto, arbol, tipo=self.resto_term_34(arbol,tipo)
        elif(self.token.cat=="PR" and self.token.valor=="HACER"):
            correcto, arbol, tipo=self.resto_term_34(arbol,tipo)
        elif(self.token.cat=="PR" and self.token.valor=="Y"):
            correcto, arbol, tipo=self.resto_term_33(arbol,tipo)
        elif(self.token.cat=="PR" and self.token.valor=="O"):
            correcto, arbol, tipo=self.resto_term_34(arbol,tipo)
        elif(self.token.cat=="OpAdd" ):
            correcto, arbol, tipo=self.resto_term_34(arbol,tipo)
        elif(self.token.cat=="OpMult" ):
            correcto, arbol, tipo=self.resto_term_32(arbol,tipo)
        elif(self.token.cat=="Simbolo" and self.token.valor==")"):
            correcto, arbol, tipo=self.resto_term_34(arbol,tipo)
        elif(self.token.cat=="OpRel" ):
            correcto, arbol, tipo=self.resto_term_34(arbol,tipo)
        else:
            self.Error (31,self.token)
            return False,NodoVacio(self.token.linea),"numero"
        return correcto, arbol, tipo


    def factor(self):
        if(self.token.cat=="Identif" ):
            correcto, arbol, tipo = self.factor_35()
        elif(self.token.cat=="Numero" ):
            correcto, arbol, tipo = self.factor_36()
        elif(self.token.cat=="Simbolo" and self.token.valor=="("):
            correcto, arbol, tipo = self.factor_37()
        elif(self.token.cat=="PR" and self.token.valor=="NO"):
            correcto, arbol, tipo = self.factor_38()
        elif(self.token.cat=="PR" and self.token.valor=="CIERTO"):
            correcto, arbol, tipo = self.factor_39()
        elif(self.token.cat=="PR" and self.token.valor=="FALSO"):
            correcto, arbol, tipo = self.factor_40()
        else:
            self.Error (32,self.token)
            return False,NodoVacio(self.token.linea),"numero"
        return correcto, arbol, tipo


    def signo(self):
        if(self.token.cat=="Simbolo" and self.token.valor=="+"):
            correcto, valor = self.signo_41()
        elif(self.token.cat=="Simbolo" and self.token.valor=="-"):
            correcto, valor = self.signo_42()
        else:
            self.Error (33,self.token)
            return False, "+"
        return correcto, valor

    ######################################################################################
    ##                                                                                          
    ## A partir de aqui se muestran los equivalentes a las reglas de nuestra gramática
    ##
    ######################################################################################


    def Programa(self):
        correcto = self.programa() 

        correcto1,_ = self.id() 
        correcto = correcto1 and correcto

        correcto = self.punto_coma() and correcto

        correcto = self.decl_var() and correcto

        correcto_aux , arbol  = self.instrucciones()
        correcto = correcto_aux and correcto

        correcto = self.punto() and correcto

        correcto = self.EOF() and correcto

        print("Se llega al final del analisis")
        print("El AST obtenido es el siguiente:")
        print(arbol)
        return correcto, arbol
            

    def decl_var_2(self):
        correcto = True
        correcto = self.var() and correcto
        correcto_aux,lista_ident=self.lista_ids([])
        correcto = correcto_aux and correcto
        print("Lista de identifcadores encontrada:",lista_ident)

        correcto = self.dos_puntos() and correcto
        correcto_aux,tipo_std = self.tipo_std()
        correcto = correcto_aux and correcto
        print("El tipo encontrado es ",tipo_std)

        for i in lista_ident:
            if(not(self.esta_tabla_simbolos(id))):
                if(self.inserta_tabla_simbolos(i,tipo_std)):
                    print("Insercion en la tabla de simbolos para la variable ",i," con exito")
                else:
                    print("Fallo en la insercion")
            else:
                print("Fallo, este identificador ya existe, no puedes volver a declararlo")

        correcto = self.punto_coma() and correcto
        correcto = self.decl_v() and correcto
        return correcto


    def decl_var_3(self):
        return True


    def decl_v_4(self):
        
        correcto,lista_ident=self.lista_ids([])
        print("Lista indent\n",lista_ident)

        correcto = self.dos_puntos() and correcto
        
        correcto_aux,tipo_std = self.tipo_std()
        print("El tipo encontrado es ",tipo_std)

        correcto = correcto_aux and correcto

        for i in lista_ident:
            if(not(self.esta_tabla_simbolos(id))):
                if(self.inserta_tabla_simbolos(i,tipo_std)):
                    print("Insercion en la tabla de simbolos para la variable ",i," con exito")
                else:
                    print("Fallo en la inserción")
            else:
                print("Fallo, este identificador ya existe, no puedes volver a declararlo")

        correcto = self.punto_coma() and correcto
        correcto = self.decl_v() and correcto
        return correcto



    def decl_v_5(self):
        return True



    def lista_id_6(self,lista_id):

        correcto, id = self.id()
        lista_id.append(id)

        correcto_aux,lista_id = self.resto_listaid(lista_id)
        correcto = correcto_aux and correcto

        return correcto,lista_id
        



    def resto_listaid_7(self,lista_id):
        correcto =self.coma()
        correcto_aux,lista_id=self.lista_ids(lista_id)
        correcto =correcto_aux and correcto

        return correcto,lista_id

    def resto_listaid_8(self,lista_id):
        return True,lista_id


    def tipo_std_9(self):
        if not(self.entero()): return False,"entero"
        return True, "entero"


    def tipo_std_10(self):
        if not(self.real()): return False,"real"
        return True, "real"


    def tipo_std_11(self):
        if not(self.booleano()): return False,"booleano"
        return True, "booleano"


    def instrucciones_12(self):
        if not(self.inicio()): return False, NodoVacio(self.token.linea)
        l = []
        correcto, lista = self.lista_ins(l)
        if(len(lista)>1):
            arb = NodoCompuesta(lista,self.token.linea)
        elif(len(lista)==1):
            arb = lista[0]
        else:
            return correcto, NodoVacio(self.token.linea)
        if not(self.fin()): return False,arb
        return correcto, arb

    def lista_inst_13(self,lista_ins):
        lista = lista_ins
        correcto,arbol = self.instruccion()
        if(correcto==True):
            lista.append(arbol)
        
        if not(self.punto_coma()): return False,lista
        correcto1, lista = self.lista_ins(lista)
        correcto = correcto and correcto1
        if not(correcto1): return False,lista
        return correcto, lista

    def lista_inst_14(self, lista_ins):
        return True, lista_ins

    def instruccion_15(self):
        if not(self.inicio()): return False, NodoVacio(self.token.linea)
        l = []
        correcto, lista_ins = self.lista_ins(l)
        if(len(lista_ins)>1):
            arbol = NodoCompuesta(lista_ins,self.token.linea)
        elif(len(lista_ins)==1):
            arbol = lista_ins[0]
        else:
            arbol = NodoVacio(self.token.linea)
    
        correcto1 = self.fin()
        correcto = correcto and correcto1
        return correcto, arbol

    def instruccion_16(self):
        correcto, arbol = self.ins_simple()
        return correcto,arbol

    def instruccion_17(self):
        correcto, arbol = self.ins_e_s()
        return correcto, arbol


    def instruccion_18(self):
        if not(self.si()): return False, NodoVacio(self.token.linea)
        correcto1, arbol1, _ = self.expresion()
        if not(self.entonces()): return False, NodoVacio(self.token.linea)
        correcto2, arbol2 = self.instruccion()
        if not(self.sino()): return False, NodoVacio(self.token.linea)
        correcto3, arbol3 = self.instruccion()
        correcto = (correcto1 and correcto2 and correcto3)
        return correcto, NodoSi(arbol1,arbol2,arbol3,self.token.linea)


    def instruccion_19(self):
        if not(self.mientras()): return False, NodoVacio(self.token.linea)
        correcto1, arbol1, _ = self.expresion() 
        if not(self.hacer()): return False, NodoVacio(self.token.linea)
        correcto2, arbol2 = self.instruccion()
        return (correcto1 and correcto2), NodoMientras(arbol1, arbol2,self.token.linea)


    def inst_simple_20(self):
        correcto, id = self.id()
        if not(self.esta_tabla_simbolos(id)):
            correcto, arbol = False, NodoVacio(self.token.linea)
        if not(self.opasigna()): return False, NodoVacio(self.token.linea)
        correcto1, arbol,_ = self.expresion()
        correcto = correcto1 and correcto
        if not (correcto) : return False, NodoVacio(self.token.linea)
        return True, NodoAsignacion(id,arbol,self.token.linea)

    def inst_e_s_21(self):
        if not(self.lee()): return False, NodoVacio(self.token.linea)
        if not(self.par_apertura()): return False, NodoVacio(self.token.linea)
        correcto, id = self.id()
        if not(correcto):
            arbol = NodoVacio(self.token.linea)
        if(self.esta_tabla_simbolos(id)):
            tipo = self.tabla_simbolos[id][1]
            if(tipo !="numero"):
                correcto= False
                arbol = NodoVacio(self.token.linea)
        else:
            print("Uso de variable sin declarar: ",id)
            correcto = False
            arbol = NodoVacio(self.token.linea)
        if not(self.par_cierre()): return False, NodoVacio(self.token.linea)
        if not(correcto):
            return correcto, arbol
        return True, NodoLee(id,self.token.linea)


    def inst_e_s_22(self):
        if not(self.escribe()): return False, NodoVacio(self.token.linea)
        if not(self.par_apertura()): return False, NodoVacio(self.token.linea)
        correcto, arbol,_ = self.expr_simple()
        if not(self.par_cierre()): return False, NodoVacio(self.token.linea)
        return correcto, NodoEscribe(arbol, self.token.linea)
        

    def expresion_23(self):
        correcto, arbol , tipo = self.expr_simple()
        correcto_aux, arbol ,tipo= self.expresion_aux(arbol,tipo)
        correcto = correcto and correcto_aux
        return correcto, arbol, tipo


    def expresion_aux_24(self,arbol,tipo):
        correcto, operador = self.oprel()
        if not(correcto): return False, NodoVacio(self.token.linea),"numero"
        correcto, arbol1, tipo1 =self.expr_simple()
        if(tipo=="booleano" and tipo1=="booleano"):
            tipo1="booleano"
        else:
            tipo1="numero"
        return correcto,NodoComparacion(arbol,arbol1,self.token.linea,operador),tipo1


    def expresion_aux_25(self,arbol,tipo):
        return True,arbol,tipo

    def expr_simple_26(self):
        correcto, arbol, tipo = self.termino()
        correcto1,arbol1,tipo1 = self.resto_exprsimple(arbol,tipo)
        return (correcto and correcto1), arbol1,tipo1


    def expr_simple_27(self):
        correcto,valor = self.signo()
        correcto_aux ,arbol,tipo = self.termino()
        correcto = correcto and correcto_aux
        correcto1,arbol1,_ = self.resto_exprsimple(arbol,tipo)
        if(valor =="-"):
            return (correcto and correcto1),NodoAritmetico(arbol1,"-1",self.token.linea,"*") ,"numero"
        return (correcto and correcto1), arbol1,"numero"


    def resto_exsimple_28(self,arbol,tipo):
        correcto,operador = self.opsuma()
        if not(correcto): return False,NodoVacio(self.token.linea),"numero"
        correcto, arbol1, tipo1 = self.termino()
        correcto_aux, arbol2,_ = self.resto_exprsimple(arbol1,tipo1)
        return (correcto and correcto_aux),NodoAritmetico(arbol,arbol2,self.token.linea,operador),"numero"


    def resto_exsimple_29(self,arbol,tipo):
        correcto, operador = self.o()
        if not(correcto): return False
        correcto, arbol1, tipo1 = self.termino()
        correcto_aux , arbol2, tipo2 = self.resto_exprsimple(arbol1,tipo1)
        correcto = correcto and correcto_aux
        if(tipo!="booleano" or tipo2!="booleano"):
            return False, NodoVacio(self.token.linea), "booleano"
        return correcto, NodoOPBool(arbol,arbol2,self.token.linea,operador), "booleano"


    def resto_exsimple_30(self,arbol,tipo):
        return True,arbol,tipo


    def termino_31(self):
        correcto,arbol,tipo = self.factor()
        correcto1,arbol1,tipo1 = self.resto_term(arbol,tipo)
        correcto = correcto and correcto1
        return correcto , arbol1, tipo1

    def resto_term_32(self,arbol,tipo):
        correcto, operador = self.opmult()
        if not(correcto): return False, NodoVacio(self.token.linea), "numero"
        correcto1, arbol1, tipo1 = self.factor()
        correcto2,arbol2,_ = self.resto_term(arbol1,tipo1)
        correcto = correcto and correcto1 and correcto2
        return correcto,NodoAritmetico(arbol,arbol2,self.token.linea,operador) ,"numero"

    def resto_term_33(self,arbol,tipo):
        correcto, operador = self.y()
        if not(correcto): return False, NodoVacio(self.token.linea), "booleano"
        correcto1,arbol1,tipo1 = self.factor()
        correcto2, arbol2,tipo2 = self.resto_term(arbol1,tipo1)
        correcto = correcto1 and correcto2
        if(tipo=="booleano" and tipo2 == "booleano"):
            return correcto, NodoOPBool(arbol,arbol2,self.token.linea,operador), "booleano"
        return correcto, NodoVacio(self.token.linea), "numero"


    def resto_term_34(self,arbol,tipo):
        return True, arbol,tipo

    def factor_35(self):
        correcto, valor = self.id()
        if not(correcto):
            return False, NodoVacio(self.token.linea),"numero"
        if(self.esta_tabla_simbolos(valor)):
            tipo = self.tabla_simbolos[valor][1]
        else:
            print("Uso de variable sin declarar: ",valor)
            correcto= False
            tipo = "numero"
        
        return correcto,NodoAccesoVariable(valor,self.token.linea,tipo),tipo
            

    def factor_36(self):
        correcto,valor,tipo = self.num()
        if(tipo=="entero"):
            return correcto, NodoEntero(valor,self.token.linea),"numero"
        return correcto, NodoReal(valor,self.token.linea),"numero"
        

    def factor_37(self):
        if not(self.par_apertura()): return False, NodoVacio(self.token.linea), "numero"
        correcto, arbol, tipo = self.expresion()
        if not(self.par_cierre()): return False, NodoVacio(self.token.linea), "numero"
        return correcto,arbol,tipo


    def factor_38(self):
        if not(self.no()): return False,NodoVacio(self.token.linea),"booleano"
        correcto, arbol, tipo = self.factor()
        if(tipo != "booleano"):
            return False, NodoVacio(self.token.linea),"booleano"
        return correcto,NodoOPBoolUnario(arbol,self.token.linea,"NO"),"booelano"


    def factor_39(self):
        if not(self.cierto()): return False,NodoVacio(self.token.linea),"booleano"
        return True,NodoBooleano(True,self.token.linea),"booleano"
        

    def factor_40(self):
        if not(self.falso()): return False,NodoVacio(self.token.linea),"booleano"
        return True,NodoBooleano(False,self.token.linea),"booleano"
        

    def signo_41(self):
        correcto,valor = self.mas()
        return correcto,valor


    def signo_42(self):
        correcto,valor = self.menos()
        return correcto,valor
        


 
########################################################
##
## Programa principal que lanza el analizador sintactico
####################################################
if __name__=="__main__":
    script, filename=argv
    txt=open(filename)
    print ("Este es tu fichero %r" % filename)
    i=0
    fl = flujo.Flujo(txt)
    anlex=analex.Analex(fl)
    S = Sintactico(anlex)
    correcto , arbol = S.Programa()
    if correcto:
      print ("Analisis semántico SATISFACTORIO. Fichero :", filename, "CORRECTO")
    else:
       print ("Analisis semántico CON ERRORES. Fichero :", filename, "ERRONEO")

