# Cálculo de Preço Médio (PM) — carteira de ações

_Data: 2026-03-20 (UTC)_
_Fonte: `file_21---456963ae-0e8b-4033-a7cb-b6aa7a316a40.xlsx` (aba `Movimentação`)_

## Método usado (resumo auditável)

Para cada ativo:

- Em compra (`Transferência - Liquidação` com `Entrada/Saída = Credito`):
  - `qtd_total += qtd_compra`
  - `custo_total += valor_operacao`
- Em venda (`Transferência - Liquidação` com `Entrada/Saída = Debito`):
  - `PM_atual = custo_total / qtd_total`
  - `custo_baixado = PM_atual * qtd_vendida`
  - `qtd_total -= qtd_vendida`
  - `custo_total -= custo_baixado`
- Em `Desdobro` e `Bonificação em Ativos`:
  - aumenta quantidade
  - custo total não muda

Regra final:

- `PM_final = custo_total / qtd_total`

## Eventos ignorados no PM

Não entram no cálculo de PM por não alterarem custo de aquisição diretamente:

- `Atualização`
- `Transferência` entre corretoras (sem valor de operação)
- direitos de subscrição não exercidos / cessões sem execução de compra

## PM final da carteira atual

- **BBAS3** — 1250 ações — custo total R$ 23.991,19 — **PM = R$ 19,192952**
- **BBSE3** — 53 ações — custo total R$ 1.008,59 — **PM = R$ 19,03**
- **EGIE3** — 35 ações — custo total R$ 923,88 — **PM = R$ 26,396571**
- **PETR4** — 69 ações — custo total R$ 2.265,89 — **PM = R$ 32,838986**
- **SAPR4** — 200 ações — custo total R$ 810,00 — **PM = R$ 4,05**

## Demonstração resumida por ativo (auditoria)

### BBAS3
Compras registradas:
- 23/08/2021: 35 (R$ 1.037,40)
- 15/09/2021: 27 (R$ 802,44)
- 17/06/2022: 61 (R$ 2.049,05)
- 14/11/2022: 58 (R$ 2.151,34)
- 17/11/2022: 41 (R$ 1.476,90)
- 09/06/2025: 56 (R$ 1.254,96)
- 10/06/2025: 350 (R$ 7.625,10)
- 11/08/2025: 200 (R$ 3.800,00)
- 13/08/2025: 200 (R$ 3.794,00)

Eventos corporativos:
- 17/04/2024: desdobro +222 ações (custo inalterado)

Resultado:
- Quantidade final: 1250
- Custo final: R$ 23.991,19
- PM: R$ 19,192952

### BBSE3
- Compra única: 08/09/2021, 53 (R$ 1.008,59)
- PM final: R$ 19,03

### EGIE3
- Compra: 20/08/2021, 25 (R$ 923,88)
- Bonificação: 28/11/2025, +10 ações
- Custo permanece R$ 923,88
- PM final: R$ 26,396571

### PETR4
- Compra única: 10/05/2022, 69 (R$ 2.265,89)
- PM final: R$ 32,838986

### SAPR4
- Compra única: 27/08/2021, 200 (R$ 810,00)
- PM final: R$ 4,05

## Observações importantes

- A transferência de corretora foi tratada corretamente como neutra de PM quando sem valor de operação.
- Em `Transferência - Liquidação`, os valores foram considerados operações efetivas de compra/venda.
- O ativo AESB3 foi totalmente zerado (venda de 497 em 24/09/2024), e ENBR3 também foi zerado.
- Este PM é contábil pela trilha do extrato B3 fornecido.
