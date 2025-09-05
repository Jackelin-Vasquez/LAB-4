class Participante():
    def __init__(self,nombre,institucion):
        self.__nombre= nombre
        self.__institucion= institucion

class BandaEscolar(Participante):
    def __init__(self,nombre,institucion,categoria):
        super().__init__(nombre,institucion)
        self._categoria= categoria
        self._puntajes= {}
        self.total = 0
        self.promedio = 0
        @property
        def categoria(self):
            return self._categoria
        @property
        def puntaje(self):
            return self._puntaje
        @categoria.setter
        def categoria(self,categoria):
            if len(categoria) <4:
                print("Categoría muy corta")
            else:
                self._categoria = categoria
        @puntaje.setter
        def puntaje(self,puntaje):
            if puntaje <0 or puntaje > 10:
                print("El puntaje debe estar entre 0 y 10")
            else:
                self._puntaje = puntaje

        def set_categoria(self, new_cat):
            pass

        def registrar_puntajes(self, calificaciones):
            punteo_mal = False
            for cat, punteo in calificaciones.items():
                if punteo < 0 and punteo > 10:
                    punteo_mal = True
                    print(f"El punteo de la categoría {cat} no está en el rango permitido (0-10)")
            if not punteo_mal:
                total = 0
                for punteo in calificaciones.values():
                    total += punteo
                promedio = round(total / len(calificaciones.values()), 0)
                self.puntajes = calificaciones
                self.total = total
                self.promedio = promedio


        def mostrar_info(self):
            pass




class Concurso():
    def __init__(self,fecha,nombre):
        self.fecha= fecha
        self.nombre= nombre
#IJD

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
