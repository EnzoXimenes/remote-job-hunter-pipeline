from bs4 import BeautifulSoup
import requests
import pandas as pd
from email.message import EmailMessage
import smtplib


#Dados de conexão
servidor_smtp = "smtp.gmail.com"
porta = 465
email_remetente = ("EMAIL REMETENTE")
senha_app = ("SENHA DO APP")

lista_vagas = []

url = "https://weworkremotely.com/" #(OU O LINK DO SITE QUE PREFERIR)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}

msg = EmailMessage()
msg["Subject"] = "Vagas estágios RJ"
msg["From"] = "EMAIL REMETENTE"
msg["To"] = "EMAIL DESTINATÁRIO"


resposta = requests.get(url, headers = headers)
soup = BeautifulSoup(resposta.text, "html.parser")
all_jobs = soup.find_all("li", class_="new-listing-container")

print(resposta.status_code)

for card in all_jobs:
    #Para varrer card por card para achar as vagas(CONFIGURAR DE ACORDO COM O SITE)
    tag_cargo = card.find("span", class_="new-listing__header__title__text")
    tag_empresa = card.find("p", class_="new-listing__company-name")
    tag_local = card.find("p", class_="new-listing__company-headquarters")
    tag_link = card.find("a")
    if tag_cargo and tag_empresa and tag_link:
        cargo = tag_cargo.text.strip()
        empresa = tag_empresa.text.strip()
        localizacao = tag_local.text.strip() if tag_local else "Não informado"
        
        href = tag_link.get("href", "")
        if href.startswith("http"):
            url_vaga = href
        else:
            url_vaga = f"https://weworkremotely.com{href}"
        vagas_filtradas = {
            "Cargo" : cargo,
            "Empresa" : empresa,
            "Localizacao" : localizacao,
            "Link" : url_vaga,
        }
        lista_vagas.append(vagas_filtradas)


#Cria o DF das vagas
df_vagas = pd.DataFrame(lista_vagas)

# Filtra as linhas onde a coluna 'Localizacao' contém 'Anywhere'
# case=False ignora maiúsculas/minúsculas; na=False trata valores vazios
df_remoto = df_vagas[
    df_vagas["Localizacao"].str.contains("Remote", case=False, na=False)
]

print(f"Total raspado: {len(df_vagas)}")
print(f"Total 100% remoto/global: {len(df_remoto)}")

df_vagas.to_csv("todas_vagas.csv", index=False)
print(df_vagas.head(20))
# 3. Salva apenas o DataFrame filtrado
df_remoto.to_csv("vagas_remoto.csv", index=False)
total_vagas = len(df_remoto)
print(df_remoto.head(20))

#Define o texto para mandar por email
msg.set_content(f"Foram encontradas {total_vagas} no Rio de Janeiro!")

#Mandar arquivos por email
with open("vagas_remoto.csv", "rb") as arquivo:
    conteudo = arquivo.read()
    msg.add_attachment(
        conteudo,
        maintype = "application",
        subtype = "octet-stream",
        filename = "vagas_remoto.csv", 
    )
with open("todas_vagas.csv", "rb") as arquivo:
    conteudo = arquivo.read()
    msg.add_attachment(
        conteudo,
        maintype = "application",
        subtype = "octet-stream",
        filename = "todas_vagas.csv", 
    )
    
    print("Arquivo adicionado com sucesso")
#Mandar o email
with smtplib.SMTP_SSL(servidor_smtp,porta) as servidor:
    servidor.login(email_remetente, senha_app)
    servidor.send_message(msg)
    print("Email enviado com sucesso!")
