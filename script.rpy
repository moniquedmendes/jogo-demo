# Personagens
define AyaPapaya = Character("Aya Papaya")
define BromeliaBromelia = Character("Bromelia Bromelia")
define SteveApple = Character("Steve Apple")
define LaranjaAnja = Character("Laranja")
define p = Character("Principal")
define Monstro = Character("Monstro")

default preferences.text_cps= 35
default score = 0

# Imagem Personagens
# Aya Papaya
image AyaPapayaAngry = im.Scale("images/Aya Papaya/Aya Papaiya Tatie Angry.png", 500, 800)
image AyaPapayaHappy = im.Scale("images/Aya Papaya/Aya Papaiya Tatie Happy.png", 500, 800)
image AyaPapayaN1 = im.Scale("images/Aya Papaya/Aya Papaiya Tatie normal 1.png", 500, 800)
image AyaPapayaN2 = im.Scale("images/Aya Papaya/Aya Papaiya Tatie normal 2.png", 500, 800)
image AyaPapayaSad = im.Scale("images/Aya Papaya/Aya Papaiya Tatie Sad.png", 500, 800)

# Bromelia Bromelia
image BromeliaBromeliaAngry = im.Scale("images/Bromelia Bromelia/Bromelia Bromelia Angry.png", 500, 800)
image BromeliaBromeliaN1 = im.Scale("images/Bromelia Bromelia/Bromelia Bromelia Normal.png", 500, 800)
image BromeliaBromeliaN2 = im.Scale("images/Bromelia Bromelia/Bromelia Bromelia Normal 2.png", 500, 800)
image BromeliaBromeliaSad = im.Scale("images/Bromelia Bromelia/Bromelia Bromelia Sad.png", 500, 800)

# Steve apple 
image SteveAppleSad = im.Scale("images/Steve apple/Steve apple sad.png", 500, 800)
image SteveAppleN1 = im.Scale("images/Steve apple/Steve apple normal.png", 500, 800)
image SteveAppleN2 = im.Scale("images/Steve apple/Steve apple normal 2.png", 500, 800)
image SteveAppleSmile = im.Scale("images/Steve apple/Steve apple smile.png", 500, 800)

# Laranja Anja
image LaranjaAnjaAngry = im.Scale("images/Laranja Anja/Laranja Anja Angry.png", 500, 800)
image LaranjaAnjaSmile = im.Scale("images/Laranja Anja/Aya Papaiya Tatie Smile.png", 500, 800)
image LaranjaAnjaN1 = im.Scale("images/Laranja Anja/Laranja Anja Normal.png", 500, 800)
image LaranjaAnjaN2 = im.Scale("images/Laranja Anja/Laranja Anja Normal 2.png", 500, 800)


define leftpos = Position(xalign=-0.1, yalign=1.0)
define midleftpos = Position(xalign=0.3, yalign=1.0)
define midrightpos = Position(xalign=0.7, yalign=1.0)
define rightpos = Position(xalign=1.1, yalign=1.0)

transform half_body:
    zoom 1.4        # aumenta o tamanho da personagem
    yalign -0.10      # desce um pouco (do tronco pra cima!!)



#------------------------------------------------------------------------------------------

#recepção 
#apartamento
#casa (lado de fora, noite)
#apartamento (base)

image bg_escritorio = im.Scale("images/Background/bg office.png", config.screen_width, config.screen_height)

image bg_ruaNoite = im.Scale("images/Background/City_Night.png", config.screen_width, config.screen_height)
image bg_ruaDia = im.Scale("images/Background/City_Morning.png", config.screen_width, config.screen_height)
image bg_ruaTarde = im.Scale("images/Background/City_Afternoon.png", config.screen_width, config.screen_height)
image bg_ruaChovendo = im.Scale("images/Background/City_Raining.png", config.screen_width, config.screen_height)


image bg_quartoDia = im.Scale("images/Background/Bedroom_Day.png", config.screen_width, config.screen_height)
image bg_quartoTarde = im.Scale("images/Background/Bedroom_Evening.png", config.screen_width, config.screen_height)
image bg_quartoNoite = im.Scale("images/Background/Bedroom_Night.png", config.screen_width, config.screen_height)
image bg_quartoNoiteDark = im.Scale("images/Background/Bedroom_Night_Dark.png", config.screen_width, config.screen_height)

image bg_parque_dia = im.Scale("images/Background/bg_parque_Dia.jpg", config.screen_width, config.screen_height)
image bg_parque_tarde = im.Scale("images/Background/bg_parque_Tarde.jpg", config.screen_width, config.screen_height)



image bg_casaDia = im.Scale("images/Background/Livingroom_Day.png", config.screen_width, config.screen_height)
image bg_casaNoite = im.Scale("images/Background/Livingroom_Night.png", config.screen_width, config.screen_height)
image bg_casaNoiteDark = im.Scale("images/Background/Livingroom_Dark.png", config.screen_width, config.screen_height)

image bg_cafeteria = im.Scale("images/Background/Restaurant_B.png", config.screen_width, config.screen_height)
image bg_cafeteriaFora = im.Scale("images/Background/bg_rua.jpg", config.screen_width, config.screen_height)

image bg_apartamentoDia = im.Scale("images/Background/Sitting_Room.png", config.screen_width, config.screen_height)
image bg_apartamentoNoite= im.Scale("images/Background/Sitting_Room_Dark.png", config.screen_width, config.screen_height)


# Sons adicionais
define sound_breath = "audio/respiracao.mp3"
define sound_rua = "audio/passos.mp3"
define sound_birds = "audio/passaros.mp3"
define sound_heartbeat = "audio/coracao.mp3"
# define sound_engasgo = "audio/engasgo.mp3"
#define sound_vento = "audio/vento_leve.mp3"
#define sound_voz_fundo = "audio/vozes_ao_fundo.mp3"

#define s_cafe = "audio/cafeteria_ambiente.mp3"
#define s_xicaras = "audio/xicaras_murmurios.mp3"
#define s_cafeteira = "audio/cafeteira.wav"
#define s_silencio_pesado = "audio/batida_coracao_lenta.mp3"

#define sound_engasgo = "audio/engasgo.mp3"
#define sound_vento = "audio/vento_leve.mp3"
#define sound_voz_fundo = "audio/vozes_ao_fundo.mp3"
#define sound_cafeteria = "audio/cafeteria.mp3"
#define sound_silence = "audio/silencio_tenso.mp3"
#define sound_chaleira = "audio/chaleira.mp3"

# Musica?
#define music_relax = "audio/musica_relaxante.mp3"

init python:
    import random, math

screen bubble_menu(opcoes):
    tag menu
    modal True
    zorder 100

    add Solid("#0003")  # fundo escurecido suave

    # Parâmetros
    default min_distance = 0.18  # distância mínima entre bolhas (0.0–1.0)
    default posicoes = []

    python:
        def distancia(a, b):
            return math.hypot(a[0] - b[0], a[1] - b[1])

        posicoes = []
        for i in range(len(opcoes)):
            tentativas = 0
            while True:
                x = random.uniform(0.15, 0.85)
                y = random.uniform(0.25, 0.75)
                if all(distancia((x, y), p) > min_distance for p in posicoes):
                    posicoes.append((x, y))
                    break
                tentativas += 1
                if tentativas > 50:  # fallback se o espaço estiver muito cheio
                    posicoes.append((x, y))
                    break

    # Criação das bolhas
    for i, (texto, acao) in enumerate(opcoes):
        $ x, y = posicoes[i]
        textbutton texto:
            action acao
            xalign x
            yalign y

            background Frame("gui/button/choice_idle_background2.png", 50, 50)
            hover_background Frame("gui/button/choice_hover_background2.png", 50, 50)

            text_color "#000"
            text_hover_color "#ffffcc"
            text_size 32
            text_align 0.5  # centraliza o texto dentro da bolha
            xminimum 380
            yminimum 90
            padding (25, 25)
            at bubble_float


transform bubble_float:
    alpha 0
    zoom 0.8
    linear 0.3 alpha 1.0 zoom 1.0
    easein 1.0 yoffset -10
    easeout 1.0 yoffset 0
    repeat


# The game starts here.

label start:

    scene bg_escritorio 
        
    "Em mais um dia normal de trabalho..."
    "O (principal) trabalha normalmente juntamente de colegas de trabalho em mais um entardecer de mais um dia."
    #sound effect de escritorio e um teclado barulhento

    p "Mais um dia cansativo..."
    #PRINCIPAL DESANIMADO

    "Sentado em sua cadeira, diante do monitor, a feição de desmotivado e pálido de Principal se torna evidente."
    "Ao refletir vagamente sobre aquele momento, o principal olha levemente ao seu redor, e percebe o desânimo também presente em seus colegas de trabalho no escritório."

    p "Pelo visto eles também..."
    #PRINCIPAL DESANIMADO

    "Principal retoma o foco em seu trabalho..."
    "Alguns minutos depois..."
    "20:00"
    #sound effect de relogio

    p "Hora de voltar para casa."
    "começa arrumar sua mesa, e preparar suas coisas para voltar para casa."

    jump cap1cena2

    #---------------------------------------------------------------------------------------------------
        #CAPITULO1 CENA2
    label cap1cena2:
    #image = RECEPCAO

    "Apos o Principal bater o ponto ele finalmente vai pra casa."

    jump cap1cena3

    #---------------------------------------------------------------------------------------------------
    #CAPITULO1 CENA3
    label cap1cena3:

    scene bg_ruaNoite

    "Ao caminho de casa diante do transito, as luzes refletem o ambiente e as pessoas que seguem de volta para suas casas."
    "Principal percebe que as pessoas ao seu redor parecem entristecidas... Desanimadas."
    #barulho de transito

    p "O que está acontecendo com o pessoal..."
    #Principal refletindo
    p "Se bem que estou parecido..."
    ##IMAGEM CASA (lado de fora, noite)
    p "Enfim em casa."



    #---------------------------------------------------------------------------------------------------
    #CAPITULO1 CENA4

    #IMAGEM CASA (lado de dentro "noite")
    scene bg_casaNoite

    "Ao chegar na casa, o Principal vai largando suas coisas pelo caminho e deixando sua casa bagunçada."
    #IMAGEM CORREDOR DE ENTRADA MEIO BAGUNCADA
    "Ao entrar na sala Princiapl senta-se em seu sofa."
    #IMAGEM SALA MEIO BAGUNCADA
    p "Que fome, vou pedir algo pra comer."
    "Ele pedi diversas comidas em seu aplicativo, encomenda lanches, fritas, sorvete e outras porcarias."
    "Apos alguns instantes... Seu pedido chega."
    "Ao voltar para a sala, Principal começa a devorar sua comida como se estivesse faminto. Mas quando percebe que a fome parece insaciável começa a chorar enquanto continua comendo..."
    "Isso aconteceu por causa da compulsão alimentar que o Principal desenvolveu por causa de seus conflitos emocionais recentes."

    jump cap1cena5

    #---------------------------------------------------------------------------------------------------
    #CAPITULO1 CENA5
    label cap1cena5:
    #IMAGEM CASA (lado de fora "dia")
    scene bg_quartoNoiteDark 

    "Depois de uma longa noite, o dia amanhece."
    scene bg_quartoDia with fade
    #IMAGEM CASA (lado de dentro "dia")
    "Principal começa a se arrumar para o trabalho, e quando vai ao banheiro se depara com algo inusitado."

    p "O QUE ESTA ACONTECENDO?!! O QUE É ISSO?! ISSO SOU EU?!"

    #IMAGEM PRINCIPAL SE OLHANDO NO ESPELHO

    "Quando está prestes a terminar de se arrumar, Principal se olha no espelho e percebe diversas escamas espalhas pelo seu corpo." 
    "Seu corpo começa a se transformar, seus dedos começam a virar batatas fritas, escamas de nugetts se espalham pelo seu pescoço."
    "Além de sua palidez aumentar por conta da pressão arterial."





    #Capitulo 2
    # Cena 1 — Quarto do Principal
    scene bg_quartoDia
    play sound sound_breath loop

    narrator "O desespero toma conta. Ele tenta arrancar os nuggets que brotam de sua pele, mas não importa quantas vezes retire, eles sempre voltam."
    
    p "Não!! Não para de sair!!! Ai! Ai!!!"
    p "Ahh, ahh...!!! Socorro! Alguém!!! Alguém me ajuda!!!"

    narrator "O ambiente está silencioso. Sua voz ecoa pela casa, apenas acompanhada pela respiração ofegante."
    narrator "Nenhuma resposta vem."

    stop sound

    narrator "Após alguns segundos, ele para e respira fundo, tentando se acalmar. Ele olha para o relógio..."
    
    p "Droga! Estou atrasado para o trabalho!"

    narrator "Ele corre até o guarda-roupa, pega um cachecol para cobrir as escamas de nuggets, coloca luvas para esconder os dedos em forma de batata frita, pega sua bolsa com papéis inacabados e sai apressado."

    # Cena 2 — Rua
    scene bg_ruaDia with fade
    play sound sound_rua loop

    narrator "Ele corre até a empresa, desviando das pessoas, sempre com a cabeça baixa para esconder o rosto."

    stop sound

    # Cena 3 — Parque (tarde)
    scene bg_parque_tarde with fade
    play sound sound_birds loop

    narrator "Já às 15h, no horário atrasado do almoço, o Principal se senta sozinho em um banco do parque."
    narrator "Ele abre um hambúrguer enorme, recheado de carne e molho, e começa a comer para matar a fome acumulada."
    narrator "Ao olhar para o lado, vê sua colega de trabalho sentada no banco ao lado. Ela devora donuts um atrás do outro, mordendo grandes pedaços e engolindo quase sem mastigar."

    narrator "Ele observa assustado, mas tenta ignorar e continua comendo."

    # Cena 4 — Parque (transformação da colega)
    # play sound sound_engasgo

    narrator "De repente, um barulho seco interrompe o momento."
    narrator "Sua colega começa a se engasgar, contraindo o corpo em dor."
    narrator "Ela perde a consciência e grita como um animal enfurecido, batendo com força no próprio peito, que incha de forma grotesca."
    narrator "Chocolate rosa começa a escorrer pelo seu rosto, confetes coloridos caem pelo chão."
    narrator "O corpo dela encolhe e se deforma."

    p "O que é isso?! O que está acontecendo???"

    # Cena 5 — Parque 
    # stop sound
    play sound sound_heartbeat loop

    narrator "Ele deixa o hambúrguer cair no chão. Suas mãos tremem."
    narrator "O medo o paralisa."
    narrator "As imagens da transformação que ele mesmo começou a sofrer pela manhã voltam à sua mente: os dedos em batata frita, as escamas de nuggets..."

    # (falta coisa)
    # show transformation_image

    stop sound
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #CAPITULO3 CENA1
    label cap3cena1:
    #IMAGEM PARQUE

    show BromeliaBromeliaAngry at leftpos, half_body
    BromeliaBromelia "Cuidado!!"
    #espectro de sombra

    "Principal se esbarra com uma jovem e ambos caem no chao."

    BromeliaBromelia "Fuja logo! Antes que voce se transforme em um Cronico!"

    p "Cronico?! O Que isso?!"

    hide BromeliaBromeliaAngry
    show BromeliaBromeliaN1 at leftpos, half_body
    show AyaPapayaN1 at rightpos, half_body
    AyaPapaya "Voce ja esta contaminado pela DECENT, se continuar desse jeito ira se transformar igual aquele monstro!"

    hide BromeliaBromeliaN1
    hide AyaPapayaN1
    "Sem entender Principal é puxado por um rapaz de oculos."

    show SteveAppleN1 at midleftpos, half_body
    SteveApple "Levanta!"

    Monstro "AAAAAAAAAAAAAARRRRGH"

    "Ao gritar  o monstro começa a jogar donuts em diversas pessoas, fazendo elas absorverem, ficando obesos, contraindo DECENT, para transforma-los em Cronicos."

    hide SteveAppleN1
    show BromeliaBromeliaAngry at leftpos, half_body
    show AyaPapayaN1 at rightpos, half_body
    BromeliaBromelia "Rapido! Precisamos fazer algo!"

    "Aiya e Bromelia se encaram e juntas golpeiam o Cronico."

    "Aiya e Bromelia" "HHAAAAAAAAAAAAAAAAAAAAAA."

    show LaranjaAnjaN1 at midrightpos, half_body
    "Logo em seguida chegam mais reforços, Laranja Anja reforça os ataques da equipe, juntos controlando os monstros no local."

    hide AyaPapayaN1
    hide BromeliaBromeliaAngry
    hide LaranjaAnjaN1
    #Capitulo 4
    # Cena 1 — Parque (após a batalha)
    #scene bg_parque_tarde_baguncado with fade
    #play wind sound_vento loop
    #play voz sound_voz_fundo loop

    
    narrator "O Principal respira com dificuldade, ainda atordoado pelo que viu. Ao seu redor, as quatro figuras misteriosas se aproximam."

    # Cena 2 — Diálogo inicial
    show AyaPapayaHappy at leftpos, half_body
    AyaPapaya "Você está bem?"

    show SteveAppleSmile at midleftpos, half_body
    SteveApple "Ele parece estar assustado..."

    show BromeliaBromeliaN2 at midrightpos, half_body
    BromeliaBromelia "Claro que está! Olha só o olhar de morto dele! kkkkkk"

    show LaranjaAnjaN1 at rightpos, half_body
    LaranjaAnja "Você quer um suco de laranja?"

    p "Ahhhhhhh... Não? Pera... O que aconteceu???"

    # Cena 3 — Revelação
    # Cena revelação
    
    BromeliaBromelia "Nós explicaremos! Somos fadas da Alimentação Saudável!"


    AyaPapaya "Estamos aqui para prevenir as DCNTs!"

    p "DCNT? O que é isso?"


    SteveApple "São Doenças Crônicas Não Transmissíveis. Aquelas doenças que você pode desenvolver comendo de forma não saudável."

    #---------------------------------------------------------------------------------------------------
    #CAPITULO4 CENA3
    label cap3cena3:
    #IMAGEM PARQUE (fim de tarde, cenário levemente bagunçado pela luta)

    # Mostrando todos os personagens já posicionados
 

    LaranjaAnja "Os mais comuns são hipertensão, obesidade e diabetes. E nós podemos ver que você está com início de transformação do Monstro #DCNT, isso acontece quando você ultrapassa de apenas uma doença para uma mutação corporal."


    AyaPapaya "E você não pode continuar desse jeito, você está totalmente péssimo. Estressado, olhe para esses olhos sem brilho, parece até um peixe morto!"


    BromeliaBromelia "Nós podemos te ajudar, mas isso só vai funcionar se você realmente querer."

    p "eu..... Eu não sei...... Eu estou com medo. Mas não sei se eu vou conseguir..."


    SteveApple "Você consegue sim, estamos aqui para ajudar todos que precisam de ajuda."

    "Todas as fadas" "SIM!"


    SteveApple "Vamos ir para algum lugar mais confortável, temos que explicar tudo certinho."

    #---------------------------------------------------------------------------------------------------

    #CAPITULO5 CENA1
        # Cena 1: cafeteria tarde
    scene bg_cafeteria with fade
    #play sound sound_cafeteria loop
    narrator "O Principal entra na cafeteria ainda abalado pelo que presenciou no parque. Ele se senta em uma mesa afastada. Aos poucos, quatro pessoas se aproximam e sentam-se ao redor."

    show SteveAppleSmile at midleftpos, half_body
    SteveApple "Primeiramente, vamos nos apresentar. Eu sou Steve Apple, consultor geral da área da saúde."

    show AyaPapayaN1 at leftpos, half_body
    AyaPapaya "Eu sou Aiya Papaya, nutricionista especialista em alimentação fit."

    show BromeliaBromeliaN2 at midrightpos, half_body
    BromeliaBromelia "Eu sou Bromélia Bromélia, nutricionista especialista em nutrição esportiva!"

    show LaranjaAnjaN1 at rightpos, half_body
    LaranjaAnja "E eu sou Laranja Anja, formada em enfermagem."

    p "Eu sou... nome do principal, apenas um assalariado comum."

    SteveApple " nome do principal, você deve estar confuso. Mas para o seu futuro, precisa compreender o que é DCNT e como isso pode mudar sua vida."

    stop sound

    # Cena 2 — Flash educativa
    #scene bg_flash with fade
    #play sound sound_flash loop
    narrator "A tela mostra gráficos, palavras-chave e ícones de saúde."
    
    SteveApple "DCNT significa Doenças Crônicas Não Transmissíveis. Você não as 'pega' de alguém, mas desenvolve com o tempo."
    SteveApple "Elas surgem por má alimentação, falta de atividade física, desidratação, carência de nutrientes, fatores genéticos..."
    SteveApple "Ou seja, para não se tornar um monstro DCNT, é preciso viver ao contrário desses maus hábitos."

    narrator "Imagens rápidas surgem: sedentarismo, fast food em excesso, refrigerantes, cigarros, seguidos por alternativas saudáveis como caminhada, frutas e água."

    #stop sound

    # Cena 3 — Confronto na cafeteria
    #scene bg_cafeteria with fade
    #play sound sound_heartbeat loop
    narrator "O clima na cafeteria fica pesado, quase silencioso, enquanto o Principal encara os quatro."

    LaranjaAnja "Nós analisamos... e vemos sinais de obesidade, colesterol alto, hipertensão e pré-diabetes."

    p "Vocês estão dizendo que eu sou um doente?!"

    BromeliaBromelia "Estamos dizendo que você corre sério risco de se tornar um monstro DCNT."

    p "Que palhaçada! Vocês falam como se eu estivesse acabado! Mas estou bem!"
    
    narrator "O Principal se levanta bruscamente, e tenta sair do local."

    

    show LaranjaAnjaAngry at rightpos, half_body
    LaranjaAnja " nome do principal, você sabe que não está bem."

    narrator "Imagens rápidas surgem como flashbacks:"
    # criar uma função pra fazer o flashback
    narrator "— Os nuggets brotando da pele."
    narrator "— Os dedos em forma de batata frita."
    narrator "— O monstro de donuts gritando no parque."

    LaranjaAnja "Sabemos como dói viver com DCNT. Seu corpo está gritando de dor agora, não está?"

    AyaPapaya "Você come em excesso para tentar silenciar essa dor física e mental."

    p "O que vocês sabem disso?! Vocês parecem tão saudáveis! Como podem dizer que me entendem?!"

    narrator "Ele tira a mão de Laranja e sai correndo da cafeteria."
    
    #play sound sound_steps loop
    narrator "Aiya corre atrás dele."
    AyaPapaya "Espere! nome do principal!!!"

    #stop sound
    #play sound porta_batendo
#---------------------------------------------------------------------------------------------------
    #CAPITULO6 CENA1
    label cap6cena1:
    #IMAGEM FORA DA CAFETERIA

    scene bg_cafeteriaFora with fade

    show LaranjaAnjaAngry at midleftpos, half_body

    AyaPapaya "A gente já passou por isso!"
    #fala, direta

    p "O que?"
    #fala, duvida

    AyaPapaya "Você disse que nós parecemos ser saudáveis, mas na verdade, nós somos porque devemos ser saudáveis"
    #fala, explicativa

    p "Como assim?"
    #fala, duvida

    AyaPapaya "Nós desenvolvemos DCNT, cada um tem o seu, e eu tenho diabetes tipo 1."
    #fala, explicativa

    p "Então você não é saudável?"
    #fala, duvida

    AyaPapaya "Eu tento ser o mais saudável possível. Lembra que o Steve disse? Que pode ser desenvolvido por causa da Genética."
    AyaPapaya "Diabetes tipo 1 não foi por eu não ser saudável. E agora, eu não consigo viver sem remédio. Eu não consigo comer muita coisa que eu quero."
    #fala, explicativa

    p "Você não pode? Porque?"
    #fala, duvida

    AyaPapaya "Se eu não controlar o que eu como, eu posso morrer."
    #fala, explicativa

    "Principal fica assustado e quieto, assim pensativo"
    #narracao

    p "Desculpa, eu não sei o que te dizer"
    #fala, magoado, indeciso

    AyaPapaya "Nós só queremos que você não seja igual nós, que não tenha sequelas"
    #fala, confortante

    "P pensa profundamente e com medo de seu estado atual, pede ajuda a ela."
    #narracao

    p "Aiya, eu preciso de ajuda de vocês"
    #fala, direta
#-----------------------------------------------------------------
    #CAPITULO 7
    # Cena 1 — cafeteria 

    scene bg_cafeteria with fade
    #play sound sound_cafeteria loop
    narrator "Os dois voltam à cafeteria, preocupados com o Principal."

    show BromeliaBromeliaN1 at leftpos, half_body
    BromeliaBromelia "Você está bem?"

    p "Desculpa gente, eu errei de novo..."

    show SteveAppleSmile at midleftpos, half_body
    SteveApple "O importante é sua vontade de mudar, de ser alguém melhor."

    show LaranjaAnjaSmile at rightpos, half_body
    LaranjaAnja "Vamos para nossa base! Lá você poderá entender melhor!"

    hide BromeliaBromeliaN1
    hide SteveAppleSmile
    hide LaranjaAnjaSmile
    stop sound

    # Cena 2: base secreta
    scene bg_apartamentoDia with fade
    #play sound sound_silence loop
    narrator "Eles seguem para a base. É uma sala comum, um apartamento aparentemente normal, mas com detalhes estranhos..."
    narrator "Não parece que alguém mora ali."

    show LaranjaAnjaN1 at midrightpos, half_body
    #play sound sound_chaleira
    LaranjaAnja "Fiz chá de ervas, sinta-se à vontade."

    narrator "Todos se acomodam na sala, reunidos ao redor de uma mesa."
    stop sound
    #play music music_relax loop

    p "O que eu devo fazer?"

    show AyaPapayaN1 at leftpos, half_body
    AyaPapaya "Você precisa entender o que você tem inicialmente. Tem alguma noção do porquê está com o início da DECENT?"

    p "Eu... eu acho que como muita gordura."

    AyaPapaya "Tem algo mais?"

    p "Como muitos doces?"

    show AyaPapayaHappy at leftpos, half_body
    AyaPapaya "Você deve estar perdido, né? (sorri) É assim mesmo. Tudo que você falou tem a ver com o desenvolvimento da mutação."

    show BromeliaBromeliaN2 at midleftpos, half_body
    BromeliaBromelia "O importante é você tentar controlar todos os fatores."

    show LaranjaAnjaN2 at midrightpos, half_body
    LaranjaAnja "Além disso, você precisa se exercitar e tomar bastante água."

    AyaPapaya "Sim, isso é muito importante. Agora, me diga: por que você come tanta gordura e doces?"

    p "Como assim? Eu como porque é gostoso?"

    BromeliaBromelia "Realmente?"

    p "....."

    LaranjaAnja "Eu te entendo. Antes de eu ser uma fada, eu também comia muitos doces..."

    p "Antes de ser fada? Você comia tanto assim? Você não parece... Mas por quê?"

    LaranjaAnja "No meu caso, eu sentia muito estresse por pressão social. Comecei a me julgar e não conseguia contar para ninguém. Então, comecei a comer sem parar. Até não conseguir mais."

    p "Você também tem DECENT?"

    narrator "Laranja sorri com um olhar triste."

    LaranjaAnja "Eu não aparento, mas tenho minhas dificuldades. É segredo."

    narrator "Com olhar envergonhado e um pouco triste, Laranja se aproxima e cochicha para o Principal."

    LaranjaAnja "Esse foi o meu caso... E você? O que te faz comer tanto?"

    narrator "O Principal lembra do trabalho árduo e estressante que possui e, cabisbaixo, comenta com elas."

    p "Eu não estou conseguindo ir bem no meu trabalho... Aí eu me sinto frustrado, angustiado e triste. Quando percebo, estou comendo compulsivamente..."

    BromeliaBromelia "Então o jeito é resolver primeiro o seu estresse."

    SteveApple "E como resolveríamos isso?"

    narrator "O Principal olha com preocupação."

    BromeliaBromelia "Saia do trabalho. Não há porque você ficar em um lugar assim. Você provavelmente é bom em computação! Temos conhecidos que precisam de um secretário. Vai lá!"

    p "Eu não consigo sair assim, do nada... Acho que não consigo."

    narrator "O Principal, ainda receoso, debate por um tempo com as fadas."
    narrator "Aos poucos, elas conseguem convencê-lo a repensar seu emprego e começar uma nova rotina para melhorar sua saúde."

    #stop music
    #Capitulo 8
    # Cena 1 
    label cena8:

    scene bg_casaNoite with fade
    "Alguns dias depois..."
    "O principal após mudar de emprego, passou acostumando ao trabalho, diminuindo seu estresse físico e psicológico, conseguindo acalmar a sua compulsão alimentar."
    "Mas ele ainda não sabia como comer de forma saudavel."
    "Ele foi atrás das fadas, pois recebeu uma mensagem do Steve Apple falando que estava pronto para começar a nova rotina."

    #imagem da rua
    #imagem de entrada de apartamento

    scene bg_ruaDia with fade

    "Ele pediu um Uber do seu serviço para ir até a base das fadas, não tendo nem 1km de distância, chegou ao local."
    "Ele entrou em um prédio não alto, subiu as escadas, morrendo de canceira, apertou a campainha e abriu a porta."
    
    scene bg_apartamentoDia with fade

    show LaranjaAnjaSmile at midleftpos, half_body
    LaranjaAnja "Seja bem-vindo! Que bom que você veio, nome do protagonista!"

    show SteveAppleSmile at midrightpos, half_body
    SteveApple "Hoje a Aiya e Bromélia estão combatendo outros DCNTs, vão demorar um pouco. Fique à vontade."
    hide LaranjaAnjaSmile

    p "Obrigado."

    SteveApple "Enquanto elas não chegam, vou explicar como você vai melhorar a sua dieta."
    SteveApple "A Aiya ajudará com suas decisões alimentares e a Bromélia com atividades práticas."

    p "Atividades práticas...? olha preocupado"

    SteveApple "Vamos começar pela alimentação saudável."

    # Mostra pirâmide alimentar
    #scene bg_escritorio

    SteveApple "Doces e oleosos devem ser consumidos o mínimo possível."
    SteveApple "Já os cereais e hortifruti devem ser a base da sua alimentação."

    # Aqui começa a parte interativa
    SteveApple "Até aí está ok?"

    menu:
        "Sim":
            SteveApple "Maravilha, vamos continuar."
            jump explicacao1

        "Não":
            SteveApple "Resumindo: coma pouco doce e gordura, e mais arroz, batata, couve, brócolis, banana, maçã..."
            jump explicacao1

label explicacao1:
    SteveApple "Temos também o consumo de alimentos proteicos, onde eles terão que ser consumidos em quantidades médias."
    SteveApple "Isso porque precisamos deles para a construção do nosso corpo, mas em excesso pode ser ruim ao nosso corpo pois teremos muita energia sobrando."

    # Mostra prato saudável
    # scene bg_escritorio

    SteveApple "Imagine seu prato dividido em 4 partes:"
    SteveApple "25%% proteínas (metade animal, metade vegetal), 25%% cereais e tubérculos e 50%% hortaliças e frutas."
    SteveApple "na verdade, tudo terá que ser equilibrado. Qual quer coisa em excesso, sendo comida boa ou ruim, faz mal ao nosso corpo."

    p "Mas eu não sinto que eu como tanto assim expressão de dúvida"
    SteveApple "Agora vamos falar sobre porção então."
    SteveApple "Primeiro, nós temos a quantidade necessária de caloria|energia para ser ingerida por dia. Isso é definido por cálculos, mas geralmente padronizado para um adulto  de 2000kcal."
    SteveApple "isso dependerá se a pessoa faz muito excessício físico, se usa muita energia do corpo para realizar atividades, se tem doenças, e outros fatores."

    #Aparece uma tela com tabelas escritas as refeições: café da manhã, colação, almoço, café 
    #da tarde, janta e ceia, com as suas porcentagens calóricas por refeições mais o Chibi Steve Apple 

    SteveApple "Vamos considerar que você consuma 2000kcal por dia. Recomenda-se que fala 6 refeições ao dia, sendo as mais calóricas: Café da manhã, almoço e janta. Os outros 3 seriam após essas refeições para não passar fome entre essas refeições. "
    
    #Aparece a imagem do prato saudável de acordo com a guia alimentar junto com Steve chibi
    #  
    SteveApple "E para cada refeições mais pesadas, você terá que partir o seu prato em 4 partes, onde 25%% do prato deve ser proteínas, sendo dividitos em metade animal e metade vegetal."
    SteveApple "Por exemplo: Feijão, grão de bico, lentilha, etc. Para proteína vegetal."
    SteveApple "Carne suína, bovina, aves, leites e derivados, ovos, peixes em proteína de origem animal."
    SteveApple "Outro 25%% deve ser de cereais, raízes e tubérculos, que são basicamente arroz (cereal), raíses como mandioca, nabo, entre outros, e batatas em geral que são os tubérculos."
    SteveApple "Agora, a maior parte do prato deve ser provenientes de hortaliças, até frutas podem entrar"
    SteveApple "Os hortfruts podem estar em formas de refogados, cozidos, grelhados, cruas, entre outras. Pode ser como salada de alface, repolho refogado, quiabo grelhado, milho cozido, entre outros."

    

    # Segunda escolha
    SteveApple "Está conseguindo acompanhar?"

    menu:
        "Sim":
            SteveApple "Perfeito, vamos prosseguir então."
            jump regra_de_ouro

        "Não":
            SteveApple "Vamos pensar em outra forma. Você tem o prato, do jeito que você essa imagem."
            #"Steve mostra a imagem do prato dividido em 4 partes e explica novamente."
            SteveApple "Como você vê, tem 4 partes, 1 é grande que refere à metade do prato, é a quantidade que deve colocar no prato de legumes e verduras em forma de refogado, cozido, crua como salada, entre outras formas de preparo."  
            SteveApple "1 é mediano, refere à metade da metade (1/4) do prato. Essa parte é cereais e tubérculos, arroz, batata, mandioca, entre outros."
            SteveApple "E tem 2 partes que está divido bem pequenino, que é 1/8."
            SteveApple "Essas duas partes são as proteínas, uma de origem animal e outra de vegetal."
            SteveApple "Origem animal seria bisteca, frango, ovo, peixe, entre outros. Já de origem vegetal seria feijão, grão de bico, lentilha, etc."

            jump regra_de_ouro

label regra_de_ouro:
    SteveApple "Agora, o importante você saber é: Regra de ouro para alimentação saudável."
    p "Regra de ouro?"
    SteveApple "Sim, uma regra muito fácil de entender. Basicamente é:"

    #[Aparece uma divisão de 2 da tela com produtos in Natura minimamente processados na 
    #esquerda, e no lado direito, os processados e ultraprocessados] 

    SteveApple "Comer mais produtos in Natura, que são frutas, legumes e verduras que não passaram por quase nenhum processo."
    SteveApple "Diminuir quantidade de produtos processados e ultraprocessados, que seria salgadinhos, doces, conservas, etc."
    SteveApple "Tem também os 10 passos para uma alimentação adequada, resumidamente é coma equilibradamente, diminuindo muitas gorduras,"
    SteveApple "sais, açúcares, alimentos ultraprocessados, presando nos alimentos frescos e comendo junto com alguém compartilhando a exeriência do comer junto, participando nos preparos e desenvolvendo juntos, entre outras ações."
    SteveApple "Se você tem interesse pesquise: 10 passos da alimentação adequada e saudável que aparecerá um arquivo do SUS"
    SteveApple "Então, conseguiu entender tudo?"

    menu:
        "Sim":
            SteveApple "Ótimo, a partir de amanhã você já sabe o que tem que fazer então!"
            LaranjaAnja "Qualquer dúvida, estaremos aqui!"
            p "Se eu quiser visitar vocês para comer juntos, vocês aceitariam?"
            "Steve e Laranja olham entre si, sorriem um pouco e dizem juntos:"
            SteveApple "Com certeza!"
            LaranjaAnja "Com certeza!"
            jump cap9

        "Não":
            SteveApple "Ok, vou repetir novamente para você."
            jump explicacao1
    SteveApple "Então, conseguiu entender tudo?"
    jump cap9


label cap9:
   #Capitulo 9
   #ação 1

    #[Nesta cena terá as fadas falando perguntando o que fará para cada ação que terá no dia, sendo 
    # 1: Café da manhã, 2: Atividade física, 3: Almoço e janta, 4: Descanço, 
    # para cada ações tem 6 alternativas, onde estão separadas em bolhas, quando clicados mostra a cena da escolha.
    #  Isso afetará no score para os tipos de finais possíveis.]


label cena9:

    scene bg_quartoDia with fade
    show AyaPapayaN1 at rightpos, half_body

    p "Onde estou agora?"
    AyaPapaya "Oi [p]! Vim te acompanhar hoje para ver como você vai passar o seu dia! 
          Não vou ficar interferindo, pois no fim, a escolha é sua. 
          Mas estarei dando dicas se você estiver com muita dúvida."

    "Agora escolha o que você vai comer no lanche da manhã/tarde:"

    call screen bubble_menu([
        ("Maçã", Jump("lanche_maca")),
        ("Cereal com leite", Jump("lanche_cereal")),
        ("Iogurte com granola", Jump("lanche_iogurte")),
        ("Pizza", Jump("lanche_pizza")),
        ("Hambúrguer", Jump("lanche_hamburguer")),
        ("Biscoito recheado", Jump("lanche_biscoito")),
    ])

label lanche_maca:
    show AyaPapayaHappy at rightpos, half_body
    AyaPapaya "Uma fruta de manhãzinha é muito gostoso! 
              Se passar fome, você pode comer mais frutas na colação. 
              Café da manhã é uma refeição importante, 
              se quiser comer pão, leite, granola etc., pode."
    $ score += 1
    jump fim_acao1

label lanche_cereal:
    show AyaPapayaN2 at rightpos, half_body
    AyaPapaya "É um bom começo! 
              Se colocar uvas, morangos ou manga, 
              fica mais nutritivo e gostoso."
    $ score += 1
    jump fim_acao1

label lanche_iogurte:
    show AyaPapayaHappy at rightpos, half_body
    AyaPapaya "A granola tem açúcar e fibras! 
              Faz bem para o intestino e enche o estômago."
    $ score += 1
    jump fim_acao1

label lanche_pizza:
    show AyaPapayaSad at rightpos, half_body
    AyaPapaya "Pizza é bem calórica. Melhor deixar para um dia específico da semana."
    $ score -= 1
    jump fim_acao1

label lanche_hamburguer:
    show AyaPapayaAngry at rightpos, half_body
    AyaPapaya "Hambúrguer é calórico para começar o dia... 
              Que tal um sanduíche de atum ou salpicão?"
    $ score -= 1
    jump fim_acao1

label lanche_biscoito:
    show AyaPapayaSad at rightpos, half_body
    AyaPapaya "Se comer uns 3, tudo bem... mas o pacote todo vai te fazer mal."
    $ score -= 1
    jump fim_acao1

label fim_acao1:
    "Você terminou sua escolha do lanche da manhã/tarde."
    jump acao2_atividade_fisica

label acao2_atividade_fisica:

    scene bg_parque_tarde with fade
    show AyaPapayaN1 at rightpos, half_body

    AyaPapaya "Antes de trabalhar, vamos praticar alguma atividade física! 
               Vou te acompanhar no que você decidir!"

    call screen bubble_menu([
        ("Correr 10 km", Jump("fisica_correr")),
        ("Dar uma volta no parque", Jump("fisica_parque")),
        ("Treinar futebol", Jump("fisica_futebol")),
        ("Tomar sol na varanda", Jump("fisica_sol")),
        ("Assistir Netflix", Jump("fisica_netflix")),
        ("Ir direto no trabalho andando", Jump("fisica_trabalho")),
    ])

label fisica_correr:
    show AyaPapayaHappy at rightpos, half_body
    AyaPapaya "É melhor parar por aqui, senão não vai aguentar o resto do dia!"
    p "Eu... Eu cansei..."
    $ score -= 2
    jump fim_acao2

label fisica_parque:
    show AyaPapayaN1 at rightpos, half_body
    AyaPapaya "Que belo dia! Como você está se sentindo, [p]?"
    p "Cansado, mas é um cansaço bom!"
    $ score += 2
    jump fim_acao2

label fisica_futebol:
    show AyaPapayaSad at rightpos, half_body
    AyaPapaya "[p]!!!!"
    p "AI!!!"
    $ score -= 2
    jump fim_acao2

label fisica_sol:
    show AyaPapayaN2 at rightpos, half_body
    AyaPapaya "Não é assim que funciona, [p]..."
    p "Perder água é emagrecer!"
    $ score -= 1
    jump fim_acao2

label fisica_netflix:
    show AyaPapayaN2 at rightpos, half_body
    AyaPapaya "[p]!?! O que você está fazendo???"
    p "Vou fazer exercício depois!"
    $ score -= 1
    jump fim_acao2

label fisica_trabalho:
    show AyaPapayaN1 at rightpos, half_body
    AyaPapaya "Tenha uma boa caminhada!"
    p "Obrigado!"
    $ score += 1
    jump fim_acao2

label fim_acao2:
    "Você terminou a atividade física do dia."
    jump acao3_almoco_janta

    

label acao3_almoco_janta:

    scene bg_quartoDia with fade
    show AyaPapayaN1 at rightpos, half_body

    AyaPapaya "[p]! Agora eu preciso ir trabalhar! 
               Não esqueça, sempre pense em comer saudavelmente!"

    call screen bubble_menu([
        ("Arroz, feijão, salada, carne", Jump("almoco_refeicao")),
        ("Sopa de mandioquinha com carne", Jump("almoco_sopa")),
        ("Whey protein", Jump("almoco_whey")),
        ("Milho espiga", Jump("almoco_milho")),
        ("Donuts", Jump("almoco_donuts")),
        ("Água", Jump("almoco_agua")),
    ])

label almoco_refeicao:
    p "Nossa, faz tempo que não como comida de verdade!"
    $ score += 2
    jump fim_acao3

label almoco_sopa:
    p "Pensei que estaria ruim... Que gostoso!"
    $ score += 1
    jump fim_acao3

label almoco_whey:
    p "Gostoso, mas estou com fome. Acho que vou beber mais."
    $ score -= 1
    jump fim_acao3

label almoco_milho:
    p "Vi que tem fibras, mas não gostei muito..."
    $ score -= 1
    jump fim_acao3

label almoco_donuts:
    p "Ai que gostoso!!!"
    p "Não sei se é bom, mas estou feliz!"
    $ score -= 1
    jump fim_acao3

label almoco_agua:
    p "Se eu não comer nada, posso abaixar o peso..."
    $ score -= 2
    jump fim_acao3

label fim_acao3:
    "Você terminou a refeição."
    jump acao4_descanso

    
label acao4_descanso:

    scene bg_quartoNoite with fade
    show AyaPapayaN1 at rightpos, half_body

    AyaPapaya "Conseguiu comer bem [p]? Agora é a hora de descansar!"

    call screen bubble_menu([
        ("Fazer alongamento", Jump("descanso_alongamento")),
        ("Estudar", Jump("descanso_estudar")),
        ("Dormir 10h", Jump("descanso_dormir")),
        ("Comer petisco", Jump("descanso_petisco")),
        ("Jogar jogo viciante", Jump("descanso_jogo")),
        ("Maratonar filme", Jump("descanso_filme")),
    ])

label descanso_alongamento:
    show AyaPapayaN1 at rightpos, half_body
    AyaPapaya "Vou te acompanhar! Chegando em casa eu vou dormir também kkkkkkk"
    $ score += 2
    jump fim_acao4

label descanso_estudar:
    show AyaPapayaN1 at rightpos, half_body
    AyaPapaya "É bom estudar antes de dormir, só não pode exagerar demais viu"
    $ score += 1
    jump fim_acao4

label descanso_dormir:
    AyaPapaya "[p]! Você está atrasado para o trabalho!!! Acorda!"
    $ score -= 2
    jump fim_acao4

label descanso_petisco:
    AyaPapaya "[p]... Fazer ceia é legal... Mas o que você está comendo não é legal..."
    $ score -= 1
    jump fim_acao4

label descanso_jogo:
    p "Que jogo legallllll!!!!!!!!!!"
    $ score -= 1
    jump fim_acao4

label descanso_filme:
    p ".........."
    $ score -= 1
    jump fim_acao4

label fim_acao4:
    "Você terminou o seu dia! Agora é hora de descansar de verdade."
    

    
label cena10_final_demo:

    scene bg_parque_dia with fade  # Cena inicial para a narração
    "Algumas semanas depois..."

    if score >= 4:  # Rota boa
        

        show AyaPapayaHappy at leftpos, half_body
        show BromeliaBromeliaHappy at midleftpos, half_body
        show LaranjaAnjaHappy at midrightpos, half_body
        show SteveAppleHappy at rightpos, half_body

        AyaPapaya "[p]! Hoje você vai passear também? Depois posso ir com você?"
        p "Claro! Eu pretendo dar uma volta pela prefeitura hoje"
        BromeliaBromelia "Podemos correr um pouco também! O Steve não atingiu a meta de hoje ainda, vamos todos juntos depois?"
        LaranjaAnja "Eu quero!"
        p "Vamos! Depois do trabalho então!"
        LaranjaAnja "Após isso, podemos jantar juntos também!"
        "Todos andando em algum lugar felizes"

        p "Eu me sinto muito melhor agora. Graças a elas, estou conseguindo diminuir aqueles sinais de DCNT."
        p "Ainda, psicologicamente me sinto mais livre depois que comecei a fazer atividades físicas."
        p "Lembrei dos sabores nostálgicos, sabores que lembram da minha infância, comida de verdade..."
        p "Ainda estou com vários problemas no corpo, mas se eu continuar com essa rotina mais saudável, eu consigo voltar a ser uma pessoa saudável."
        p "Obrigado pessoal, eu agora sinto mais vivo do que antes."
   
        p "A partir de amanhã, eu vou tentar novas coisas!"
        "Final do Demo"

    elif score > 2:  # Rota mediano

        p "Não mudou nada depois que elas vieram...."
        p "Me sinto mesma coisa, não vejo nada demais......"
        p "Será que eu preciso ser saudável para viver mesmo?...."
        p "Eu sou a mesma coisa de antes....."
        p "Eu mudei de trabalho, não me estresso mais quanto antes..."
        p "Eu diminui o que eu como, mas ainda continuo comendo doces, salgados, entre outros......."
        p "Eu até comecei a comer verduras......"
        p "Mas não mudei nada..."
        p "Ah...... Se é assim, vou continuar sendo assim mesmo. Acho que sou mais feliz do jeito que estou agora..."
        scene black with fade
        p "Acho que não vai acontecer mais nada......"
        

    else:  # Rota ruim, score < 2


        show AyaPapayaSad at leftpos, half_body
        show BromeliaBromeliaSad at midleftpos, half_body
        show LaranjaAnjaN1 at midrightpos, half_body
        show SteveAppleSad at rightpos, half_body

        SteveApple "Não conseguimos de novo........"
        BromeliaBromelia "Será que algum dia conseguiremos combater essa maldição?"
        LaranjaAnja "Aiya............"
        AyaPapaya "Eu......... Cancei..............."

        AyaPapaya "Porque as pessoas não entendem que DCNT pode matar????..............."
        SteveApple "Aiya...... O que você quer fazer?"
        BromeliaBromelia "Aiya...... É a sua escolha."
        AyaPapaya ".............."
        LaranjaAnja "Você já fez o bastante......... Não precisa fazer mais que isso........."
        scene black with fade
        AyaPapaya "Está bem....... Vamos começar de novo...."


    "Final da Demo"
return
