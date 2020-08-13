import pygame
from pygame.locals import *

pygame.init()
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))
pygame.display.set_caption("MI PRIMER JUEGO")
reloj = pygame.time.Clock()

#Clase Personaje
class personaje(object):

	def __init__(self, x, y, fuente, limite):
		self.x = x
		self.y = y
		self.velocidad = 12
		#Atributos para animación de Sprites
		self.va_izquierda = False
		self.va_derecha = False
		self.contador_pasos = 0
		fuente += "/"
		self.camina_izquierda = [pygame.image.load("img/"+fuente+"l1.png"),pygame.image.load("img/"+fuente+"l2.png"),pygame.image.load("img/"+fuente+"l3.png"),pygame.image.load("img/"+fuente+"l4.png")]
		self.camina_derecha = [pygame.image.load("img/"+fuente+"r1.png"),pygame.image.load("img/"+fuente+"r2.png"),pygame.image.load("img/"+fuente+"r3.png"),pygame.image.load("img/"+fuente+"r4.png")]
		self.quieto = pygame.image.load("img/"+fuente+"standing.png")
		self.ancho = self.quieto.get_width()
		self.alto = self.quieto.get_height()
		#Desplazamiento automático
		self.camino = [self.x, limite]
		#Nivel de Salud
		self.salud = 10
		#zona de impacto
		self.zona_impacto = (self.x + 15, self.y + 10, 30, 50)


	def dibujar(self, cuadro):
		#Son 9 imágenes de la animación, para que cada una dure 3 vueltas de ciclo se multiplica por 3
		if self.contador_pasos + 1 > 27:
			self.contador_pasos = 0

		if self.va_izquierda:
			cuadro.blit(self.camina_izquierda[self.contador_pasos//7],(self.x,self.y))
			self.contador_pasos += 1
		elif self.va_derecha:
			cuadro.blit(self.camina_derecha[self.contador_pasos//7],(self.x,self.y))
			self.contador_pasos += 1
		else:
			if self.va_derecha:
				cuadro.blit(self.camina_derecha[0],(self.x,self.y))
			elif self.va_izquierda:
				cuadro.blit(self.camina_izquierda[0],(self.x,self.y))
			else:
				cuadro.blit(self.quieto, (self.x,self.y))
		#Crear clase barra de vida
		pygame.draw.rect(cuadro, (255,0,0), (self.x+8, self.y - 40, 70, 10))
		pygame.draw.rect(cuadro, (0,128,0), (self.x+8, self.y - 40, 70 - (5 * (10 - self.salud)), 10))
		#hitbox
		self.zona_impacto = (self.x + 15, self.y + 10, 60, 80)
		pygame.draw.rect(cuadro, (255,0,0), self.zona_impacto,2)

	def se_mueve_segun(self, k, iz, de, ar, ab):
		if k[iz] and self.x > self.velocidad:
			self.x -= self.velocidad
			#Controles de animación
			self.va_izquierda = True
			self.va_derecha = False

		elif k[de] and self.x < ventana_x - self.ancho - self.velocidad:
			self.x += self.velocidad
			#Controles de animación
			self.va_derecha = True
			self.va_izquierda = False

		else:
			#Controles de animación en caso de dejar de moverse en horizonal
			self.va_izquierda = False
			self.va_derecha = False
			self.contador_pasos = 0

		if k[ar] and self.y > self.velocidad:
				self.y -= self.velocidad
		if k[ab] and self.y < ventana_y - self.alto - self.velocidad:
				self.y += self.velocidad
		

	def se_mueve_solo(self):
		if self.velocidad > 0:
			if self.x + self.velocidad < self.camino[1]:
				self.x += self.velocidad-5 
				self.va_derecha = True
				self.va_izquierda = False
			else:
				self.velocidad = self.velocidad * -1
				self.contador_pasos = 0
		else:
			if self.x - self.velocidad > self.camino[0]:
				self.x += self.velocidad-5
				self.va_izquierda = True
				self.va_derecha = False
			else:
				self.velocidad = self.velocidad * -1
				self.contador_pasos = 0

	#Las colisiones
	def se_encuentra_con(self, alguien):
		R1_ab = self.zona_impacto[1] + self.zona_impacto[3]
		R1_ar = self.zona_impacto[1]
		R1_iz = self.zona_impacto[0]
		R1_de = self.zona_impacto[0] + self.zona_impacto[2]
		R2_ab = alguien.zona_impacto[1] + alguien.zona_impacto[3]
		R2_ar = alguien.zona_impacto[1]
		R2_iz = alguien.zona_impacto[0]
		R2_de = alguien.zona_impacto[0] + alguien.zona_impacto[2]

		return R1_de > R2_iz and R1_iz < R2_de and R1_ar < R2_ab and R1_ab > R2_ar
		
	#recibir daño
	def es_golpeado(self):
		self.x = 100
		self.y = 410
		self.contador_pasos = 0
		self.salud -= 5
		pygame.time.delay(200)

#Función para repintar el cuadro de juego
def repintar_cuadro_juego():
	#Dibujar fondo del nivel
	#ventana.fill((0,0,0))
	ventana.blit(imagen_fondo,(0,0))
	#Dibujar Héroe
	heroe.dibujar(ventana)
	#Dibujar Villano
	villano.dibujar(ventana)
	#Se refresca la imagen
	pygame.display.update()

# Inicio Funcion principal

repetir = True #Variable que controla la repeticion del juego completo con todas sus pantallas
#Ciclo de repeticion de todo el juego
while repetir:

	# Inicializacion de elementos del juego
	imagen_fondo = pygame.image.load('img/Ecenario/habitacion1.png')
	ruta_musica = "music/musicaf.mp3"
	musica_fondo = pygame.mixer.music.load(ruta_musica)
	pygame.mixer.music.play(-1)

	#Creación Personaje Héroe
	heroe=personaje(int(ventana_x/2), int(ventana_y/2),"heroe", ventana_x)#Agregar límite
	villano=personaje(0, int(ventana_y/2),"villano",int(ventana_x/2))
	
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
		heroe.se_mueve_segun(teclas,pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
		villano.se_mueve_solo()
		#verificacion de daño
		if heroe.se_encuentra_con(villano):
			heroe.es_golpeado()
		repintar_cuadro_juego()
# Termina el juego y finaliza los elementos de pygame
pygame.quit()