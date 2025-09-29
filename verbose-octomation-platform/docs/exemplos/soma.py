from system.config.config_file import DIRETORIO_RAIZ


def soma(valor1: int, valor2: int) -> int:
    return sum([valor1, valor2])


FILE = __file__.replace(f'{(DIRETORIO_RAIZ / __package__)}\\', '')
FILE = FILE.replace('.py', '')

print(FILE)
print(__name__)


# if __name__ == f'{__package__}.{FILE}':
resultado_soma: int = soma(
    int(input('Digite o primeiro valor para soma:')),
    int(input('Digite o segundo valor para a soma:')),
)

print(f'A soma dos valores é {resultado_soma}.')
