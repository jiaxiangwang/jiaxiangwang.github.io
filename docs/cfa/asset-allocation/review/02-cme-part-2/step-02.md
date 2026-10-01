---
title: "Step 2 — 从盈利、分红与估值拆解 Equity Return"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "02 · 股票回报分解与全球整合"
study: {"section": "Review Course", "module": "CME Part 2", "moduleLink": "/cfa/asset-allocation/review/02-cme-part-2/", "step": 2, "total": 5}
studyNav: {"previous": {"label": "← Previous", "title": "将 Yield、Risk Premium 与实现回报分开", "link": "/cfa/asset-allocation/review/02-cme-part-2/step-01"}, "map": {"label": "Learning Map", "title": "CME Part 2", "link": "/cfa/asset-allocation/review/02-cme-part-2/"}, "next": {"label": "Next Step →", "title": "把租金、Cap Rate 与估值平滑串起来", "link": "/cfa/asset-allocation/review/02-cme-part-2/step-03"}}
---

# 从盈利、分红与估值拆解 Equity Return

::: info 本步目标
能用 Grinold–Kroner 解释回报来源，用 Singer–Terhaar 解释风险补偿，并区分所需溢价、总回报和过渡性重估。
:::

## Why · 为什么盈利增长不能回答所有股票回报问题？

股票持有人既收到分红，也承受股数变化和估值变化。即使企业盈利增长不错，P/E 下调仍可能使一年回报偏低。跨市场比较时，还要判断投资者要求多高的风险补偿。

本步把两个模型的任务分开：**Grinold–Kroner (G–K)** 拆解 expected return 的来源；**Singer–Terhaar** 在不同 integration 程度下估计 equilibrium risk premium。先选对问题，再代入公式。

## Core & Intuition · Cash flow / valuation 与 risk compensation 是两条链

G–K 的顺序是：**收入收益 → 名义盈利增长 → 股数变化 → P/E repricing**。企业整体盈利增长不等于 EPS 增长，因为 issuance 会稀释，repurchases 会提高给定盈利对应的每股份额。

Singer–Terhaar 的顺序是：**市场整合程度 → 哪种风险不能分散 → 对该风险要求补偿**。完全 integrated 的投资者可以全球分散，因此得到补偿的是与 global market 共变的风险；segmented 市场无法充分分散本地风险，所需补偿更接近总风险。

**Intuition：** integration 提高时，风险变得更可分散，长期 required premium 通常下降。折现率下降可以令当前价格重估上涨，所以“过渡期 gain”与“新均衡下较低 required return”可以同时出现。

两种模型都不允许仅凭高 required return 判市场便宜。高所需回报可能只是政治、治理或无法分散风险更高；要谈 valuation attractiveness，还要有价格与预期现金流等信息。

## Example · 澳大利亚股票：把盈利和估值分开算

<p class="source-note">Source: Local 原版书 CME / No.2020012102000004 — adapted；答案为推导。</p>

预期 dividend yield 2.4%、inflation 2.3%、real earnings growth 5%，P/E 从当前 14.5 下降到 14.0，股数不变。

估值贡献是相对变化 $14.0/14.5-1=-3.45\%$，不是负 0.5%。预期股票回报约 $2.4+2.3+5.0-3.45=6.25\%$。若求 forward-looking equity-vs-bonds premium，再扣**当前**匹配国债 yield 2.3%，得到约 3.95%。

题中还给历史债券 yield 和历史股票回报，那是 historical premium 的输入。将历史基准混到 forward-looking calculation，会得到算术正确但问题口径错误的答案。

## CFA Language & Formula

::: info Formula · Must memorize · Grinold–Kroner
现金流增长与估值变化共同决定股票持有人的预期回报：

$$E(R_e)\approx D/P+\pi+g_{real\ earnings}-\Delta S+\Delta(P/E)$$

$\Delta S$ 是净股数增长，repurchases 时为负，所以 $-\Delta S$ 对回报作正贡献。$\Delta(P/E)$ 是相对变化率；多年度题需按题干转为 annualized change。别把 aggregate earnings 与 EPS 重复计算。
:::

::: info Formula · Know how to use · Singer–Terhaar
全球整合时，系统性波动是 $\rho_{i,G}\sigma_i$，以 global Sharpe ratio 定价：

$$RP_i^{int}=\rho_{i,G}\sigma_i\frac{RP_G}{\sigma_G}$$

分割时 $RP_i^{seg}=\sigma_i SR_i$；部分整合时：

$$RP_i=\phi RP_i^{int}+(1-\phi)RP_i^{seg}$$

$\phi$ 是题干给定的 integration weight；$SR_i$ 是给定的本地市场 Sharpe ratio。若求 total return，最后加 $r_f$。例如 fully integrated、$\rho=0.60,\sigma=15\%,SR_G=0.35$，premium 为 3.15%；加 $r_f=1.5\%$ 才得到 4.65%。
:::

**Equity-vs-bonds premium** 是相对指定债券基准的差额；不要默认所有题都以同一短期 risk-free asset 作比较。

## Connection

[Trend Growth](/cfa/asset-allocation/review/01-cme-part-1/step-02) 为长期盈利提供经济边界；[VCV estimation](/cfa/asset-allocation/review/02-cme-part-2/step-05) 提供 Singer–Terhaar 的波动与相关性。[Robust MVO](/cfa/asset-allocation/review/04-principles/step-02) 会同时面对这两类输入的不确定性。

## Exam Focus

- **Exam Trigger — Calculate：** 依次检查 share-repurchase sign、relative P/E change、premium vs total return 和所用基准。
- **Common Trap：** 把回购率再减一次；把 P/E 下降 0.5 倍写成 −0.5%；把 integration 后的较低 required premium 当作没有过渡期收益。
- **Boundary Condition：** 盈利长期外推受经济增长与利润份额约束；缺价格或预期实现收益时，不用 required premium 单独排序市场吸引力。
- **Constructed Response：** 对 integration 的判断，分别写“更可分散风险 → required premium 下降”和“折现率下降 → transition repricing”。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other CME，No.2025060303000024 — adapted；答案为推导。</p>

A fully integrated market has volatility 15%, correlation with global market 0.60, global Sharpe ratio 0.35 and risk-free rate 1.5%. Expected total return is:


<div class="review-options">

A. 3.15%.

B. 4.65%.

C. 6.00%.



</div>

::: tip Answer & Reasoning
**Answer: B.** $RP=0.6\times15\%\times0.35=3.15\%$，再加 1.5%。A 漏掉 risk-free return。

**Exam Takeaway：** 先选现金流模型还是风险补偿模型，再核对符号、估值变化率与基准。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-equity)

</div>
