import pygame,sys
from pygame.locals import *
from random import randint


pygame.init()
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))
pygame.display.set_caption("prubas")
reloj = pygame.time.Clock()

def repintar_cuadro_juego():
	ventana.blit(imagen_fondo,(0,0))
	pygame.draw.rect(ventana,(255,0,0), (x1,y1,ancho1,alto1))
	pygame.draw.rect(ventana,(130,12,85), (x2,y2,ancho2,alto2))


	pygame.display.update()



#colorbg = pygame.Color(5,22,150)
#colorob = (38,148,5)
#mi_imagen = pygame.image.load("Imagenes/personaje.png")
#posX = (1)
#posY = (10)
#variables para el movimiento
#velocidad=30
repetir=True

while repetir:

	imagen_fondo = pygame.image.load('img/Ecenario/bg.jpg')
	ruta_musica = "music/musicaf.mp3"
	musica_fondo = pygame.mixer.music.load(ruta_musica)
	pygame.mixer.music.play(-1)



esta_jugando=True 
while esta_jugando:
	reloj.tick(24)
	

	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()

			#variables de figuras
			x1=50
			y1=50
			alto1=60
			ancho1=40
			x2=500
			y2=300
			alto2=80
			ancho2=100
		#movimiento para el jugador
		#elif evento.type == pygame.KEYDOWN:
		#	if evento.key ==K_LEFT:
		#		posX -= velocidad
		#	elif evento.key == K_RIGHT:
		#		posX += velocidad
		#	elif evento.key == K_UP:
		#		posY -= velocidad
		#	elif evento.key == K_DOWN:
		#		posY += velocidad

			repintar_cuadro_juego()

			

	pygame.display.update()