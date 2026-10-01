---
title: "CORE → Asset Allocation Topic Review"
pageClass: cfa-study
prev: false
next: false
study: {"section": "Topic Review", "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous Module Review", "title": "Real-World Constraints", "link": "/cfa/asset-allocation/review/05-constraints/review"}, "map": {"label": "Learning Map", "title": "Asset Allocation", "link": "/cfa/asset-allocation/"}, "next": {"label": "Question Bank →", "title": "Module Practice", "link": "/cfa/asset-allocation/questions/"}}
---

# Asset Allocation · Topic Review

## Big Picture

Asset Allocation 的最终问题是：**以可实施、可长期执行的风险，支付投资者真正需要支付的东西。** 高回报预测、有数学最优解、或持有多种资产，都不是单独的成功标准。

先定义失败：asset-only 的资产风险效率、liability-relative 的资金/贡献风险、goals-based 的目标 shortfall。再把预期与工具放进这个目标；绝不能先运行 optimizer，事后替它找一个目标。

## Module-to-Module Knowledge Chain

| 决策节点 | 哪个 Module 支持 | 向下一节点交付什么 |
| --- | --- | --- |
| 谁承担风险、要支付什么？ | Overview：economic balance sheet / governance | Human capital、liabilities、goals、risk definition |
| 世界怎样演变？ | CME Part 1 | 一致的 trend、cycle、inflation、policy、FX regime 情景 |
| 各资产如何响应？ | CME Part 2 | Returns、risk premiums、VCV、currency assumptions，标明输入限制 |
| 权重怎样产生？ | Principles | Asset efficiency / liability hedge / goal funding 与 risk budget |
| 是否真能买、能持有、能调整？ | Real-World Constraints | Product capacity、liquidity、after-tax exposure、IPS rules |
| 如何保持与修订？ | Overview + Constraints | Rebalancing、authorized TAA、bias controls、SAA review 与 CME feedback |

一个通胀冲击可同时改变 bond yields、property cap rates、currency expectations、目标支出与 index-linked liabilities。它不是只在 CME 页出现的术语，而是贯穿“资产价值—负债价值—可消费财富”的共同 factor。

## Must Remember

1. **目标先行。** 养老金资产 Sharpe 最高的配置不一定稳定 contribution；cash volatility 最低也不一定降低 funded-status risk。
2. **完整财富。** 雇主股、human capital、sponsor revenue、受限 donations 与 future consumption 改变经济风险容量，不能只看证券账户。
3. **可持续输入。** 长期盈利要有经济支持；P/E、capital share 或 cap-rate compression 不能永久创造回报。
4. **风险不是标签。** Asset classes 可以共享 growth/liquidity factors；1/N 不是 risk parity；appraisal smoothing 不是经济风险降低。
5. **条件性计算。** Yield、expected return、required premium、realized return 不可互换；net tax / currency / horizon 口径要一致。
6. **实施与授权。** Illiquidity premium 先要求 liquidity capacity；TAA 先满足 IPS，net incremental return 再与 SAA 比较。

## Important Formulas

| Formula | 经济含义 / 使用条件 | 要求 |
| --- | --- | --- |
| $g_{real}\approx g_{labor}+g_{productivity}$ | 趋势真实增长的供给来源 | Must memorize |
| $i^*=r^*+\pi_e+0.5(\pi_e-\pi^*)+0.5(g_e-g_{trend})$ | 本地题给定的 Taylor growth-gap 版本；不混用 level output gap | Know how to use |
| $E(R_e)\approx D/P+\pi+g-\Delta S+\Delta(P/E)$ | Equity income + earnings / shares + repricing | Must memorize |
| $RP_i^{int}=\rho_{i,G}\sigma_i RP_G/\sigma_G$ | 整合市场的全球系统风险补偿；total return 再加 $r_f$ | Know how to use |
| $E(R_{RE})\approx c_0+g_{NOI}-\%\Delta c$ | Property 收入、成长与 cap-rate 相对重估的近似 | Know how to use |
| $U=\mu-0.5\lambda\sigma^2$ | Decimal inputs；percentage numbers 改用 0.005 | Must memorize |
| $w_T=(R_{target}-r_f)/(R_T-r_f)$ | 目标回报与 risk-free / tangency mixing | Know how to use |
| $MCTR_i=\beta_{i,p}\sigma_p,\ ACTR_i=w_iMCTR_i$ | 边际与绝对风险贡献，beta 相对本组合 | Must memorize |
| $S=A-L,\ F=A/L$ | Dollar surplus 与 funding ratio 不同 | Must memorize |
| $SFR=(\mu-R_L)/\sigma$ | 相对目标阈值的 standardised buffer；相同正态/可比较分布假设 | Know how to use |
| $PV_{goal}=FV/(1+r_{min})^T$ | $r_{min}$ 匹配 horizon 与 success probability | Must memorize |
| $PV=C_0\sum_{t=0}^{N-1}[(1+g)/(1+r)]^t$ | 立即开始的 inflation-linked spending；期末开始需改时点 | Know how to use |
| $R_{AT}=(1-t)R_{PT},\ \sigma_{AT}=(1-t)\sigma_{PT}$ | 固定税率、正线性缩放的简化，非所有税制 | Know how to use |
| $\Delta R_{TAA}=\sum_i(w_i^{TAA}-w_i^{SAA})R_i$ | 相对 policy weights 的 gross 增量，再减额外成本 | Know how to use |

## Cross-Module Traps

| 容易混淆的两件事 | 更可靠的判断 |
| --- | --- |
| High required return / attractive valuation | 更高风险也提高 required return；需要价格或预测实现回报才能判便宜 |
| Growth / equity return | 还要 dividend、share dilution 与 valuation；长期增长受经济边界限制 |
| Asset-only volatility / liability risk | 资产与负债共同变化决定 surplus/funding risk |
| Equal dollars / equal risk | MCTR 与 correlation 决定 actual risk contribution |
| High average return / high success | 目标资金取决于 matched minimum expectation return |
| Long horizon / low liquidity need | 每期提款、calls 与 inflow shocks 可使长期账户今天缺 cash |
| Rebalancing / TAA / SAA review | 分别处理 drift、短期 view、长期目标/信念/约束变化 |
| Better alpha forecast / permission to trade | IPS bounds 是硬约束，forecast 不产生权限 |

## Boundary Conditions

- **Rates：** horizon≈Macaulay Duration 的抵消是简化近似，曲线扭曲、违约、成本或多次利率变动会改变结果。
- **Correlation：** sample VCV、investment factors 和 appraisal indices 的正常时期关系可能在 stress 改变；risk models 要保留 residual risk。
- **Tax：** correlation 不变限于固定正线性缩放；不同账户、递延资本利得与不对称 loss treatment 需另看。
- **Goals：** 每个目标满足 success probability 不等于全部目标联合达到同概率；withdrawal timing 与 inflation 必须明示。
- **Liabilities：** closed to new employees 不等于 frozen fixed benefits；即使 A/L 同额改变、surplus 不变，funding ratio 仍可能变化。
- **Implementation：** market benchmark、asset-class index 和 actual vehicle 是三个层次；无法复制的低波动输入不能直接变成可执行权重。

## Final Integrated Practice

### Case 1 — Sponsor Risk、Funding 与模型选择

<div class="review-practice">

Source: Local Other AA，Sabonete Case No.2025072102000043 — adapted；答案为推导。

SPP is 90% funded, closed to new employees but still accruing benefits. Its sponsor is heavily exposed to emerging markets and African property. It wants full funding in five years, stable contributions and low costs. Option 1 has higher asset Sharpe and a 95% chance of full funding but variable contributions; Option 2 has steadier contributions with a lower chance of full funding.

**Recommend** a modeling framework. **Explain** why the highest-Sharpe/endowment-style allocation is not automatically best. **Identify** one cross-balance-sheet risk.

**Minimum Passing Answer:**

- Use integrated ALM to model multi-year liabilities, funding and contributions.
- Asset Sharpe does not capture contribution stability or liability-relative risk; more illiquid alternatives do not guarantee the payment objective.
- Sponsor EM/property risk can coincide with pension losses and reduced contribution capacity; reduce unintended shared exposure.

**Exam takeaway：** 同一个 growth shock 同时作用于 sponsor ability、portfolio 与 contribution need。先做 economic balance sheet，才知道哪种“分散化”是真的。

[Review This Concept →](/cfa/asset-allocation/review/04-principles/step-05) · [Practice More Questions →](/cfa/asset-allocation/questions/2025072102000043)

</div>

### Case 2 — Goal、Tax 与再平衡纪律

<div class="review-practice">

Source: Local Other AA，Martin Case No.2025072102000050 — adapted；答案为推导。

A full scholarship releases education cash. Baseline retirement is secured; a low-priority estate gift is long term. Equities drift to 71% after three years of 20% returns. Interest tax exceeds capital-gains/dividend tax; the investor resists selling because recent returns will “continue.”

**Identify** the review trigger, the bias and the different roles of location/rebalancing. **Justify** a more growth-oriented gift sub-portfolio without jeopardizing retirement.

**Minimum Passing Answer:**

- Scholarship changes goal funding and releases near-term cash; reassess its use.
- Recent-winner extrapolation is representativeness; follow the written rebalancing policy.
- Place relatively tax-inefficient exposures in suitable tax-advantaged accounts; use wider taxable bands while controlling combined economic risk.
- The low-priority long-term gift can take more equity risk because essential retirement/education funding is protected.

**Exam takeaway：** 释放目标资金不等于全账户风险容量无限增加；税与心理都影响执行，需恢复总体政策约束。

[Review This Concept →](/cfa/asset-allocation/review/05-constraints/step-04) · [Practice More Questions →](/cfa/asset-allocation/questions/2025072102000050)

</div>

### Case 3 — 同一 PE 权重，完全不同的风险

<div class="review-practice">

Source: Local Other AA，Titan/Fordhart Case No.2025072102000052 — adapted；答案为推导。

A $10m endowment with falling tuition/donations and mandatory spending proposes 10% PE with a $1m minimum. A $2bn endowment with improving tuition and removal of a $50m annual obligation proposes 10% in a $500m PE vehicle, while cutting equity and increasing bonds.

**Discuss** one liquidity and one size/capacity concern across the two funds.

**Minimum Passing Answer:** The small fund faces lower inflows/higher support needs while locking $1m (10%) in PE, impairing liquidity and diversification. The large fund's $200m ticket is 40% of the PE vehicle; vehicle capacity/concentration is a concern despite adequate minimum-ticket size. Its lower spending pressure does not by itself support a sharp move toward bonds.

**Exam takeaway：** 权重是模型输出，absolute tickets、现金流和vehicle limits才决定是否可实施。

[Review This Concept →](/cfa/asset-allocation/review/05-constraints/step-01) · [Practice More Questions →](/cfa/asset-allocation/questions/2025072102000052)

</div>
