class cliente:
    def __init__(self):
        self.membresia = []
    def agregar_membresia (self, nombre, membresia_activa):
        self.membresia.append({"nombre": nombre, "membresia_activa": membresia_activa})
        
        