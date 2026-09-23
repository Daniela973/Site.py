import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PrimeTech | Engenharia de Software e Soluções Digitais de Elite",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
        }
        .card h3 { color: #fff; margin-top: 0; }
        .card p { color: var(--text-muted); font-size: 0.9rem; }
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
    </header>
    <section class="hero">
        <h1>Engenharia de Software de Elite para <span>Ecossistemas Digitais</span>.</h1>
        <p>Desenvolvemos aplicações web, sistemas corporativos e arquiteturas sob medida.</p>
        <a href="#contato" class="cta-btn">Solicitar Diagnóstico</a>
    </section>
    <section class="section">
        <h2 class="section-title">Cases de Sucesso & Projetos</h2>
        <div class="grid-3">
            <div class="card">
                <h3>SaaS de Gestão & Analytics</h3>
                <p>Plataforma de alta volumetria com painéis em tempo real e infraestrutura em nuvem.</p>
            </div>
            <div class="card">
                <h3>Automação & Logística</h3>
                <p>Microsserviços integrados a múltiplos gateways com baixa latência.</p>
            </div>
            <div class="card">
                <h3>E-commerce Enterprise</h3>
                <p>Focado em conversão extrema e resiliência a picos de tráfego.</p>
            </div>
        </div>
    </section>
    <footer>
        <p>&copy; 2026 PrimeTech. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)
