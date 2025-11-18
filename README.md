# 📘 GS Cloud – FIAP
## Processamento e Visualização de CSV no Azure WebApp
### Autor: **Victor Sabino Machado**

Este projeto implementa uma solução completa de ingestão, processamento e visualização de dados na nuvem utilizando:

- **Python + Flask**
- **Azure WebApp (App Service Linux)**
- **Azure CLI para provisionamento**
- **GitHub Actions para CI/CD**
- **Dataset "Future of Work" (O*NET)**

A aplicação permite o upload de um arquivo CSV, realiza detecção automática de encoding/separador e exibe os dados processados no navegador com interface moderna.

---

# 🚀 Objetivos da Solução

- Criar infraestrutura em Azure via script reprodutível  
- Configurar pipeline CI/CD para deploy automático  
- Adaptar a aplicação DisplayCSV  
- Processar e visualizar dados do dataset Future of Work  
- Garantir que toda alteração no código resulte em novo deploy  
- Publicar o WebApp online acessível por URL pública  

---

# 📁 Estrutura do Projeto

```
displaycsv/
│
├── app.py                         # Lógica da aplicação Flask (upload + processamento CSV)
├── requirements.txt               # Dependências Python
│
├── templates/
│   ├── index.html                 # Página de upload (estilizada)
│   └── display.html               # Página de visualização dos dados (estilizada)
│
├── data/
│   └── Futurework.csv             # Dataset usado no projeto
│
├── infra/
│   └── create_infra.sh            # Script Azure CLI para provisionamento 
│
├── .github/
│   └── workflows/
│       └── deploy.yml             # Pipeline CI/CD – GitHub Actions
│
└── prints/                        # Prints obrigatórios da GS
    ├── print-gs-cloud-1.png
    ├── print-gs-cloud-2.png
    ├── print-gs-cloud-3.png
    ├── print-gs-cloud-4.png
    ├── print-gs-cloud-5.png
    ├── print-gs-cloud-6.png
    ├── print-gs-cloud-7.png
    ├── print-gs-cloud-8.png
    ├── print-gs-cloud-9.png
    ├── print-gs-cloud-10.png
    ├── print-gs-cloud-11.png
    ├── print-gs-cloud-12.png
    ├── print-gs-cloud-13.png
    ├── print-gs-cloud-14.png
    └── print-gs-cloud-15.png

```

---

# ☁ Provisionamento da Infraestrutura (Azure CLI)

O script `infra/create_infra.sh` cria automaticamente:

- Resource Group  
- App Service Plan (Linux)  
- WebApp Python 3.12  
- Configuração de build automático (SCM_DO_BUILD_DURING_DEPLOYMENT)

### Para executar:

```bash
chmod +x create_infra.sh
./create_infra.sh
```

Ao final, o script retorna a URL pública do WebApp.

---

# 🔄 CI/CD – GitHub Actions

O arquivo `.github/workflows/deploy.yml` contém o pipeline responsável por:

- Clonar o repositório  
- Instalar dependências  
- Empacotamento da aplicação  
- Deploy automático para o Azure WebApp  

### O pipeline usa o secret:

```
AZUREAPPSERVICE_PUBLISHPROFILE
```

Criado em:

`GitHub → Settings → Secrets → Actions → New repository secret`

O valor é obtido no Azure em:

**WebApp → Get Publish Profile**

---

# 🧠 Lógica da Aplicação (app.py)

A aplicação:

- Recebe um arquivo CSV via formulário  
- Detecta automaticamente o encoding usando `chardet`  
- Detecta automaticamente o separador usando `sep=None`  
- Processa com Pandas  
- Exibe até 500 linhas para evitar lentidão  
- Renderiza tabela estilizada em HTML

Totalmente alinhado ao projeto original **DisplayCSV** da FIAP.

---

# 🧪 Como Testar

1. Acessar o WebApp:

```
https://webapp-gs-cloud.azurewebsites.net
```

2. Selecionar o arquivo `Futurework.csv`  
3. Enviar  
4. Ver os dados sendo exibidos automaticamente  

---

# 🖼 Prints Obrigatórios (incluídos na pasta /prints)

1. **Execução do script no Cloud Shell (Azure CLI)**  
2. **Workflow do GitHub Actions executado com sucesso**  
3. **WebApp online exibindo seu CSV**  

---

# 🛠 Tecnologias Utilizadas

- Python 3.12  
- Flask  
- Pandas  
- Chardet (detecção automática de encoding)  
- Azure WebApp (Linux)  
- Azure CLI  
- GitHub Actions  
- HTML + CSS  

---

# ✔ Conclusão

Este projeto demonstra um pipeline completo de ingestão e visualização de dados na nuvem, integrando:

- Infraestrutura como código (Azure CLI)  
- Deploy contínuo (GitHub Actions)  
- Processamento inteligente de CSV  
- Aplicação Flask com layout profissional  
- Publicação em ambiente cloud escalável  

Atendendo integralmente os requisitos da **GS Cloud FIAP**.

---

# 📩 Contato

Desenvolvido por **Victor Sabino Machado**.
