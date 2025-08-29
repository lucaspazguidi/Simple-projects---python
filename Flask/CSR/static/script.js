const botao = document.getElementById('carregar-btn');
const botaoResetar = document.getElementById('resetar-img');
const divConteudo = document.getElementById('conteudo');

let indiceImagem = 0;
let imagens = [];

fetch('/api/alunos')
    .then(response => response.json())
    .then(dados_agostinho => {
        imagens = dados_agostinho;
    });

botao.addEventListener('click', () => {
    if (imagens.length > 0) {
        divConteudo.innerHTML = `<img src="${imagens[indiceImagem].nome}" alt="Imagem do aluno" style="max-width: 100%; height: auto; margin: 10px;">`;
        indiceImagem = (indiceImagem + 1) % imagens.length;
    }
});

botaoResetar.addEventListener('click', () => {
    indiceImagem = 0;
    if (imagens.length > 0) {
        divConteudo.innerHTML = "";
    }
});
