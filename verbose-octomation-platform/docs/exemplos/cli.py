import argparse

parser = argparse.ArgumentParser(
    description='Criação de um CLI',
)

parser.add_argument('-c', '-d', dest='c', help='Ajuda no argumento c')
parser.add_argument('-e', help='Ajuda no argumento e')

args = parser.parse_args()

if not args.c:
    raise ValueError('Necessário digitar a opção -c')

print(args.c)
