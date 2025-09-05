class Participante():
    def __init__(self,nombre,institucion):
        self.__nombre= nombre
        self.__institucion= institucion

    @property
    def nombre(self):
        return self.__nombre

    @property
    def institucion(self):
        return self.__institucion

    def mostrar_informacion(self):
        return f"{self.nombre} - {self.__institucion}"

class BandaEscolar(Participante):
    def __init__(self,nombre,institucion,categoria,puntuaje):
        super().__init__(nombre,institucion)
        self._categoria= categoria
        self._puntuaje= puntuaje

class Concurso():
    def __init__(self,fecha,nombre):
        self.fecha= fecha
        self.nombre= nombre
        self.bandas= {}

    def inscribir_banda(self,banda):
        if banda.nombre in self.bandas:
            raise ValueError (f"La banda {self.nombre} ya se encuentra inscrita...")
        self.bandas[banda.nombre] = banda

    def registrar_evaluacion(self,nombre,puntuaje):
        if not nombre in self.bandas:
            raise ValueError(f"No existe banda con el nombre {nombre}...")
        self.bandas[nombre].registrar_evaluacion(puntuaje)


    def listar_bandas(self):
        for banda in self.bandas.values():
            print(banda.mostrar_informacion)

    def ranking(self):
        valores_ordenados=dict(sorted(self.bandas.values(),key=lambda item: item.promedio))
        print(valores_ordenados)

import tkinter as tk

def inscribir_banda():
    print("Se abrió la ventana: Inscribir Banda")
    ventana_inscribir = tk.Toplevel(ventana)
    ventana_inscribir.title("Inscribir Banda")
    ventana_inscribir.geometry("400x300")

def registrar_evaluacion():
    print("Se abrió la ventana: Registrar Evaluación")
    ventana_eval = tk.Toplevel(ventana)
    ventana_eval.title("Registrar Evaluación")
    ventana_eval.geometry("400x300")

def listar_bandas():
    print("Se abrió la ventana: Listado de Bandas")
    ventana_listado = tk.Toplevel(ventana)
    ventana_listado.title("Listado de Bandas")
    ventana_listado.geometry("400x300")

def ver_ranking():
    print("Se abrió la ventana: Ranking Final")
    ventana_ranking = tk.Toplevel(ventana)
    ventana_ranking.title("Ranking Final")
    ventana_ranking.geometry("400x300")

def salir():
    print("Aplicación cerrada")
    ventana.quit()

ventana = tk.Tk()
ventana.title("Concurso de Bandas - Quetzaltenango")
ventana.geometry("500x300")

barra_menu = tk.Menu(ventana)

menu_opciones = tk.Menu(barra_menu, tearoff=0)
menu_opciones.add_command(label="Inscribir Banda", command=inscribir_banda)
menu_opciones.add_command(label="Registrar Evaluación", command=registrar_evaluacion)
menu_opciones.add_command(label="Listar Bandas", command=listar_bandas)
menu_opciones.add_command(label="Ver Ranking", command=ver_ranking)
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

ventana.config(menu=barra_menu)

etiqueta = tk.Label(
    ventana,
    text="Sistema de Inscripción y Evaluación de Bandas Escolares\nDesfile 15 de Septiembre - Quetzaltenango",
    font=("Arial", 12, "bold"),
    justify="center"
)
etiqueta.pack(pady=50)

ventana.mainloop()
