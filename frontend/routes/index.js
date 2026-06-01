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

router.get('/modulos/:id', (req, res) => {
    const moduleId = req.params.id;
    res.render('modulo_detalhes', { 
        title: `CivIA - Módulo ${moduleId}`,
        moduleId: moduleId 
    });
});

router.get('/modulos/:id/topicos/:topicoId', (req, res) => {
    const { id, topicoId } = req.params;
    
    const nomeArquivo = `modulo_${id}_${topicoId.replace('.', '_')}`;
    res.render(nomeArquivo, { 
        title: `CivIA - Tópico ${id}.${topicoId}` 
    });
});