import pygame
from pygame.locals import *

pygame.init()
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))
pygame.display.set_caption("Coronaviros THE GAME")
reloj = pygame.time.Clock()

#Clase 1)personajes

class personaje(object):

	def __init__(self, x, y, fuente):
		self.x = x
		self.y = y
		
		self.velocidad = 9
		#animacion de sprite
		self.va_izquierda = False
		self.va_derecha = False
		self.va_back = False
		self.va_frente = False
		self.contador_pasos = 0
		fuente += "/"
		self.camina_izquierda = [pygame.image.load("img/"+fuente+"/l1.png"), pygame.image.load("img/"+fuente+"/l2.png"), pygame.image.load("img/"+fuente+"/l3.png"), pygame.image.load("img/"+fuente+"/l4.png")]
		self.camina_derecha = [pygame.image.load("img/"+fuente+"/r1.png"), pygame.image.load("img/"+fuente+"/r2.png"), pygame.image.load("img/"+fuente+"/r3.png"), pygame.image.load("img/"+fuente+"/r4.png")]
		self.camina_frente = [pygame.image.load("img/"+fuente+"/f1.png"), pygame.image.load("img/"+fuente+"/f2.png"), pygame.image.load("img/"+fuente+"/f3.png"), pygame.image.load("img/"+fuente+"/f4.png")]
		self.camina_back = [pygame.image.load("img/"+fuente+"/b1.png"), pygame.image.load("img/"+fuente+"/b2.png"), pygame.image.load("img/"+fuente+"/b3.png"), pygame.image.load("img/"+fuente+"/b4.png")]
		self.quieto = pygame.image.load("img/"+fuente+"/f1.png")
		self.ancho = self.quieto.get_width()
		self.alto = self.quieto.get_height()

	def dibujar(self, cuadro):

		if self.contador_pasos + 1> 27:
			self.contador_pasos = 0

		if self.va_izquierda:
			cuadro.blit(self.camina_izquierda[self.contador_pasos//7],(self.x,self.y))
			self.contador_pasos += 1

		elif self.va_derecha:
			cuadro.blit(self.camina_derecha[self.contador_pasos//7],(self.x,self.y))
			self.contador_pasos += 1

		elif self.va_back:
			cuadro.blit(self.camina_back[self.contador_pasos//7],(self.x,self.y))
			self.contador_pasos += 1

		elif self.va_frente:
			cuadro.blit(self.camina_frente[self.contador_pasos//7],(self.x,self.y))
			self.contador_pasos += 1

		else:

			cuadro.blit(self.quieto,(self.x,self.y))


	def se_mueve_segun(self, k, iz, de, ar, ab):
		if k[iz] and self.x > self.velocidad:
			self.x -= self.velocidad
			#animacion
			self.va_izquierda = True
			self.va_derecha = False
			self.va_back = False
			self.va_frente = False

		elif k[de] and self.x < ventana_x - self.ancho - self.velocidad:
			self.x += self.velocidad
			#animacion
			self.va_derecha = True
			self.va_izquierda = False
			self.va_back = False
			self.va_frente = False


		elif k[ar] and self.y > self.velocidad:
			self.y -= self.velocidad
			self.va_izquierda = False
			self.va_derecha = False
			self.va_frente = False
			self.va_back = True

		elif k[ab] and self.y < ventana_y - self.alto - self.velocidad:
			self.y += self.velocidad
			self.va_izquierda = False
			self.va_derecha = False
			self.va_frente = True
			self.va_back = False
		else:
			self.va_derecha = False
			self.va_izquierda = False
			self.va_frente = False
			self.va_back = False
			self.contador_pasos = 0

#Función para repintar el cuadro de juego
def repintar_cuadro_juego():
	#Dibujar fondo del nivel
	#ventana.fill((0,0,0))
	ventana.blit(imagen_fondo,(0,0))
	#Dibujar Personaje
	prota.dibujar(ventana)
	#Se refresca la imagen
	pygame.display.update()

# Inicio Funcion principal

repetir = True 
while repetir:

	# Inicializacion de elementos del juego
	imagen_fondo = pygame.image.load('img/Ecenario/habitacion1.png')
	ruta_musica = "music/musicaf.mp3"
	musica_fondo = pygame.mixer.music.load(ruta_musica)
	pygame.mixer.music.play(-1)

	#Creación del prota
	prota=personaje(int(ventana_x/2), int(ventana_y/2),"personajes")
	
	
	# Seccion de juego
	esta_jugando=True
	while esta_jugando:
		reloj.tick(27)
		# evento de boton de cierre de ventana
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit()
		
		teclas=pygame.key.get_pressed()
		prota.se_mueve_segun(teclas,pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
		repintar_cuadro_juego()
# Termina el juego
pygame.quit()