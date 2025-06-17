# 🍪 Gerenciando Cookies com Flask

Este projeto é uma aplicação simples em Python usando o framework Flask, com o objetivo de **demonstrar como trabalhar com cookies**: criação, leitura, remoção, flags de segurança e contador de visitas.

---

## 🔧 Funcionalidades

- Definir cookie de sessão com `HttpOnly` e `Secure`
- Definir cookie persistente (7 dias) com `HttpOnly` e `Secure`
- Ler os cookies armazenados
- Remover cookies
- Contador de visitas persistente (1 ano)

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

# Visualizar o contador

 http://localhost:5000/contador-visitas
