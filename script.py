
# Projeto: Filtragem de Notas de Alunos com Python

alunos = [
    {"nome": "Carlos", "nota": 8.5},
    {"nome": "Ana", "nota": 6.0},
    {"nome": "Pedro", "nota": 9.0},
    {"nome": "Maria", "nota": 5.5},
    {"nome": "João", "nota": 7.0}
]

print("=== SISTEMA DE NOTAS DOS ALUNOS ===")

print("\nAlunos aprovados:")
for aluno in alunos:
    if aluno["nota"] >= 7:
        print(f'{aluno["nome"]} - Nota: {aluno["nota"]}')

print("\nAlunos reprovados:")
for aluno in alunos:
    if aluno["nota"] < 7:
        print(f'{aluno["nome"]} - Nota: {aluno["nota"]}')

print("\n=== FIM DO PROGRAMA ===")
