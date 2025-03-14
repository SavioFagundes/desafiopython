INDICE = 13
SOMA = sum(range(1, INDICE + 1))
print(f'1) O valor final de SOMA é: {SOMA}')
def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero or numero == 0
num = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))
print(f'2) O número {num} {"pertence" if pertence_fibonacci(num) else "NÃO pertence"} à sequência de Fibonacci.')
import json
dados_json = '{"faturamento": [10, 20, 0, 30, 40, 0, 50, 60, 0, 10, 5, 80, 0, 90]}'
faturamento = [dia for dia in json.loads(dados_json)["faturamento"] if dia > 0]
menor, maior = min(faturamento), max(faturamento)
media = sum(faturamento) / len(faturamento)
dias_acima_media = sum(1 for dia in faturamento if dia > media)
print(f'3) Menor faturamento: {menor}\n3) Maior faturamento: {maior}\n3) Dias com faturamento acima da média: {dias_acima_media}')
faturamento_estados = {
    "SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53
}
total = sum(faturamento_estados.values())
percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento_estados.items()}
print("4) Percentual de representatividade por estado:")
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
def inverter_string(s):
    return s[::-1]
string = input("Digite uma string para inverter: ")
print(f'5) String invertida: {inverter_string(string)}')
