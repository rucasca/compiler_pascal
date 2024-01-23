#!/usr/bin/env python

#import arboles

import componentes
import flujo
import analex
import sys
from sys import argv
#import errores


class Sintactico:
#Constructor de la clase que implementa el Analizador Sintactico
#Solicita el primer compnente lexico 
    def __init__(self, lexico):
        self.lexico= lexico
        self.token=self.lexico.Analiza()
        self.lista=[]

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
            self.token = self.lexico.Analiza()
        else:
            self.Error (2,self.token)
            return False
        return True
        
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
            return False
        return True


    def o(self):
        if(self.token.cat=="PR" and self.token.valor=="O"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (42,self.token)
            return False
        return True


    def opasigna(self):
        if(self.token.cat=="OpAsigna" ):
            self.token = self.lexico.Analiza()
        else:
            self.Error (43,self.token)
            return False
        return True


    def opsuma(self):
        if(self.token.cat=="OpAdd" ):
            self.token = self.lexico.Analiza()
        else:
            self.Error (44,self.token)
            return False
        return True

    def opmult(self):
        if(self.token.cat=="OpMult" ):
            self.token = self.lexico.Analiza()
        else:
            self.Error (45,self.token)
            return False
        return True


    def oprel(self):
        if(self.token.cat=="OpRel" ):
            self.token = self.lexico.Analiza()
        else:
            self.Error (46,self.token)
            return False
        return True

    def mas(self):
        if(self.token.cat=="Simbolo" and self.token.valor=="+"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (47,self.token)
            return False
        return True

    def menos(self):
        if(self.token.cat=="Simbolo" and self.token.valor=="-"):
            self.token = self.lexico.Analiza()
        else:
            self.Error (48,self.token)
            return False
        return True


    def num(self):
        if(self.token.cat=="Numero" ):
            self.token = self.lexico.Analiza()
        else:
            self.Error (49,self.token)
            return False
        return True

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

    def lista_ids(self):
        if(self.token.cat=="Identif" ):
            if  not(self.lista_id_6()): return False 
        else:
            self.Error (18,self.token)
            return False 
        return True

    def resto_listaid(self):
        if(self.token.cat=="Simbolo" and self.token.valor==","):
            if  not(self.resto_listaid_7()): return False 
            
        elif(self.token.cat=="Simbolo" and self.token.valor==":"):
            if  not(self.resto_listaid_8()): return False 
            
        else:
            self.Error (19,self.token)
            return False
        
        return True


    def tipo_std(self):
        if(self.token.cat=="PR" and self.token.valor=="ENTERO"):
            if  not(self.tipo_std_9()): return False 
            
        elif(self.token.cat=="PR" and self.token.valor=="REAL"):
            if  not(self.tipo_std_10()): return False 
            
        elif(self.token.cat=="PR" and self.token.valor=="BOOLEANO"):
            if  not(self.tipo_std_11()): return False 
            
        else:
            self.Error (20,self.token)
            return False
        return True


    def instrucciones(self):
        if(self.token.cat=="PR" and self.token.valor=="INICIO"):
            if  not(self.instrucciones_12()): return False   
        else:
            self.Error (21,self.token)
            return False
        return True

    def lista_ins(self):
        if(self.token.cat=="Identif" ):
            if  not(self.lista_inst_13()): return False  
        elif(self.token.cat=="PR" and self.token.valor=="INICIO"):
            if  not(self.lista_inst_13()): return False
        elif(self.token.cat=="PR" and self.token.valor=="SI"):
            if  not(self.lista_inst_13()): return False
        elif(self.token.cat=="PR" and self.token.valor=="ENTONCES"):
            if  not(self.lista_inst_13()): return False
        elif(self.token.cat=="PR" and self.token.valor=="MIENTRAS"):
            if  not(self.lista_inst_13()): return False
        elif(self.token.cat=="PR" and self.token.valor=="LEE"):
           if  not(self.lista_inst_13()): return False
        elif(self.token.cat=="PR" and self.token.valor=="ESCRIBE"):
            if  not(self.lista_inst_13()): return False
        elif(self.token.cat=="PR" and self.token.valor=="FIN"):
            if  not(self.lista_inst_14()): return False
        else:
            self.Error (22,self.token)
            return False
        return True

    def instruccion(self):
        if(self.token.cat=="Identif" ):
            if  not(self.instruccion_16()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="INICIO"):
            if  not(self.instruccion_15()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="SI"):
            if  not(self.instruccion_18()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="LEE"):
            if  not(self.instruccion_17()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="ESCRIBE"):
            if  not(self.instruccion_17()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="MIENTRAS"):
            if  not(self.instruccion_19()): return False 
        else:
            self.Error (23,self.token)
            return False
        return True


    def ins_simple(self):
        if(self.token.cat=="Identif" ):
            if  not(self.inst_simple_20()): return False 
        else:
            self.Error (24,self.token)
            return False
        return True

    def ins_e_s(self):
        if(self.token.cat=="PR" and self.token.valor=="LEE"):
            if  not(self.inst_e_s_21()): return False 
            
        elif(self.token.cat=="PR" and self.token.valor=="ESCRIBE"):
            if  not(self.inst_e_s_22()): return False 
            
        else:
            self.Error (25,self.token)
            return False
        return True


    def expresion(self):
        if(self.token.cat=="Identif" ):
            if  not(self.expresion_23()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="NO"):
            if  not(self.expresion_23()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="CIERTO"):
            if  not(self.expresion_23()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="FALSO"):
            if  not(self.expresion_23()): return False 
        elif(self.token.cat=="Simbolo" and self.token.valor=="+"):
            if  not(self.expresion_23()): return False 
        elif(self.token.cat=="Simbolo" and self.token.valor=="-"):
            if  not(self.expresion_23()): return False 
        elif(self.token.cat=="Numero"):
            if  not(self.expresion_23()): return False
        elif(self.token.cat=="Simbolo" and self.token.valor=="("):
            if  not(self.expresion_23()): return False
        else:
            self.Error (26,self.token)
            return False
        return True


    def expresion_aux(self):
        if(self.token.cat=="Simbolo" and self.token.valor==";"):
            if  not(self.expresion_aux_25()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="ENTONCES"):
            if  not(self.expresion_aux_25()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="SINO"):
            if  not(self.expresion_aux_25()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="HACER"):
            if  not(self.expresion_aux_25()): return False 
        elif(self.token.cat=="Simbolo" and self.token.valor==")"):
            if  not(self.expresion_aux_25()): return False 
        elif(self.token.cat=="OpRel" ):
            if  not(self.expresion_aux_24()): return False 
        else:
            self.Error (27,self.token)
            return False
        return True


    def expr_simple(self):
        if(self.token.cat=="Identif" ):
            if  not(self.expr_simple_26()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="NO"):
            if  not(self.expr_simple_26()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="CIERTO"):
            if  not(self.expr_simple_26()): return False 
        elif(self.token.cat=="PR" and self.token.valor=="FALSO"):
            if  not(self.expr_simple_26()): return False 
        elif(self.token.cat=="Numero"):
            if  not(self.expr_simple_26()): return False 
        elif(self.token.cat=="Simbolo" and self.token.valor=="("):
            if  not(self.expr_simple_26()): return False 
        elif(self.token.cat=="Simbolo" and self.token.valor=="+"):
            if  not(self.expr_simple_27()): return False 
        elif(self.token.cat=="Simbolo" and self.token.valor=="-"):
            if  not(self.expr_simple_27()): return False 
        else:
            self.Error (28,self.token)
            return False
        return True


    def resto_exprsimple(self):
        if(self.token.cat=="Simbolo" and self.token.valor==";"):
            if  not(self.resto_exsimple_30()): return False
        elif(self.token.cat=="PR" and self.token.valor=="ENTONCES"):
            if  not(self.resto_exsimple_30()): return False
        elif(self.token.cat=="PR" and self.token.valor=="SINO"):
            if  not(self.resto_exsimple_30()): return False
        elif(self.token.cat=="PR" and self.token.valor=="HACER"):
            if  not(self.resto_exsimple_30()): return False
        elif(self.token.cat=="Simbolo" and self.token.valor==")"):
            if  not(self.resto_exsimple_30()): return False
        elif(self.token.cat=="OpRel"):
            if  not(self.resto_exsimple_30()): return False
        elif(self.token.cat=="OpAdd"):
            if  not(self.resto_exsimple_28()): return False
        elif(self.token.cat=="PR" and self.token.valor=="O"):
            if  not(self.resto_exsimple_29()): return False
        else:
            self.Error (29,self.token)
            return False
        return True


    def termino(self):
        if(self.token.cat=="Identif" ):
            if  not(self.termino_31()): return False
        elif(self.token.cat=="PR" and self.token.valor=="NO"):
            if  not(self.termino_31()): return False
        elif(self.token.cat=="PR" and self.token.valor=="CIERTO"):
            if  not(self.termino_31()): return False
        elif(self.token.cat=="PR" and self.token.valor=="FALSO"):
            if  not( self.termino_31()): return False
        elif(self.token.cat=="Numero" ):
            if  not(self.termino_31()): return False
        elif(self.token.cat=="Simbolo" and self.token.valor=="("):
            if  not(self.termino_31()): return False
        else:
            self.Error (30,self.token)
            return False
        return True


    def resto_term(self):
        

        if(self.token.cat=="Simbolo" and self.token.valor==";"):
            if  not(self.resto_term_34()): return False
        elif(self.token.cat=="PR" and self.token.valor=="ENTONCES"):
            if  not(self.resto_term_34()): return False
        elif(self.token.cat=="PR" and self.token.valor=="SINO"):
            if  not(self.resto_term_34()): return False
        elif(self.token.cat=="PR" and self.token.valor=="HACER"):
            if  not(self.resto_term_34()): return False
        elif(self.token.cat=="PR" and self.token.valor=="Y"):
            if  not(self.resto_term_33()): return False
        elif(self.token.cat=="PR" and self.token.valor=="O"):
            if  not(self.resto_term_34()): return False
        elif(self.token.cat=="OpAdd" ):
            if  not(self.resto_term_34()): return False
        elif(self.token.cat=="OpMult" ):
            if  not(self.resto_term_32()): return False
        elif(self.token.cat=="Simbolo" and self.token.valor==")"):
            if  not(self.resto_term_34()): return False
        elif(self.token.cat=="OpRel" ):
            if  not( self.resto_term_34()): return False
        else:
            self.Error (31,self.token)
            return False
        return True


    def factor(self):
        if(self.token.cat=="Identif" ):
            if  not(self.factor_35()): return False
        elif(self.token.cat=="Numero" ):
            if  not(self.factor_36()): return False
        elif(self.token.cat=="Simbolo" and self.token.valor=="("):
            if  not(self.factor_37()): return False
        elif(self.token.cat=="PR" and self.token.valor=="NO"):
            if  not(self.factor_38()): return False
        elif(self.token.cat=="PR" and self.token.valor=="CIERTO"):
            if  not(self.factor_39()): return False
        elif(self.token.cat=="PR" and self.token.valor=="FALSO"):
            if  not(self.factor_40()): return False
        else:
            self.Error (32,self.token)
            return False
        return True


    def signo(self):
        if(self.token.cat=="Simbolo" and self.token.valor=="+"):
            if  not(self.signo_41()): return False
        elif(self.token.cat=="Simbolo" and self.token.valor=="-"):
            if  not(self.signo_42()): return False
        else:
            self.Error (33,self.token)
            return False
        return True

    ######################################################################################
    ##                                                                                          
    ## A partir de aqui se muestran los equivalentes a las reglas de nuestra gramática
    ##
    ######################################################################################


    def Programa(self):
        print("programa ")
        if not(self.programa()): return False
        if not(self.id()): return False
        if not(self.punto_coma()): return False
        if not(self.decl_var()): return False
        if not(self.instrucciones()): return False
        if not(self.punto()): return False
        if not(self.EOF()): return False
        return True
            

    def decl_var_2(self):
        print("decl_var_2 ")
        if not(self.var()): return False
        if not(self.lista_ids()): return False
        if not(self.dos_puntos()): return False
        if not(self.tipo_std()): return False
        if not(self.punto_coma()): return False
        if not(self.decl_v()): return False
        return True


    def decl_var_3(self):
        print("decl_var_3 ")
        return True


    def decl_v_4(self):
        print("decl var 4_1")
        if not(self.lista_ids()): return False
        if not(self.dos_puntos()): return False
        if not(self.tipo_std()): return False
        if not(self.punto_coma()): return False
        if not(self.decl_v()): return False
        return True



    def decl_v_5(self):
        print("decl var 5 ")
        return True



    def lista_id_6(self):
        print("lista_id_6 ")
        if not(self.id()): return False
        if not(self.resto_listaid()): return False
        return True
        



    def resto_listaid_7(self):
        print("resto_lista_id_7 ")
        if not(self.coma()): return False
        if not(self.lista_ids()): return False
        return True

    def resto_listaid_8(self):
        print("resto_lista_id_8 ")
        return True


    def tipo_std_9(self):
        print("tipo std 9 ")
        if not(self.entero()): return False
        return True


    def tipo_std_10(self):
        print("tipo std 10 ")
        if not(self.real()): return False
        return True


    def tipo_std_11(self):
        print("tipo std 11 ")
        if not(self.booleano()): return False
        return True


    def instrucciones_12(self):
        print("intrsucciones_12 ")
        if not(self.inicio()): return False
        if not(self.lista_ins()): return False        
        if not(self.fin()): return False
        return True

    def lista_inst_13(self):
        print("lista_inst_13 ")
        if not(self.instruccion()): return False
        if not(self.punto_coma()): return False
        if not(self.lista_ins()): return False
        return True

    def lista_inst_14(self):
        print("lista_intr_14 ")
        return True

    def instruccion_15(self):
        print("intrsuccion_15 ")
        if not(self.inicio()): return False
        if not(self.lista_ins()): return False
        if not(self.fin()): return False
        return True

    def instruccion_16(self):
        print("intrsuccion_16 ")
        if not(self.ins_simple()): return False
        return True

    def instruccion_17(self):
        print("intrsuccion_17 ")
        if not(self.ins_e_s()): return False
        return True


    def instruccion_18(self):
        print("intrsuccion_18 ")
        if not(self.si()): return False
        if not(self.expresion()): return False
        if not(self.entonces()): return False
        if not(self.instruccion()): return False
        if not(self.sino()): return False
        if not(self.instruccion()): return False
        return True


    def instruccion_19(self):
        print("intrsuccion_19 ")
        if not(self.mientras()): return False
        if not(self.expresion()): return False   
        if not(self.hacer()): return False
        if not(self.instruccion()): return False
        return True


    def inst_simple_20(self):
        print("isnt_simple_20 ")
        if not(self.id()): return False
        if not(self.opasigna()): return False
        if not(self.expresion()): return False
        return True

    def inst_e_s_21(self):
        print("ins_e_s_21 ")
        if not(self.lee()): return False
        if not(self.par_apertura()): return False
        if not(self.id()): return False
        if not(self.par_cierre()): return False
        return True


    def inst_e_s_22(self):
        print("ins_e_s_22 ")
        if not(self.escribe()): return False
        if not(self.par_apertura()): return False
        if not(self.expr_simple()): return False
        if not(self.par_cierre()): return False
        return True
        

    def expresion_23(self):
        print("expresion23 ")
        if not(self.expr_simple()): return False
        if not(self.expresion_aux()): return False
        return True


    def expresion_aux_24(self):
        print("expresion_aux_24 ")
        if not(self.oprel()): return False
        if not(self.expr_simple()): return False
        return True


    def expresion_aux_25(self):
        print("expresion_aux_25 ")
        return True

    def expr_simple_26(self):
        print("expr_simple_26 ")
        if not(self.termino()): return False
        if not(self.resto_exprsimple()): return False
        return True


    def expr_simple_27(self):
        print("expr_simple_27 ")
        if not(self.signo()): return False
        if not(self.termino()): return False
        if not(self.resto_exprsimple()): return False
        return True


    def resto_exsimple_28(self):
        print("resto_expsimple_28 ")
        if not(self.opsuma()): return False
        if not(self.termino()): return False
        if not(self.resto_exprsimple()): return False
        return True


    def resto_exsimple_29(self):
        print("resto_expsimple_29 ")
        if not(self.o()): return False
        if not(self.termino()): return False
        if not(self.resto_exprsimple()): return False
        return True


    def resto_exsimple_30(self):
        print("resto_expsimple_30 ")
        return True


    def termino_31(self):
        print("termino31 ")
        if not(self.factor()): return False
        if not(self.resto_term()): return False
        return True

    def resto_term_32(self):
        print("resto_term_32 ")
        if not(self.opmult()): return False
        if not(self.factor()): return False
        if not(self.resto_term()): return False
        return True

    def resto_term_33(self):
        print("resto_term_33 ")
        if not(self.y()): return False
        if not(self.factor()): return False
        if not(self.resto_term()): return False
        return True


    def resto_term_34(self):
        print("resto_term_34 ")
        return True

    def factor_35(self):
        print("factor_35 ")
        if not(self.id()): return False
        return True
        

    def factor_36(self):
        print("factor_36 ")
        if not(self.num()): return False
        return True
        

    def factor_37(self):
        print("factor_37 ")
        if not(self.par_apertura()): return False
        if not(self.expresion()): return False
        if not(self.par_cierre()): return False
        return True


    def factor_38(self):
        print("factor_38 ")
        if not(self.no()): return False
        if not(self.factor()): return False
        return True


    def factor_39(self):
        print("factor_39 ")
        if not(self.cierto()): return False
        return True
        

    def factor_40(self):
        print("factor_40 ")
        if not(self.falso()): return False
        return True
        

    def signo_41(self):
        print("signo_41 ")
        if not(self.mas()): return False
        return True


    def signo_42(self):
        print("signo_42 ")
        if not(self.menos()): return False
        return True


 
########################################################
##
## PRograma principal que lanza el analizador sintactico
####################################################
if __name__=="__main__":
    script, filename=argv
    txt=open(filename)
    print ("Este es tu fichero %r" % filename)
    i=0
    fl = flujo.Flujo(txt)
    anlex=analex.Analex(fl)
    S = Sintactico(anlex)
    if S.Programa():
      print ("Analisis sintactico SATISFACTORIO. Fichero :", filename, "CORRECTO")
    else:
       print ("Analisis sintactico CON ERRORES. Fichero :", filename, "ERRONEO")

