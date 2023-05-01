
const socketIO = require('socket.io');
const http = require('http');

const server = http.createServer();
const io = socketIO(server);

io.on('connection', (socket) => {
    console.log('nuevo cliente conectado');

    socket.on("conexionRecv", () => {
        io.emit("conexionRecibida")
    });

    socket.on("solicitoConexion", () => {
        io.emit("reciboConexion")
    });

    socket.on('apagar compu', () => {
        console.log('recibido apagar compu');
        io.emit('apagar compu');
    });
    
    socket.on('disconnect', () => {
        console.log('cliente desconectado')
    });

    socket.on('cerrar sesion', () => {
        console.log('recibido cerrar sesion')
        io.emit('cerrar sesion');
    });

    socket.on('click derecho', () => {
        console.log('recibido click derecho')
        io.emit('click derecho');
    });

    socket.on('click izquierdo', () => {
        console.log('recibido click izquierdo');
        io.emit('click izquierdo');
    });

    socket.on("moverMouse", (params) => {
        console.log("moviendo mouse", params);
        io.emit("moverMouse", params);
    })

});

server.listen(+(process.env.PORT || "") || 5000, () => {
    console.log('server a la espeera en el puerto 5000');
});