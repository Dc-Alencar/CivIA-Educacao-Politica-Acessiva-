import { Router } from 'express';

export const router = Router();

router.get('/', (req, res) => {
    res.render('index', { title: 'CivIA - Frontend', message: 'Bem-vindo ao CivIA!' });
});

router.get('/login', (req, res) => {
    res.render('login', { title: 'CivIA - Login' });
});

router.get('/cadastro', (req, res) => {
    res.render('cadastro', { title: 'CivIA - Cadastro' });
});

router.get('/modulos', (req, res) => {
    res.render('modulos', { title: 'CivIA - Módulos' });
});