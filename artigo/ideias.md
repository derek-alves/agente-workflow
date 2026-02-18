1. Definicao da fundação do projeto(rules)
   Problema: as regras atuais foram definidas no projeto quando nao existiam recursos de otimizacao de contexto(command/skills/subagents), o que acabou ocasionando em rules genéricas e de contextos distintos que sao atraladas a qualquer interacao com o chat do cursor. Isso acaba impactando em alguns pontos importantes: 
	1. degradação do contexto: Mesmo as janelas de contextos sendo grandes hoje em dia(100k), existem estudos falando que a degradacao do contexto é inicializado a partir 25-30k de token, impactando diretamente na assertividade dos resultados
	2. Sobrecarga de informação: Cada token adicional reduz a influência dos anteriores. Muito contexto aumenta custo computacional e piora a capacidade do modelo de focar no que importa.
	3. Custo adicional: Adicao de contexto desnecessário está ligado diretamente a maiores utilizacao de tokens e consequentemente maior custo monetario
	No cenário atual está sendo carregados 7 rules de contextos diferentes para qualquer interacao, passando por todos os problemas citados a cima.
	A soulacao proposta seria converter a rules importantes para skills e criar rules de função que iria agregar valor em cada execucao, essa estrutura iria ser composta pela combinacao de duas fundaçoes
	 - escopo do projeto: vai conter todas definicoes do projeto que sao importantes manter para todos contexto: versão das ferramentas, padrao arquitetural, servicos, etc..
	 - escopo de feature: vai conter definições que sejam importantes para feature tais como as infraestrutura dos dados realtime, servicos, produtos, etc...
2. Definicao das ferramentas core do projeto(subagents especialidazados, skills,commands,rules)
   Essa é uma das etapas mais importantes por que vai ser necessário definir todos os padroes core do projeto referentes a desenvolvimento de software, sendo necessário responder algumas perguntas: Qual visão do time sobre qualidade de código? qual o padrao de testes do projeto? como deve ser coordenado uma execucao de uma tarefa? Qual visão sobre seguranca? 
   Com a resposta de todas essas perguntas vai ser possivel definir todo o nosso kit de skills e agentes que vao estar ligado diretamente na assertividade e na qualidade dos resultados gerados. sao essas coisas que vao viabilizar o ganho real de produtividade e a padronizacao da qualidade do código entre todos os times da empresa.
   
   Proposta de estrutura:
   **Tier 1: Workflow Orchestrators (Gerência e Visão Geral)**
	- mobile-architect: Gerencia arquitetura (Clean Arch), Design System e State Management. Garante consistência entre módulos.
	- feature-software-engineer: Executor ponta-a-ponta de features (scaffold, implement, test). Constrói as telas e lógica.
	- test-engineer: Garante qualidade de testes unitários/widget e cenários BDD (Happy Path, Edge Cases).
	- code-quality: Guardião de padrões de código, linter, performance e complexidade ciclomática.

	**Tier 2: Specialized Execution (Infraestrutura & Core)**
	- flutter-platform-engineer: Mantém o "Design System", Networking, Storage Local e utilitários globais usados pelos times.
	- security-mobile: Foca em OWASP Mobile, validação de root, pinning de certificado e criptografia.
	- analytics-specialist: Governança de dados e taxonomia, garantindo consistência nos eventos de analytics.
	- docs-maintainer: Mantém documentação viva, KDocs/DartDocs e diagramas de arquitetura.

	**Tier 3: Domain Specialists (Regras de Negócio / Squads)**
	- investments-specialist: Fornece regras de negócio de investimentos (ex: cálculo de IR).
	- fx-specialist: Especialista em Câmbio, taxas em tempo real e compliance cambial.\
	- cards-specialist: Domínio de Cartões (fatura, limite, PCI-DSS).
	- onboarding-specialist: Especialista em Cadastro, KYC, biometria e documentoscopia.
   
3. Agente de implementação central: Orquestra subagents, controle de memória, otimizacao de recursos
   O Orquestrador atua como o cérebro central, tratando os subagentes como funções stateless isoladas que recebem um contexto específico e retornam um artefato padronizado. Os subagentes não possuem acesso direto à memória do projeto; eles operam exclusivamente com o Contexto Injetado pelo orquestrador no momento da execução (ex: "Aqui está o resumo do Report X, seu objetivo é Y").

	Essa arquitetura resolve o problema de alucinação e "amnésia" através de três camadas de persistência:
	1. Registry (_registry.md): Atua como a Memória de Longo Prazo do orquestrador. Antes de qualquer ação, o orquestrador consulta este índice para entender o estado atual do projeto e o que já foi construído, garantindo continuidade entre sessões e evitando retrabalho.
	
	2. Reports Padronizados (reports/): É o protocolo de comunicação. Os subagentes não "conversam" entre si; eles geram relatórios (em Markdown) que servem como input para os próximos agentes. Isso cria um Audit Trail completo de cada decisão tomada.
	
	3. Tech Debt (_tech-debt.md): Funciona como um Buffer de Foco. Se um subagente encontra um problema fora do seu escopo imediato, ele não desvia para corrigir. Em vez disso, ele registra o item como Débito Técnico para ser priorizado futuramente, mantendo a execução atual limpa e objetiva
		   

