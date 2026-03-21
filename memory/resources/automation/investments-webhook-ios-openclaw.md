# Automação de Investimentos (iOS + XP + OpenClaw)

_Data: 2026-03-21_
_Status: concluído e operacional_

## Objetivo

Construir um fluxo prático e confiável para atualizar automaticamente os arquivos live de investimentos do Atlas, reduzindo fricção operacional e dependência de registro manual em conversa.

Objetivo específico:

1. receber eventos de investimentos no iPhone;
2. enviar esses eventos ao OpenClaw com segurança;
3. atualizar automaticamente os arquivos de referência da carteira:
   - `memory/user/investments-portfolio-live.md`
   - `memory/user/investments-proventos-live.md`

## Contexto e restrições

- Corretora: XP.
- Plataforma móvel: iOS.
- Limitação crítica: iOS não permite captura totalmente automática de notificações de apps de terceiros (como XP) em background de forma livre.
- Conclusão prática: o melhor modelo viável é **atalho com entrada rápida + envio automático por webhook**.

## O que foi implementado

## 1) Padronização dos arquivos live

Foram consolidados dois arquivos principais para operação contínua:

- `memory/user/investments-portfolio-live.md`
- `memory/user/investments-proventos-live.md`

Outros arquivos transitórios anteriores de investimentos foram removidos para manter uma base limpa e única.

## 2) Webhook de ingestão no OpenClaw

Configuração aplicada no OpenClaw:

- hooks habilitados;
- token dedicado de autenticação;
- restrições de segurança (agent permitido, session policy, limite de body);
- mapeamento de endpoint:
  - `POST /hooks/investments`

Esse endpoint recebe payload JSON simples (event/ativo/valor/data/fonte) e aciona processamento interno.

## 3) Conectividade iPhone → OpenClaw via Tailnet

Como o gateway estava em loopback, foi ajustado para bind em tailnet e validado acesso no IP tailnet:

- `http://100.106.52.10:18789/hooks/investments`

No atalho iOS, envio com:

- `Authorization: Bearer <token>`
- `Content-Type: application/json`
- body JSON com os campos do evento.

## 4) Fluxo validado em produção (com teste controlado)

- Erro inicial identificado: uso indevido de `/hooks/agent` sem campo `message` (`message required`).
- Correção aplicada: troca para `/hooks/investments` com body compatível.
- Evento de provento foi recebido e aplicado automaticamente.
- Reversão manual do valor de teste fictício foi realizada e logada corretamente.

## Aprendizados principais

1. **Automação total passiva não é realista no iOS para esse caso** (notificação XP), mas automação de baixo atrito é plenamente viável.
2. **Endpoint correto + payload correto** são o núcleo da confiabilidade.
3. **Padronizar dois arquivos live** reduz complexidade e evita drift de memória.
4. **Registrar log de alterações** é essencial para auditabilidade.
5. Em automações financeiras, é obrigatório ter caminho de reversão para testes fictícios.

## Resultado final

Estado final alcançado:

- fluxo iOS Shortcut → webhook OpenClaw funcional;
- atualização automática dos arquivos live habilitada;
- base de investimentos simplificada e operacional;
- processo auditável com logs em arquivo.

## Padrão reutilizável para futuras automações

Arquitetura replicável:

1. captura leve no cliente (atalho/form);
2. webhook seguro com token;
3. parser/evento padronizado;
4. aplicação determinística em memória operacional;
5. log de alteração + mecanismo de reversão.

Esse padrão pode ser reutilizado para:

- despesas pessoais;
- fluxo de tarefas recorrentes;
- eventos de RH/operação no negócio;
- monitoramento periódico com reconciliação.

## Próximas ideias

1. criar atalhos separados para `provento`, `compra`, `venda` com payload já fechado;
2. adicionar idempotência por `event_id` para evitar duplicidade;
3. criar rotina de reconciliação semanal (check de consistência);
4. incluir resposta estruturada do webhook para confirmação explícita de sucesso/erro no iPhone;
5. evoluir para transformação determinística (script dedicado) quando o volume de eventos crescer.
