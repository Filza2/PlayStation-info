from requests import get
import re,os

os.system('cls' if os.name=='nt' else 'clear');print("""
██████╗ ███████╗███╗   ██╗      ██╗███╗   ██╗███████╗ ██████╗ 
██╔══██╗██╔════╝████╗  ██║      ██║████╗  ██║██╔════╝██╔═══██╗
██████╔╝███████╗██╔██╗ ██║█████╗██║██╔██╗ ██║█████╗  ██║   ██║
██╔═══╝ ╚════██║██║╚██╗██║╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║
██║     ███████║██║ ╚████║      ██║██║ ╚████║██║     ╚██████╔╝
╚═╝     ╚══════╝╚═╝  ╚═══╝      ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                             
                   By @TweakPY - @vv1ck
""")
username=input('- username : ');username=username.strip()#Attention, keys/letters are sensitive in this input
r=get(f'https://psnprofiles.com/{username}',headers={'Host': 'psnprofiles.com','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Te': 'trailers'},allow_redirects=False)

if r.status_code==302:print("- user not found ");exit()
try:Description=re.findall('                	<meta name="Description" content=" (.*?)" />',r.text)[0];info=str(Description).split();level=info[2];trophies=info[4];games=info[7];world_rank=info[12];country_rank=info[16];print(f'- Level [ {level} ]');print(f'- Trophies [ {trophies} ]');print(f'- Games [ {games} ]');print(f'- World Rank [ {world_rank} ]');print(f'- Country Rank [ {country_rank} ]\n')
except IndexError:print('- Error ! ')
try:
    games_names=re.findall(f'							<a class="title" href="/trophies/(.*?)/{username}" rel="nofollow">(.*?)</a>',r.text)
    print('- Games : \n') 
    for i in games_names:
        i=i[1]
        if '&#039' in i :
            i=str(i).replace('&#039',"'")
        if ';' in i :
            i=str(i).replace(';','')
        print(i)
    print('\n')
except IndexError:print('- Error ! ')
