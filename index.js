
const socketIO = require('socket.io');
const http = require('http');

const server = http.createServer();
const io = socketIO(server);

io.on('conection', (socket) => {
    console.log('nuevo cliente conectado');

    socket.on('apagar compu', () => {
        console.log('recibido apagar compu');
        io.emit('apagar compu');
    });
    
    socket.on('disconect', () => {
        console.log('cliente desconectado')
    });

});

server.listen(5000, () => {
    console.log('server a la espeera en el puerto 5000');
});