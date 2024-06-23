const net = require('net');


const client = net.createConnection({port:8080}, ()=>{
    console.log("Client Connected");
    client.write("hello from the client");
});

client.on('data', (serverData) => {
    console.log("Data received from server is", serverData.toString());
});