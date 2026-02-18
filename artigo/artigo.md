# Arquitetura de Agentes de IA para Desenvolvimento Mobile

## Introdução

### O Cenário Atual
Até pouco tempo atrás, tudo se resumia às tentativas de documentação de padrões importantes em "rules" para que fosse possível reaproveitar conteúdos e funcionalidades. O intuito era nobre, pois buscava aprimorar os resultados ao fornecer contexto prévio ao modelo.

Nesse sentido, o cenário atual dos projetos se mantem na utilização apenas das rules globais e a adoção dessa abordagem impacta diretamente na assertividade da IA. Um exemplo prático que enfrentamos ocorreu quando, ao solicitar uma tarefa simples para o agente, foram atreladas à requisição sete rules com contextos totalmente diferentes.

Porém com a evolução das ferramentas, hoje existem camadas de abstração muito mais sofisticadas que auxiliam nos resultados, tais como commands, **skills e subagents.
Essas novas estruturas permitem que a Inteligência Artificial – IA atue com mais assertividade, sendo capaz de focar em tarefas específicas com maior contexto, evitar erros ou alucinações, além de atingir maior eficiência da utilização dos tokens.


### A Resolução do Problema

A resolução para esse impasse exigiu uma mudança de mentalidade. Entendemos que continuar empilhando "rules" globais era lutar contra a própria natureza evolutiva das ferramentas. A solução não estava em refinar as regras existentes, mas em abraçar as novas camadas de abstração.

Assim, é evidente a necessidade de transicionar de uma abordagem estática para uma arquitetura dinâmica. Ao invés de um único contexto gigante, passamos a definir contextos persistentes que são relevantes para o projeto e para cada feature e a orquestrar agentes especializados que utilizam skills e commands sob demanda. Portanto, a virada de chave é tratar o contexto como um recurso finito e precioso, onde apenas a informação crítica para a tarefa atual é injetada.

### A Solução: Três Pilares

### 1. Fundação: Contexto Persistente

A "Fundação" não é apenas uma rule, é uma estratégia de arquitetura de contexto. A ideia central é que nem todo conhecimento é igual: existe o que é imutável no projeto e o que é variável na feature. O padrão que adotamos quebra o conjunto de "Rules" generalistas em dois escopos distintos que são combinados dinamicamente:

**A. Escopo do Projeto (Global)**
Aqui residem as verdades absolutas que todo agente precisa saber para não quebrar a aplicação.
*   **Tech Stack:** Versões exatas (Flutter 3.x, Java 17, etc).
*   **Padrões Arquiteturais:** Clean Arch, MVVM, estrutura de pastas.
*   **Serviços Core:** Como autenticar, como logar, como fazer networking seguro.
*   **Commands** Os commands disponiveis no projeto.
*   **Skills** As skills disponiveis no projeto.
*   **Subagents** Os subagents disponiveis no projeto.

**B. Escopo de Feature (Local)**
Aqui está o contexto vivo, necessário apenas para quem está trabalhando *naquela* funcionalidade específica.
*   **Infraestrutura de Dados:** Contratos de API específicos da feature, sockets realtime.
*   **Regras de Produto:** Lógica de negócio isolada (ex: cálculo de rendimento de um investimento).
*   **Serviços Locais:** Utilitários que só existem naquele módulo.

**O Impacto na Prática**
Ao adotar essa separação, **eliminamos o ruído**. Quando um agente vai atuar na feature de "Investimentos", ele carrega o *Escopo do Projeto* + *Escopo de Investimentos*. Ele **não** sabe (e nem deve saber) sobre as regras de validação de cartão de crédito ou fluxo de onboarding.

Isso reduz drasticamente a carga cognitiva do modelo. Em vez de injetar 7 arquivos de regras desconexas, injetamos apenas a intersecção exata do que é necessário. O resultado? Menos alucinação, respostas mais rápidas e um custo de token controlado. A fundação deixa de ser um peso morto e vira um trampolim para a assertividade.

### 2. Agentes Especializados em 3 Tiers

Definir a fundação é o primeiro passo, mas quem executa o trabalho? Aqui entra a segunda grande mudança: sair do modelo de "Agente Genérico que faz de tudo" para um time de especialistas.

Essa é uma das etapas mais críticas e deve ser construída **em conjunto com o time**. É preciso alinhar: Qual é a *nossa* visão sobre qualidade? Qual o *nosso* padrão de testes? Como garantimos segurança? A resposta para isso não é um texto solto, mas sim um consenso que será traduzido na criação de agentes que encarnam esses papéis e possuem as **skills** e **commands** necessários para executar o trabalho conforme a visão do time.

Estruturamos em três camadas (Tiers) de responsabilidade:

**Tier 1: Workflow Orchestrators (Gerência e Visão Geral)**
Eles têm a visão do todo. Não necessariamente escrevem cada linha de código, mas garantem que a arquitetura e os requisitos sejam seguidos.
*   **Mobile Architect:** O guardião da Clean Architecture e do State Management. Garante a consistência entre módulos.
*   **Feature Software Engineer:** O executor ponta-a-ponta, constrói as telas e lógica da funcionalidade.
*   **Test Engineer:** Especialista em garantir que nada suba sem cobertura de testes unitários, de widget e cenários de testes.
*   **Code Quality:** O guardião dos padrões, validando linter, complexidade ciclomática e qualidade do código.

**Tier 2: Specialized Execution (Infraestrutura & Core)**
Quando o problema é técnico e profundo, chamamos esses especialistas em infraestrutura.
*   **Flutter Platform Engineer:** Mantém o "Design System", Networking, Storage Local e utilitários globais.
*   **Security Mobile:** Foca em OWASP Mobile, validação de root, pinning de certificado e criptografia.
*   **Analytics Specialist:** Garante a governança de dados e taxonomia nos eventos.
*   **Docs Maintainer:** Mantém a documentação viva, gerando KDocs/DartDocs e diagramas.

**Tier 3: Domain Specialists (Regras de Negócio)**
Aqui vive o conhecimento de negócio que diferencia sua empresa, agindo como squads virtuais.
*   **Investments Specialist:** Fornece regras de negócio de investimentos (ex: cálculo de IR).
*   **Cards Specialist:** Domínio de faturas, limites e PCI-DSS.
*   **Onboarding Specialist:** Cuida de cadastro, KYC e biometria.

Com essa divisão, não pedimos para um "robô" fazer um app de investimentos. Pedimos para o *Mobile Architect* desenhar a solução, o *Feature Engineer* implementar a tela, e o *Investment Specialist* validar a lógica de juros. Cada um com seu contexto, cada um com sua expertise.

### 3. Orquestração com Memória Persistente

O maior vilão dos agentes autônomos é a "amnésia". Um agente resolve um problema complexo agora, mas daqui a 10 minutos, em uma nova sessão, ele esqueceu tudo. Para resolver isso, a proposta é criar um **Agente de Implementação Central** que não retenha conhecimento em si, mas gerencie o fluxo de informação através de recursos persistentes.

A ideia é que ele atue como um orquestrador que trata os subagentes como **funções sem estado interno (stateless)**: insere contexto, pede uma execução, recebe um resumo do que foi feito e encerra o agente. Para que isso funcione sem perda de inteligência, a orquestração será baseada em três pilares de memória:

**A. Histórico  (Memória de Longo Prazo)**
Atuará como o índice mestre do projeto. Antes de qualquer ação, o orquestrador deverá consultar esse recurso para saber o estado atual. O objetivo é que ele responda sempre à pergunta: "O que já foi feito?".
*   *Aplicação:* Antes de criar uma nova skill, o orquestrador verificará no Histórico se já não existe um report recente sobre o tema, evitando retrabalho.

**B. Reports Padronizados (O Protocolo de Comunicação)**
Os agentes não devem "conversar" em chat aberto, mas sim gerar documentos estruturados. Um agente de *Code Quality*, por exemplo, não dirá apenas "está ruim"; ele gerará um report com estrutura fixa (Resumo, Bloqueadores, Sugestões).
*   **Audit Trail:** Criaremos um rastro de decisão. Se a arquitetura mudar, existirá um documento explicando o *porquê*.
*   **Handoff Limpo:** O agente de Segurança não precisará ler todo o código novamente; ele lerá o resumo do Agente de Arquitetura e focará apenas nas vulnerabilidades.

**C. Tech Debt (O Buffer de Foco)**
Este pilar visa manter a produtividade. Se um agente estiver refatorando uma tela e encontrar um bug na API fora do seu escopo, ele **não** deverá desviar para consertar.
*   Ele registrará o problema no backlog de dívida técnica.
*   Continuará sua tarefa original.

Isso impedirá que o agente entre em "rabbit holes" (tocas de coelho), garantindo que cada execução tenha início, meio e fim definidos dentro do escopo planejado.
