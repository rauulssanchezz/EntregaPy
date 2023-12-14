import tkinter as tk

class tipos:
    AGUA="Agua"
    FUEGO="Fuego"
    PLANTA="Planta"

respuesta=""

def funcion():
    funcionando=True
    statsTipos={tipos.PLANTA:"El tipo Pierra es fuerte contra tipo Agua y debil contra tipo Aire",
                tipos.FUEGO:"El tipo Fuego es fuerte contra tipo Planta y debil contra tipo Agua",
                tipos.AGUA: "El tipo Agua es fuerte contra el tipo Fuego y debil contra el tipo Planta"}

    while funcionando:
        tipoPok=str(entry.get())
        if tipoPok==tipos.AGUA or tipoPok==tipos.FUEGO or tipoPok==tipos.PLANTA:
            funcionando=False
            respuesta=statsTipos.get(tipoPok)
            label2 = tk.Label(ventana, text=respuesta)
            label2.pack(pady=10)
        else:
            respuesta="No es una respuesta correcta"
            label2 = tk.Label(ventana, text=respuesta)
            label2.pack(pady=10)


ventana = tk.Tk()
ventana.title("Pokemon hazte con todos")
ventana.geometry("300x200")
label =tk.Label(ventana, text="Introduce tipo pokemon")
label.pack(pady=10)
entry = tk.Entry(ventana)
entry.pack(pady=10)
boton=tk.Button(ventana, text="Boton",command=funcion)
boton.pack(pady=10)
ventana.mainloop()