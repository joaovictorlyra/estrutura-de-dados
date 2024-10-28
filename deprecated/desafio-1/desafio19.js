let idades = [15, 22, 18, 30];
let index = -1;

for (let i = 0; i< idades.length; i++) {
    if (idades[i] >= 21) {
        index = i;
        break;
    }
}

console.log("A primeira idade maior que 21 é :" + index);