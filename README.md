# 🍪 Sessões e Cookies com Flask

Este projeto é uma aplicação simples em Python usando o framework Flask, com o objetivo de **demonstrar o uso de sessões e cookies**, incluindo:

- Criação, leitura, remoção de cookies
- Flags de segurança (`HttpOnly`, `Secure`)
- Contador de visitas persistente
- Carrinho de compras com sessão (armazenamento no lado do servidor)

---

## 🔧 Funcionalidades

### 🍪 Cookies
- Definir cookie de sessão com `HttpOnly` e `Secure`
- Definir cookie persistente (7 dias) com `HttpOnly` e `Secure`
- Ler os cookies armazenados
- Remover cookies
- Contador de visitas persistente (1 ano)

### 🛒 Sessões
- Login com sessão (usuário: `aluno`, senha: `123`)
- Dashboard protegido por login
- Carrinho de compras:
  - Adição de itens
  - Visualização direta na tela inicial
  - Botão para limpar o carrinho
- Sessão permanente com tempo limite configurável

---

## 🚀 Como rodar o projeto

### Pré-requisitos:
- Python 3.x instalado
- Flask instalado (`pip install flask`)

### Passos:

```bash
# Clone o repositório
git clone https://github.com/DavidReis23/Cookies.git

# Acesse a pasta
cd Cookies

# Rode o servidor Flask
python app.py
