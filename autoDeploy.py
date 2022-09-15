from ctypes.wintypes import tagMSG
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

envs = {
1:'qa',
2:'int',
3:'asia'
}
gameList = {
0:'lobby',
1:'diaochan',
2:'gem-saviour',
3:'fortune-gods',
6:'medusa2',
7:'medusa',
17:'wizdom-wonders',
18:'hood-wolf',
20:'reel-love',
24:'win-win-won',
25:'plushie-frenzy',
26:'fortune-tree',
28:'hotpot',
29:'dragon-legend',
31:'baccarat-deluxe',
33:'hip-hop-panda',
34:'legend-of-hou-yi',
35:'mr-hallow-win',
36:'prosperity-lion',
37:'santas-gift-rush',
38:'gem-saviour-sword',
39:'piggy-gold',
40:'jungle-delight',
41:'symbols-of-egypt',
42:'ganesha-gold',
43:'three-monkeys',
44:'emperors-favour',
48:'double-fortune',
49:'chicky-royale',
50:'journey-to-the-wealth',
53:'the-great-icescape',
54:'captains-bounty',
57:'dragon-hatch',
58:'vampires-charm',
59:'ninja-vs-samurai',
60:'leprechaun-riches',
61:'flirting-scholar',
62:'gem-saviour-conquest',
63:'dragon-tiger-luck',
64:'muay-thai-champion',
65:'mahjong-ways',
67:'shaolin-soccer',
68:'fortune-mouse',
69:'bikini-paradise',
70:'candy-burst',
71:'cai-shen-wins',
73:'egypts-book-mystery',
74:'mahjong-ways2',
75:'ganesha-fortune',
79:'dreams-of-macau',
80:'circus-delight',
82:'phoenix-rises',
83:'wild-fireworks',
84:'queen-bounty',
85:'genies-wishes',
86:'the-galactic-gems',
87:'treasures-aztec',
88:'jewels-prosper',
89:'lucky-neko',
90:'secrets-of-cleopatra',
91:'guardians-of-ice-and-fire',
92:'thai-river',
93:'opera-dynasty',
94:'bali-vacation',
95:'majestic-treasures',
97:'jack-frost-winter',
98:'fortune-ox',
100:'candy-bonanza',
101:'rise-of-apollo',
102:'mermaid-riches',
103:'crypto-gold',
104:'wild-bandito',
105:'heist-stakes',
106:'ways-of-qilin',
107:'lgd-monkey-kg',
108:'buffalo-win',
109:'sushi-oishi',
110:'jurassic-kingdom',
111:'groundhog',
112:'oriental-pros',
113:'crypt-fortune',
114:'emoji-riches',
115:'sprmkt-spree',
116:'farm-invaders',
117:'cocktail-nite',
118:'mask-carnival',
119:'spirit-wonder',
120:'queen-banquet',
121:'dest-sun-moon',
122:'garuda-gems',
123:'rooster-rbl',
124:'battleground',
125:'btrfly-blossom',
126:'fortune-tiger',
127:'speed-winner',
128:'legend-perseus',
129:'win-win-fpc',
130:'lucky-piggy',
132:'wild-coaster',
135:'wild-bounty-sd',
1312883:'prosper-ftree',
1338274:'totem-wonders',
1340277:'asgardian-rs',
1368367:'alchemy-gold',
1372643:'diner-delights',
1418544:'bakery-bonanza'
}

df = pd.read_csv(r'C:\Users\ZH\Desktop\deployFile.csv')
env = envs[int(input(f'{envs}:'))]
fail=[]

for i in df.values:
    try:
        # jenkins v1
        url=f'https://be-jenkins.sige.la/view/game-development-team/job/gamedev_game_{gameList[i[1]]}/build?delay=0sec'
        s=Service(r'C:\Users\ZH\Downloads\chromedriver_win32\chromedriver')
        chrome=webdriver.Chrome(service=s)
        chrome.get(url)

        # 登入帳號
        account=chrome.find_element(By.XPATH, "/html/body/div/div/form/div[1]/input")
        account.send_keys('qaqa123zh@gmail.com')
        # time.sleep(1)

        # 登入密碼
        password=chrome.find_element(By.XPATH, "/html/body/div/div/form/div[2]/input")
        password.send_keys('zHvfb7D8jyjHnXrsc3LHf4Z4y8CgNdsm')
        # time.sleep(1)
        
        # 登入
        chrome.find_element(By.XPATH, "/html/body/div/div/form/div[4]/button").click()

        # 版本
        TAG=chrome.find_element(By.XPATH, "/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]/div/input[2]")
        TAG.clear()
        TAG.send_keys(i[2])
        # time.sleep(1)

        # 環境
        ENV=chrome.find_element(By.XPATH, "/html/body/div[3]/div[2]/form/div[1]/div[2]/div[3]/div/input[2]")
        ENV.clear()
        if env == 'qa':
            ENV.send_keys('qa_debug ')
        elif env == 'int':
            ENV.send_keys('int_release ')
        elif env == 'asia':
            ENV.send_keys('prod_asia')
        # time.sleep(2)

        # 建置
        chrome.find_element(By.XPATH, "/html/body/div[3]/div[2]/form/div[1]/div[3]/div/span/span/button").click()

        print(f'========= {gameList[i[1]]} deployed Successfully=========')

    except:
        fail.append(i[0])
        print(f'========= {i[0]} deployed Unsuccessfully=========')

    finally:
        chrome.quit()

print(fail)
print('finish')