import pygame
import time

class Personaje:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.pos_x = pantalla.get_width() // 2
        self.pos_y = pantalla.get_height() // 2

        self.imagenes = {
            "frente_reposo": pygame.image.load(r'n\imagen.png'),
            "frente_paso_izquierdo": pygame.image.load(r'n\imagen2.png'),
            "frente_paso_derecho": pygame.image.load(r'n\imagen4.png'),
            "derecha_reposo": pygame.image.load(r'n\derreposo.png'),  # Usa una imagen de reposo para derecha
            "derecha_paso_izquierdo": pygame.image.load(r'n\imagender1.png'),
            "derecha_paso_derecho": pygame.image.load(r'n\imagender2.png'),
            "izquierda_reposo": pygame.image.load(r'n\atrasreposo.png'),  # Usa una imagen de reposo para izquierda
            "izquierda_paso_izquierdo": pygame.image.load(r'n\imagenizq1.png'),
            "izquierda_paso_derecho": pygame.image.load(r'n\imagenizq4.png'),
            "atras_reposo": pygame.image.load(r'n\atrasreposo.png'),  # Usa una imagen de reposo para atrás
            "atras_paso_izquierdo": pygame.image.load(r'n\imagenatras.png'),
            "atras_paso_derecho": pygame.image.load(r'n\imagenatras2.png')
        }

        self.direccion = "frente"
        self.estado = "reposo"
        self.tiempo_ultimo_movimiento = time.time()
        self.paso = 0
        self.velocidad = 0.9  # Velocidad del personaje en píxeles

    def actualizar(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            self.direccion = "derecha"
            self.estado = "paso_derecho" if self.paso % 2 == 0 else "paso_izquierdo"
            self.pos_x += self.velocidad
            self.paso += 1
            self.tiempo_ultimo_movimiento = time.time()
        elif teclas[pygame.K_LEFT]:
            self.direccion = "izquierda"
            self.estado = "paso_derecho" if self.paso % 2 == 0 else "paso_izquierdo"
            self.pos_x -= self.velocidad
            self.paso += 1
            self.tiempo_ultimo_movimiento = time.time()
        elif teclas[pygame.K_UP]:
            self.direccion = "atras"
            self.estado = "paso_derecho" if self.paso % 2 == 0 else "paso_izquierdo"
            self.pos_y -= self.velocidad
            self.paso += 1
            self.tiempo_ultimo_movimiento = time.time()
        elif teclas[pygame.K_DOWN]:
            self.direccion = "frente"
            self.estado = "paso_derecho" if self.paso % 2 == 0 else "paso_izquierdo"
            self.pos_y += self.velocidad
            self.paso += 1
            self.tiempo_ultimo_movimiento = time.time()
        else:
            if time.time() - self.tiempo_ultimo_movimiento > 2:
                self.estado = "reposo"
            else:
                self.estado = "paso_derecho" if self.paso % 2 == 0 else "paso_izquierdo"

    def mostrar(self):
        self.actualizar()
        imagen_actual = self.imagenes[f"{self.direccion}_{self.estado}"]
        print(f"Mostrando imagen: {self.direccion}_{self.estado}")  # Mensaje de depuración
        self.pantalla.blit(imagen_actual, (self.pos_x - imagen_actual.get_width() // 2, self.pos_y - imagen_actual.get_height() // 2))
