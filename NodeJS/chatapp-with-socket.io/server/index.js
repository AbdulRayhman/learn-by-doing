const http = require("http").createServer();

const io = require("socket.io")(http, { cors: { origin: "*" } });

io.on('connection', (socket) => {
	socket.on('message', (message) => {
		io.emit("message", `${socket.id.substr(0, 2)} said ${message}`);
	})
});

http.listen(8080, "127.0.0.1", () => console.log("127.0.0.1 on PORT 8080"));
