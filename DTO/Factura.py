class Factura
	def __init__(self, metodo_pago, monto, horaCreacion, idUsuarioCompra, idUsuarioVenta)
		self.metodo_pago = metodo_pago
		self.monto = monto
		self.horaCreacion = horaCreacion
		self.idUsuarioCompra = idUsuarioCompra
		self.idUsuarioVenta = idUsuarioVenta

	## Getters ##

	def darMetodoPago(self):
		return metodo_pago

	def darMonto(self):
		return monto

	def darHoraCreacion(self):
		return horaCreacion

	def idUsuarioCompra(self):
		return idUsuarioCompra

	def idUsuarioVenta(self):
		return idUsuarioVenta

	## Setters ##

	def setMetodoPago(self, metodoPagoX):
		self.metodo_pago = metodoPagoX

	def setMonto(self, montoX):
		self.monto = montoX

	def setHoraCreacion(self, horaCreacionX):
		self.horaCreacion = horaCreacionX

	def setIdUsuarioCompra(self, idUsuarioCompraX):
		self.idUsuarioCompra = idUsuarioCompraX

	def setIdUsuarioVenta(self, idUsuarioVentaX):
		self.idUsuarioVenta = idUsuarioVentaX



