import pygame

pygame.init() #Necesario para iniciar pygame
ancho, alto = 500, 400
pantalla = pygame.display.set_mode((ancho, alto)) #Alto y ancho de la pantalla de juego
pygame.display.set_caption("Juego con Pygame") #Título de la pantalla
rojo = (255, 0, 0)
blanco = (255, 255, 255) #definine colores con código RGB
x, y = ancho // 2, alto // 2 #define variables para asignar la posición inicial del cuadrado
velocidad = 5 #define variale velocidad en pixeles

jugando = True
while jugando:
    pygame.time.delay(30) #Bucle principal del juego, el delay 30 le hace esperar 30 milisegundos entre iteraciones
    for evento in pygame.event.get(): #Obtiene eventos del usuario.
        if evento.type == pygame.QUIT: #Detecta si se cerró la ventana para salir del bucle.
            jugando = False
    teclas = pygame.key.get_pressed() #Verifica las teclas presionadas.
    if teclas[pygame.K_LEFT]: x -= velocidad
    if teclas[pygame.K_RIGHT]: x += velocidad
    if teclas[pygame.K_UP]: y -= velocidad
    if teclas[pygame.K_DOWN]: y += velocidad
    pantalla.fill(blanco) #Borra la pantalla: Cada vez que el jugador se mueve, necesitamos limpiar la pantalla y volver a dibujar el cuadrado en su nueva posición.
    pygame.draw.rect(pantalla, rojo, (x, y, 40, 40)) #Dibuja el cuadrado rojo.
    pygame.display.update() #Actualiza la pantalla
        
pygame.quit() #cierra el programa