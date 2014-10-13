#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       MenuProyecto calculadora de bitcoins dolares y bolivares



import sys
import os

def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ('clear')
    elif os.name == ('ce', 'nt', 'dos'):
        os.system ('cls')
	
		

def salir():
    sys.exit()

#opciones de menu principal
def opciones():
   opc = int(raw_input ('Escoge una opcion "3" para salir: '))
   if opc == 1:
       print"currency"
       menudivisa()
   elif opc == 2:
       print"otras cosas"
       #menutemperatura()
   elif opc == 3:
       print "ha salido del menu"
       salir()
   elif opc != 3:
       print "introduzca un valor correcto"
       
          
   else:
       print "invalido marque entre 1 y 4"



		
##menu principal
def menu():
    print "*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*"
    print "              Menú convertidor – Convertidor Tipo A              "
    print "                                     "
    print "           Autor(es): David rodriguez            "
    print "*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*"
    print "                         "
    print "1) divisas"
    print "3). Salir"
###############################################################################

#submenu Currency
def menudivisa():
    print "*/*/*/*/*/*/*/*/*/*/*/*/*/"
    print "menu conversion de divisas"
    print "*/*/*/*/*/*/*/*/*/*/*/*/*/"
    print "1)bolivares a dolares."
    print "2)dolares a btc."
    print "3)btc a mbtc."
    print "4)btc a bolivares"
    print "5)"
    print "6)Salir"	
    opc = int(input('Escoge una opcion "6" para salir: '))
    if opc == 1:
		print "VEF a USD"
		uspar=''
		print  str(vu(uspar)) + " Dolares "
    elif opc == 2:
		print "USD a BTC"
		bit=""
		print float(bu(bit)) , " Bitcoins "    
    elif opc == 3:
		print "BTC a Mbtc"
		mbit=""
		print mb(mbit) , " MiliBitcoins "		
    elif opc == 4:
		print "BTC a vef"
		resvef=""
		resusd=""
		print btvef(resvef, resusd) , " Bolivares  y dolares"
    elif opc == 5:
		print "otras"
		mbit=''
		print " MiliBitcoins "
    elif opc == 6:
		print "chao"
		salir()
    elif opc > 7:
		print "invalido marque entre 1 y 6"
    else:
	    print "vuelve"
#funcion vu

def vu(uspar):
	vef=int(input('Introduce el número de VEF a convertir: '))
	usd=96.76
	uspar =vef/usd
	return uspar

def bu(bit):
	usd=float(input('Introduce el número de USD a convertir: '))
	btc=402
	bit=usd/btc
	return bit

def mb(mbit):
	btc=input('Introduce el número de BTC a convertir: ')
	mbit=btc*1000
	return mbit
	
def btvef(resvef, resusd):
	btc=input('Introduce el número de BTC a convertir: ')
	vef=input('Introduce el número de vef: ')
	btcusd=input('Introduce el número de dolarbtc: ')
	resvef=btc*vef/1
	resusd=btc*btcusd
	return resvef, resusd
	

while True:
   menu()
   opciones()



