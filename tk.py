import tkinter as tk
from tkinter import messagebox

def registrar_estudiante():
    nombre_estudiante = entry_nombre.get()
    apellido_estudiante = entry_apellido.get()
    edad_estudiante = entry_edad.get()
    clase = entry_clase.get()
    seccion = entry_seccion.get()
    estado_inscripcion = var_estado_inscripcion.get()
    materias = [var_musica.get(), var_deporte.get()]
    comentarios = text_comentarios.get("1.0", tk.END).strip()
    nivel_escolar = var_nivel_escolar.get()

    mensaje = f"Estudiante registrado:\nNombre del Estudiante: {nombre_estudiante} {apellido_estudiante}\nEdad: {edad_estudiante}\nClase: {clase}\nSección: {seccion}\nEstado de inscripción: {estado_inscripcion}\nMaterias optativas: {materias}\nComentarios: {comentarios}\nNivel escolar: {nivel_escolar}"

    messagebox.showinfo("Registro Exitoso", mensaje)

def limpiar_formulario():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    var_estado_inscripcion.set("")
    var_musica.set(0)
    var_deporte.set(0)
    text_comentarios.delete("1.0", tk.END)
    var_nivel_escolar.set("Primaria")

# Crear ventana principal 
ventana = tk.Tk()
ventana.title("Registro de estudiantes en la escuela InnovadoresX")

# Frames
frame_datos_personales = tk.Frame(ventana)
frame_datos_personales.pack(pady=10)

frame_detalle = tk.Frame(ventana)
frame_detalle.pack(pady=10)

frame_estado_inscripcion = tk.Frame(ventana)
frame_estado_inscripcion.pack(pady=10)

frame_materias = tk.Frame(ventana)
frame_materias.pack(pady=10)

frame_comentarios = tk.Frame(ventana)
frame_comentarios.pack(pady=10)

# Información del estudiante
label_nombre = tk.Label(frame_datos_personales, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_datos_personales)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

label_apellido = tk.Label(frame_datos_personales, text="Apellido:")
label_apellido.grid(row=0, column=2, padx=5, pady=5)
entry_apellido = tk.Entry(frame_datos_personales)
entry_apellido.grid(row=0, column=3, padx=5, pady=5)

label_edad = tk.Label(frame_datos_personales, text="Edad:")
label_edad.grid(row=1, column=0, padx=5, pady=5)
entry_edad = tk.Entry(frame_datos_personales)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

# Detalles Académicos
label_clase = tk.Label(frame_detalle, text="Clase:")
label_clase.grid(row=0, column=0, padx=5, pady=5)
entry_clase = tk.Entry(frame_detalle)
entry_clase.grid(row=0, column=1, padx=5, pady=5)

label_seccion = tk.Label(frame_detalle, text="Sección:")
label_seccion.grid(row=0, column=2, padx=5, pady=5)
entry_seccion = tk.Entry(frame_detalle)
entry_seccion.grid(row=0, column=3, padx=5, pady=5)

# Estado de Inscripción
var_estado_inscripcion = tk.StringVar()
label_estado_inscripcion = tk.Label(frame_estado_inscripcion, text="Estado de Inscripción:")
label_estado_inscripcion.grid(row=0, column=0, padx=5, pady=5)
radio_inscrito = tk.Radiobutton(frame_estado_inscripcion, text="Inscrito", variable=var_estado_inscripcion, value="Inscrito")
radio_inscrito.grid(row=0, column=1, padx=5, pady=5)
radio_no_inscrito = tk.Radiobutton(frame_estado_inscripcion, text="No inscrito", variable=var_estado_inscripcion, value="No inscrito")
radio_no_inscrito.grid(row=0, column=2, padx=5, pady=5)

# Materias optativas
var_musica = tk.IntVar()
var_deporte = tk.IntVar()
label_materias = tk.Label(frame_materias, text="Materias Optativas:")
label_materias.grid(row=0, column=0, padx=5, pady=5)
check_musica = tk.Checkbutton(frame_materias, text="Música", variable=var_musica)
check_musica.grid(row=0, column=1, padx=5, pady=5)
check_deporte = tk.Checkbutton(frame_materias, text="Deporte", variable=var_deporte)
check_deporte.grid(row=0, column=2, padx=5, pady=5)

# Comentarios Adicionales
label_comentarios = tk.Label(frame_comentarios, text="Comentarios:")
label_comentarios.grid(row=0, column=0, padx=5, pady=5)
text_comentarios = tk.Text(frame_comentarios, height=6, width=30)
text_comentarios.grid(row=1, column=0, padx=5, pady=5)

# Menú desplegable para nivel escolar
label_nivel_escolar = tk.Label(frame_datos_personales, text="Nivel escolar:")
label_nivel_escolar.grid(row=2, column=0, padx=5, pady=5)
nivel_escolar = ["Primaria", "Secundaria"]
var_nivel_escolar = tk.StringVar()
var_nivel_escolar.set(nivel_escolar[0])
menu_nivel_escolar = tk.OptionMenu(frame_datos_personales, var_nivel_escolar, *nivel_escolar)
menu_nivel_escolar.grid(row=2, column=1, padx=5, pady=5)

# Botones de acción
btn_registrar = tk.Button(ventana, text="Registrar Estudiante", command=registrar_estudiante)
btn_registrar.pack(pady=10)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_formulario)
btn_limpiar.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()










