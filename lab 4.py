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
        if not any(new_cat == cat for cat in ["primaria", "basico", "diversificado"]):
            print("Categoría inválida")
        else:
            self._categoria = new_cat
            print(f"Categoría establecida como {new_cat}")

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
        print(f"Nombre: {self.nombre}\nInstitución: {self.institucion}\nCategoria: {self.categoria}\nPuntajes:")
        for tipo, punteo in self.puntajes.items():
            print(f"{tipo}: {punteo}")
        print(f"Total: {self.total}\nPromedio: {self.promedio}")


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

    def ranking(self): #rank
        ordenadas = sorted(self.bandas.values(), key=lambda b: b.promedio, reverse=True)
        for i, banda in enumerate(ordenadas, 1):
            print(f"{i}. {banda.nombre} - Promedio: {banda.promedio}")

import tkinter as tk

class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")
        tk.Toplevel(self.ventana).title("Inscribir Banda")

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        tk.Toplevel(self.ventana).title("Registrar Evaluación")

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        tk.Toplevel(self.ventana).title("Listado de Bandas")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Ranking Final")


if __name__ == "__main__":
    ConcursoBandasApp()
