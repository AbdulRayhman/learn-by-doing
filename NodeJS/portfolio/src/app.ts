import express, { Application, Request, Response, NextFunction} from 'express';

const app: Application = express();
app.use('/static', express.static('public'))
// app.use('/static', express.static(path.join(__dirname, 'public')))
app.get('/', (req: Request, res: Response, next: NextFunction) => {
	res.send({
		code: 200,
	message:'Sucessfully Rendered'})
});
const port = process.env.PORT || 5000;
app.listen(5000, () => console.log(`Server Running on ${port} port.`));