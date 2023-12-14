class tipos:
    AGUA="Agua"
    FUEGO="Fuego"
    PLANTA="Planta"

funcionando=True
statsTipos={tipos.PLANTA:"El tipo Pierra es fuerte contra tipo Agua y debil contra tipo Aire",
            tipos.FUEGO:"El tipo Fuego es fuerte contra tipo Planta y debil contra tipo Agua",
            tipos.AGUA: "El tipo Agua es fuerte contra el tipo Fuego y debil contra el tipo Planta"}

while funcionando:
    tipoPok=input("Tipo del pokemon (Agua, Fuego, Planta):")
    if tipoPok==tipos.AGUA or tipoPok==tipos.FUEGO or tipoPok==tipos.PLANTA:
        funcionando=False
        print(statsTipos.get(tipoPok))
    else:
        print("No es una respuesta correcta")
