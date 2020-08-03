import pygame
from pygame.locals import *

pygame.init()
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))
pygame.display.set_caption("The game")
reloj = pygame.time.Clock()
#clase de personaje
	class personaje(object):
		def __init__(self, x, y, fuente:
			self.x = x
			self.y = y
			fuente+='/'
			self.quieto = pygame.image.load("img/+fuente+f1.png")
			self.ancho = self.quieto.get_width()
			self.alto = self.quieto.get_height()
			self.velocidad = 5

		def dibujar(self,cuadro):
			cuadro.blit(self.quieto, (self.x,self.y))

		def se_mueve_segun(self,k,iz,de,ar,ab):
			if k[iz] and self.x > self.velocidad:
				self.x-=self.velocidad
			if k[de] and self.x < ventana_x - self.ancho - self.velocidad:
				self.x+=self.velocidad
			if k[ar] and self.y > self.velocidad:
				self.y-=self.velocidad
			if k[ab] and self.y < ventana_y - self.alto - self.velocidad:
				self.y+=self.velocidad

#Función para repintar el cuadro de juego
def repintar_cuadro_juego():
	#ventana.fill((0,0,0))
	ventana.blit(imagen_fondo,(0,0))
	prota,dubujar(ventana)
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
	#The prota
	f1 = personaje(int(ventana_x/2),int(ventana_y/2),"f1")
		
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
	f1.se_mueve_segun(teclas,pygame.K_LEFT, pygame.k_RIGHT, pygame.K_UP, pygame.K_DOWN)



		repintar_cuadro_juego()

pygame.quit()