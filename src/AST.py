#!/usr/bin/env python

class AST:
	def __str__(self):
		return self.arbol()

class NodoAsignacion(AST):
	def __init__(self, izda, exp, linea):
		self.izda = izda
		self.exp = exp
		self.linea = linea

	def arbol(self):
		return '( "Asignacion"  "linea: %s" %s %s\n)' % (self.linea, self.izda, self.exp)

class NodoSi(AST):
	def __init__(self, exp, si, sino, linea):
		self.exp = exp
		self.si = si
		self.sino = sino
		self.linea = linea

	def arbol(self):
		return '( "Si" "linea: %s" %s\n %s\n %s\n )' % (self.linea, self.exp, self.si, self.sino)

class NodoMientras(AST):
	def __init__(self, exp, inst, linea):
		self.exp = exp
		self.inst = inst
		self.linea = linea

	def arbol(self):
		return '( "Mientras" "linea: %s" %s\n %s\n )' % (self.linea, self.exp, self.inst)

class NodoLee(AST):
	def __init__(self,var,linea):
		self.var = var
		self.linea = linea

	def arbol(self):
		return '( "Lee" "linea: %s" %s )' % (self.linea, self.var)

class NodoEscribe(AST):
	def __init__(self, exp, linea):
		self.exp = exp
		self.linea = linea

	def arbol(self):
		return '( "Escribe" "linea: %s" %s )' % (self.linea, self.exp)

class NodoCompuesta(AST):
	def __init__(self, lsen, linea):
		self.lsen = lsen
		self.linea = linea

	def arbol(self):
		r= ""
		for sent in self.lsen:
			r+= sent.arbol()+"\n"
		return '( "Compuesta"\n %s)' % r

class NodoComparacion(AST):
	def __init__(self, izq, dcha, linea, op):
		self.izq = izq
		self.dcha = dcha
		self.linea = linea
		self.op = op
		self.tipo = "booleano"

	def arbol(self):
		return '( "Comparacion" "op: %s" "tipo: %s" "linea: %s" \n %s\n %s\n)' % (self.op, self.tipo, self.linea, self.izq, self.dcha)

class NodoAritmetico(AST):
	def __init__(self, izq, dcha, linea, op):
		self.izq = izq
		self.dcha = dcha
		self.linea = linea
		self.op = op
		self.tipo = "numero"

	def arbol(self):
		return '( "Aritmetica" "op: %s" "tipo: %s" "linea: %s" \n %s\n %s\n)' % (self.op, self.tipo, self.linea, self.izq, self.dcha)

class NodoOPBool(AST):
	def __init__(self, izq, dcha, linea, op):
		self.izq = izq
		self.dcha = dcha
		self.linea = linea
		self.op = op
		self.tipo = "booleano"

	def arbol(self):
		return '( "Operacion Booleana" "op: %s" "tipo: %s" "linea: %s" \n %s\n %s\n)' % (self.op, self.tipo, self.linea, self.izq, self.dcha)

class NodoOPBoolUnario(AST):
	def __init__(self, izq, linea, op):
		self.izq = izq
		self.linea = linea
		self.op = op
		self.tipo = "booleano"

	def arbol(self):
		return '( "Operacion Booleana" "op: %s" "tipo: %s" "linea: %s" \n %s\n )' % (self.op, self.tipo, self.linea, self.izq)

class NodoEntero(AST):
	def __init__(self, valor, linea):
		self.valor = valor
		self.linea = linea
		self.tipo = "numero"
	
	def arbol(self):
		return '( "Entero" "valor: %s" "tipo: %s" "linea: %s" )' % (self.valor, self.tipo, self.linea)


class NodoReal(AST):
	def __init__(self, valor, linea):
		self.valor = valor
		self.linea = linea
		self.tipo = "numero"
	def arbol(self):
		return '( "Real" "valor: %s" "tipo: %s" "linea: %s" )' % (self.valor, self.tipo, self.linea)

class NodoBooleano(AST):
	def __init__(self, valor, linea):
		self.valor = valor
		self.linea = linea
		self.tipo = "booleano"
	
	def arbol(self):
		return '( "BOOLEANO" "valor: %s" "tipo: %s" "linea: %s" )' % (self.valor, self.tipo, self.linea)

class NodoAccesoVariable(AST):
	def __init__(self, var, linea, tipo):
		self.var = var
		self.linea = linea
		self.tipo = tipo

	def arbol(self):
		return '( "AccesoVariable" "v: %s" "linea: %s" )' % (self.var, self.linea)

class NodoVacio(AST):
	def __init__(self,nl):
		self.linea = nl
	
	def arbol(self):
		return '( "Nodo Vacio linea: %s" )' % (self.linea)

	
		