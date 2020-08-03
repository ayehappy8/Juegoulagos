import pygame
from pygame.locals import *

pygame.init()
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))
pygame.display.set_caption("The game")
reloj = pygame.time.Clock()

#Función para repintar el cuadro de juego
def repintar_cuadro_juego():
	#ventana.fill((0,0,0))
	ventana.blit(imagen_fondo,(0,0))
	#Se refresca la imagen
	ventana.blit(imagen_personaje,(x,y))
	pygame.display.update()

# Inicio Funcion principal

repetir = True
while repetir:

	# Inicializacion
	imagen_fondo = pygame.image.load('img/Ecenario/habitacion1.png')
	ruta_musica = "music/musicaf.mp3"
	musica_fondo = pygame.mixer.music.load(ruta_musica)
	pygame.mixer.music.play(-1)

	#Variables para figuras (usar así para luego retomar en "Clases y objetos")
	#Hablar de la orientación de las coordenadas
	#(Jugar con las ubicaciones, tamaños y colores)
	x1=50
	y1=50
	alto1=60
	ancho1=40
	x2=500
	y2=300
	alto2=80
	ancho2=100
	#The personaje
	x = int(ventana_x/2)
	y = int(ventana_y/2)
	velocidad = 10
	alto = 1
	ancho = 1
	imagen_personaje = pygame.image.load('img/personajes/Prota.png')
	alto=imagen_personaje.get_height()
	ancho=imagen_personaje.get_width()


	# Seccion de juego
	esta_jugando=True
	while esta_jugando:
		# control de velocidad del juego
		reloj.tick(27)
		# evento de boton de cierre de ventana
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit()

		teclas=pygame.key.get_pressed()
	
		if teclas[pygame.K_LEFT] and x > velocidad:
			x-=velocidad
		if teclas[pygame.K_RIGHT] and x < ventana_x - ancho - velocidad:
			x+=velocidad
		if teclas[pygame.K_UP] and y > velocidad:
			y-=velocidad
		if teclas[pygame.K_DOWN] and y < ventana_y - alto - velocidad:
			y+=velocidad
		repintar_cuadro_juego()

pygame.quit()