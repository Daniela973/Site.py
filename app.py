import streamlit as st
import streamlit.components.v1 as components

# Configuração da página para ocupar a largura total e tela cheia (Dark Mode)
st.set_page_config(
    page_title="PrimeTech | Engenharia de Software e Soluções Digitais de Elite",
    page_layout="wide",
    initial_sidebar_state="collapsed"
)

# Código HTML e CSS do site da PrimeTech
html_code = """
<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root {
            --bg-deep: #0b0b14;
            --bg-card: #13131f;
            --accent-cyan: #00f2fe;
            --accent-blue: #4facfe;
            --accent-purple: #7f00ff;
            --text-main: #e2e8f0;
            --text-muted: #94a3b8;
        }
        body {
            background-color: var(--bg-deep);
            color: var(--text-main);
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }
        header {
            padding: 1.5rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: #fff;
            letter-spacing: -0.5px;
        }
        .logo span { color: var(--accent-cyan); }
        
        .hero {
            padding: 4rem 5% 3rem 5%;
            text-align: center;
            max-width: 900px;
            margin: 0 auto;
        }
        .hero h1 {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            letter-spacing: -1px;
            color: #fff;
        }
        .hero h1 span {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero p {
            font-size: 1.1rem;
            color: var(--text-muted);
            margin-bottom: 2rem;
        }
        
        .cta-btn {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            color: var(--bg-deep);
            padding: 0.9rem 2.2rem;
            font-size: 1rem;
            font-weight: 700;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
            box-shadow: 0 0 20px rgba(0, 242, 254, 0.3);
            display: inline-block;
        }

        .section {
            padding: 3rem 5%;
            max-width: 1100px;
            margin: 0 auto;
        }
        .section-title {
            font-size: 1.8rem;
            margin-bottom: 2rem;
            text-align: center;
            color: #fff;
        }
        
        .grid-3 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }
        .card {
            background-color: var(--bg-card);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 1.5rem;
            position: relative;
            overflow: hidden;
        }
        .card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 3px;
            background: linear-gradient(90deg, var(--accent-cyan), var(--accent-purple));
        }
        .card h3 { color: #fff; margin-top: 0; }
        .card p { color: var(--text-muted); font-size: 0.9rem; }

        .platforms-badge {
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
            margin-top: 2.5rem;
            padding: 1rem;
            background: rgba(255,255,255,0.02);
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .badge-item {
            color: var(--text-muted);
            font-weight: 600;
            font-size: 0.8rem;
            letter-spacing: 1px;
        }

        footer {
            text-align: center;
            padding: 2rem;
            color: var(--text-muted);
            border-top: 1px solid rgba(255,255,255,0.05);
            font-size: 0.85rem;
        }
    </style>
</head>
<body>

    <header>
        <div class="logo">Prime<span>Tech</span></div>
        <div><a href="#contato" class="cta-btn" style="padding: 0.5rem 1rem; font-size: 0.85rem;">Iniciar Projeto</a></div>
    </header>

    <section class="hero">
        <h1>Engenharia de Software de Elite para <span>Ecossistemas Digitais</span>.</h1>
        <p>Desenvolvemos aplicações web, sistemas corporativos robustos e arquiteturas em nuvem sob medida para o seu negócio.</p>
        <a href="#contato" class="cta-btn">Solicitar Diagnóstico & Arquitetura Gratuita</a>

        <div class="platforms-badge">
            <span class="badge-item">LINKEDIN</span>
            <span class="badge-item">UPWORK</span>
            <span class="setItem badge-item">FIVERR</span>
            <span class="badge-item">WORKANA</span>
            <span class="badge-item">99FREELAS</span>
        </div>
    </section>

    <section class="section">
        <h2 class="section-title">Cases de Sucesso & Projetos</h2>
        <div class="grid-3">
            <div class="card">
                <h3>SaaS de Gestão & Analytics</h3>
                <p>Plataforma de alta volumetria com painéis em tempo real e infraestrutura elástica em nuvem.</p>
            </div>
            <div class="card">
                <h3>Automação & Logística</h3>
                <p>Microsserviços integrados a múltiplos gateways com redução drástica de latência.</p>
            </div>
            <div class="card">
                <h3>E-commerce Enterprise</h3>
                <p>Focado em conversão extrema e alta resiliência a picos de tráfego corporativo.</p>
            </div>
        </div>
    </section>

    <section class="section" style="background: rgba(255,255,255,0.01);">
        <h2 class="section-title">Especificações Técnicas</h2>
        <div class="grid-3">
            <div class="card">
                <h3>Stack Moderna</h3>
                <p>React.js, Next.js, Node.js, Python/FastAPI, PostgreSQL e AWS Cloud Architecture.</p>
            </div>
            <div class="card">
                <h3>Segurança Máxima</h3>
                <p>Criptografia ponta a ponta e padrões rígidos de proteção de dados corporativos.</p>
            </div>
            <div class="card">
                <h3>Metodologia Ágil</h3>
                <p>Pipelines automatizados de CI/CD e documentação enterprise rigorosa.</p>
            </div>
        </div>
    </section>

    <section id="contato" class="section" style="text-align: center;">
        <h2 class="section-title">Vamos Escalar o seu Negócio?</h2>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem;">Fale diretamente com nossa equipe de arquitetura através das plataformas globais.</p>
        <a href="mailto:contato@primetech.com" class="cta-btn">Falar com Arquiteto</a>
    </section>

    <footer>
        <p>&copy; 2026 PrimeTech. Todos os direitos reservados.</p>
    </footer>

</body>
</html>
"""

# Renderiza o site completo dentro do Streamlit ajustando a altura
components.html(html_code, height=1400, scrolling=True)
