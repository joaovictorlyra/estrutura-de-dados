const vendasDiarias = [150, 200, 180, 220, 170, 160, 190];

function identificarMaiorEMenorVenda(vendas) {
    const maiorVenda = Math.max(...vendas);
    const menorVenda = Math.min(...vendas);
    return { maiorVenda, menorVenda };
}

function calcularMediaVendas(vendas) {
    const soma = vendas.reduce((acc, venda) => acc + venda, 0);
    return soma / vendas.length;
}

function exibirResultados(vendas) {
    const { maiorVenda, menorVenda } = identificarMaiorEMenorVenda(vendas);
    const mediaVendas = calcularMediaVendas(vendas);

    const diaMaiorVenda = vendas.indexOf(maiorVenda) + 1;
    const diaMenorVenda = vendas.indexOf(menorVenda) + 1;

    console.log(`Dia com maior número de vendas: Dia ${diaMaiorVenda} com ${maiorVenda} vendas`);
    console.log(`Dia com menor número de vendas: Dia ${diaMenorVenda} com ${menorVenda} vendas`);
    console.log(`Média de vendas diárias: ${mediaVendas.toFixed(2)}`);
}

exibirResultados(vendasDiarias);
