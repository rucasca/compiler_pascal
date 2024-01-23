#!/usr/bin/env python
# -*- coding: latin-1 -*-

import os
#########################################################################################
##
##  Clase: Flujo.
##  Funcion:  Permite leer una cadena caracter a caracter
##
##
########################################################################################
class Flujo:
  #  Contructor de la clase. Se le pasa la cadena a leer
  def __init__(self,f):
    self.pos= -1
    self.fic=f

  #Devuelve un caracter de la cadenma
  def siguiente(self):
    return self.fic.read(1)

  # Revierte un caracter no leido a la cadena de partida
  def devuelve(self, c):
     self.fic.seek(self.fic.tell()-1, 0)

  # Indica la posicion leida
  def posleida(self):
    return self.pos

  # Devuelve la cadena en la que estamos leyendo
  def cadena(self):
    return self.cad

