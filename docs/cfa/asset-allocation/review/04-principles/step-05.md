---
title: "Step 5 — 按 Funding Situation 选择 Liability-relative 方法"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "05 · 负债方法与 Funding Situation"
study: {"section": "Review Course", "module": "Principles of Asset Allocation", "moduleLink": "/cfa/asset-allocation/review/04-principles/", "step": 5, "total": 7, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "用 MCTR 区分 Capital Weight 与 Risk Weight", "link": "/cfa/asset-allocation/review/04-principles/step-04"}, "map": {"label": "Learning Map", "title": "Principles of Asset Allocation", "link": "/cfa/asset-allocation/review/04-principles/"}, "next": {"label": "Next Step →", "title": "把 Probability、Horizon 与 Funding Cost 连起来", "link": "/cfa/asset-allocation/review/04-principles/step-06"}}
---

# 按 Funding Situation 选择 Liability-relative 方法

::: info 本步目标
能比较 surplus 和 funding ratio，按负债可对冲性、资金状态与多期出资目标选择 liability-relative 方法。
:::

## Why · 为什么欠资养老金不能只寻找最高 Sharpe Ratio？

养老金需要在未来支付承诺，还可能希望稳定 sponsor contributions。资产自身效率高，不一定减少资产相对负债的风险；如果 sponsor 经营同时恶化，还可能无法及时补足资金。

本步先量化 funded status，再选择方法。选择依据是负债怎样变化、资产能否对冲、现有资金是否足够，以及是否需要多期动态安排。

## Core & Intuition · 单期 Surplus、两组合与多期 ALM

先恢复三项共同输入：**liability cash flows / valuation risks → assets 的共同变动 → sponsor 的出资能力**。然后根据问题选择工具：

| Method | 决策思路 | 适配与边界 |
| --- | --- | --- |
| Surplus optimization | 单期平衡 expected surplus return 与 surplus variance | 能直接纳入相对负债风险，但不自动描述多期出资 |
| Hedging / return-seeking portfolios | 先构建 liability hedge，再将余资用于回报 | 资金足够、义务可可靠对冲时清楚；欠资不能凭空足额建 hedge |
| Integrated ALM | 多期共同模拟资产、负债、contributions 与动态决策 | 适合 future funding / contribution stability；模型与治理要求更高 |

**Intuition：** 若负债可用某种资产匹配，先保障这部分支付，再决定余资风险，更容易解释政策。但负债随工资、寿命、通胀或未来服务变化时，仅一个静态 hedge 未必足够。

Closed to new employees 不一定是 frozen plan：现有员工仍可能 accrue benefits。Sponsor 的经营风险也会同时影响资产价值和出资能力，不能将 sponsor 当作无风险补资来源。

## Example · Johansson：先覆盖义务，再配置余资

<p class="source-note">Source: Local 原版书 AA / No.2018031301000005 — adapted；答案为推导。</p>

Johansson 的 assets 为 10 billion，liabilities 为 8.5 billion；负债由 index-linked government bonds 驱动。若题干条件允许用这些债券可靠匹配，liability-hedging portion 为 assets 的 85%，return-seeking portion 为 15%。

这里先选择能支持负债的 exposure，而不是选预期回报最高的组合。85% 是在价值充分匹配假设下的资金比例；实际实施仍要检查现金流、duration、inflation exposure 与信用是否匹配。

## CFA Language & Formula

::: info Formula · Must memorize
Surplus 衡量金额差，funding ratio 衡量相对覆盖程度：

$$Surplus=A-L,\qquad Funding\ Ratio=\frac{A}{L}$$

$A$ 与 $L$ 必须来自同一时点和一致估值口径。Assets 205、liabilities 241，ratio 为 85.06%；两者各减 25 后，surplus 仍为 −36，但 ratio 降到 83.33%。
:::

**Know how to use：** Surplus return 的归一化依题干。若用期初 assets，$R_S\approx R_A-(L_0/A_0)R_L$；欠资时 liability changes 相对 assets 更重要。不能把不同资料中同名 surplus-return symbols 直接替换。

**Hedging** 降低相对负债风险；**return-seeking** 承担为产生余资回报所需的风险；**integrated ALM** 将其放进多期状态与出资政策。

## Connection

[Economic Balance Sheet](/cfa/asset-allocation/review/03-overview/step-02) 恢复 sponsor 与义务，[Risk Definition](/cfa/asset-allocation/review/03-overview/step-03) 指定失败标准，[Fixed-income CME](/cfa/asset-allocation/review/02-cme-part-2/step-01) 提供资产利率暴露。方法选择要把三者一起用。

## Exam Focus

- **Exam Trigger — Most appropriate：** 单期 surplus trade-off、多期 contributions 或足额 hedge，是不同的选择线索。
- **Common Trap：** 同额资产/负债下降就断言 ratio 不变；把 closed 视作 frozen；以最高资产回报替代负债目标。
- **Boundary Condition：** 两组合的静态比例依可靠匹配与足够资金；工资、通胀、contingencies 与动态现金流会要求更多检验。
- **Constructed Response：** 对方法选择写“目标 + 为什么该方法能处理”，如 multi-period ALM models future funding and contribution variability。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000046-3 — adapted；答案为推导。</p>

Assets are $205m and liabilities $241m. Both fall $25m. Funding ratio will:


<div class="review-options">

A. Decrease.

B. Stay unchanged.

C. Increase.



</div>

::: tip Answer & Reasoning
**Answer: A.** 85.06% → 83.33%，尽管 surplus 不变。

**Exam Takeaway：** 先识别负债、资金状态和出资目标，再决定采用哪个 liability-relative 方法。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-liability)

</div>
