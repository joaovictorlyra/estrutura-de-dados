const alunos = [
    {
        nome: "João",
        notas: [8, 8, 10, 5, 7]
    },
    {
        nome: "Kaio",
        notas: [7, 8, 9, 10 ,2]
    },
    {
        nome: "William",
        notas: [10, 9 , 5, 8, 9]
    }
];

function calculaMedia(notas) {
    const soma = notas.reduce((acc, nota) => acc + nota, 0);
    return soma / notas.length;
}

function precisaRecuperacao(notas) {
    return notas.some(nota => nota < 7);
}

function encontraMaiorMenotNota(notas) {
    const maiorNota = Math.max(...notas);
    const menorNota = Math.min(...notas);
    return { maiorNota, menorNota};
}

alunos.forEach(aluno => {
    const media = calculaMedia(aluno.notas);
    const recuperacao = precisaRecuperacao(aluno.notas);
    const { maiorNota, menorNota} = encontraMaiorMenotNota(aluno.notas);

    console.log(`Aluno: ${aluno.nome}`);
    console.log(`Notas: ${aluno.notas}`);
    console.log(`Média: ${media.toFixed(2)}`);
    console.log(`Maior nota: ${maiorNota}`);
    console.log(`Menor nota: ${menorNota}`);
    console.log(`Precisa de recuperação? ${aluno.recuperacao ? "Sim" : "Não"}`);
    console.log('-----')
});
