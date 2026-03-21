# Carteira de Investimentos — Portfolio Live (Atlas)

_Última atualização: 2026-03-21 20:45 UTC_
_Status: validado_

## Snapshot da Carteira (posição atual)

| Ativo | Quantidade | Preço atual (R$) | PM (R$) | Valor de mercado (R$) | P/L não realizado (R$) | P/L não realizado (%) | Peso na carteira (%) |
|---|---:|---:|---:|---:|---:|---:|---:|
| BBAS3 | 1.250 | 23,27 | 19,192952 | 29.087,50 | 5.096,31 | 21,24% | 79,11% |
| BBSE3 | 53 | 34,09 | 19,03 | 1.806,77 | 798,18 | 79,14% | 4,91% |
| EGIE3 | 35 | 31,31 | 26,396571 | 1.095,85 | 171,97 | 18,61% | 2,98% |
| PETR4 | 69 | 45,67 | 32,838986 | 3.151,23 | 885,34 | 39,07% | 8,57% |
| SAPR4 | 200 | 8,14 | 4,05 | 1.628,00 | 818,00 | 100,99% | 4,43% |

## Totais da carteira

- Valor total em ações (R$): **36.769,35**
- Custo total (R$): **28.999,55**
- Resultado não realizado total (R$): **7.769,80**
- Resultado não realizado total (%): **26,79%**

## Automação de atualização (ativa)

Este arquivo está integrado ao webhook de eventos de investimentos do Atlas.

Quando o Atlas receber um `ATLAS_EVENT` válido:

- `event=compra` ou `event=venda` → atualizar automaticamente este arquivo (`portfolio live`), recalculando posição, PM, valor e totais.
- `event=provento` → não altera posição/PM, mas registra evento para reconciliação com o arquivo de proventos.

### Formato operacional do evento (referência)

`ATLAS_EVENT tipo=<provento|compra|venda> ativo=<TICKER> valor=<VALOR> data=<DD/MM/AAAA> fonte=ios_shortcut`

### Política operacional

- Atualização automática é a regra padrão para eventos recebidos por webhook.
- Em caso de inconsistência de campo (ticker inválido, valor ausente, data inválida), o evento deve ser sinalizado para revisão manual.
- Toda atualização automática deve gerar registro no `Log de alterações`.

## Origem dos dados

> **Inativo por enquanto** — esta seção será ativada quando definirmos a estrutura oficial de arquivos e fontes.

## Log de alterações

- 2026-03-21 18:12 UTC — preenchimento inicial com posição consolidada, PM e P/L por ativo.
- 2026-03-21 20:45 UTC — adicionada diretriz formal de automação via webhook (`ATLAS_EVENT`) para atualização automática do portfolio live.
