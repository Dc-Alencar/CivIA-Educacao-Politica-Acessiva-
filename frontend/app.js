import express from 'express';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import session from 'express-session';
import flash from 'connect-flash';
import { router } from './routes/index.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const app = express();


app.set('view engine', 'ejs');
app.set('views', join(__dirname, 'views'));
app.use(express.static(join(__dirname, 'public')));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use(session({
    secret: process.env.SESSION_SECRET || 'segredo-dev',
    resave: false,
    saveUninitialized: false,
    cookie: { secure: false },
}));

app.use(flash());

app.use('/', router);

export default app;
