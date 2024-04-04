import requests
from bs4 import BeautifulSoup
import os

url = "https://infoprovas.dcc.ufrj.br/prova.php"
headers = {
    "Cookie": "__utma=263428936.73292053.1709834993.1709834993.1709834993.1; __utmz=263428936.1709834993.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=d761hemvs8esinu0o74vsqi714",
    "Sec-Ch-Ua": '"Not(A:Brand";v="24", "Chromium";v="122"',
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Origin": "https://infoprovas.dcc.ufrj.br",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://infoprovas.dcc.ufrj.br/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=1, i"
}


os.makedirs('provas', exist_ok=True)  # Cria o diretório 'provas' se ele não existir

nomes_por_id = {}
for i in range(1000):
    data = {
        "id": str(i)
    }
    response = requests.post(url, headers=headers, data=data, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")
    strong = soup.find("strong")
    if strong:
        nome_arquivo = strong.text.replace('/', '-')
        nomes_por_id[i] = nome_arquivo
        pdf = requests.get(f'https://infoprovas.dcc.ufrj.br/provas/{i}.pdf', headers=headers, verify=False)
        with open(f'provas/{nome_arquivo}.pdf', 'wb') as f:
            f.write(pdf.content)
    else:
        nomes_por_id[i] = None
