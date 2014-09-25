#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  valores btc usd y VEB
#  
#  Copyright 2014 David Rodriguez <davidrodriguez at gmail dot com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



#importando los  modulos a usar
import urllib2
import simplejson
import json 

#esta es la url donde esta el archivo json 
url = "http://api.bitven.com/prices"
 
#Aqui usamos urllib2 para abrir la pagina 
resp = urllib2.Request(url)
opener = urllib2.build_opener()
#aqui obtenemos la data
data = opener.open(resp)
#en este punto  decodificamos la data y podemos separar lo que necesitemos 
result = simplejson.load(data)
# Se separa las llaves 
rk=result.keys()
# Se separan los valores
rv=result.values()
 
# Se formatea el resultado de lo requerido 
print 'bitcoin   | dolartoday'
print '%s | %s' % (rk[0], ' '+ rk[1])
print '-' * 30
print str(rv[0]), '       |        ' + str(rv[1])
