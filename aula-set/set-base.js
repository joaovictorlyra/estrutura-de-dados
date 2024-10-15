function Set() {
    var items = {}

    this.add = function(value) {
        if(!this.has(value)) {
            items[value] = value
            return true
        }
        return false
    }

    this.delete = function(value) {
        if(this.has(value)) {
            delete items[value]
            return true
        }
        return false
    }

    this.has = function(value) {
        return items.hasOwnProperty(value)
    }

    this.clear = function() {
        items = {}
    }

    this.size = function() {
        return Object.keys(items).length
    }

    this.values = function() {
        var values = [],
        keys = Object.keys(items)
        for(var i = 0; i < keys.length; i++) {
            values.push(items[keys[i]])
        }
        return values
    }

    this.union = function(otherSet) { // 1º união 
        var unionSet = new Set(),
        values = this.values()

        for(var i = 0; i < values.length; i++) {
            unionSet.add(values[i])
        }

        values = otherSet.values()

        for(var i = 0; i < values.length; i++) {
            unionSet.add(values[i])
        }

        return unionSet
    }

    this.intersection = function(otherSet) { // 2º passo
        var intersectionSet = new Set(),
        values = this.values()

        for(var i = 0; i < values.length; i++) {
            if(otherSet.has(values[i])) {
                intersectionSet.add(values[i])
            }
        }
        return intersectionSet
    }

    this.difference = function(otherSet) { // 3º passo - diferença 
        var differenceSet = new Set(),
        values = this.values()

        for(var i = 0; i < values.length; i++) {
            if(!otherSet.has(values[i])) {
                differenceSet.add(values[i])
            }
        }
        return differenceSet
    }

    this.subset = function(otherSet) { // 4º passo 
        if(this.size() > otherSet.size()) {
            return false
        } else {
            var values = this.values()

            for(var i = 0; i < values.length; i++) {
                if(!otherSet.has(values[i])) {
                    return false
                }
            }
            return true
        }
    }
}


let participantes = new Set();

participantes.add("João");
participantes.add("Kaio");
participantes.add("William");
participantes.add("Wagner");

participantes.delete("Wagner");

console.log(participantes.has("João"));

console.log(participantes.values());


// Questão 2:
class ControleAcesso {
    constructor() {
        this.usuarios = new Set(); // Usamos um Set para garantir que não haja usuários duplicados
    }

    adicionarUsuario(usuario) {
        if (this.usuarios.has(usuario)) {
            console.log(`Usuário ${usuario} já tem acesso.`);
        } else {
            this.usuarios.add(usuario);
            console.log(`Usuário ${usuario} adicionado com sucesso.`);
        }
    }

    removerUsuario(usuario) {
        if (this.usuarios.has(usuario)) {
            this.usuarios.delete(usuario);
            console.log(`Usuário ${usuario} removido com sucesso.`);
        } else {
            console.log(`Usuário ${usuario} não encontrado.`);
        }
    }

    verificarAcesso(usuario) {
        if (this.usuarios.has(usuario)) {
            console.log(`Usuário ${usuario} tem acesso.`);
            return true;
        } else {
            console.log(`Usuário ${usuario} não tem acesso.`);
            return false;
        }
    }
}


// Testes
const sistema = new ControleAcesso();

// Testando a adição de usuários
sistema.adicionarUsuario("Alice"); // Usuário Alice adicionado com sucesso.
sistema.adicionarUsuario("Bob");   // Usuário Bob adicionado com sucesso.
sistema.adicionarUsuario("Alice"); // Usuário Alice já tem acesso.

// Testando a verificação de acesso
sistema.verificarAcesso("Alice"); // Usuário Alice tem acesso.
sistema.verificarAcesso("Bob");   // Usuário Bob tem acesso.
sistema.verificarAcesso("Charlie"); // Usuário Charlie não tem acesso.

// Testando a remoção de usuários
sistema.removerUsuario("Bob");     // Usuário Bob removido com sucesso.
sistema.verificarAcesso("Bob");    // Usuário Bob não tem acesso.

// Tentando remover um usuário que não existe
sistema.removerUsuario("Charlie"); // Usuário Charlie não encontrado.