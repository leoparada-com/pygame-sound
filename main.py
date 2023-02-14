import pygame

# Inicializa Pygame
pygame.init()

# Carga el sonido en MP3
sound = pygame.mixer.Sound("sound.mp3")

# Crea un bucle de juego para detectar la entrada del usuario
running = True
while running:
    # Revisa si se presionó alguna tecla
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Revisa si se presionó la flecha hacia arriba
            if event.key == pygame.K_UP:
                # Reproduce el sonido
                sound.play()

    # Establece el modo de visualización
    screen = pygame.display.set_mode((640, 480))


    # Actualiza la pantalla
    pygame.display.update()

# Finaliza Pygame
pygame.quit()
