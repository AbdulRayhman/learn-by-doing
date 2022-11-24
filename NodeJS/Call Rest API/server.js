import http from "http";
import fetch from "node-fetch";
import express from "express";
const app = express();
const getData = async () => {
	const data = await fetch(
		"http://159.65.148.48:9091/api/student/personal/info",
		{
			method: "GET",
			headers: {
				"Content-Type": "application/json",
				Authorization:
					"Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJuZXdUZXN0VXNlciIsImV4cCI6MTY2ODY0Nzk2MiwiaWF0IjoxNjY4NjI5OTYyfQ.yGyR1afLXWkgecc_tg7NasKyZMfsedBGrFj1g-UHE9dGZY_sFStl3IjSYth_HGFujyXudSYgkFc5Mzf8RyrdoQ",
			},
		}
	);
	return data
		.json()
		.then((res) => res)
		.catch((err) => err);
};
// getData();
// http.get("/info", (req, res, next) => {
// 	res.se;
// });
// const server = http
// 	.createServer(async function (req, res) {
// 		res.writeHead(200, { "Content-Type": "text/html" }); // http header
// 		var url = req.url;
// 		if (url === "/about") {
// 			const info = await getData();
// 			res.write(JSON.stringify(info)); //write a response
// 			res.end(); //end the response
// 		} else if (url === "/contact") {
// 			res.write("<h1>contact us page<h1>"); //write a response
// 			res.end(); //end the response
// 		} else {
// 			res.write("<h1>Hello World!<h1>"); //write a response
// 			res.end(); //end the response
// 		}
// 	})
// 	.listen(8000, () => {
// 		console.log("Server is running on *000");
// 	});
app.get("/info", async (req, res) => {
	// we can get the TOKEN|| URL from req params as well
	// 200 status code means OK
	const info = await getData();
	res.status(200).send(info);
});
app.listen(8000, () => {
	console.log("Server is running on port 8000");
});
