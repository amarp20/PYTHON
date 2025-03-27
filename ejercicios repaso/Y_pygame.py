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

jugando = True
while jugando:
    sound.play()
    pygame.time.delay(30) #Bucle principal del juego, el delay 30 le hace esperar 30 milisegundos entre iteraciones
    for evento in pygame.event.get(): #Obtiene eventos del usuario.
        if evento.type == pygame.QUIT: #Detecta si se cerró la ventana para salir del bucle.
            jugando = False
    teclas = pygame.key.get_pressed() #Verifica las teclas presionadas.
    if teclas[pygame.K_LEFT]: x -= velocidad
    if teclas[pygame.K_RIGHT]: x += velocidad
    if teclas[pygame.K_UP]: y -= velocidad
    if teclas[pygame.K_DOWN]: y += velocidad
    
    x += vel_x
    y += vel_y #actualizamos la posoción del cuadrado

    if x <= 0 or x + tamano_cuadrado >= ancho: #Si el tamaño del cuadrado se sale del ancho
        vel_x *= -1  # Invierte la velocidad en el eje X
    if y <= 0 or y + tamano_cuadrado >= alto:  #Si el tamaño del cuadrado se sale del alto
        vel_y *= -1  # Invierte la velocidad en el eje Y
    
    pantalla.fill(blanco) #Borra la pantalla: Cada vez que el jugador se mueve, necesitamos limpiar la pantalla y volver a dibujar el cuadrado en su nueva posición.
    pygame.draw.rect(pantalla, rojo, (x, y, 40, 40)) #Dibuja el cuadrado rojo.
    pygame.display.update() #Actualiza la pantalla

pygame.quit() #cierra el programa