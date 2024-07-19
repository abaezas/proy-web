
class Carrito():

    def __init__(self, request):

        self.session = request.session

        carrito = self.session.get('session_key')

        if 'session_key' not in request.session:
            carrito = self.session['session_key'] = {}

        self.carrito = carrito


    def agregar(self, producto):

        producto_id = str(producto.id)

        self.carrito[producto_id] = {'precio': str(producto.precio)}        

        self.session.modified = True