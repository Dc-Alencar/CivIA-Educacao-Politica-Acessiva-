import express from 'express';
import 'dotenv/config';
import app from './app.js';

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Servidor Frontend (EJS) rodando na porta ${PORT}`);
});