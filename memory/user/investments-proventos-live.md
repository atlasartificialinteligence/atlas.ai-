# Proventos por Ação — Live (Atlas)

_Última atualização: 2026-03-21 21:02 UTC_
_Status: validado_

## Proventos acumulados por ação (R$)

| Ativo | Proventos acumulados (R$) |
|---|---:|
| BBAS3 | 3.228,21 |
| PETR4 | 2.162,05 |
| BBSE3 | 791,47 |
| EGIE3 | 256,70 |
| SAPR4 | 179,03 |
| ENBR3 | 166,12 |
| AESB3 | 37,08 |

## Total geral

- **R$ 6.820,66**

## Automação de atualização (ativa)

Este arquivo é o destino automático de eventos de proventos recebidos via webhook do Atlas.

Quando o Atlas receber um `ATLAS_EVENT` válido com `event=provento`:

- somar o valor em `Proventos acumulados (R$)` do ativo correspondente;
- criar o ativo na tabela se ainda não existir;
- recalcular o `Total geral`;
- registrar a atualização no `Log de alterações`.

### Formato operacional do evento (referência)

`ATLAS_EVENT tipo=<provento|compra|venda> ativo=<TICKER> valor=<VALOR> data=<DD/MM/AAAA> fonte=ios_shortcut`

### Política operacional

- `event=provento` altera este arquivo automaticamente.
- `event=compra`/`event=venda` não alteram este arquivo diretamente.
- Eventos inválidos/incompletos devem ser bloqueados e sinalizados para revisão.

## Origem dos dados

> **Inativo por enquanto** — esta seção será ativada quando definirmos a estrutura oficial de arquivos e fontes.

## Log de alterações

- 2026-03-21 18:12 UTC — criação do arquivo live de proventos por ação com valores acumulados consolidados.
- 2026-03-21 20:45 UTC — adicionada diretriz formal de automação via webhook (`ATLAS_EVENT`) para atualização automática de proventos.
- 2026-03-21 20:54 UTC — evento `provento` aplicado: PETR4 + R$ 40,03 (fonte: ios_shortcut; data informada: 21/03/2026).
- 2026-03-21 20:57 UTC — reversão manual de teste fictício: PETR4 - R$ 40,03; valores restaurados ao estado original.
- 2026-03-21 21:02 UTC — evento `provento` aplicado: PETR4 + R$ 31,48 (fonte: ios_shortcut; data informada: 20/03/2026).
