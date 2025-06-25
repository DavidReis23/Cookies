# app.py
from flask import Flask, request, redirect, url_for, session, render_template_string, make_response
from flask import Flask, request, redirect, url_for, session, render_template_string, make_response, flash, get_flashed_messages
from datetime import datetime, timedelta

# Inicializa a aplicação Flask
app = Flask(__name__)
app.secret_key = 'uma_chave_secreta_muito_forte_e_aleatoria_para_o_projeto_1234567890'

# app.py
# ... (importações e app.secret_key) ...

# Rota principal para uma mensagem de boas-vindas e links de navegação
@app.route('/')
def index():
    if 'user_id' in session:
        return f"""
        <h1>Bem-vindo, {session['user_id']}!</h1>
        <p>Você está logado.</p>
        <ul>
            <li><a href="/dashboard">Ir para o Dashboard (Área Restrita)</a></li>
            <li><a href="/ver-carrinho">Ver Carrinho</a></li>
            <li><a href="/logout">Logout</a></li>
        </ul>
        <hr>
        <p><h3>Demonstrações de Cookies (continuam funcionando independentemente da sessão):</h3></p>
        <ul>
            <li><a href="/definir-cookie-sessao">Definir cookie de sessão</a></li>
            <li><a href="/definir-cookie-persistente">Definir cookie persistente (expira após 7 dias)</a></li>
            <li><a href="/ler-cookie">Ler o cookie armazenado</a></li>
            <li><a href="/remover-cookie">Remover cookie</a></li>
            <li><a href="/contador-visitas">Contador de Visitas (com cookie)</a></li>
        </ul>
        """
    else:
        return """
        <h1>Bem-vindo à aplicação de demonstração de Sessões e Cookies!</h1>
        <p>Este sistema simula operações básicas de gerenciamento de estado.</p>
        <ul>
            <li><a href="/login">Fazer Login</a></li>
        </ul>
        <hr>
        <p><h3>Demonstrações de Cookies:</h3></p>
        <ul>
            <li><a href="/definir-cookie-sessao">Definir cookie de sessão</a></li>
            <li><a href="/definir-cookie-persistente">Definir cookie persistente (expira após 7 dias)</a></li>
            <li><a href="/ler-cookie">Ler o cookie armazenado</a></li>
            <li><a href="/remover-cookie">Remover cookie</a></li>
            <li><a href="/contador-visitas">Contador de Visitas (com cookie)</a></li>
        </ul>
        """

# app.py
# ... (código anterior) ...

# Rota de login: exibe formulário (GET) e processa login (POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        flash('Você já está logado.', 'info')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'aluno' and password == '123':
            session['user_id'] = username
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciais inválidas.', 'error')
            return redirect(url_for('login'))

    mensagens = get_flashed_messages(with_categories=True)
    html = ''.join([f"<p class='{cat}'>{msg}</p>" for cat, msg in mensagens])
    html += """
        <h1>Login</h1>
        <form method="POST" action="/login">
            <label for="username">Usuário:</label>
            <input type="text" id="username" name="username" value="aluno"><br><br>
            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" value="123"><br><br>
            <button type="submit">Entrar</button>
        </form>
        <p><a href="/">Voltar à Página Inicial</a></p>
        <style>
            .success { color: green; }
            .error { color: red; }
            .info { color: blue; }
        </style>
    """
    return render_template_string(html)


# app.py
# ... (código anterior) ...

# Rota do Dashboard (área restrita)
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Você precisa estar logado para acessar o dashboard.', 'error')
        return redirect(url_for('login'))

    mensagens = get_flashed_messages(with_categories=True)
    html = ''.join([f"<p class='{cat}'>{msg}</p>" for cat, msg in mensagens])
    html += f"""
        <h1>Bem-vindo ao Dashboard, {session['user_id']}!</h1>
        <p>Esta é uma área protegida por sessão.</p>
        <p><a href="/">Voltar à Página Inicial</a></p>
        <p><a href="/logout">Logout</a></p>
        <style>
            .success {{ color: green; }}
            .error {{ color: red; }}
            .info {{ color: blue; }}
        </style>
    """
    return render_template_string(html)

# ... (restante do código virá aqui) ...
# app.py
# ... (código anterior) ...

# Rota de logout
@app.route('/logout')
def logout():
    session.clear()
    flash('Logout realizado com sucesso.', 'info')
    return redirect(url_for('index'))


# ... (resto do código do contador de visitas e if __name__ == '__main__': app.run(debug=True)) ...


# Rotas

# ... (código anterior) ...

# Rotas

# Define um cookie de sessão (válido até o navegador ser fechado)
@app.route('/definir-cookie-sessao')
def definir_cookie_sessao():
    # make_response é usado para criar um objeto de resposta que podemos modificar
    resposta = make_response("Cookie de sessão 'usuario_logado' definido com sucesso.")
    # set_cookie é o método que adiciona o cabeçalho 'Set-Cookie' na resposta HTTP.
    # Por padrão, se 'max_age' ou 'expires' não forem definidos, será um cookie de sessão.
    resposta.set_cookie('usuario_logado', 'admin')
    # Exemplo para HttpOnly
    resposta.set_cookie('meu_cookie_seguro', 'valor', httponly=True)

    # Exemplo para Secure (lembre-se que Secure só funciona plenamente com HTTPS)
    # Em ambiente de desenvolvimento local (http://localhost), ele pode não se comportar como esperado
    resposta.set_cookie('meu_cookie_secure', 'valor', secure=True)
    return resposta
    
# Fim das Rotas

# ... (resto do código) ...

# ... (código anterior) ...

# Define um cookie persistente com validade de 7 dias
@app.route('/definir-cookie-persistente')
def definir_cookie_persistente():
    resposta = make_response("Cookie persistente 'token_autenticacao' definido. Ele expira em 7 dias.")
    # Usamos o parâmetro 'max_age' para definir a duração do cookie em segundos.
    # 60 segundos * 60 minutos * 24 horas * 7 dias = 604800 segundos.
    resposta.set_cookie('token_autenticacao', 'abc123DEF456', max_age=60*60*24*7)
    resposta.set_cookie('meu_cookie_seguro', 'valor', httponly=True)
    # Exemplo para Secure (lembre-se que Secure só funciona plenamente com HTTPS)
    #Em ambiente de desenvolvimento local (http://localhost), ele pode não se comportar como esperado
    resposta.set_cookie('meu_cookie_secure', 'valor', secure=True)
    
    return resposta

# Fim das Rotas

# ... (resto do código) ...

# ... (código anterior) ...

# Lê os cookies recebidos na requisição
@app.route('/ler-cookie')
def ler_cookie():
    # request.cookies é um objeto tipo dicionário que contém todos os cookies
    # que o navegador enviou com a requisição atual.
    # Usamos .get() para evitar erros se o cookie não existir.
    usuario = request.cookies.get('usuario_logado', 'Nenhum cookie de sessão encontrado.')
    token = request.cookies.get('token_autenticacao', 'Nenhum cookie persistente encontrado.')
    return f"""
    <h1>Cookies Atuais</h1>
    <p>Valor do cookie de sessão <strong>'usuario_logado'</strong>: <strong>{usuario}</strong></p>
    <p>Valor do cookie persistente <strong>'token_autenticacao'</strong>: <strong>{token}</strong></p>
    <p><a href="/">Voltar à Página Inicial</a></p>
    """

# Fim das Rotas

# ... (resto do código) ...

# ... (código anterior) ...

# Remove os cookies do navegador
@app.route('/remover-cookie')
def remover_cookie():
    resposta = make_response("Cookies 'usuario_logado' e 'token_autenticacao' removidos com sucesso.")
    # Para remover um cookie, definimos seu valor como vazio e sua data de expiração no passado (expires=0).
    # O navegador, ao receber este Set-Cookie, entende que deve apagar o cookie.
    resposta.set_cookie('usuario_logado', '', expires=0)
    resposta.set_cookie('token_autenticacao', '', expires=0)
    return resposta
    
# Esta seção ficará vazia por enquanto, mas logo adicionaremos mais rotas aqui.
@app.route('/contador-visitas')
def contador_visitas():
    # Tenta obter o valor atual do cookie
    visitas = request.cookies.get('visitas_count')

    # Se existir, incrementa. Se não, inicia com 1.
    if visitas:
        visitas = int(visitas) + 1
    else:
        visitas = 1

    # Cria uma resposta com a mensagem
    resposta = make_response(f"Você visitou esta página {visitas} vezes.")

    # Define o cookie com validade de 1 ano
    expira_em = datetime.now() + timedelta(days=365)
    resposta.set_cookie('visitas_count', str(visitas), expires=expira_em)

    return resposta

@app.route('/ver-carrinho')
def ver_carrinho():
    carrinho = session.get('carrinho', [])
    mensagens = get_flashed_messages(with_categories=True)

    html = ''.join([f"<p class='{cat}'>{msg}</p>" for cat, msg in mensagens])
    html += "<h1>Seu Carrinho:</h1>"

    if carrinho:
        html += "<ul>"
        for item in carrinho:
            html += f"<li>{item}</li>"
        html += "</ul>"
    else:
        html += "<p>O carrinho está vazio.</p>"

    html += """
        <h3>Adicionar itens:</h3>
        <ul>
            <li><a href="/adicionar-ao-carrinho/fone">➕ Fone</a></li>
            <li><a href="/adicionar-ao-carrinho/mouse">➕ Mouse</a></li>
            <li><a href="/adicionar-ao-carrinho/teclado">➕ Teclado</a></li>
            <li><a href="/adicionar-ao-carrinho/monitor">➕ Monitor</a></li>
        </ul>

        <p>
            <a href="/limpar-carrinho">🧹 Limpar Carrinho</a><br>
            <a href="/">🏠 Voltar para Página Inicial</a>
        </p>

        <style>
            .success { color: green; }
            .error { color: red; }
            .info { color: blue; }
            ul { list-style-type: none; padding-left: 0; }
            li { margin-bottom: 6px; }
            a { text-decoration: none; }
        </style>
    """
    return render_template_string(html)

@app.route('/adicionar-ao-carrinho/<item_nome>')
def adicionar_ao_carrinho(item_nome):
    carrinho = session.get('carrinho', [])
    carrinho.append(item_nome)
    session['carrinho'] = carrinho
    flash(f'Item "{item_nome}" adicionado ao carrinho!', 'success')
    return redirect(url_for('ver_carrinho'))

@app.route('/limpar-carrinho')
def limpar_carrinho():
    session.pop('carrinho', None)
    flash('Carrinho limpo com sucesso!', 'info')
    return redirect(url_for('ver_carrinho'))

# Esta seção ficará vazia por enquanto, mas logo adicionaremos mais rotas aqui.
# Fim das Rotas

# Bloco para rodar a aplicação quando o script é executado diretamente
if __name__ == '__main__':
    app.run(debug=True) # debug=True ativa o modo de depuração (reinicia ao salvar e mostra erros)