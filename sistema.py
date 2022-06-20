#Definindo as funções:

firstName = input('\nOlá! Antes de começarmos, poderia nos informar o seu primeiro nome? \n') 
#lastName = input('Qual seu sobrenome? ')
NumCont = '+55 ' + input('Insira seu número para contato (00)00000-0000: ')


def PitchSecurity():
    while True:
        opcao = str(input(f'Sr(a) {firstName}, escolha um dos serviços abaixo: \n       SERVIÇOS:       \n [1] - Dúvidas \n [2] - Consultas \n [3] - Informações \n [4] - Contatos \n [5] - Sair\n'))
        if opcao == '1':
            duvidas()
        elif opcao == '2':
            consultas()
        elif opcao == '3':
            informacoes()
        elif opcao == '4':
            contato()
        elif opcao == '5':
            print("A Pitch Security agradeçe o seu acesso! Volte sempre que precisar!")
            exit()
        else:
            print('Escolha uma das opções informadas:\n')

def duvidas():
    while True:
        voltar_inicio = False
        tipo = input('Escolha sobre qual modalidade de seguros você gostaria de tirar dúvidas: \n [1] - Auto: \n [2] - Celular: \n [3] - Sair\n')
        if tipo == '1':
            while True:
                duvida = input('Escolha uma das opções: \n --> Para Auto: \n [1] - Em quais situações há a cobertura? \n [2] - Quais as formas de pagamento? \n [3] - Quais veículos são aceitos?:  \n [4] - Retornar ao início\n ')
                if duvida == '1':
                    print('Manutenção: vidro, parachoque, lataria, pintura. Desastres naturais: alagamento, chuva de granizo, queda de árvore. Roubo e furto!')
                    voltar_inicio = sair_ou_voltar()
                    break
                elif duvida == '2': #Quais as formas de pagamento?:
                    print('Pix, Cartão de Crédito em até 12x e débito em conta corrente!')
                    voltar_inicio = sair_ou_voltar()
                    break
                elif duvida == '3': #Quais veículos são aceitos?:
                    print('Veículos de passeio, utilitários e caminhonetes!')
                    voltar_inicio = sair_ou_voltar()
                    break
                elif duvida == '4':
                    voltar_inicio = True
                    break
                else:
                    print('Escolha uma das opções informadas:\n')
        elif tipo == '2':
            while True:
                duvida = input('Escolha uma das opções: \n--> Para Celular: \n [1] - Em quais situações há a cobertura? \n [2] - Quais as formas de pagamento? \n [3] - Como localizar o IMEI do celular?: \n [4] - Retornar ao início\n')
                if duvida == '1': #'Em quais situações há a cobertura?:':
                    print('Manutenção: Tela quebrada, bateria e carregador. Roubo e furto!')
                    voltar_inicio = sair_ou_voltar()
                    break
                elif duvida == '2':#'Quais as formas de pagamento?':
                    print('Pix, Cartão de Crédito em até 12x e débito em conta corrente!')
                    voltar_inicio = sair_ou_voltar()
                    break
                elif duvida == '3': #'Como localizar o IMEI do celular?':
                    print('Para ter acesso ao IMEI do seu smartphone, basta digitar o código *#06# em seu teclado. O número aparecerá na tela')
                    voltar_inicio = sair_ou_voltar()
                    break
                elif duvida == '4':
                    voltar_inicio = True
                    break
                else:
                    print('Escolha uma das opções informadas:\n')
        elif tipo == '3':
            print("A Pitch Security agradeçe o seu acesso! Volte sempre que precisar!")
            exit()
        else:
            print('Escolha uma das opções informadas:\n')
        if voltar_inicio == True:
            break

def sair_ou_voltar():
    duvida = input(f'\nSr(a) {firstName}, sua solicitação foi atendida?:\n[1] - Sim \n[2] - Não \n')
    if duvida == '2':
        print('O problema não foi resolvido? Não se preocupe. É só ligar para ouvidoria: seg-sex, das 8h-18h: 0800-0001. E fale com um dos nossos atendentes.') 
    elif duvida == '1':
        print('A Pitch Security agradeçe o seu acesso! Volte sempre que precisar!')
    voltar_sair = input('Escolha uma opção: \n[1] - Retornar ao menu inicial \n[2] - Sair \n')
    if voltar_sair == '2':
        print("A Pitch Security agradeçe o seu acesso! Volte sempre que precisar!")
        exit()
    elif voltar_sair == '1': 
        return True 

def contato():
    while True:
        voltar = False
        tipo = input('Escolha sobre qual modalidade de seguros você gostaria de entrar em contato: \n [1] - Auto: \n [2] - Celular: \n [3] - Sair\n')
        if tipo == '1':
            while True:
                resposta = input('Contatos: \n [1] - Seguradora: \n [2] - Meu Corretor: \n [3] - Oficinas Credenciadas: \n [4] - Informar Sinistro \n[5] - Retornar ao início')
                if resposta =='1':
                    print(f'\nSr(a) {firstName} segue, informações: \nPitch Security: 0800-0001 \n  Mandamos essas informações em um SMS para {NumCont} ')
                    voltar = sair_ou_voltar()
                    break
                elif resposta =='2':
                    print(f'\nSr(a) {firstName} segue, informações: \nSergio Antunes: (41) 99999-5555 \n Mandamos essas informações em um SMS para {NumCont} ')
                    voltar = sair_ou_voltar()
                    break
                elif resposta =='3':
                    print(f'\nSr(a) {firstName} segue, informações: \nCar neves: (41)99999-4444 \n Concerto Vip: (41)99999-3333 \n VapVupt: (41)99999-6666 \n Mandamos essas informações em um SMS para {NumCont} ')
                    voltar = sair_ou_voltar()
                    break
                elif resposta =='4':
                    print(f'\n Sr(a) {firstName} segue, informações: \n Sinistros: (41)99888-5225 \n Consultar sinistro: (41)99777-5445 \n Mandamos essas informações em um SMS para {NumCont} ')
                    voltar = sair_ou_voltar()
                    break
                elif resposta == '5':
                    voltar = True
                    break
                else:
                    print('Escolha uma das opções informadas:\n')
        elif tipo == '2':
            while True:
                resposta = input('Contatos: \n [1] - Seguradora: \n [2] - Meu Corretor: \n [3] - Assistencias Credenciadas: \n [4] - Informar Sinistro \n[5] - Retornar ao início\n')
                if resposta =='1':
                    print(f'\n Sr(a) {firstName} segue, informações: \n Pitch Security: 0800-0001 \n Mandamos essas informações em um SMS para {NumCont}')
                    voltar = sair_ou_voltar()
                    break
                elif resposta =='2':
                    print(f'\n Sr(a) {firstName} segue, informações: \n Meu Corretor: (41)99999-5555 \n Mandamos essas informações em um SNS para {NumCont}')
                    voltar = sair_ou_voltar()
                    break
                elif resposta =='3':
                    print(f'\nSr(a) {firstName} segue, informações: \n Assistência tec: (41)99999-4444 \n Assistência Vip: (41)99999-3333 \n MariAssistência: (41)98888-5555 \n Mandamos essas informações em um SMS para {NumCont} ')
                    voltar = sair_ou_voltar()
                    break
                elif resposta =='4':
                    print(f'\n Sr(a) {firstName} segue, informações: \n Sinistros: (41)99888-5225 \n Consultar sinistro: (41)99777-5445 \n Mandamos essas informações em um SMS para {NumCont} ')
                    voltar = sair_ou_voltar()
                    break
                elif resposta == '5':
                    voltar = True
                    break
                else:
                    print('Escolha uma das opções informadas:\n')
        elif tipo == '3':
            print("A Pitch Security agradeçe o seu acesso! Volte sempre que precisar!")
            exit()
        else:
            print('Escolha uma das opções informadas:\n')
        if voltar == True:
            break 

def consultas():
    while True:
        voltar = False
        tipo = input('Escolha sobre qual modalidade de seguros você gostaria de entrar em contato: \n [1] - Auto: \n [2] - Celular: \n [3] - Sair\n')
        if tipo == '1':
            while True:
                resposta = input('Consultas: \n [1] - Consultar apólice de seguros \n [2] - Consultar última fatura \n [3] - Consultar informe de rendimento \n [4] - Retornar ao início\n ')
                if resposta =='1':
                    email = input("\nEscreva seu e-mail:\n")
                    print(f'\n{firstName}, apólice de seguros foi enviado para o e-mail {email}.\n ')
                    voltar = sair_ou_voltar()
                    break
                elif resposta =='2':
                    email = input("\nEscreva seu e-mail:\n")
                    print(f'\nSr(a) {firstName}, última fatura foi enviada para o e-mail {email}.\n')
                    voltar = sair_ou_voltar()
                    break
                elif resposta =='3':
                    email = input("\nEscreva seu e-mail:\n")
                    print(f'\nSr(a) {firstName}, o informe de rendimento foi enviado para o e-mail {email}.\n')
                    voltar = sair_ou_voltar()
                    break
                elif resposta =='4':
                    voltar = True
                    break
                else:
                    print('Escolha uma das opções informadas:\n')
        elif tipo == '2':
            while True:
                resposta = input('Consultas: \n [1] - Consultar apólice de seguros \n [2] - Consultar última fatura \n [3] - Consultar informe de rendimento \n [4] - Retornar ao início\n ')
                if resposta =='1':
                    email = input("\nEscreva seu e-mail:\n")
                    print(f'\nSr(a) {firstName}, apólice de seguros foi enviado para o e-mail {email}.\n ')
                    voltar = sair_ou_voltar()
                    break
                elif resposta =='2':
                    email = input("\nEscreva seu e-mail:\n")
                    print(f'\nSr(a) {firstName}, última fatura foi enviada para o e-mail {email}.\n')
                    voltar = sair_ou_voltar()
                    break
                elif resposta =='3':
                    email = input("\nEscreva seu e-mail:\n")
                    print(f'\nSr(a) {firstName}, o informe de rendimento foi enviado para o e-mail {email}.\n')
                    voltar = sair_ou_voltar()
                    break
                elif resposta =='4':
                    voltar = True
                    break
                else:
                    print('Escolha uma das opções informadas:\n')
        elif tipo == '3':
            print("A Pitch Security agradeçe o seu acesso! Volte sempre que precisar!")
            exit()
        else:
            print(f'Por gentileza Sr(a) {firstName} escolha uma modalidade de consultas correta!')
        if voltar == True:
            break

def informacoes():
    while True:
        voltar = False
        tipo = str(input('\nEscolha sobre qual a informação que deseja ter:\n\n[1] - Quem somos:\n[2] - Missão, visão e valores: \n[3] - Sair \n\n'))
        if tipo == '1':
            while True:
                resp = input('Escolha uma das opções: \n\n [1] - Sobre a Pitch Security \n [2] - Nossa essência \n [3] - Nossa história \n [4] - Retornar ao início \n\n')
                if resp == '1':
                    print(f'\n{firstName}, a Empresa\n\nA Pitch Security é uma seguradora que respeita você e seus mais de 100000 clientes. Contamos com investidores nacionais como Zvest e Xvest. A Pitch Security é mais que uma seguradora, é um ecossistema de soluções de serviços de proteção com tecnologia embarcada, para melhorar e facilitar a experiência do cliente.\n')
                    voltar = sair_ou_voltar()
                    break
                elif resp == '2':
                    print(f'\nEssência\n\nA Pitch Security Seguradora oferece aos brasileiros proteção com pagamento mensal, zelamos pelo o que é seu de uma forma descomplicada, entregamos um tratamento personalizado e com reembolsos instântaneos. Tudo isso sem burocracia ou palavras difíceis. Queremos fornecer a melhor experiência sempre respeitando a individualidade de cada um, incluindo você, {firstName}.\n')
                    voltar = sair_ou_voltar()
                    break
                elif resp == '3':
                    print('\nUm pouco da nossa história\n\nA Pitch Security Seguradora iniciou suas atividades em 1945, com apenas 50 funcionários. Atualmente, é composta por 27 empresas com quase 14 mil funcionários. Reconhecida como uma das maiores seguradoras do País, a Pitch Security Seguradora hoje é mais que uma seguradora, é um ecossistema de soluções de serviços de proteção com tecnologia embarcada, para melhorar e facilitar a experiência do cliente. Com mais de 70 anos de mercado, a atuação da companhia se concentra hoje em dois pilares estratégicos de negócio: Seguros Auto e Seguros Celular.\n')
                    voltar = sair_ou_voltar()
                    break
                elif resp =='4':
                    voltar = True
                    break
                else:
                    print('Escolha uma das opções informadas:\n')
        elif tipo == '2':
            while True:
                resp = input('\nEscolha uma das opções:\n\n [1] - Missão \n [2] - Visão \n [3] - Valores \n [4] - Retornar ao início \n\n')
                if resp == '1':
                    print('\nMissão\n\nNosso papel no mundo é oferecer as melhores soluções para nossos clientes, colaborando para que o planeta seja um lugar melhor hoje e para as futuras gerações. Nossa missão é assumir riscos e prestar serviços, por meio de um atendimento familiar que supere expectativas, garantindo agilidade a custos competitivos com responsabilidade social e ambiental.\n')
                    voltar = sair_ou_voltar()
                    break
                elif resp == '2':
                    print('\nVisão\n\nNossos Valores | A Base de Tudo O Que Fazemos\n\nIntegridad\n\nSomos honestos, éticos e fazemos a coisa certa.\n\nRespeito\n\nTratamos uns aos outros com respeito e somos respeitados pela maneira que agimos.\n\nResponsabilidade\n\nSomos responsáveis por nosso trabalho, pelo nosso time e por contribuir para o sucesso de nossa empresa.\n\nExcelência\n\nSomos determinados por atingir altos níveis de desempenho – para nós mesmos e para nossos clientes, investidores e comunidades.\n')
                    voltar = sair_ou_voltar()
                    break
                elif resp == '3':
                    print('\nValores\n\nDiversidade, Inclusão, Equidade e Pertencimento\n\nEstamos comprometidos em ser uma empresa na qual todas as pessoas pertencem, de forma genuína, sendo respeitadas e valorizadas, podendo fazer o seu melhor, e onde a diversidade, a inclusão e a equidade são vantagens competitivas.\n\nNossa meta, até 2030 é aumentar a representatividade Feminina, de Pessoas Negras, de Pessoas com Deficiência e LGBTQI+, anualmente, nos Quadros administrativos e operacionais, incluindo a liderança. Por isso, 80% dos shortlists de seleções externas serão diversos, sendo Responsabilidade da liderança analisar e admitir novos talentos que promovam a diversidade em suas áreas.\n')
                    voltar = sair_ou_voltar()
                    break
                elif resp =='4':
                    voltar = True
                    break
                else:
                    print('Escolha uma das opções informadas:\n')
        elif tipo == '3':
            print("A Pitch Security agradeçe o seu acesso! Volte sempre que precisar!")
            exit()
        else:
            print(f'Por gentileza Sr(a) {firstName} escolha uma modalidade de consultas correta!')
        if voltar == True:
            break

PitchSecurity()
