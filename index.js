
const socketIO = require('socket.io');
const http = require('http');

const server = http.createServer();
const io = socketIO(server);

io.on('connection', (socket) => {
    console.log('nuevo cliente conectado');

    socket.on('apagar compu', () => {
        console.log('recibido apagar compu');
        io.emit('apagar compu');
    });
    
    socket.on('disconnect', () => {
        console.log('cliente desconectado')
    });

    socket.on('cerrar secion', () => {
        console.log('recibido cerrar secion')
        io.emit('cerrar secion');
    });

});

server.listen(+(process.env.PORT || "") || 5000, () => {
    console.log('server a la espeera en el puerto 5000');
});