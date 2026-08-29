#asignamos valor
angulo = 80

# establcemos el condicional if para saber que tipo de angulo es el del valor ingresado
if angulo < 90:
    # si mide menos de 90 grados es un angulo agudo
    print("angulo agudo")
elif angulo > 90:
    # si mide mas de 90 grados es un angulo obtuso
    print("angulo obtuso")
else:
    # si mide 90 grados es un angulo recto
    print("angulo recto")