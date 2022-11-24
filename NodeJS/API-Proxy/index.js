import express from "express";
import cors from "cors";
import dotenv from "dotenv";

dotenv.config();
const app = express();
const PORT = process.env.PORT || 5000;

console.log(process.env.PORT);
//http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=63be4b4ce5fbe681f9f33f99328e138f
app.use(cors());
app.listen(PORT, () => console.log(`Server is listen on ${PORT}.`));

