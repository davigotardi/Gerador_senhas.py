import string
import random

def gerar_senha(tamanho=12):
    if tamanho < 4:
        raise ValueError("O tamanho da senha deve ser no mínimo 4")

    caracteres = {
        'maiusculas': string.ascii_uppercase,
        'minusculas': string.ascii_lowercase,
        'digitos': string.digits,
        'pontuacao': string.punctuation
    }

    # Garante que a senha tenha pelo menos um caractere de cada tipo
    senha = [
        random.choice(caracteres['maiusculas']),
        random.choice(caracteres['minusculas']),
        random.choice(caracteres['digitos']),
        random.choice(caracteres['pontuacao'])
    ]

    # Preenche o resto da senha com caracteres aleatórios
    todos_caracteres = ''.join(caracteres.values())
    senha += random.sample(todos_caracteres, tamanho - 4)

    # Embaralha os caracteres para evitar padrão previsível
    random.shuffle(senha)

    return ''.join(senha)

# Solicita ao usuário o comprimento da senha desejada
tamanho_senha = int(input("Digite o comprimento da senha (mínimo 4): "))
senha = gerar_senha(tamanho_senha)
print("Senha gerada:", senha)
