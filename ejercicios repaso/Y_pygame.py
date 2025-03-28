import pygame

pygame.init() #Necesario para iniciar pygame
pygame.mixer.init() #Para iniciar el sonido
ancho, alto = 500, 400
pantalla = pygame.display.set_mode((ancho, alto)) #Alto y ancho de la pantalla de juego
pygame.display.set_caption("Juego con Pygame") #Título de la pantalla
rojo = (255, 0, 0)
blanco = (255, 255, 255) #definine colores con código RGB
x, y = ancho // 2, alto // 2 #define variables para asignar la posición inicial del cuadrado
vel_x, vel_y = 5, 5 #define variale velocidad inicial en pixeles de los dos ejes
velocidad = 5 #define variale velocidad en pixeles de los dos ejes
tamano_cuadrado = 40 #tamaño del cuadrado
sound = pygame.mixer.Sound("recursos/sonido.mp3")
imagen_coche = pygame.image.load("recursos/coche.png")  # Archivo de imagen del coche
imagen_coche = pygame.transform.scale(imagen_coche, (50, 50))  # Ajusta el tamaño de la imagen

jugando = True

while jugando:
    sound.play()
    pygame.time.delay(30) #Bucle principal del juego, el delay 30 le hace esperar 30 milisegundos entre iteraciones
    for evento in pygame.event.get(): #Obtiene eventos del usuario.
        if evento.type == pygame.QUIT: #Detecta si se cerró la ventana para salir del bucle.
            jugando = False
    teclas = pygame.key.get_pressed() #Verifica las teclas presionadas.
    if teclas[pygame.K_LEFT] and x >0: x -= velocidad
    if teclas[pygame.K_RIGHT] and x + 50 < ancho: x += velocidad
    if teclas[pygame.K_UP] and y >0: y -= velocidad
    if teclas[pygame.K_DOWN] and y + 50 < alto: y += velocidad
    
    pantalla.fill(blanco) #Borra la pantalla: Cada vez que el jugador se mueve, necesitamos limpiar la pantalla y volver a dibujar el cuadrado en su nueva posición.
    pantalla.blit(imagen_coche, (x, y))  # Dibuja la imagen del coche en su nueva posición
    pygame.display.update() #Actualiza la pantalla

pygame.quit() #cierra el programa