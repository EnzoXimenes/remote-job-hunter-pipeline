# remote-job-hunter-pipeline

# 🌐 Remote Job Alert & Web Scraping Pipeline

Pipeline automatizado em Python desenvolvido para monitorar oportunidades de emprego no portal **We Work Remotely**, filtrar posições 100% remotas globais, estruturar os dados em formato tabular e despachar relatórios diários por e-mail com planilha CSV anexada.

---

## 📌 Principais Recursos

- **Web Scraping Estruturado:** Parsing dos cards de vagas utilizando `BeautifulSoup4` e `requests`, com tratamento contra elementos dinâmicos nulos (`NoneType`) e headers que simulam navegação real (`User-Agent`).
- **Tratamento e Filtragem de Dados:** Normalização dos textos com `pandas`, geração de links absolutos e filtragem condicional para manter apenas posições globais/remotas (`Anywhere in the World`).
- **Disparo Automatizado de E-mail (SMTP):** Construção da mensagem via biblioteca nativa `email.message.EmailMessage` com leitura binária (`octet-stream`) do arquivo CSV e envio seguro via `smtplib.SMTP_SSL`.
- **Segurança e Boas Práticas:** Isolamento de credenciais com 

---

## 🛠️ Tecnologias e Bibliotecas

| Ferramenta | Aplicação |
| :--- | :--- |
| **Python 3** | Linguagem base do projeto |
| **BeautifulSoup4** | Extração de dados da árvore DOM (HTML) |
| **Requests** | Comunicação e requisições HTTP |
| **Pandas** | Manipulação, estruturação e exportação para CSV |
| **SMTPLib & EmailMessage** | Protocolo seguro de transporte e formatação de e-mail |

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o repositório
```bash
git clone [https://github.com/EnzoXimenes/remote-job-hunter-pipeline.git](https://github.com/EnzoXimenes/remote-job-hunter-pipeline.git)
cd remote-job-hunter-pipeline
