
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
    <title>PrimeTech - Software Engineering</title>
    <style>
        :root {
            --bg-deep: #07070c;
            --bg-card: #10101a;
            --bg-card-hover: #161624;
            --accent-cyan: #00f2fe;
            --accent-blue: #4facfe;
            --accent-purple: #7f00ff;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
            --border-glow: rgba(0, 242, 254, 0.2);
        }

        * { box-sizing: border-box; }

        body {
            background-color: var(--bg-deep);
            color: var(--text-main);
            font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* Fundo com efeito subtil de prédios/cidade e grelha tecnológica */
        .tech-bg {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: 
                linear-gradient(to bottom, rgba(7,7,12,0.85), rgba(7,7,12,0.95)),
                radial-gradient(circle at 50% 20%, rgba(127,0,255,0.15) 0%, transparent 50%),
                repeating-linear-gradient(0deg, transparent, transparent 50px, rgba(255,255,255,0.01) 50px, rgba(255,255,255,0.01) 51px);
            z-index: -1;
        }

        /* Silhueta subtil de prédios no fundo */
        .city-silhouette {
            position: fixed;
            bottom: 0; left: 0; width: 100%; height: 180px;
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none"><path d="M0,120 L0,90 L30,90 L30,60 L50,60 L50,120 L80,120 L80,40 L110,40 L110,120 L150,120 L150,30 L180,30 L180,120 L220,120 L220,70 L250,70 L250,120 L300,120 L300,20 L340,20 L340,120 L400,120 L400,50 L430,50 L430,120 L480,120 L480,10 L520,10 L520,120 L580,120 L580,45 L610,45 L610,120 L660,120 L660,25 L700,25 L700,120 L760,120 L760,60 L790,60 L790,120 L850,120 L850,15 L890,15 L890,120 L950,120 L950,40 L980,40 L980,120 L1040,120 L1040,30 L1080,30 L1080,120 L1200,120 Z" fill="%230b0b14" opacity="0.4"/></svg>') repeat-x;
            z-index: -1;
            pointer-events: none;
        }

        header {
            padding: 1.2rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(11, 11, 20, 0.8);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255,255,255,0.08);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .logo {
            font-size: 1.6rem;
            font-weight: 800;
            color: #fff;
            letter-spacing: -0.5px;
        }
        .logo span { color: var(--accent-cyan); text-shadow: 0 0 15px rgba(0,242,254,0.5); }

        .header-contacts {
            display: flex;
            gap: 1rem;
            align-items: center;
        }

        .contact-pill {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.1);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            color: var(--text-main);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.3s ease;
        }
        .contact-pill:hover {
            border-color: var(--accent-cyan);
            box-shadow: 0 0 10px rgba(0,242,254,0.2);
        }

        .hero {
            padding: 5rem 5% 3rem 5%;
            text-align: center;
            max-width: 1000px;
            margin: 0 auto;
        }

        .hero h1 {
            font-size: 3rem;
            font-weight: 900;
            margin-bottom: 1.5rem;
            letter-spacing: -1.5px;
            color: #fff;
            line-height: 1.2;
        }

        .hero h1 span {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            font-size: 1.2rem;
            color: var(--text-muted);
            margin-bottom: 2.5rem;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }

        /* Barra de Pesquisa de Serviços */
        .search-container {
            max-width: 600px;
            margin: 0 auto 3rem auto;
            position: relative;
        }

        .search-input {
            width: 100%;
            padding: 1rem 1.5rem 1rem 3rem;
            background: rgba(19, 19, 31, 0.9);
            border: 1px solid rgba(0, 242, 254, 0.3);
            border-radius: 30px;
            color: #fff;
            font-size: 1rem;
            outline: none;
            box-shadow: 0 0 25px rgba(0, 242, 254, 0.1);
            transition: all 0.3s ease;
        }

        .search-input:focus {
            border-color: var(--accent-cyan);
            box-shadow: 0 0 30px rgba(0, 242, 254, 0.3);
        }

        .search-icon {
            position: absolute;
            left: 1.2rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--accent-cyan);
            font-size: 1.1rem;
        }

        .cta-btn {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
            color: var(--bg-deep);
            padding: 0.9rem 2.5rem;
            font-size: 1rem;
            font-weight: 800;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
            box-shadow: 0 0 25px rgba(0, 242, 254, 0.4);
            display: inline-block;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .cta-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 0 35px rgba(0, 242, 254, 0.6);
        }

        /* Secção de Serviços Flutuantes (Um em cima do outro) */
        .section {
            padding: 4rem 5%;
            max-width: 900px;
            margin: 0 auto;
        }

        .section-title {
            font-size: 2rem;
            margin-bottom: 2.5rem;
            text-align: center;
            color: #fff;
            font-weight: 800;
            letter-spacing: -0.5px;
        }

        .services-stack {
            display: flex;
            flex-direction: column;
            gap: 1.2rem;
        }

        .service-card {
            background-color: var(--bg-card);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 1.8rem;
            position: relative;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        .service-card:hover {
            background-color: var(--bg-card-hover);
            border-color: var(--accent-cyan);
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(0, 242, 254, 0.15);
        }

        .service-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 4px; height: 100%;
            background: linear-gradient(180deg, var(--accent-cyan), var(--accent-purple));
            border-radius: 14px 0 0 14px;
        }

        .service-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.8rem;
        }

        .service-card h3 {
            color: #fff;
            margin: 0;
            font-size: 1.25rem;
            font-weight: 700;
        }

        .service-badge {
            font-size: 0.75rem;
            background: rgba(0, 242, 254, 0.1);
            color: var(--accent-cyan);
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-weight: 600;
            border: 1px solid rgba(0, 242, 254, 0.2);
        }

        .service-card p {
            color: var(--text-muted);
            margin: 0;
            font-size: 0.95rem;
            line-height: 1.5;
        }

        /* Botão Flutuante do WhatsApp */
        .whatsapp-float {
            position: fixed;
            bottom: 25px;
            right: 25px;
            background: #25d366;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            box-shadow: 0 4px 20px rgba(37, 211, 102, 0.5);
            z-index: 1000;
            text-decoration: none;
            transition: transform 0.3s ease;
        }
        .whatsapp-float:hover {
            transform: scale(1.1);
        }

        footer {
            text-align: center;
            padding: 3rem 2rem;
            color: var(--text-muted);
            border-top: 1px solid rgba(255,255,255,0.05);
            font-size: 0.9rem;
            background: rgba(7,7,12,0.95);
        }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2.2rem; }
            .header-contacts { display: none; }
        }
    </style>
</head>
<body>

    <div class="tech-bg"></div>
    <div class="city-silhouette"></div>

    <header>
        <div class="logo">Prime<span>Tech</span></div>
        <div class="header-contacts">
            <a href="tel:+5511999999999" class="contact-pill">📞 +55 (11) 99999-9999</a>
            <a href="https://wa.me/5511999999999" target="_blank" class="contact-pill" style="border-color: #25d366; color: #25d366;">💬 WhatsApp Direto</a>
        </div>
    </header>

    <section class="hero">
        <h1>Engenharia de Software de Elite para <span>Ecossistemas Digitais</span>.</h1>
        <p>Desenvolvemos aplicações web robustas, microsserviços de alta performance e arquiteturas em nuvem desenhadas para escalar o seu negócio globalmente nas plataformas Upwork, Fiverr e LinkedIn.</p>
        
        <!-- Barra de Pesquisa Interativa -->
        <div class="search-container">
            <span class="search-icon">🔍</span>
            <input type="text" id="serviceSearch" class="search-input" placeholder="Pesquisar serviços (ex: SaaS, Cloud, APIS, Segurança)..." onkeyup="filterServices()">
        </div>

        <a href="https://wa.me/5511999999999" target="_blank" class="cta-btn">Solicitar Diagnóstico & Arquitetura Gratuita</a>
    </section>

    <section class="section">
        <h2 class="section-title">Nossos 20 Principais Serviços de Engenharia</h2>
        
        <div class="services-stack" id="servicesList">
            
            <div class="service-card" data-name="desenvolvimento de saas plataformas web cloud">
                <div class="service-header">
                    <h3>1. Desenvolvimento de Plataformas SaaS do Zero</h3>
                    <span class="service-badge">Alta Demanda</span>
                </div>
                <p>Construção completa de softwares como serviço prontos para monetização, com foco em retenção de utilizadores e alta escalabilidade financeira.</p>
            </div>

            <div class="service-card" data-name="arquitetura de microsservicos backend cloud">
                <div class="service-header">
                    <h3>2. Arquitetura de Microsserviços Escaláveis</h3>
                    <span class="service-badge">Enterprise</span>
                </div>
                <p>Descentralização de sistemas monolíticos pesados em módulos independentes, garantindo que falhas isoladas não derrubem a sua operação.</p>
            </div>

            <div class="service-card" data-name="integracao de apis sistemas legados gateways">
                <div class="service-header">
                    <h3>3. Integração de APIs e Sistemas Legados</h3>
                    <span class="service-badge">Essencial</span>
                </div>
                <p>Conexão perfeita entre o seu software antigo e ferramentas modernas de pagamento, ERPs, CRMs e inteligência artificial externa.</p>
            </div>

            <div class="service-card" data-name="otimizacao de performance e velocidade web">
                <div class="service-header">
                    <h3>4. Otimização Extrema de Performance e Velocidade</h3>
                    <span class="service-badge">Performance</span>
                </div>
                <p>Redução drástica do tempo de carregamento de páginas e consultas lentas à base de dados, elevando a conversão de vendas.</p>
            </div>

            <div class="service-card" data-name="modernizacao de sistemas legados refatoracao">
                <div class="service-header">
                    <h3>5. Modernização e Refatoração de Código Legado</h3>
                    <span class="service-badge">Manutenção</span>
                </div>
                <p>Limpeza, reescrita e otimização de códigos antigos e instáveis, tornando o sistema seguro e fácil de atualizar pela sua equipa.</p>
            </div>

            <div class="service-card" data-name="migracao para nuvem aws cloud architecture">
                <div class="service-header">
                    <h3>6. Migração e Gestão de Infraestrutura em Nuvem (AWS/Azure)</h3>
                    <span class="service-badge">Cloud</span>
                </div>
                <p>Transferência segura da sua operação para servidores elásticos na nuvem, garantindo estabilidade total mesmo em picos de tráfego.</p>
            </div>

            <div class="service-card" data-name="automacao de processos e robos rpa">
                <div class="service-header">
                    <h3>7. Automação Avançada de Processos e Workflows</h3>
                    <span class="service-badge">Produtividade</span>
                </div>
                <p>Eliminação de tarefas manuais repetitivas através de robôs de software e scripts inteligentes integrados ao seu ecossistema.</p>
            </div>

            <div class="service-card" data-name="dashboards de analise de dados em tempo real">
                <div class="service-header">
                    <h3>8. Painéis de Business Intelligence e Analytics em Tempo Real</h3>
                    <span class="service-badge">Dados</span>
                </div>
                <p>Criação de dashboards interativos para monitorização de KPIs, métricas de vendas e comportamento de utilizadores ao vivo.</p>
            </div>

            <div class="service-card" data-name="seguranca da informacao cibernetica lgpd compliance">
                <div class="service-header">
                    <h3>9. Blindagem de Segurança e Compliance de Dados</h3>
                    <span class="service-badge">Segurança</span>
                </div>
                <p>Implementação de protocolos rígidos de encriptação de ponta a ponta, prevenção contra ataques e conformidade com leis de privacidade.</p>
            </div>

            <div class="service-card" data-name="desenvolvimento de aplicativos mobile multiplataforma">
                <div class="service-header">
                    <h3>10. Desenvolvimento de Aplicações Mobile Nativas e Híbridas</h3>
                    <span class="service-badge">Mobile</span>
                </div>
                <p>Criação de aplicativos para iOS e Android de alta fluidicidade, integrados com notificações push e geolocalização.</p>
            </div>

            <div class="service-card" data-name="pipelines de ci cd automacao de deploys devops">
                <div class="service-header">
                    <h3>11. Implementação de Pipelines de CI/CD (DevOps)</h3>
                    <span class="service-badge">DevOps</span>
                </div>
                <p>Automatização completa do processo de testes e publicação de novas versões do seu software sem interrupção do serviço.</p>
            </div>

            <div class="service-card" data-name="solucoes de comercio eletronico enterprise e-commerce">
                <div class="service-header">
                    <h3>12. E-commerce Enterprise de Alta Conversão</h3>
                    <span class="service-badge">E-commerce</span>
                </div>
                <p>Lojas virtuais personalizadas preparadas para lidar com milhões de acessos simultâneos sem lentidão no checkout.</p>
            </div>

            <div class="service-card" data-name="implementacao de inteligência artificial e modelos de llm">
                <div class="service-header">
                    <h3>13. Integração de Inteligência Artificial e Chatbots Avançados</h3>
                    <span class="service-badge">IA & Inovação</span>
                </div>
                <p>Incorporação de modelos de linguagem (LLMs) e assistentes virtuais inteligentes treinados com os dados internos da sua empresa.</p>
            </div>

            <div class="service-card" data-name="desenvolvimento de portais corporativos e intranets">
                <div class="service-header">
                    <h3>14. Desenvolvimento de Portais Corporativos e Intranets</h3>
                    <span class="service-badge">Corporativo</span>
                </div>
                <p>Sistemas internos seguros para gestão de equipas, partilha de documentos confidenciais e controlo de acessos hierárquicos.</p>
            </div>

            <div class="service-card" data-name="auditoria de codigo fonte e testes de qualidade qa">
                <div class="service-header">
                    <h3>15. Auditoria de Código e Garantia de Qualidade (QA)</h3>
                    <span class="service-badge">Qualidade</span>
                </div>
                <p>Revisão profunda por especialistas para detetar bugs ocultos, falhas de arquitetura e gargalos de desempenho no seu software atual.</p>
            </div>

            <div class="service-card" data-name="criacao de bases de dados de alta performance sql nosql">
                <div class="service-header">
                    <h3>16. Modelação e Otimização de Bases de Dados (SQL/NoSQL)</h3>
                    <span class="service-badge">Data Engineering</span>
                </div>
                <p>Estruturação de bases de dados complexas capazes de processar milhões de registos por segundo com índices ultrarrápidos.</p>
            </div>

            <div class="service-card" data-name="consultoria de arquitetura de software estrategica cto">
                <div class="service-header">
                    <h3>17. Consultoria Estratégica de Tecnologia e CTO as a Service</h3>
                    <span class="service-badge">Consultoria</span>
                </div>
                <p>Aconselhamento técnico executivo para escolher as melhores tecnologias, reduzir custos de servidores e planear o roadmap do produto.</p>
            </div>

            <div class="service-card" data-name="desenvolvimento de web3 contratos inteligentes blockchain">
                <div class="service-header">
                    <h3>18. Soluções em Blockchain e Contratos Inteligentes</h3>
                    <span class="service-badge">Web3</span>
                </div>
                <p>Desenvolvimento de aplicações descentralizadas e contratos inteligentes seguros para auditoria e transações digitais auditáveis.</p>
            </div>

            <div class="service-card" data-name="gestao de incidentes e suporte tecnico 24 7">
                <div class="service-header">
                    <h3>19. Suporte Técnico Crítico e Monitorização 24/7</h3>
                    <span class="service-badge">Suporte</span>
                </div>
                <p>Vigilância proativa da saúde dos seus servidores e aplicações com resposta imediata a qualquer queda ou anomalia operacional.</p>
            </div>

            <div class="service-card" data-name="redesenho de interfaces ui ux e experiencia do utilizador">
                <div class="service-header">
                    <h3>20. Redesenho Completo de UI/UX e Experiência do Utilizador</h3>
                    <span class="service-badge">Design System</span>
                </div>
                <p>Transformação visual de interfaces confusas em painéis modernos, intuitivos e altamente agradáveis que cativam o cliente final.</p>
            </div>

        </div>
    </section>

    <!-- Botão Flutuante WhatsApp -->
    <a href="https://wa.me/5511999999999" target="_blank" class="whatsapp-float" title="Falar no WhatsApp">
        💬
    </a>

    <footer>
        <p>&copy; 2026 PrimeTech. Todos os direitos reservados. Engenharia de Software focada em resultados globais.</p>
    </footer>

    <script>
        // Script de pesquisa em tempo real para os serviços
        function filterServices() {
            let input = document.getElementById('serviceSearch').value.toLowerCase();
            let cards = document.getElementsByClassName('service-card');

            for (let i = 0; i < cards.length; i++) {
                let text = cards[i].getAttribute('data-name');
                if (text.includes(input)) {
                    cards[i].style.display = "";
                } else {
                    cards[i].style.display = "none";
                }
            }
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=1800, scrolling=True)
