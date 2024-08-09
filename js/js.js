// Função para adicionar item ao carrinho
function adicionarAoCarrinho(sabor) {
    const carrinho = document.getElementById('lista-carrinho');
    const item = document.createElement('li');
    item.textContent = sabor;
    carrinho.appendChild(item);
}

// Adicionando evento de clique aos botões de escolha
const botoesEscolha = document.querySelectorAll('.botao-escolha');
botoesEscolha.forEach(botao => {
    botao.addEventListener('click', () => {
        const sabor = botao.getAttribute('data-sabor');
        adicionarAoCarrinho(sabor);
    });
});

const botaoFinalizarPedido = document.querySelector('.finalizar-pedido');

// Adiciona um evento de clique ao botão de finalizar pedido
botaoFinalizarPedido.addEventListener('click', () => {
    // Redireciona para a página de cadastro
    window.location.href = './login.html';
});
