# -*- coding: utf-8 -*- 
import os
import sys
import random
import time 
tablero = [] #Tablero PC
tablero2 = [] #Tablero Jugador1
tablero3 = [] #Tablero Jugador2
intercambio = 0 
#*********************************************Anclaje a nueva guerra :)**************************************************
def reinicio_juego():
		jugar_nuevo = True
		while jugar_nuevo == True:
			nueva_guerra = raw_input("\t\t\t\t\t¿Tripulante, desea provocar otra guerra? si/no: ")
			if nueva_guerra.lower() == "no":
				os.system("clear")
				print "\t\t\t\t\t   Preparando retirada de los barcos..."
				time.sleep(2)
				os.system("clear")
				print "\t\t\t\t\t             Tropas retiradas"
				sys.exit()
				break
			elif nueva_guerra.lower() == "si":
				os.system("clear")
				validacion_menu = False
				break
			else:
				print "\t\t\t\t\t\tTripulante no entiendo su lenguaje."
				jugar_nuevo = True
print "                                "
print ""
print "\t\t██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗      █████╗     ███╗   ██╗ █████╗ ██╗   ██╗ █████╗ ██╗  ✈ "
print "\t\t██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║     ██╔══██╗    ████╗  ██║██╔══██╗██║   ██║██╔══██╗██║     "
print "\t\t██████╔╝███████║   ██║   ███████║██║     ██║     ███████║    ██╔██╗ ██║███████║██║   ██║███████║██║     " 
print "\t\t██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██║     ██╔══██║    ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══██║██║  ✈ "
print "\t\t██████╔╝██║  ██║   ██║   ██║  ██║███████╗███████╗██║  ██║    ██║ ╚████║██║  ██║ ╚████╔╝ ██║  ██║███████╗"
print "\t\t╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝"
print "\t\t|  ~                                    ~                    ☀            ~                 ~~         |"
print "\t\t|                                      ☁                                          ~~~~                 |"
print "\t\t|            ~~~~~~~~         ~~~~               |>         ~~~    ☁                                   |"
print "\t\t|       ~                                   ~~   |   ~~~~            ~~        ~~~~~~~~          ~~    |"
print "\t\t|                                      ~~~~      |    \O/     ~~~                                      |"
print "\t\t|   ~~~~        ~~     ~~~~~     ~~ _____________|_____|__________          ~~                         |"
print "\t\t|                                   \----------------------------/ ~~                    ~~~~~~        |"
print "\t\t|        ~~~~                 ~~     \--------------------------/     ~~                               |"
print "\t\t|                               ~~    \________________________/   ~~           ~~~~~~                 |"
print "\t\t|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
print "\t\t\______________________________________________________________________________________________________/"
print ""
print ""
print "\t\t\t\t\t   Tripulante estamos recargando sus municiones..."
print ""
time.sleep(2)
os.system("clear")
#==================Menú=======================
validacion_menu = True
while validacion_menu == True:
	tablero = [] #Tablero PC
	tablero2 = [] #Tablero Jugador1
	tablero3 = [] #Tablero Jugador2
	try:
		print ""
		print ""
		print ""
		print ""
		print"\t\t\t\t\t\t███╗   ███╗███████╗███╗   ██╗██╗   ██╗"
		print"\t\t\t\t\t\t████╗ ████║██╔════╝████╗  ██║██║   ██║"
		print"\t\t\t\t\t\t██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║"
		print"\t\t\t\t\t\t██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║"
		print"\t\t\t\t\t\t██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝"
		print"\t\t\t\t\t\t╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝"
		print ""
		print ""
		print "\t\t\t\t\t\tSelecciona número de opción que desees: "
		print "\t\t\t\t\t\t1.) Juego individual"
		print "\t\t\t\t\t\t2.) Multijugador (2 Jugadores) "
		print "\t\t\t\t\t\t3.) Instrucciones"
		print "\t\t\t\t\t\t4.) Salir"
		print ""
		print"\t\t\t\t                           .                  |>"
		print"\t\t\t\t                            |>   ☀            |"
		print"\t\t\t\t                  .         |               *+W+-*"
		print"\t\t\t\t     .           +y        +W+              . H                 ."
		print"\t\t\t\t  .  +y            |I.   y  |               ! H= .           .  ^"
		print"\t\t\t\t  !   \     .     |H '. /   |  ___.        .! H  !   +--.--y !  V"
		print"\t\t\t\t  !    \     \  +=|H|=='.=+ | |====\   _  '_H_H__H_. H_/=  J !  !"
		print"\t\t\t\t. !     \'    VVV_HHH_/__'._H |  E  \_|=|_|========|_|==|____H. ! _________"
		print"\t\t\t\t I-H_I=I=HH_==_|I_IIIII_I_I_=HH|======.I-I-I-=======-I=I=I=I_=H|=H'===I=I/"
		print"\t\t\t\t\                                                                       /"
		print"\t\t\t\t \                                                                     /"
		print"\t\t\t\t .\___________________________________________________________________/."
		print ""
		menu = input("\t\t\t\t\t\t   Ingrese número de opción: ")
#******************Elección de modo un jugador*******************
		if menu == 1:
			os.system("clear")
			turno = 0
			fallido = 0 
			hundido = 0 

			for x in range(0,10):
				tablero.append(["0"] * 10)

			def print_tablero(tablero):
				for fila in tablero:
					print "\t\t\t\t\t\t     ",
					print " ".join(fila)
			print ""
			print ""
			print"\t\t\t████████╗ █████╗ ██████╗ ██╗     ███████╗██████╗  ██████╗     ██████╗  ██████╗"
			print"\t\t\t╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝██╔══██╗██╔═══██╗    ██╔══██╗██╔════╝"
			print"\t\t\t   ██║   ███████║██████╔╝██║     █████╗  ██████╔╝██║   ██║    ██████╔╝██║     "
			print"\t\t\t   ██║   ██╔══██║██╔══██╗██║     ██╔══╝  ██╔══██╗██║   ██║    ██╔═══╝ ██║     "
			print"\t\t\t   ██║   ██║  ██║██████╔╝███████╗███████╗██║  ██║╚██████╔╝    ██║     ╚██████╗"
			print"\t\t\t   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚═╝      ╚═════╝"
			print ""
			print_tablero(tablero)
			print ""
			print "\t\t\t\t\t\t   Hunde mis barcos, si puedes."
			print ""

			def fila_aleatoria(tablero):
				return random.randint(0,len(tablero)-1)

			def columna_aleatoria(tablero):
				return random.randint(0,len(tablero[0])-1)

#***********************************************Tablero de la PC***********************************
#*************************************************Primer barco*************************************
			barco_fila = fila_aleatoria(tablero)
			barco_col = columna_aleatoria(tablero)
			print ""
			print "\t\t\t\t\t\tUbicacion correcta barco 1:"
			print "\t\t\t\t\t\tLa flota del barco1 es : " + str(barco_fila),
			print ": " + str(barco_col)
			print ""

#*************************************Ubicación segundo barco, 2 flotas*****************************

			barco_fila2 = random.randint(0,8)
			barco_col2 = random.randint(0,8)
			complemento_col2 = barco_col2 + 1
			barco2_validacion = True
			while barco2_validacion == True:
				if tablero[barco_fila2][barco_col2] =="0" and tablero[barco_fila2][complemento_col2] == "0":
					tablero[barco_fila2][barco_col2] 
					tablero[barco_fila2][barco_col2 + 1] 
					break
				elif tablero[barco_fila2][barco_col2] =="X" or tablero[barco_fila2][complemento_col2] == "X":
					barco_fila2 = random.randint(0,8)
					barco_col2 = random.randint(0,8)
					barco2_validacion == True

#*****************************************Ubicación tercer barco, 3 flotas****************************

			barco_fila3 = random.randint(0,7)
			barco_col3 = random.randint(0,7)
			complemento2_col3 = barco_col3 + 1
			complemento3_col3 = barco_col3 + 2
			barco3_validacion = True
			while barco3_validacion == True:
				if tablero[barco_fila3][barco_col3] =="0" and tablero[barco_fila3][complemento2_col3] == "0" and tablero[barco_fila3][complemento3_col3] == "0":
					tablero[barco_fila3][barco_col3] 
					
					break
				elif tablero[barco_fila3][barco_col3] =="X" or tablero[barco_fila3][complemento2_col3] == "X" or tablero[barco_fila3][complemento3_col3] == "X":
					barco_fila3 = random.randint(0,7)
					barco_col3 = random.randint(0,7)
					barco3_validacion = True



#*******************************Tenemos un barco de un nivel de 2 flotas*********************************
#******************************************Coordenadas de la Pc******************************************

			print "\t\t\t\t\t\tUbicacion correcta barco 2:"
			print "\t\t\t\t\t\tLa primera flota del barco2 es: " + str(barco_fila2),
			print ": " + str(barco_col2)
			print "\t\t\t\t\t\tLa segunda flota del barco2 es: " + str(barco_fila2),
			print ": " + str(barco_col2 + 1)
			print "" 

#********************************Tenemos un barco de un nivel con 3 flotas*******************************
			print "\t\t\t\t\t\tUbicacion correcta barco 3:"
			print "\t\t\t\t\t\tLa primera flota del barco3 es: " + str(barco_fila3),
			print ": " + str(barco_col3)
			print "\t\t\t\t\t\tLa segunda flota del barco3 es: " + str(barco_fila3),
			print ": " + str(complemento2_col3)
			print "\t\t\t\t\t\tLa tercera flota del barco3 es: " + str(barco_fila3),
			print ": " + str(complemento3_col3)
			print ""

#********************************procedimiento de impacto a los barcos PC********************************
			adivinanza = True
			while adivinanza == True:
				for turno in range(9):
					try:
						adivina_fila = input("\t\t\t\t\t\t      Adivina fila:    ")
						adivina_columna = input("\t\t\t\t\t\t      Adivina columna: ")
						os.system ("clear")

						if adivina_fila == barco_fila and adivina_columna == barco_col:
							if(tablero[adivina_fila][adivina_columna] == "*"):
								print ""
								print "\t\t\t\t\t    Barco hundido tripulante, no rematemos."
								print ""
							else:
								print ""
								print "\t\t\t\t\t¡Felicitaciones! ¡Hundiste un barco de 1 flota.!"
								tablero[adivina_fila][adivina_columna] = "*"
								hundido = hundido + 1
								print "\t\t\t\t\t\tHundiste este barco con: " + str(turno + 1) + " intentos."
								validacion_menu = False
								adivinanza = False

						elif adivina_fila == barco_fila2 and adivina_columna == barco_col2 or adivina_fila == barco_fila2  and adivina_columna == barco_col2 + 1:
							if(tablero[adivina_fila][adivina_columna] == "*" ):
								print "\t\t\t\t\t    Barco hundido tripulante, no rematemos."
							else:
								print ""
								print "\t\t\t\t\t¡Felicitaciones! ¡Hundiste un barco de 2 flotas!"
								tablero[adivina_fila][adivina_columna] = "*"
								hundido = hundido + 1
								print
								print "\t\t\t\t\t\tHundiste este barco con: " + str(turno + 1) + " intentos."
								print "\t\t\t\t\t\t\tIntentos fallidos: " + str(fallido)
								validacion_menu = False
								adivinanza = False

						elif adivina_fila == barco_fila3 and adivina_columna == barco_col3 or adivina_fila == barco_fila3 and adivina_columna == complemento2_col3 or adivina_fila == barco_fila3 and adivina_columna == complemento3_col3:
							if(tablero[adivina_fila][adivina_columna] == "*" ):
								print "\t\t\t\t\t    Barco hundido tripulante, no rematemos."
								print ""
							else:
								print "\t\t\t\t\t¡Felicitaciones! ¡Hundiste un barco de 3 flotas!" 
								tablero[adivina_fila][adivina_columna] = "*"
								hundido = hundido + 1
								print "\t\t\t\t\t\tHundiste este barco con: " + str(turno + 1) + " intentos."
								print "" 
								validacion_menu = False
								adivinanza = False

						else:
								if (adivina_fila < 0 or adivina_fila > 9) or (adivina_columna < 0 or adivina_columna > 9):
										fallido  = fallido + 1
										print "\t\t\t\t\tDisparo fuera de rango, apunte bien tripulante."

								elif(tablero[adivina_fila][adivina_columna] == "X"):
										fallido  = fallido + 1
										validacion_turn = False
										if validacion_turn == False:
												print ""
												print "\t\t\t        * Amigo tripulante ya has impactado en este lugar anteriormente."
												print " "
												print " \t\t\t\t\t\t     * Trata de no fallar"
												print " "
								elif (tablero[adivina_fila][adivina_columna] == "*"):
										fallido = fallido + 1
										validacion_turn = False
										print "\t\t\t                       Este barco ya está destruido."
										print ""
								else:
										print ""
										print "\t\t\t\t\t\t¡No impactaste barco enemigo!"
										fallido  = fallido + 1
										tablero[adivina_fila][adivina_columna] = "X"

	#****************************************Validación de turnos******************************************* 
						validacion_turn = True
						if validacion_turn == True:
							if turno == 8:
								print "\t\t\t\t   Amigo tripulante ya ha gastado todas nuestras municiones."
								print u" \t\t\t\t  Tripulante lamentablemente usted ha perdido esta batalla."
								print "\t\t\t\t\t\t     Intentos fallidos: " + str(fallido)
								print ""
								adivinanza = False
								print_tablero(tablero)
								print ""
								print "\t\t\t\t\t\t Total de barcos hundidos: " + str(hundido)
								print "" 
								adivinanza = False
								reinicio_juego()
							elif hundido == 3:
								print ""
								print "\t\t\t\t   ¡Felicidades tripulante usted ha ganado esta batalla!"
								print "\t\t\t\t\t\t     Intentos fallidos: " + str(fallido)
								print ""
								adivinanza = False
								print_tablero(tablero)
								print ""
								print "\t\t\t\t\t\t Total de barcos hundidos: " + str(hundido)
								print "" 
								adivinanza = False
								reinicio_juego()
							else:
								print "\t\t\t\t\t\tEste fue tu intento número: " + str(turno + 1)
								print ""
								print_tablero(tablero)
								print ""
								print "\t\t\t\t\t\t      Barcos hundidos: " + str(hundido) + "/3"
								print "\t\t\t\t\t\t      Intentos fallidos: " + str(fallido)
								print ""
					except NameError:
						print "\t\t\t\t\t\tNo se puede leer esta coordenada."
#**********************************************Multiplayer*********************************************
#*******************************************Tablero Jugador1*******************************************
		elif menu == 2:
			os.system ("clear")
			hundido1 = 0
			hundido2 = 0
			fallido1 = 0
			fallido2 = 0
			turno1 = 0
			turno2 = 0
			

			for x2 in range(0,10):
				tablero2.append(["0"] * 10)

			def impresion_jugador1(tablero2):
				for recorrido_p1 in tablero2:
					print "\t\t\t\t\t\t     ",
					print " ".join(recorrido_p1)
			print ""
			print "\t\t\t\t\t\t      ¡Tablero Jugador1"
			print ""
			impresion_jugador1(tablero2)
			print ""

#*************************************************Primer barco**************************************
			p1barco_fila = random.randint(0,7)
			p1barco_col = random.randint(0,7)
			p1barco_fila = p1barco_col

#*************************************Ubicación segundo barco, 2 flotas*****************************

			p1barco_fila2 = random.randint(0,8)
			p1barco_col2 = random.randint(0,8)
			p1complemento_col2 = p1barco_col2 + 1
			p1barco2_validacion = True
			while p1barco2_validacion == True:
				if tablero2[p1barco_fila2][p1barco_col2] =="0" and tablero2[p1barco_fila2][p1complemento_col2] == "0":
					tablero2[p1barco_fila2][p1barco_col2] 
					tablero2[p1barco_fila2][p1barco_col2 + 1] 
					break
				elif tablero2[p1barco_fila2][p1barco_col2] =="X" or tablero2[p1barco_fila2][p1complemento_col2] == "X":
					p1barco_fila2 = random.randint(0,8)
					p1barco_col2 = random.randint(0,8)
					p1barco2_validacion == True

#*****************************************Ubicación tercer barco, 3 flotas****************************

			p1barco_fila3 = random.randint(0,7)
			p1barco_col3 = random.randint(0,7)
			p1complemento2_col3 = p1barco_col3 + 1
			p1complemento3_col3 = p1barco_col3 + 2
			p1barco3_validacion = True
			while p1barco3_validacion == True:
				if tablero2[p1barco_fila3][p1barco_col3] =="0" and tablero2[p1barco_fila3][p1complemento2_col3] == "0" and tablero2[p1barco_fila3][p1complemento3_col3] == "0":
					tablero2[p1barco_fila3][p1barco_col3] 
					tablero2[p1barco_fila3][p1barco_col3 + 1]
					tablero2[p1barco_fila3][p1barco_col3 + 2]
					
					break
				elif tablero2[p1barco_fila3][p1barco_col3] =="X" or tablero2[p1barco_fila3][p1complemento2_col3] == "X" or tablero2[p1barco_fila3][p1complemento3_col3] == "X":
					p1barco_fila3 = random.randint(0,7)
					p1barco_col3 = random.randint(0,7)
					p1barco3_validacion = True
#***************************************Coordenadas del jugador 1********************************************
#************************************************1 Flota****************************************************L
			print "\t\t\t\t\t\tUbicacion correcta barco1:"
			print "\t\t\t\t\t\tLa flota del barco1 es: " + str(p1barco_fila),
			print ": " + str(p1barco_col)
			print "" 
#*******************************Tenemos un barco de un nivel de 2 flotas*************************************

			print "\t\t\t\t\t\tUbicacion correcta barco 2:"
			print "\t\t\t\t\t\tLa primera flota del barco2 es: " + str(p1barco_fila2),
			print ": " + str(p1barco_col2)
			print "\t\t\t\t\t\tLa segunda flota del barco2 es: " + str(p1barco_fila2),
			print ": " + str(p1complemento_col2)
			print "" 

#********************************Tenemos un barco de un nivel con 3 flotas***********************************

			print "\t\t\t\t\t\tUbicacion correcta barco 3:"
			print "\t\t\t\t\t\tLa primera flota del barco3 es: " + str(p1barco_fila3),
			print ": " + str(p1barco_col3)
			print "\t\t\t\t\t\tLa segunda flota del barco3 es: " + str(p1barco_fila3),
			print ": " + str(p1complemento2_col3)
			print "\t\t\t\t\t\tLa tercera flota del barco3 es: " + str(p1barco_fila3),
			print ": " + str(p1complemento3_col3)
			print ""
			validacion_menu = False
#************************************************Tablero Jugador2********************************************
			for x3 in range(0,10):
				tablero3.append(["0"] * 10)

			def impresion_jugador2(tablero3):
				for recorrido_p2 in tablero3:
					print "\t\t\t\t\t\t     ",
					print " ".join(recorrido_p2)
			print "\t\t\t\t\t\t      ¡Tablero Jugador2"
			impresion_jugador2(tablero3)
			print ""

#********************************************Ubicacion barco, 1 flota****************************************
			p2barco_fila = random.randint(0,7)
			p2barco_col = random.randint(0,7)
			p2barco_fila = p2barco_col

#*************************************Ubicación segundo barco, 2 flotas*************************************I

			p2barco_fila2 = random.randint(0,8)
			p2barco_col2 = random.randint(0,8)
			p2complemento_col2 = p1barco_col2 + 1
			p2barco2_validacion = True
			while p1barco2_validacion == True:
				if tablero3[p2barco_fila2][p2barco_col2] =="0" and tablero3[p2barco_fila2][p2complemento_col2] == "0":
					tablero3[p2barco_fila2][p2barco_col2] 
					tablero3[p2barco_fila2][p2barco_col2 + 1] 
					break
				elif tablero3[p1barco_fila2][p2barco_col2] =="X" or tablero3[p2barco_fila2][p2complemento_col2] == "X":
					p2barco_fila2 = random.randint(0,8)
					p2barco_col2 = random.randint(0,8)
					p2barco2_validacion == True

#*****************************************Ubicación tercer barco, 3 flotas****************************

			p2barco_fila3 = random.randint(0,7)
			p2barco_col3 = random.randint(0,7)
			p2complemento2_col3 = p2barco_col3 + 1
			p2complemento3_col3 = p2barco_col3 + 2
			p2barco3_validacion = True
			while p2barco3_validacion == True:
				if tablero3[p2barco_fila3][p2barco_col3] =="0" and tablero3[p2barco_fila3][p2complemento2_col3] == "0" and tablero3[p2barco_fila3][p2complemento3_col3] == "0":
					tablero3[p2barco_fila3][p2barco_col3] 
					tablero3[p2barco_fila3][p2barco_col3 + 1]
					tablero3[p2barco_fila3][p2barco_col3 + 2]
					
					break
				elif tablero3[p2barco_fila3][p2barco_col3] =="X" or tablero3[p2barco_fila3][p2complemento2_col3] == "X" or tablero3[p2barco_fila3][p2complemento3_col3] == "X":
					p2barco_fila3 = random.randint(0,7)
					p2barco_col3 = random.randint(0,7)
					p2barco3_validacion = True

					#***************************************Coordenadas del jugador 2********************************************
#************************************************1 Flota****************************************************L
			print "\t\t\t\t\t\tUbicacion correcta barco 1:"
			print "\t\t\t\t\t\tLa flota del barco1 es: " + str(p2barco_fila),
			print ": " + str(p2barco_col)
			print "" 
#*******************************Tenemos un barco de un nivel de 2 flotas*************************************

			print "\t\t\t\t\t\tUbicacion correcta barco 2:"
			print "\t\t\t\t\t\tLa primera flota del barco2 es: " + str(p2barco_fila2),
			print ": " + str(p2barco_col2)
			print "\t\t\t\t\t\tLa segunda flota del barco2 es: " + str(p1barco_fila2),
			print ": " + str(p1complemento_col2)
			print "" 

#********************************Tenemos un barco de un nivel con 3 flotas***********************************

			print "\t\t\t\t\t\tUbicacion correcta barco 3:"
			print "\t\t\t\t\t\tLa primera flota del barco3 es: " + str(p2barco_fila3),
			print ": " + str(p2barco_col3)
			print "\t\t\t\t\t\tLa segunda flota del barco3 es: " + str(p2barco_fila3),
			print ": " + str(p2complemento2_col3)
			print "\t\t\t\t\t\tLa tercera flota del barco3 es: " + str(p2barco_fila3),
			print ": " + str(p2complemento3_col3)
			print ""

			for a in range(3):
				os.system("clear")
				print ""
				print "\t████████╗██╗   ██╗██████╗ ███╗   ██╗ ██████╗          ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗ ██████╗         ██╗"
				print "\t╚══██╔══╝██║   ██║██╔══██╗████╗  ██║██╔═══██╗         ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╗    ███║"
				print "\t   ██║   ██║   ██║██████╔╝██╔██╗ ██║██║   ██║         ██║██║   ██║██║  ███╗███████║██║  ██║██║   ██║██████╔╝╚═╝    ╚██║"
				print "\t   ██║   ██║   ██║██╔══██╗██║╚██╗██║██║   ██║    ██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██║   ██║██╔══██╗██╗     ██║"
				print "\t   ██║   ╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝    ╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝██║  ██║╚═╝     ██║"
				print "\t   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝        ╚═╝"
				print""

				for turno2 in range(1):
					try:
						print "\t\t\t\t\t\t     Tablero de Jugador: 1"
						impresion_jugador1(tablero2)
						print ""
						adivina_filap2 = input("\t\t\t\t\t\t      Adivina fila:    ")
						adivina_columnap2 = input("\t\t\t\t\t\t      Adivina columna: ")

						if adivina_filap2 == p2barco_fila and adivina_columnap2 == p2barco_col:
							if(tablero3[adivina_filap2][adivina_columnap2] == "*"):
								print ""
								print "\t\t\t\t\t    Barco hundido tripulante, no rematemos."
								print ""
							else:
								print ""
								print "\t\t\t\t   ¡Felicitaciones! ¡Hundiste un barco de 1 flota de tu oponente!"
								tablero3[adivina_filap2][adivina_columnap2] = "*"
								hundido2 = hundido2 + 1
								print "\t\t\t\t\t    Hundiste este barco con: " + str(a + 1) + " intentos."
								print ""
								impresion_jugador2(tablero3)
								validacion_menu = False
								adivinanza_p2 = False
								

						elif adivina_filap2 == p2barco_fila2 and adivina_columnap2 == p2barco_col2 or adivina_filap2 == p2barco_fila2  and adivina_columnap2 == p2barco_col2 + 1:
							if(tablero3[adivina_filap2][adivina_columnap2] == "*"):
								print ""
								print "\t\t\t\t\t    Barco hundido tripulante, no rematemos."
								print ""
							else:
								print ""
								print "\t\t\t\t    ¡Felicitaciones! ¡Hundiste un barco de 2 flotas de tu oponente!"
								tablero3[p2barco_fila2][p2barco_col2] = "*"
								tablero3[p2barco_fila2][p2barco_col2 + 1]  = "*" 
								hundido2 = hundido2 + 1
								print
								print "\t\t\t\t\t\tHundiste este barco con: " + str(a + 1) + " intentos."
								print "\t\t\t\t\t\tIntentos fallidos: " + str(fallido2)
								print ""
								impresion_jugador2(tablero3)
								validacion_menu = False
								adivinanza_p2 = False
								

						elif adivina_filap2 == p2barco_fila3 and adivina_columnap2 == p2barco_col3 or adivina_filap2 == p2barco_fila3 and adivina_columnap2 == p2complemento2_col3 or adivina_filap2 == p2barco_fila3 and adivina_columnap2 == p2complemento3_col3:
							if(tablero3[adivina_filap2][adivina_columnap2] == "*"):
								print ""
								print "\t\t\t\t\t    Barco hundido tripulante, no rematemos."
								print ""
							else:
								print ""
								print "\t\t\t\t\t¡Felicitaciones! ¡Hundiste un barco de 3 flotas!" 
								tablero3[p2barco_fila3][p2barco_col3] = "*" 
								tablero3[p2barco_fila3][p2barco_col3 + 1] = "*"
								tablero3[p2barco_fila3][p2barco_col3 + 2] = "*"
								hundido2 = hundido2 + 1
								print "\t\t\t\t\t    Hundiste este barco con: " + str(a + 1) + " intentos."
								print ""
								impresion_jugador2(tablero3)
								validacion_menu = False
								adivinanza_p2 = False
								
						else:
								if (adivina_filap2 < 0 or adivina_filap2 > 9) or (adivina_columnap2 < 0 or adivina_columnap2 > 9):
										fallido2  = fallido2 + 1
										print "\t\t\t\t\t\tDisparo fuera de rango, apunte bien tripulante."
										impresion_jugador2(tablero3)

								elif(tablero3[adivina_filap2][adivina_columnap2] == "X") or (tablero3[adivina_filap2][adivina_columnap2] == "*"):
										fallido2 = fallido2 + 1
										validacion_turnp2 = False
										if validacion_turnp2 == False:
												print ""
												print "\t\t\t       * Amigo tripulante ya has impactado en este lugar anteriormente."
												print " "
												print " \t\t\t\t\t\t     * Trata de no fallar"
												print " "
												impresion_jugador2(tablero3)
								else:
										print ""
										print "\t\t\t\t\t    ¡No impactaste a ningun barco enemigo!"
										print ""
										fallido2  = fallido2 + 1
										tablero3[adivina_filap2][adivina_columnap2] = "X"
										impresion_jugador2(tablero3),
										print "\t\t\t\t\t             Tablero de Jugador: 2"
						print ""
						print "\t\t\t\t\t\t     Enter para continuar"
						pausa=raw_input("")
					except NameError:
						print "No es posible leer esa coordenada"

				

		#*********************************************************************************************************************************************************
					os.system("clear")
					print ""
					print"\t████████╗██╗   ██╗██████╗ ███╗   ██╗ ██████╗          ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗ ██████╗        ██████╗ "
					print"\t╚══██╔══╝██║   ██║██╔══██╗████╗  ██║██╔═══██╗         ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╗    ╚════██╗"
					print"\t   ██║   ██║   ██║██████╔╝██╔██╗ ██║██║   ██║         ██║██║   ██║██║  ███╗███████║██║  ██║██║   ██║██████╔╝╚═╝     █████╔╝"
					print"\t   ██║   ██║   ██║██╔══██╗██║╚██╗██║██║   ██║    ██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██║   ██║██╔══██╗██╗    ██╔═══╝ "
					print"\t   ██║   ╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝    ╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝██║  ██║╚═╝    ███████╗"
					print"\t   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝       ╚══════╝"
					print ""
					for turno1 in range(1):
						print "\t\t\t\t\t\t     Tablero de Jugador: 2"
						impresion_jugador2(tablero3)
						print ""
						adivina_filap1 = input("\t\t\t\t\t\t      Adivina fila:    ")
						adivina_columnap1 = input("\t\t\t\t\t\t      Adivina columna: ")
						if adivina_filap1 == p1barco_fila and adivina_columnap1 == p1barco_col:
							if(tablero2[adivina_filap1][adivina_columnap1] == "*"):
								print ""
								print "\t\t\t\t\t    Barco hundido tripulante, no rematemos."
								print ""
							else:
								print ""
								print "\t\t\t\t\t¡Felicitaciones! ¡Hundiste un barco de 1 flota.!"
								tablero2[adivina_filap1][adivina_columnap1] = "*"
								hundido1 = hundido1 + 1
								print "\t\t\t\t\t    Hundiste este barco con: " + str(a + 1) + " intentos."
								print ""
								impresion_jugador1(tablero2)
								validacion_menu = False
								adivinanza_p1 = False

						elif adivina_filap1 == p1barco_fila2 and adivina_columnap1 == p1barco_col2 or adivina_filap1 == p1barco_fila2  and adivina_columnap1 == p1barco_col2 + 1:
							if(tablero2[adivina_filap1][adivina_columnap1] == "*"):
								print ""
								print "\t\t\t\t\t    Barco hundido tripulante, no rematemos."
								print ""
							else:
								print ""
								print "\t\t\t\t    ¡Felicitaciones! ¡Hundiste un barco de 2 flotas de tu oponente!"
								tablero2[p1barco_fila2][p1barco_col2] = "*" 
								tablero2[p1barco_fila2][p1barco_col2 + 1] = "*"
								hundido1 = hundido1 + 1
								print
								print "\t\t\t\t\t\tHundiste este barco con: " + str(a + 1) + " intentos."
								print "\t\t\t\t\t\t     Intentos fallidos: " + str(fallido1)
								print ""
								impresion_jugador1(tablero2)
								validacion_menu = False
								adivinanza_p1 = False

						elif adivina_filap1 == p1barco_fila3 and adivina_columnap1 == p1barco_col3 or adivina_filap1 == p1barco_fila3 and adivina_columnap1 == p1complemento2_col3 or adivina_filap1 == p1barco_fila3 and adivina_columnap1 == p1complemento3_col3:
							if(tablero2[adivina_filap1][adivina_columnap1] == "*"):
								print ""
								print "\t\t\t\t\t    Barco hundido tripulante, no rematemos."
								print ""
							else:
								print ""
								print "\t\t\t\t\t¡Felicitaciones! ¡Hundiste un barco de 3 flotas!" 
								tablero2[p1barco_fila3][p1barco_col3] = "*"
								tablero2[p1barco_fila3][p1barco_col3 + 1] = "*"
								tablero2[p1barco_fila3][p1barco_col3 + 2] = "*"
								hundido1 = hundido1 + 1
								print "\t\t\t\t\t    Hundiste este barco con: " + str(a + 1) + " intentos."
								print ""
								impresion_jugador1(tablero2)
								validacion_menu = False
								adivinanza_p1 = False
						else:
								if (adivina_filap1 < 0 or adivina_filap1 > 9) or (adivina_columnap1 < 0 or adivina_columnap1 > 9):
										fallido1  = fallido1 + 1
										print "\t\t\t\t\tDisparo fuera de rango, apunte bien tripulante."
										print ""
										impresion_jugador1(tablero2)

								elif(tablero2[adivina_filap1][adivina_columnap1] == "X") or (tablero2[adivina_filap1][adivina_columnap1] == "*"):
										fallido1 = fallido1 + 1
										validacion_turnp1 = False
										if validacion_turnp1 == False:
												print ""
												print "\t\t\t       * Amigo tripulante ya has impactado en este lugar anteriormente."
												print " "
												print " \t\t\t\t\t\t     * Trata de no fallar"
												print " "
												impresion_jugador1(tablero2)
								else:
										print ""
										print "\t\t\t\t\t   ¡No impactaste a ningun barco enemigo!"
										print ""
										fallido1  = fallido1 + 1
										tablero2[adivina_filap1][adivina_columnap1] = "X"
										impresion_jugador1(tablero2),
										print "\t\t\t\t\t\t      Tablero Jugador: 1"
				print ""
				print "\t\t\t\t\t\t      Enter para continuar"
				pausa = raw_input("")

							 

				if a == 2:
					if hundido1 == 3 or hundido2 == 3 or hundido1 < 3 or hundido2 < 3:
						os.system ("clear")
						print ""
						print"\t\t\t\t\t███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗  " 
						print"\t\t\t\t\t██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝██╗"
						print"\t\t\t\t\t███████╗   ██║   ███████║   ██║   ██║   ██║███████╗╚═╝"
						print"\t\t\t\t\t╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║██╗"
						print"\t\t\t\t\t███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║╚═╝"
						print"\t\t\t\t\t╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝ "
						print ""
						print "\t\t\t\t\t       Impactos Jugador: 1 a Jugador 2 "
						print ""
						impresion_jugador2(tablero3)
						print ""
						print "\t\t\t\t\t\t      Barcos hundidos: " + str(hundido2) + "/3"
						print "\t\t\t\t\t\t      Intentos fallidos: " + str(fallido2)
						print ""
						print "\t\t\t\t\t       Impactos Jugador: 2 a Jugador: 1 "
						print ""
						impresion_jugador1(tablero2)
						print ""
						print "\t\t\t\t\t\t      Barcos hundidos: " + str(hundido1) + "/3"
						print "\t\t\t\t\t\t      Intentos fallidos: " + str(fallido1)
						print ""
						print "\t\t\t\t\t\t     Enter para continuar"
						validacion_menu = True
						if hundido2 > hundido1:
							print "\t\t\t\t\t\t   El ganador es el Jugador: 1"
						elif hundido1 > hundido2:
							print "\t\t\t\t\t\t   El ganador es el Jugador: 2"
						else:
							print "\t\t\t\t\t\t     ¡Empate Tripulante!"
						pausa = raw_input("")
						time.sleep(2)
						reinicio_juego()

#*********************************************Instrucciones**************************************************
		elif menu == 3:
			print ""
			print "\t\t\t\t                 ☣ MORTAL BATTLE SHIP INSTRUCTIONS☣ "
			print ""
			print "\t\t\t\t                           *MODO 1 JUGADOR*"
			print ""
			print "\t\t\t\t- Amigo tripulante usted posee 9 intentos recuerde aprovecharlos todos."
			print "\t\t\t\t- Jugará en un tablero de 10*10 con barcos de barias flotas; 1, 2 y 3."
			print "\t\t\t\t- Usted ganará sólo si hunde todos los barcos, tripulante sea cuidadoso."
			print "\t\t\t\t- Usted perderá si desperdicia municiones y no impacta a todos los barcos."
			print "\t\t\t\t- El tablero posee indices de filas y columnas que empienzan en: "+ str(0)
			print "\t\t\t\t- Importante: Amigo tripulante, recuerda no desperdiciar tus municiones."
			print ""
			time.sleep(1)
			print "\t\t\t\t                     ¡ADELANTE! ¡VE POR ELLOS!"
			print "" 
			time.sleep(1)
			regreso_menu = True
			while regreso_menu == True:
				reinicio = raw_input("\t\t\t\t\t\t  ¿Desea volver al menú? si/no: ")
				if reinicio.lower() == "si":
					os.system("clear")
					regreso_menu = False
					validacion_menu = True
				elif reinicio.lower() == "no":
					os.system("clear")
					adivinanza = False
					regreso_menu = False
					validacion_menu = False
					break
				else:
					print "\t\t\t\t\t\t        Opción inválida."
					validacion_menu = True
		elif menu == 4:
			print ""
			print "\t\t\t\t\t\t     Hasta luego tripulante"
			time.sleep(1)
			sys.exit()

	except NameError:
		os.system("clear")
		print "\t\t\t   Por favor asegurese de ingresar correctamente el número de opción indicado."
		validacion_menu = True
	except SyntaxError:
		os.system("clear")
		print "\t\t\t   Por favor asegurese de ingresar correctamente el número de opción indicado."
		validacion_menu = True
