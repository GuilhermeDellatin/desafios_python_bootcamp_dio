import functools
from datetime import datetime

# Objetivo
#
# Modificar o atual decorador de log, que imprime informações no console, para que ele
# salve essas informações em um arquivo de log, possibilitando uma revisão mais fácil
# e uma análise mais detalhada das operações dos usuários.

# Requisitos
#
# O decorador deve registrar o seguinte para cada chamada de função:
# 1. Data e hora atuais.
# 2. Nome da função.
# 3. Argumentos da função.
# 4. Valor retornado pela função.
# 5. O arquivo de log deve ser chamado log.txt.
# 6. Se o arquivo log.txt já existir, os novos devem ser adicionados ao final do arquivo.
# 7. Cada entrada de log deve estar em uma nova linha.

def log_transacao(func):
    """
    Decorador que registra data/hora, função, argumentos e retorno em log.txt.
    """
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        retorno = func(*args, **kwargs)
        registro = (
            f"{datetime.now():%Y-%m-%d %H:%M:%S} | "
            f"{func.__name__} | "
            f"args={args!r} | kwargs={kwargs!r} | retorno={retorno!r}"
        )

        try:
            with open("log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(registro + "\n")
        except OSError as err:
            # Mantém o programa funcional mesmo que o log falhe.
            print(f"[LOG] Falha ao registrar transação: {err}")

        return retorno

    return envelope