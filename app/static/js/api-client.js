/**
 * Obtener todos los usuarios
 * @returns {Promise<Object[]>}
 */
export async function obtenerUsuarios() {
  try {
    const respuesta = await axios.get('/api/usuarios');
    return respuesta.data;
  } catch (error) {
    console.error('Error al obtener usuarios:', error);
  }
}

/**
 * Crear un nuevo usuario
 * @param {{nombre: string, email: string, contraseña: string, telefono: string}} datos
 * @returns {Promise<Object>}
 */
export async function crearUsuario(datos) {
  try {
    const respuesta = await axios.post('/api/usuarios', datos);
    return respuesta.data;
  } catch (error) {
    console.error('Error al crear usuario:', error);
  }
}

/**
 * Obtener un usuario por ID
 * @param {number} id
 * @returns {Promise<Object>}
 */
export async function obtenerUsuario(id) {
  try {
    const respuesta = await axios.get('/api/usuarios/${id}');
    return respuesta.data;
  } catch (error) {
    console.error(`Error al obtener usuario ${id}:`, error);
  }
}

/**
 * Actualizar un usuario
 * @param {number} id
 * @param {{nombre: string, email: string, contraseña: string, telefono: string}} datos
 * @returns {Promise<Object>}
 */
export async function actualizarUsuario(id, datos) {
  try {
    const respuesta = await axios.put('/api/usuarios/${id}', datos);
    return respuesta.data;
  } catch (error) {
    console.error(`Error al actualizar usuario ${id}:`, error);
  }
}

/**
 * Eliminar un usuario
 * @param {number} id
 * @returns {Promise<Object>}
 */
export async function eliminarUsuario(id) {
  try {
    const respuesta = await axios.delete('/api/usuarios/${id}');
    return respuesta.data;
  } catch (error) {
    console.error(`Error al eliminar usuario ${id}:`, error);
  }
}

/**
 * Obtener productos
 * @returns {Promise<Object[]>}
 */
export async function obtenerProductos() {
  try {
    const respuesta = await axios.get('/api/productos');
    return respuesta.data;
  } catch (error) {
    console.error('Error al obtener productos:', error);
  }
}

/**
 * Crear producto
 * @param {{nombre: string, descripcion: string, stock: number, precio: number}} datos
 * @returns {Promise<Object>}
 */
export async function crearProducto(datos) {
  try {
    const respuesta = await axios.post('/api/productos', datos);
    return respuesta.data;
  } catch (error) {
    console.error('Error al crear producto:', error);
  }
}

/**
 * Obtener carritos
 * @returns {Promise<Object[]>}
 */
export async function obtenerCarritos() {
  try {
    const respuesta = await axios.get('/api/carritos');
    return respuesta.data;
  } catch (error) {
    console.error('Error al obtener carritos:', error);
  }
}

/**
 * Crear carrito
 * @param {{id_usuario: number, total: number}} datos
 * @returns {Promise<Object>}
 */
export async function crearCarrito(datos) {
  try {
    const respuesta = await axios.post('/api/carritos', datos);
    return respuesta.data;
  } catch (error) {
    console.error('Error al crear carrito:', error);
  }
}

/**
 * Obtener detalles del carrito
 * @returns {Promise<Object[]>}
 */
export async function obtenerDetallesCarrito() {
  try {
    const respuesta = await axios.get('/api/detalles-carrito');
    return respuesta.data;
  } catch (error) {
    console.error('Error al obtener detalles del carrito:', error);
  }
}

/**
 * Crear detalle de carrito
 * @param {{id_carrito: number, id_producto: number, cantidad: number, subtotal: number}} datos
 * @returns {Promise<Object>}
 */
export async function crearDetalleCarrito(datos) {
  try {
    const respuesta = await axios.post('/api/detalles-carrito', datos);
    return respuesta.data;
  } catch (error) {
    console.error('Error al crear detalle del carrito:', error);
  }
}

/**
 * Obtener contactos
 * @returns {Promise<Object[]>}
 */
export async function obtenerContactos() {
  try {
    const respuesta = await axios.get('/api/contactos');
    return respuesta.data;
  } catch (error) {
    console.error('Error al obtener contactos:', error);
  }
}

/**
 * Crear contacto
 * @param {{id_usuario: number, direccion: string, telefono: string, email: string}} datos
 * @returns {Promise<Object>}
 */
export async function crearContacto(datos) {
  try {
    const respuesta = await axios.post('/api/contactos', datos);
    return respuesta.data;
  } catch (error) {
    console.error('Error al crear contacto:', error);
  }
}

/**
 * Obtener métodos de pago
 * @returns {Promise<Object[]>}
 */
export async function obtenerMetodosPago() {
  try {
    const respuesta = await axios.get('/api/metodos-pago');
    return respuesta.data;
  } catch (error) {
    console.error('Error al obtener métodos de pago:', error);
  }
}

/**
 * Crear método de pago
 * @param {{tipo: string, detalles: string}} datos
 * @returns {Promise<Object>}
 */
export async function crearMetodoPago(datos) {
  try {
    const respuesta = await axios.post('/api/metodos-pago', datos);
    return respuesta.data;
  } catch (error) {
    console.error('Error al crear método de pago:', error);
  }
}

/**
 * Obtener pedidos
 * @returns {Promise<Object[]>}
 */
export async function obtenerPedidos() {
  try {
    const respuesta = await axios.get('/api/pedidos');
    return respuesta.data;
  } catch (error) {
    console.error('Error al obtener pedidos:', error);
  }
}

/**
 * Crear pedido
 * @param {{fecha: string, id_usuario: number, id_metodo_pago: number, total: number, estado: string}} datos
 * @returns {Promise<Object>}
 */
export async function crearPedido(datos) {
  try {
    const respuesta = await axios.post('/api/pedidos', datos);
    return respuesta.data;
  } catch (error) {
    console.error('Error al crear pedido:', error);
  }
}

/**
 * Obtener detalles de pedido
 * @returns {Promise<Object[]>}
 */
export async function obtenerDetallesPedido() {
  try {
    const respuesta = await axios.get('/api/detalles-pedido');
    return respuesta.data;
  } catch (error) {
    console.error('Error al obtener detalles del pedido:', error);
  }
}

/**
 * Crear detalle de pedido
 * @param {{id_pedido: number, id_producto: number, cantidad: number, subtotal: number}} datos
 * @returns {Promise<Object>}
 */
export async function crearDetallePedido(datos) {
  try {
    const respuesta = await axios.post('/api/detalles-pedido', datos);
    return respuesta.data;
  } catch (error) {
    console.error('Error al crear detalle del pedido:', error);
  }
}

/**
 * Obtener citas
 * @returns {Promise<Object[]>}
 */
export async function obtenerCitas() {
  try {
    const respuesta = await axios.get('/api/citas');
    return respuesta.data;
  } catch (error) {
    console.error('Error al obtener citas:', error);
  }
}

/**
 * Crear cita
 * @param {{fecha: string, hora: string, id_usuario: number, id_servicio: number, estado: string}} datos
 * @returns {Promise<Object>}
 */
export async function crearCita(datos) {
  try {
    const respuesta = await axios.post('/api/citas', datos);
    return respuesta.data;
  } catch (error) {
    console.error('Error al crear cita:', error);
  }
}

/**
 * Obtener servicios
 * @returns {Promise<Object[]>}
 */
export async function obtenerServicios() {
  try {
    const respuesta = await axios.get('/api/servicios');
    return respuesta.data;
  } catch (error) {
    console.error('Error al obtener servicios:', error);
  }
}

/**
 * Crear servicio
 * @param {{nombre: string, descripcion: string, precio: number}} datos
 * @returns {Promise<Object>}
 */
export async function crearServicio(datos) {
  try {
    const respuesta = await axios.post('/api/servicios', datos);
    return respuesta.data;
  } catch (error) {
    console.error('Error al crear servicio:', error);
  }
}
