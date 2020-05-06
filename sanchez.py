import random
import tweepy
from time import sleep

auth = tweepy.OAuthHandler(1, 2)  # API keys you get from twitter
auth.set_access_token(3, 4)
                      
api = tweepy.API(auth, wait_on_rate_limit=True)


def read_last_seen_id():
    with open('last_seen_id.txt', 'r') as f:
        return int(f.read().strip())


def store_last_seen_id(id):
    with open('last_seen_id.txt', 'w') as f:
        f.write(str(id))


possible_answers = ['ATEMSAO!!! SABADO TEM AULÃO DA PROFESSORA CLAUNDIA MAGONE! AQUI NO MURAL Ó !!!',
                    'maria eduarda BATMAN! JF!!!', 'PEDRO SCHWARZENEGGER !!! COORDENAÇÃO JF !!! ',
                    'Ó QUEM EU CHAMAR É PRA IR LA FALAR COM A CRIS! GABRIEL VENTORÉZZI, PEDRO YUNES, MATHEUS SILVERIO E PEDRO AUGUSTO COSTO!',
                    'leticia COSHTELI! JF !!!', 'MEU TIME PREFERIDO É O REMO!',
                    'GABRIELA ZANLUXI E ALEXANDRA MATEH JF!!!!!!!!!!!', 'O SCHWARZENEGGER EH O MEU FAVORITO!',
                    'QUEM AQUI É VENTOREZZI?? TU NAO TA INDO EM! TA SUBINDO METADE DA ESCADA E VOLTANDO!',
                    'BRENO BARROSO E GABRIEL ROSSETI A CRIS TA CHAMANDO VCS LA!',
                    'CADE O FRANCISCO PAULO E O ARTUR HENRIQUE HEIN???', 'ALEXANDE PERESONE COORDENACAO',
                    'um minutinho professora? Ó AMANHA É O DIA DE BATER FOTO EM!',
                    'JA JUSTIFICOU A TUA FALTA NO DIA 30/02?????????????????????????',
                    'JF AGORA']


while True:
    id = read_last_seen_id()
    mentions = api.mentions_timeline(id, tweet_mode='extended')
    try:
        store_last_seen_id(mentions[len(mentions) - 1].id)
    except IndexError:
        pass
    for mention in mentions:
        while True:
            print(f"\nfound {mention.full_text} {mention.id}")
            try:
                api.update_status(f"@{mention.user.screen_name} {possible_answers[random.randint(0, len(possible_answers) - 1)]}",
                              mention.id)
            except tweepy.TweepError:
                print("error, trying again")
                continue
            else:
                print("replied\n")
                break
        sleep(10)
    sleep(20)
