class Ubicacion:
	def __init__(self, edi, ref, dire, coor ):
		self.edificio = edi
		self.referencia = ref
		self.direccion = dire
		self.coordenada = coor

	#GETS#

	def darEdificio(self):
		return self.edificio

	def darReferencia(self):
		return self.referencia

	def darDireccion(self):
		return self.direccion

	def darCoordenada(self):
		return self.coordenada

	#SETS#

	def setEdificio(self, ed):
		self.edificio = ed

	def setReferencia(self, refe):
		self.referencia = refe

	def setDireccion(self, di):
		self.direccion = di

	def setCoordenada(self, co):
		self.coordenada = co


