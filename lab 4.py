import tkinter as tk
from tkinter import messagebox

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

    def registrar_puntajes(self, calificaciones):
        punteo_mal = False
        for cat, punteo in calificaciones.items():
            if punteo < 0 or punteo > 10:
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

    def mostrar_info(self, root):
        tk.Label(root, text=f"-----------------------\nNombre: {self.nombre}\nInstitución: {self.institucion}\nCategoria: {self.categoria}\nPuntajes:")
        if self.puntajes:
            for tipo, punteo in self.puntajes.items():
                tk.Label(root, text=f"{tipo}: {punteo}")
        else:
            tk.Label(root, text="No hay puntajes")


class Concurso():
    def __init__(self,fecha,nombre):
        self.fecha= fecha
        self.nombre= nombre
        self.bandas= {}

    def inscribir_banda(self,banda):
        if banda.nombre in self.bandas.values():
            raise ValueError (f"La banda {self.nombre} ya se encuentra inscrita...")
        self.bandas[banda.nombre] = banda

    def registrar_evaluacion(self,nombre,puntuaje):
        if not nombre in self.bandas:
            raise ValueError(f"No existe banda con el nombre {nombre}...")
        self.bandas[nombre].registrar_evaluacion(puntuaje)

    def listar_bandas(self):
        if not self.bandas:
            return []
        lista_info = []
        for indice, banda in enumerate(self.bandas.values(), 1):
            informacion = str(indice) + "." + banda.mostrar_informacion()
            if banda.puntajes:
                puntajes = ""
                for criterio, puntaje in banda.puntajes.items():
                    if puntajes != "":
                        puntajes += ", "
                    puntajes += criterio + ": " + str(puntaje)
                informacion += " Puntajes: " + puntajes
                informacion += " Total: " + str(banda.total)
                informacion += " Promedio: " + str(banda.promedio)
            else:
                informacion += " No evaluada aun"
            lista_info.append(informacion)
        return lista_info

    def ranking(self):
        if not self.bandas:
            return "no hay bandas..."
        bandas= list(self.bandas.values())
        banda_ordendas= sorted(bandas, key =lambda b:(b.total,b.promedio),reverse=True)
 #       ordenadas = sorted(self.bandas.values(), key=lambda b: b.promedio, reverse=True)
        return banda_ordendas

    def hay_bandas(self):
        if self.bandas:
            return True
        else:
            return False

concurso = Concurso("14-09-2025", "Independencia")


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
        v_inscribir = tk.Toplevel(self.ventana)
        v_inscribir.title("Inscribir Banda")
        tk.Label(v_inscribir, text="Inscribir Banda")

        nombre_entrada = tk.StringVar(v_inscribir)
        tk.Label(v_inscribir, text="Nombre de la banda").pack()
        tk.Entry(v_inscribir, textvariable=nombre_entrada).pack()

        insti_entrada = tk.StringVar(v_inscribir)
        tk.Label(v_inscribir, text="Institución").pack()
        tk.Entry(v_inscribir, textvariable=insti_entrada).pack()

        tk.Label(v_inscribir, text="Seleccione una categoría").pack()
        opciones = ["primaria","básico","diversificado"]
        categoria = tk.StringVar(v_inscribir)
        categoria.set(opciones[0])
        menu = tk.OptionMenu(v_inscribir, categoria, *opciones).pack()

        def guardar():
            nombre = nombre_entrada.get()
            insti = insti_entrada.get()
            cat = categoria.get()
            if nombre and insti:
                nombre_dupe = False
                if concurso.bandas:
                    for bandita_name in concurso.bandas.keys():
                        if bandita_name == nombre:
                            messagebox.showerror(title="Error", message="Ya hay una banda con ese nombre")
                            nombre_dupe = True
                if not nombre_dupe:
                    banda = BandaEscolar(nombre, insti, cat)
                    concurso.inscribir_banda(banda)
                    print(f"Banda guardada con éxito: {nombre}, {insti}, {cat}")
                    v_inscribir.destroy()
            else:
                messagebox.showerror("Error", "Debe llenar todos los campos para guardar")
        tk.Button(v_inscribir, text="Guardar", command=guardar).pack()


    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        v_registrar = tk.Toplevel(self.ventana)
        v_registrar.title("Registrar Evaluación")
        listado = concurso.hay_bandas()
        if listado:
            def validar_entrada(val):
                if val == "":
                    return True
                if val.isdigit():
                    numero = int(val)
                    return 0 <= numero <= 10
                return False
            val_cmd = (v_registrar.register(validar_entrada), "%P")

            tk.Label(v_registrar, text="Seleccione una banda").pack()
            bandas = [banda for banda in concurso.bandas.keys()]
            banditas = tk.StringVar(v_registrar)
            banditas.set(bandas[0])
            menu = tk.OptionMenu(v_registrar, banditas, *bandas).pack()

            c_ritmo = tk.StringVar(v_registrar)
            tk.Label(v_registrar, text= "Punteo por ritmo").pack()
            tk.Entry(v_registrar, textvariable=c_ritmo, validate="key", validatecommand=val_cmd).pack()

            c_uniformidad = tk.StringVar(v_registrar)
            tk.Label(v_registrar, text="Punteo por uniformidad").pack()
            tk.Entry(v_registrar, textvariable=c_uniformidad, validate="key", validatecommand=val_cmd).pack()

            c_coreo = tk.StringVar(v_registrar)
            tk.Label(v_registrar, text="Punteo por coreografía").pack()
            tk.Entry(v_registrar, textvariable=c_coreo, validate="key", validatecommand=val_cmd).pack()

            c_alineacion = tk.StringVar(v_registrar)
            tk.Label(v_registrar, text="Punteo por alineación").pack()
            tk.Entry(v_registrar, textvariable=c_alineacion, validate="key", validatecommand=val_cmd).pack()

            c_puntualidad = tk.StringVar(v_registrar)
            tk.Label(v_registrar, text="Punteo por puntualidad").pack()
            tk.Entry(v_registrar, textvariable=c_puntualidad, validate="key", validatecommand=val_cmd).pack()

            def guardar():
                if not validar_entrada(c_ritmo.get()) or not validar_entrada(c_uniformidad.get()) or not validar_entrada(c_coreo.get()) or not validar_entrada(c_alineacion.get()) or not validar_entrada(c_alineacion.get()):
                    messagebox.showerror("Error", "Los punteos deben ser números enteros del 0 al 10")
                else:
                    punteos = {}
                    punteos["ritmo"] = int(c_ritmo.get())
                    punteos["uniformidad"] = int(c_uniformidad.get())
                    punteos["coreo"] = int(c_coreo.get())
                    punteos["alineacion"] = int(c_alineacion.get())
                    punteos["puntualidad"] = int(c_puntualidad.get())
                    for banda_search, n in concurso.bandas.items():
                        if banda_search == banditas.get():
                            n.registrar_puntajes(punteos)
                            messagebox.showinfo("Punteos guardados", "Punteos registrados correctamente")
                            v_registrar.destroy()
            tk.Button(v_registrar, text="Guardar", command=guardar).pack()

        else:
            messagebox.showerror("Error", "No hay bandas registradas")
            v_registrar.destroy()

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        v_listar = tk.Toplevel(self.ventana)
        v_listar.title("Listado de Bandas")
        lista_info = concurso.listar_bandas()

        if not lista_info:
            tk.Label(v_listar, text="No hay bandas registradas...").pack()
        else:
            for info in lista_info:
                tk.Label(v_listar, text=info, anchor="w",).pack()

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        v_rankear = tk.Toplevel(self.ventana)
        v_rankear.title("Ranking Final")
        lista_ordenada = concurso.ranking()

        if not lista_ordenada:
            tk.Label(v_rankear, text="No hay bandas registradas").pack()
        else:
            for i, banda in enumerate(lista_ordenada, 1):
                informacion = f"{i}. {banda.mostrar_informacion()} - Total: {banda.total} - Promedio: {banda.promedio}"
                tk.Label(v_rankear, text=informacion).pack()

if __name__ == "__main__":
    ConcursoBandasApp()
