import pygame

# Clase Menu para gestionar el menú principal del juego
class Menu:
    def __init__(self, pantalla):
        self.pantalla = pantalla  # Superficie donde se dibuja el menú
        self.opciones = ["Crear partida", "Cargar partida", "Ver histórico", "Salir"]  # Opciones del menú
        self.seleccionada = 0  # Opción actualmente seleccionada
        
        # Cargar la fuente para el menú
        self.fuente_menu = pygame.font.Font(None, 36)  # Fuente para el texto del menú
        
        # Cargar las imágenes de bienvenida
        self.imagen_bienvenida = pygame.image.load(r'n\mushCity.png')
        self.imagen_bienvenida2 = pygame.image.load(r'Geneacity.png')
        self.imagen_bienvenida3 = pygame.image.load(r'hon.png')
        
        # Redimensionar las imágenes al tamaño deseado
        self.imagen_bienvenida = pygame.transform.scale(self.imagen_bienvenida, (800, 600))  # Especifica el tamaño deseado
        self.imagen_bienvenida2 = pygame.transform.scale(self.imagen_bienvenida2, (600, 100))  # Especifica el tamaño deseado
        self.imagen_bienvenida3 = pygame.transform.scale(self.imagen_bienvenida3, (150, 150))  # Especifica el tamaño deseado

    # Método para mostrar la pantalla de bienvenida
    def mostrar_bienvenida(self):
        mostrar_bienvenida = True
        while mostrar_bienvenida:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Salir del juego si se cierra la ventana
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:  # Continuar si se presiona Enter
                        mostrar_bienvenida = False

            self.pantalla.fill((0, 0, 0))  # Limpiar la pantalla
            self.pantalla.blit(self.imagen_bienvenida, (0, 0))  # Dibujar la imagen de bienvenida (fondo)
            self.pantalla.blit(self.imagen_bienvenida2, (100, 50))  # Dibujar la imagen de bienvenida2 (rótulo)
            
            # Calcular la posición de imagen_bienvenida3 para que esté centrada
            x = (800 - self.imagen_bienvenida3.get_width()) // 2
            y = (870 - self.imagen_bienvenida3.get_height()) // 2
            self.pantalla.blit(self.imagen_bienvenida3, (x, y))  # Dibujar la imagen_bienvenida3 centrada
            
            # Renderizar y dibujar el texto de instrucciones
            texto = self.fuente_menu.render("Presione Enter para continuar", True, (255, 255, 255))  # Mensaje en pantalla
            self.pantalla.blit(texto, (200, 500))  # Posicionar el mensaje en la pantalla
            pygame.display.flip()  # Actualizar la pantalla

    # Método para mostrar el menú principal
    def mostrar(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Salir del juego si se cierra la ventana
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:  # Mover la selección hacia arriba
                    self.seleccionada = (self.seleccionada - 1) % len(self.opciones)
                elif evento.key == pygame.K_DOWN:  # Mover la selección hacia abajo
                    self.seleccionada = (self.seleccionada + 1) % len(self.opciones)
                elif evento.key == pygame.K_RETURN:  # Seleccionar la opción actual
                    return self.opciones[self.seleccionada]
            pygame.display.flip()  # Actualizar la pantalla

        self.pantalla.fill((0, 0, 0))  # Limpiar la pantalla
        for i, opcion in enumerate(self.opciones):
            color = (255, 255, 255) if i == self.seleccionada else (100, 100, 100)  # Color de la opción seleccionada
            texto = self.fuente_menu.render(opcion, True, color)  # Renderizar el texto de la opción
            self.pantalla.blit(texto, (350, 250 + i * 40))  # Posicionar el texto en la pantalla

        pygame.display.flip()  # Actualizar la pantalla
        return None  # No se seleccionó ninguna opción aún

# Inicialización de Pygame y creación de la pantalla principal
pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("GeneaCity")

# Crear una instancia del menú y mostrar la bienvenida
menu = Menu(pantalla)
menu.mostrar_bienvenida()

# Mostrar el menú principal
opcion_seleccionada = None
while opcion_seleccionada is None:
    opcion_seleccionada = menu.mostrar()

print(f"Opción seleccionada: {opcion_seleccionada}")

pygame.quit()
