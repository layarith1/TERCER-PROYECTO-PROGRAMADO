import pygame
from menu import Menu
from personaje import Personaje
import gestion_partidas as gp
import api_consultas as api

#CERAMICAS PYGAME


def main():
    pygame.init()  # Inicializa Pygame
    pantalla = pygame.display.set_mode((800, 600))  # Crea una ventana de 800x600 píxeles
    pygame.display.set_caption("GeneaCity")  # Establece el título de la ventana

    menu = Menu(pantalla)  # Crea una instancia del menú, pasándole la pantalla como parámetro
    personaje = Personaje(pantalla)  # Crea una instancia del personaje, pasándole la pantalla como parámetro

    menu.mostrar_bienvenida()  # Muestra la pantalla de bienvenida

    corriendo = True  # Variable para controlar el bucle principal del juego
    partida_creada = False  # Variable para controlar si una partida ha sido creada

    def partida_creada():
        print("Mostrando personaje...")  # Mensaje de depuración
        pantalla.fill((0, 0, 0))  # Llena la pantalla con el color negro
        personaje.mostrar()  # Muestra el personaje en la pantalla
        pygame.display.flip()  # Actualiza la pantalla para reflejar los cambios

    while corriendo:
        for evento in pygame.event.get():  # Itera sobre los eventos de Pygame
            if evento.type == pygame.QUIT:  # Si se cierra la ventana
                corriendo = False  # Termina el bucle principal del juego

        if not partida_creada:  # Si no se ha creado una partida
            opcion_seleccionada = menu.mostrar()  # Muestra el menú y obtiene la opción seleccionada
            if opcion_seleccionada:
                if opcion_seleccionada == "Crear partida":
                    print("Crear partida seleccionada")
                    partida_creada = True  # Marca que una partida ha sido creada
                    break
                elif opcion_seleccionada == "Cargar partida":
                    print("Cargar partida seleccionada")
                    partida_creada = True  # Marca que una partida ha sido cargada
                    # Aquí podrías cargar una partida guardada, restaurar el estado del personaje, etc.
                elif opcion_seleccionada == "Ver histórico":
                    print("Ver histórico seleccionado")
                    # Aquí podrías mostrar el historial de partidas o cualquier otro dato relevante.
                elif opcion_seleccionada == "Salir":
                    corriendo = False  # Termina el bucle principal del juego
        else:  # Si se ha creado una partida
            print("Mostrando personaje...")  # Mensaje de depuración
            pantalla.fill((0, 0, 0))  # Llena la pantalla con el color negro
            personaje.mostrar()  # Muestra el personaje en la pantalla
            pygame.display.flip()  # Actualiza la pantalla para reflejar los cambios

    pygame.quit()  # Cierra Pygame

if __name__ == "__main__":
    main()

