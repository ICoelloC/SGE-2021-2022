from policia import Policia


class JefePatrulla (Policia):
    def __init__(self, id, nombre, n_placa, id_patrulla):
        super().__init__(id, nombre, n_placa)
        self.delincientes = []

    @property
    def delincientes(self):
        return self.delincientes

    @delincientes.setter
    def delincientes(self, delincientes):
        self.delincientes = delincientes

    def agregar_delincuente(self, delincuente):
        self.delincientes.append(delincuente)

    def ver_registro(self):
        registro = {'patrulla': self.id_patrulla, 'delincuente': []}
        for d in self.delincientes:
            registro.get('delincuente').append(d.get_datos())
        return registro
