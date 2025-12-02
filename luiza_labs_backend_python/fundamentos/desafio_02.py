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