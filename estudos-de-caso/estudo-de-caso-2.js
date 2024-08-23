let estoque = [
    { nome: "Produto A", quantidade: 10 },
    { nome: "Produto B", quantidade: 8 },
    { nome: "Produto C", quantidade: 3 },
    { nome: "Produto D", quantidade: 15 }
];

function exibirEstoque() {
    console.log("Estoque Atual:");
    estoque.forEach(produto => {
        console.log(`${produto.nome}: ${produto.quantidade} unidades`);
    });
    console.log('-----');
}

function adicionarProduto(nome, quantidade) {
    const produto = estoque.find(p => p.nome === nome);
    if (produto) {
        produto.quantidade += quantidade;
    } else {
        estoque.push({ nome, quantidade });
    }
    verificarEstoqueBaixo();
}

function removerProduto(nome, quantidade) {
    const produto = estoque.find(p => p.nome === nome);
    if (produto) {
        if (produto.quantidade >= quantidade) {
            produto.quantidade -= quantidade;
            if (produto.quantidade < 0) produto.quantidade = 0;
        } else {
            console.log(`Não há quantidade suficiente de ${nome} para remover.`);
        }
        verificarEstoqueBaixo();
    } else {
        console.log(`Produto ${nome} não encontrado no estoque.`);
    }
}

function verificarEstoqueBaixo() {
    estoque.forEach(produto => {
        if (produto.quantidade < 5) {
            console.log(`Alerta: ${produto.nome} está com pouco estoque (${produto.quantidade} unidades)!`);
        }
    });
}

exibirEstoque();

adicionarProduto("Produto A", 5);
removerProduto("Produto C", 2);
adicionarProduto("Produto E", 7);
removerProduto("Produto B", 10);

exibirEstoque();
