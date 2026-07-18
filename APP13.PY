# funçao para calcular a frequencia 
def calcular_frequencia(total_aulas, presencas);
# calcular a frequencia em porcentrual
frequencia = (presencas / total_aulas) * 100
return frequencia

# funçao para incluir a presença dos alunos
def incluir_presenca():
alunos = {}
total_aulas = int(input("digite o numero total de aulas: "))
while true:
nome = input("digite o nome do aulo (ou 'fim' para terminar): ")
if nome.lower() == 'fim':break
presenças = int(input(f"digite o numero de aulas presentes de {nome}:"))
alunos[nome] = presencas

return alunos, total_aulas

# funçao principal para processar a frequencia
def calcular_frequencia_alunos():
alunos, total_aulas = incluir_presenca()

# exibindo a frequencia de cada alunos
for aluno, presenças in alunos.items():
frequencia = calcular_frequencia(total_aulas, presencas)
print(f' frequencia de {aluno}: {frequencia: .2f}%')

# chama a funcao principal 
calcular_frequencia-alunos()
alexandre