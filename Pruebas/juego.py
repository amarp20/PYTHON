import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 400
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego del Boxeador - Barra de Vida")

# Colores y reloj
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
reloj = pygame.time.Clock()

# Añadir sonidos
golpe_sonido = pygame.mixer.Sound("punch.mp3")

# Posiciones iniciales
boxeador1 = pygame.Rect(100, 150, 50, 50)
boxeador2 = pygame.Rect(650, 150, 50, 50)

# Velocidades de movimiento
velocidad_boxeador1 = 5
velocidad_boxeador2 = [3, -3]
golpeando_boxeador1 = False
golpeando_boxeador2 = False

# Vidas de los boxeadores
vidas_boxeador1 = 10
vidas_boxeador2 = 10

def dibujar_barra_vida(vidas, x, y):
    """Dibuja la barra de vida en la pantalla."""
    for i in range(vidas):
        pygame.draw.rect(screen, VERDE, (x + i * 20, y, 15, 15))

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:  # Golpe del boxeador1
                golpeando_boxeador1 = True
                golpe_sonido.play()
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_SPACE:
                golpeando_boxeador1 = False

    # Controles para mover al boxeador1
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and boxeador1.top > 0:
        boxeador1.y -= velocidad_boxeador1
    if teclas[pygame.K_s] and boxeador1.bottom < ALTO:
        boxeador1.y += velocidad_boxeador1
    if teclas[pygame.K_a] and boxeador1.left > 0:
        boxeador1.x -= velocidad_boxeador1
    if teclas[pygame.K_d] and boxeador1.right < ANCHO:
        boxeador1.x += velocidad_boxeador1

    # Movimiento automático del boxeador2
    boxeador2.x += velocidad_boxeador2[0]
    boxeador2.y += velocidad_boxeador2[1]

    # Mantener al boxeador2 dentro de los límites
    if boxeador2.left < 0 or boxeador2.right > ANCHO:
        velocidad_boxeador2[0] *= -1
    if boxeador2.top < 0 or boxeador2.bottom > ALTO:
        velocidad_boxeador2[1] *= -1

    # Detección de colisiones entre boxeadores
    if boxeador1.colliderect(boxeador2):
        golpe_sonido.play()
        if golpeando_boxeador1 and vidas_boxeador2 > 0:
            vidas_boxeador2 -= 1
        elif golpeando_boxeador2 and vidas_boxeador1 > 0:
            vidas_boxeador1 -= 1

    # Puñetazo aleatorio del boxeador2
    if random.randint(1, 100) > 95:
        golpeando_boxeador2 = True
        golpe_sonido.play()
    else:
        golpeando_boxeador2 = False

    # Fin del juego
    if vidas_boxeador1 <= 0 or vidas_boxeador2 <= 0:
        screen.fill(NEGRO)
        fuente = pygame.font.Font(None, 74)
        if vidas_boxeador1 > 0:
            texto = fuente.render("¡Ha ganado el boxeador 1!", True, BLANCO)
        else:
            texto = fuente.render("¡Ha ganado el boxeador 2!", True, BLANCO)
        screen.blit(texto, (100, ALTO // 2 - 37))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    # Dibujar en pantalla
    screen.fill(NEGRO)
    pygame.draw.rect(screen, BLANCO, boxeador1)
    pygame.draw.rect(screen, BLANCO, boxeador2)

    # Dibujar barras de vida
    dibujar_barra_vida(vidas_boxeador1, 50, 20)  # Barra de vida del boxeador1
    dibujar_barra_vida(vidas_boxeador2, ANCHO - 200, 20)  # Barra de vida del boxeador2

    # Representar golpes
    if golpeando_boxeador1:
        pygame.draw.rect(screen, ROJO, (boxeador1.x + 50, boxeador1.y + 10, 20, 20))
    if golpeando_boxeador2:
        pygame.draw.rect(screen, ROJO, (boxeador2.x - 20, boxeador2.y + 10, 20, 20))

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60)