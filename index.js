// Desafio com Interface (nível iniciante — HTML + JavaScript) 
// Tema: Entrada, processamento e saída usando a lógica do computador em uma página web 
// Objetivo: Criar uma calculadora simples que recebe o ano de nascimento e retorna a idade atual. 
function calcularIdade(){
    const anoNascimento= document.getElementById("ano").value;
    const anoAtual= new Date().getFullYear();
    const idade= anoAtual - anoNascimento;

    document.getElementById("resultado").innerText=
    "Sua idade é : " + idade + " anos.";
}
