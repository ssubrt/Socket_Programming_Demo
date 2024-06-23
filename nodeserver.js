const net = require('net');

const server = net.createServer((socket) =>{
    socket.on('data',(clientData) => {
        console.log("Data recieved from client",clientData.toString());
        socket.write("received on server thank you");
    })
});

server.listen(8080,()=>{
    console.log("New Server ip on port 8080");
});