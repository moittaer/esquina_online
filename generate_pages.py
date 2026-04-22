import os
import re

# Set correct paths
input_html_path = 'index.html'

# Read original index
with open(input_html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Extract header, footer, etc.
head_split = html_content.split('<!-- 1. HERO -->')
top_part = head_split[0]
bottom_split = head_split[1].split('<!-- 7. FOOTER -->')
main_original = bottom_split[0]
footer_part = '<!-- 7. FOOTER -->' + bottom_split[1]

# Re-point navigation in top_part and footer_part to index.html
top_part = top_part.replace('href="#', 'href="index.html#')
footer_part = footer_part.replace('href="#', 'href="index.html#')

# Fix button hire back to contact
top_part = top_part.replace('href="index.html#contact" class="btn-hire"', 'href="#contact" class="btn-hire"')

# Read the contact form string from index to re-use
contact_str = html_content[html_content.find('<!-- 6. CONTATO -->'):html_content.find('<!-- 7. FOOTER -->')]

# Define repetitive block
bloco_repetido = """
<!-- BLOCO REPETIDO -->
<section class="section" id="why-us" style="background: linear-gradient(160deg,#f0f9ff 0%,#faf5ff 40%,#fdf2f8 70%,#fffbeb 100%); color: var(--black);">
  <div style="text-align: center; margin-bottom: 3rem;">
    <span class="section-label">Diferencial</span>
    <h2 class="section-title" style="color: var(--black);">Por que escolher a Esquina Online?</h2>
  </div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; max-width: 1200px; margin: 0 auto;">
    
    <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 2rem;">
      <span class="step-num" style="min-width: auto; font-size: 1.8rem;">01/</span>
      <div class="step-text" style="width: 100%;">
        <h3 style="margin-bottom: 0.8rem; font-size: 1.2rem;">Imersão Completa</h3>
        <p style="font-size: 0.95rem; color: var(--g600); line-height: 1.6; font-family: var(--fb); font-weight: 500;">Mergulhamos no seu negócio para entender desafios e objetivos. Estratégias que fazem sentido para sua realidade.</p>
      </div>
    </div>

    <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 2rem;">
      <span class="step-num" style="min-width: auto; font-size: 1.8rem;">02/</span>
      <div class="step-text" style="width: 100%;">
        <h3 style="margin-bottom: 0.8rem; font-size: 1.2rem;">Soluções Únicas</h3>
        <p style="font-size: 0.95rem; color: var(--g600); line-height: 1.6; font-family: var(--fb); font-weight: 500;">Sem fórmulas prontas. Cada projeto é único. Soluções sob medida para suas necessidades específicas.</p>
      </div>
    </div>

    <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 2rem;">
      <span class="step-num" style="min-width: auto; font-size: 1.8rem;">03/</span>
      <div class="step-text" style="width: 100%;">
        <h3 style="margin-bottom: 0.8rem; font-size: 1.2rem;">Expertise</h3>
        <p style="font-size: 0.95rem; color: var(--g600); line-height: 1.6; font-family: var(--fb); font-weight: 500;">15 anos de experiência. R$20 milhões em campanhas. Certificados pelas maiores plataformas do mundo.</p>
      </div>
    </div>

    <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 2rem;">
      <span class="step-num" style="min-width: auto; font-size: 1.8rem;">04/</span>
      <div class="step-text" style="width: 100%;">
        <h3 style="margin-bottom: 0.8rem; font-size: 1.2rem;">Resultados Reais</h3>
        <p style="font-size: 0.95rem; color: var(--g600); line-height: 1.6; font-family: var(--fb); font-weight: 500;">Obsessão por dados que viram resultados. ROI, ROAS, CPA. Sucesso medido em crescimento real.</p>
      </div>
    </div>

    <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 2rem;">
      <span class="step-num" style="min-width: auto; font-size: 1.8rem;">05/</span>
      <div class="step-text" style="width: 100%;">
        <h3 style="margin-bottom: 0.8rem; font-size: 1.2rem;">Alto Impacto</h3>
        <p style="font-size: 0.95rem; color: var(--g600); line-height: 1.6; font-family: var(--fb); font-weight: 500;">Campanhas que ressoam com seu público. Alto impacto que fortalece marca e impulsiona crescimento.</p>
      </div>
    </div>

    <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 2rem;">
      <span class="step-num" style="min-width: auto; font-size: 1.8rem;">06/</span>
      <div class="step-text" style="width: 100%;">
        <h3 style="margin-bottom: 0.8rem; font-size: 1.2rem;">Proximidade</h3>
        <p style="font-size: 0.95rem; color: var(--g600); line-height: 1.6; font-family: var(--fb); font-weight: 500;">Extensão da sua equipe. Parceria transparente, comunicação clara e acessibilidade total sempre.</p>
      </div>
    </div>

  </div>
</section>
<!-- /BLOCO REPETIDO -->
"""

pages = [
    {
        'file': 'midia-digital.html',
        'title': 'Mídia Digital',
        'subtitle': 'Alcance, Engajamento e Conversão',
        'main_content': """
  <section class="section" style="background: var(--black); padding-top: 2rem; position: relative;">
    <div class="hero-inner" style="grid-template-columns: 1fr; max-width: 900px; margin: 0 auto; display: block;">
      <div style="font-size: 1.15rem; line-height: 1.8; color: var(--g300); margin-bottom: 3rem; text-align: left;">
        <p style="margin-bottom: 1.5rem;">Não existe uma plataforma única que funcione para todos. Cada rede social, cada mecanismo de busca, cada canal de mídia atrai públicos diferentes em momentos diferentes.</p>
        <p style="margin-bottom: 1.5rem;">O verdadeiro poder do marketing digital moderno está em estar presente exatamente onde seus clientes estão conectados, com a mensagem certa, no formato certo e no momento certo. Dominar múltiplas plataformas não é sobre estar em todos os lugares, é sobre estar nos lugares que importam para o seu negócio.</p>
        <p style="margin-bottom: 1.5rem;">Na Esquina, entendemos que cada cliente é único e cada negócio tem suas próprias necessidades. Por isso, não oferecemos soluções genéricas. Analisamos profundamente seu público, seus objetivos e seu mercado para desenhar um mix de plataformas que maximize seu retorno.</p>
        <p>Seja impulsionando as vendas de um e-commerce, orquestrando o mix de mídia de uma campanha política ou conectando o seu B2B que encontra seus clientes no LinkedIn, temos a experiência para encontrar a melhor solução para o seu negócio.</p>
      </div>

      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); padding: 3rem; border-radius: 20px; text-align: center;">
        <h3 style="font-family: var(--fd); font-size: 1.8rem; color: var(--white); margin-bottom: 1rem; font-weight: 800; letter-spacing: -0.02em;">Transforme mídia em resultado</h3>
        <p style="color: var(--g400); font-size: 1.05rem; margin-bottom: 2.5rem; line-height: 1.6;">Planejamento, dados e performance para dominar seu mercado com decisões inteligentes.</p>
        
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
          <a href="#" class="btn-outline" style="border-color: rgba(255,255,255,0.2); color: var(--white);">Baixar Mídia Kit</a>
          <a href="#contact" class="btn-play" style="opacity:1; transform:none; animation:none;">Converse com um especialista</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="clients" style="padding-top: 0; padding-bottom: 4rem;">
    <span class="section-label" style="text-align: center;">Plataformas que Operamos</span>
    <div class="carousel-track-wrap" style="margin-top: 2rem;">
      <div class="carousel-track">
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Google Ads</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">YouTube</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Globo</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Netflix</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Disney</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Meta</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Spotify</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">TikTok</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Kwai</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">LinkedIn</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">X</div>
        
        <!-- Repetição para o loop contínuo -->
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Google Ads</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">YouTube</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Globo</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Netflix</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Disney</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Meta</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Spotify</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">TikTok</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">Kwai</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">LinkedIn</div>
        <div class="client-logo" style="color: black; font-weight: bold; font-family: var(--fd);">X</div>
      </div>
    </div>
  </section>
"""
    },
    {
        'file': 'data-driven-dashboard.html',
        'title': 'Data-driven Dashboard',
        'subtitle': '',
        'main_content': """
  <section class="section" style="background: var(--black); padding-top: 2rem; position: relative;">
    <div class="hero-inner" style="grid-template-columns: 1fr; max-width: 900px; margin: 0 auto; display: block;">
      <div style="font-size: 1.15rem; line-height: 1.8; color: var(--g300); margin-bottom: 3rem; text-align: left;">
        <p style="margin-bottom: 1.5rem;">No marketing moderno, a velocidade da decisão é um diferencial competitivo. No entanto, com dados espalhados por múltiplas plataformas (Google Analytics, Meta Ads, CRM, etc.), ter uma visão clara e em tempo real da performance se torna um desafio complexo.</p>
        <p>Nosso serviço de Data-driven Dashboard resolve exatamente isso. Nós coletamos, processamos e visualizamos todos os seus dados de marketing em um único lugar. Construímos painéis personalizados que respondem às perguntas mais importantes do seu negócio, permitindo que você e sua equipe monitorem KPIs, identifiquem tendências e descubram insights sem depender de relatórios manuais. É a clareza que você precisa para otimizar investimentos e acelerar o crescimento com segurança.</p>
      </div>

      <div style="margin-bottom: 4rem;">
        <h3 style="font-family: var(--fd); font-size: 1.8rem; color: var(--white); margin-bottom: 2rem; font-weight: 800; letter-spacing: -0.02em;">Metodologia Esquina</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Planejamento</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Conversamos com o cliente para definir KPI’s e visibilidade do Dashboard.</p>
            </div>
          </div>
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Wireframe</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Desenho de um rascunho do Dashboard para aprovação.</p>
            </div>
          </div>
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Desenvolvimento</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Integração com plataformas, programação de campos e métricas, layout e textos.</p>
            </div>
          </div>
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Manutenção e Otimização</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Acompanhamento, análise e criação de novas páginas, campos ou métricas para acompanhamento.</p>
            </div>
          </div>
        </div>
      </div>

      <div style="background: linear-gradient(135deg, rgba(139,92,246,.15) 0%, rgba(236,72,153,.15) 100%); border: 1px solid rgba(255,255,255,0.1); padding: 3rem; border-radius: 20px; text-align: center;">
        <h3 style="font-family: var(--fd); font-size: 1.8rem; color: var(--white); margin-bottom: 1rem; font-weight: 800; letter-spacing: -0.02em;">Na Esquina, o dado dita a regra.</h3>
        <p style="color: var(--g300); font-size: 1.05rem; line-height: 1.6; margin-bottom: 2rem;">Não deixe o seu crescimento ao acaso. Transforme informações em decisões inteligentes e domine o seu mercado.</p>
        <a href="#contact" class="btn-play" style="opacity:1; transform:none; animation:none; margin: 0 auto;">Converse com um especialista</a>
      </div>
    </div>
  </section>
"""
    },
    {
        'file': 'planejamento-digital.html',
        'title': 'Planejamento Digital',
        'subtitle': '',
        'main_content': """
  <section class="section" style="background: var(--black); padding-top: 2rem; position: relative;">
    <div class="hero-inner" style="grid-template-columns: 1fr; max-width: 900px; margin: 0 auto; display: block;">
      <div style="font-size: 1.15rem; line-height: 1.8; color: var(--g300); margin-bottom: 3rem; text-align: left;">
        <p style="margin-bottom: 1.5rem;">Investir em marketing digital sem um plano é como navegar sem um mapa: você pode até se mover, mas dificilmente chegará ao destino desejado. Muitas campanhas falham não pela execução, mas pela falta de uma estratégia sólida por trás delas.</p>
        <p style="margin-bottom: 1.5rem;">Nosso serviço de Planejamento Digital existe para eliminar o "achismo" e construir uma base sólida para o crescimento. Nós realizamos uma imersão profunda no seu negócio, analisando seu mercado, seus concorrentes, seu público e seus objetivos.</p>
        <p>O resultado é um documento estratégico, um verdadeiro plano de ação que define o quê, porquê, como, onde e quando suas ações de marketing devem acontecer. É a garantia de que suas campanhas nascerão com um propósito claro e um caminho definido para o sucesso.</p>
      </div>

      <div style="margin-bottom: 4rem;">
        <h3 style="font-family: var(--fd); font-size: 1.8rem; color: var(--white); margin-bottom: 2rem; font-weight: 800; letter-spacing: -0.02em;">Nossa Estratégia</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Diagnóstico e Estratégia</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Diagnóstico da presença digital e desenvolvimento da estratégia.</p>
            </div>
          </div>
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Estratégia de Divulgação</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Pesquisa, análise e criação de uma estratégia digital de divulgação.</p>
            </div>
          </div>
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Planejamento de Mídia Online</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Desenvolvimento de uma estratégia de mídia online / tráfego pago.</p>
            </div>
          </div>
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Estratégia de Conteúdo</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Pesquisa, análise e criação de uma estratégia de conteúdo.</p>
            </div>
          </div>
        </div>
      </div>

      <div style="background: linear-gradient(135deg, rgba(139,92,246,.15) 0%, rgba(236,72,153,.15) 100%); border: 1px solid rgba(255,255,255,0.1); padding: 3rem; border-radius: 20px; text-align: center;">
        <h3 style="font-family: var(--fd); font-size: 1.8rem; color: var(--white); margin-bottom: 1rem; font-weight: 800; letter-spacing: -0.02em;">Planejamento que gera escala</h3>
        <p style="color: var(--g300); font-size: 1.05rem; line-height: 1.6; margin-bottom: 2rem;">Do diagnóstico da sua presença digital à estratégia de divulgação em canais como Google, Meta e LinkedIn. O caminho seguro para o seu sucesso começa aqui.</p>
        <a href="#contact" class="btn-play" style="opacity:1; transform:none; animation:none; margin: 0 auto;">Converse com um especialista</a>
      </div>
    </div>
  </section>
"""
    },
    {
        'file': 'vendas-e-gestao-de-leads.html',
        'title': 'Vendas | Gestão de Leads',
        'subtitle': '',
        'main_content': """
  <section class="section" style="background: var(--black); padding-top: 2rem; position: relative;">
    <div class="hero-inner" style="grid-template-columns: 1fr; max-width: 900px; margin: 0 auto; display: block;">
      <div style="font-size: 1.15rem; line-height: 1.8; color: var(--g300); margin-bottom: 3rem; text-align: left;">
        <p style="margin-bottom: 1.5rem;">De que adianta ter um grande volume de leads se eles não se transformam em clientes? Muitas empresas investem pesado para atrair visitantes, mas perdem dinheiro com um funil de vendas ineficiente.</p>
        <p style="margin-bottom: 1.5rem;">Nosso serviço de Vendas e Gestão de Leads atua exatamente nesse ponto crítico.</p>
        <p style="margin-bottom: 1.5rem;">Nós analisamos e otimizamos cada etapa da jornada do seu cliente após o clique: da landingpage ao formulário, da automação de e-mails ao script de vendas.</p>
        <p>Implementamos processos e tecnologias (como CRM e automação de marketing) para garantir que cada lead seja nutrido, qualificado e abordado no momento certo, da maneira certa. O resultado é um processo de vendas mais eficiente, um ciclo de vendas mais curto e, o mais importante, um aumento significativo na sua receita.</p>
      </div>

      <div style="margin-bottom: 4rem;">
        <h3 style="font-family: var(--fd); font-size: 1.8rem; color: var(--white); margin-bottom: 2rem; font-weight: 800; letter-spacing: -0.02em;">Etapas / Serviços Relacionados</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Treinamento SDR</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Treinamento para equipe e desenvolvimento de Scripts.</p>
            </div>
          </div>
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Treinamento Closer</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Treinamento para equipe e desenvolvimento de Scripts.</p>
            </div>
          </div>
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Scripts de Vendas</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Scripts de venda para propostas e apresentações.</p>
            </div>
          </div>
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Consultoria CRM</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Análise e otimização do CRM, ou planejamento para implementação.</p>
            </div>
          </div>
        </div>
      </div>

      <div style="background: linear-gradient(135deg, rgba(139,92,246,.15) 0%, rgba(236,72,153,.15) 100%); border: 1px solid rgba(255,255,255,0.1); padding: 3rem; border-radius: 20px; text-align: center;">
        <h3 style="font-family: var(--fd); font-size: 1.8rem; color: var(--white); margin-bottom: 1rem; font-weight: 800; letter-spacing: -0.02em;">Da captação de Leads ao pós-venda</h3>
        <p style="color: var(--g300); font-size: 1.05rem; line-height: 1.6; margin-bottom: 2rem;">Aqui na Esquina você encontra a solução que você precisa para o seu negócio.</p>
        <a href="#contact" class="btn-play" style="opacity:1; transform:none; animation:none; margin: 0 auto;">Converse com um especialista</a>
      </div>
    </div>
  </section>
"""
    },
    {
        'file': 'desenvolvimento-de-websites.html',
        'title': 'Desenvolvimento de Websites',
        'subtitle': '',
        'main_content': """
  <section class="section" style="background: var(--black); padding-top: 2rem; position: relative;">
    <div class="hero-inner" style="grid-template-columns: 1fr; max-width: 900px; margin: 0 auto; display: block;">
      <div style="font-size: 1.15rem; line-height: 1.8; color: var(--g300); margin-bottom: 3rem; text-align: left;">
        <p style="margin-bottom: 1.5rem;">Seu website é o seu principal ativo de marketing, o destino final de todas as suas campanhas. Um site lento, confuso ou que não funciona bem no celular pode arruinar todo o seu investimento em mídia. É por isso que nosso serviço de Desenvolvimento de Websites vai muito além da estética.</p>
        <p style="margin-bottom: 1.5rem;">Nós construímos a fundação digital do seu negócio com foco em três pilares: Performance, Experiência do Usuário (UX) e Conversão.</p>
        <p>Nossos sites são projetados para carregar em alta velocidade, oferecer uma navegação intuitiva em qualquer dispositivo e guiar o visitante de forma clara em direção à ação desejada. Com as melhores práticas de SEO implementadas desde o início e uma estrutura pronta para análise de dados, seu novo site nascerá pronto para crescer.</p>
      </div>

      <div style="margin-bottom: 4rem;">
        <h3 style="font-family: var(--fd); font-size: 1.8rem; color: var(--white); margin-bottom: 2rem; font-weight: 800; letter-spacing: -0.02em;">Metodologia Esquina</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Planejamento</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Conversamos com o cliente para definir objetivos, referências e alinhar expectativas.</p>
            </div>
          </div>
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Protótipo</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Desenho de um rascunho do website para aprovação.</p>
            </div>
          </div>
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Desenvolvimento</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Programação do site utilizando CMS, configuração de plugins e aplicação do layout e textos finais.</p>
            </div>
          </div>
          <div class="process-step" style="opacity: 1; transform: none; flex-direction: column; gap: 0.5rem; align-items: flex-start; padding: 1.5rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
            <div class="step-text" style="width: 100%;">
              <h3 style="color: var(--orange); margin-bottom: 0.5rem; font-size: 1.1rem;">Manutenção e Otimização</h3>
              <p style="font-size: 0.95rem; color: var(--g400); line-height: 1.6;">Webtracking, configuração de ferramentas de análises e acompanhamento para propor melhorias.</p>
            </div>
          </div>
        </div>
      </div>

      <div style="background: linear-gradient(135deg, rgba(139,92,246,.15) 0%, rgba(236,72,153,.15) 100%); border: 1px solid rgba(255,255,255,0.1); padding: 3rem; border-radius: 20px; text-align: center;">
        <h3 style="font-family: var(--fd); font-size: 1.8rem; color: var(--white); margin-bottom: 1rem; font-weight: 800; letter-spacing: -0.02em;">Velocidade, Design e Estratégia em um só lugar</h3>
        <p style="color: var(--g300); font-size: 1.05rem; line-height: 1.6; margin-bottom: 2rem;">Desenvolvemos sites profissionais com WordPress e Elementor, focados na melhor experiência para o usuário e otimizados para os algoritmos de busca.</p>
        <a href="#contact" class="btn-play" style="opacity:1; transform:none; animation:none; margin: 0 auto;">Converse com um especialista</a>
      </div>
    </div>
  </section>
"""
    }
]

for page in pages:
    hero_section = f"""<main>
  <section class="hero" id="home" style="min-height: 48vh; padding: 10rem 2.5rem 4rem; position: relative; background: var(--black);">
    <div class="gradient-blob" style="width: 40vw; height: 40vw; opacity: 0.4;"></div>
    <div class="hero-inner" style="grid-template-columns: 1fr; text-align: center;">
      <div class="hero-text" style="align-items: center;">
        {f'<p class="hero-eyebrow" style="opacity:1; transform:none; animation:none; color: var(--g400);">{page["subtitle"]}</p>' if page["subtitle"] else ''}
        <h1 class="hero-headline" style="opacity:1; transform:none; animation:none; margin-bottom: 2rem;">
          <span class="hl-static" style="color: var(--white);">{page["title"]}</span>
        </h1>
      </div>
    </div>
  </section>
"""

    page_html = top_part + hero_section + page["main_content"] + bloco_repetido + contact_str + footer_part
    with open(page["file"], 'w', encoding='utf-8') as f:
        f.write(page_html)

print("Pages created successfully.")
