# Importar o 'choice' para randomizar as escolhas do computador do módulo 'random'
from random import choice

# Criar uma variavel com o valor 0
opcao = 0

#Mensagem de boas vindas
print('-' * 30)
print('Bem vindo ao Joquempô!')
print('-' * 30)

#Loop principal do jogo
while True:

    # Criação de dicionarios para o movimento (indicando qual jogada ganha de qual) e o placar
    movimentos = {'PEDRA': 'TESOURA', 'PAPEL': 'PEDRA', 'TESOURA': 'PAPEL'}
    placar = {'Jogador 1': 0, 'Jogador 2': 0}

    #Solicita a modalidade e armazena na variavel 'modalidade'
    modalidade = input('HH: Humano x Humano\n'
                        'HC: Humano x Computador\n'
                        'CC: Computador x Computador\n'
                        'Digite a modalidade desejada: ').upper().strip()

    #Verifica se a modalidade é válida para sair do loop
    if modalidade in ['HH', 'HC', 'CC']:
        break
    else:
        print('Modo de jogo inválido. Tente novamente.')

#Loop do jogo
while opcao == 0:
    print('O jogo iniciou!')

#Verifica a modalidade escolhida e pede as jogadas
    if modalidade == 'HH':
        j1mov = input('Jogador 1: PEDRA, PAPEL ou TESOURA? ').upper().strip()
        j2mov = input('Jogador 2: PEDRA, PAPEL ou TESOURA? ').upper().strip()
    elif modalidade == 'HC':
        j1mov = input('Jogador: PEDRA, PAPEL ou TESOURA? ').upper().strip()
        j2mov = choice(['PEDRA', 'PAPEL', 'TESOURA'])
        print('O computador escolheu aleatoriamente {}!'.format(j2mov))
    else:
        j1mov = choice(['PEDRA', 'PAPEL', 'TESOURA'])
        j2mov = choice(['PEDRA', 'PAPEL', 'TESOURA'])
        print()
        print('O Bot 1 escolheu {}\n'
              'O Bot 2 escolheu {}'.format(j1mov, j2mov))

#Verifica se teve empate ou qual jogador ganhou a rodada
    if j1mov == j2mov:
        print()
        print('Rodada empatada!')

    elif movimentos[j1mov] == j2mov:
        print()
        print('O vencedor é o Jogador 1!')
        placar['Jogador 1'] += 1
    else:
        print()
        print('O vencedor é o Jogador 2!')
        placar['Jogador 2'] += 1

#Loop para jogar novamente
    while True:
        print('=' * 50)
        novamente = input('Deseja jogar novamente? (S/N)').upper().strip()

        if novamente == 'S':
            break
        elif novamente == 'N':
            #Definir a variavel = 1, para sair do loop principal
            opcao = 1
            print('=' * 50)
            print('\n O placar final é:')
            print('Jogador 1: {}'.format(placar['Jogador 1']))
            print('Jogador 2: {}'.format(placar['Jogador 2']))
            print('Obrigado por jogar o Joquempô, até a próxima!')
            print('ENCERRANDO...\n')
            print('=' * 50)
            break
        else:
            print('Ocorreu um erro. Tente novamente!\n')
