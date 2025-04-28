#TESTE
print ("a");
print ("b" ,"b");
print ("c","c","c");

# Receber dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calcular a média
media = (numero1 + numero2) / 2

# Imprimir a média
print(f"A média dos dois números é:{media}")

# Receber um número do usuário 
numero = int(input(f"Digite um número: "))  

# Verificar se o número é par ou ímpar  
if numero % 2 == 0: 
    print(f"O número {numero} é par.") 
else: 
    print(f"O número {numero} é ímpar.")

#alterando valores das variáveis
nome= "Maria";
idade = 25;
altura = 1.60;
eh_estudante= False;

#imprimindo novos valores
print(f"Nome atualizado: ", nome);
print(f"idade atualizada: ", idade);
print(f"altura atualizada: ", altura);
print(f"É estudante? (atualizado)", eh_estudante);

#receber mensagem do usuário
mensagem = input("Digite uma mensagem: ");

#imprimir a mensagem original 
print(f"você digitou: {mensagem}");

#converter a mensagem para caixa alta e imprimir
mensagem_caixa_alta= mensagem.upper();
print(f"Mensagem em caixa alta: {mensagem_caixa_alta}");

# Imagine que um desenvolvedor deseja escrever um código que faça com que as seguintes frases sejam impressas no console do computador: Como seria o código que ele deveria escrever para alcançar o seu objetivo?



#Crie um programa em Python que ajude um usuário a calcular a quantidade total de armazenamento disponível em seu computador, somando: 
# O espaço do HD (em GB) 
# O espaço do SSD (em GB) 
# A quantidade de memória RAM (em GB), mesmo que ela não seja de armazenamento permanente, apenas para exibir no final. 
# O programa deve solicitar que o usuário digite esses valores, depois mostrar: 
# O total de armazenamento HD + SSD 
# Um resumo exibindo os três valores (HD, SSD, RAM) 


frase = input("Digite sua frase: ");
print(f"sua frase é: {frase}");



hd = int(input("Digite o tamanho do HD (em GB): "))
ssd = int(input("Digite o tamanho do SSD (em GB): "))
ram = int(input("Digite a quantidade de memória RAM (em GB): "))

total=hd+ssd;

print(f"Armazenamento total (HD + SSD): {total} GB");
print(f"Resumo:");
print(f"HD: {hd} GB"); 
print(f"SSD: {ssd} GB"); 
print(f"RAM: {ram} GB"); 

