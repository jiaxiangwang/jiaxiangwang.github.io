---
title: "Step 1 — 用 Asset Size、Capacity 与 Regulation 划定可行配置"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "01 · 规模、Capacity 与授权边界"
study: {"section": "Review Course", "module": "Real-World Constraints", "moduleLink": "/cfa/asset-allocation/review/05-constraints/", "step": 1, "total": 6, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "Overview", "link": "/cfa/asset-allocation/review/05-constraints/"}, "map": {"label": "Learning Map", "title": "Real-World Constraints", "link": "/cfa/asset-allocation/review/05-constraints/"}, "next": {"label": "Next Step →", "title": "用现金流压力检验 Illiquidity Budget", "link": "/cfa/asset-allocation/review/05-constraints/step-02"}}
---

# 用 Asset Size、Capacity 与 Regulation 划定可行配置

::: info 本步目标
能把配置比例转为金额，分别检查 minimum ticket、vehicle concentration、strategy capacity、治理资源与 regulation。
:::

## Why · 为什么同样 10% 的 PE 配置，大小账户问题不同？

10% 对小基金可能刚够最低投资额，对大基金却可能占一只产品的大部分容量。比例看起来相同，实施风险完全不同。

Asset size 的分析必须把权重转为绝对金额，并区分“能够买到”“有能力管理”和“适合投资者”。再高的预期收益，也只能在已授权、可执行的机会集中比较。

## Core & Intuition · 资金规模 → 产品可达性 → 容量与治理 → 硬约束

小投资者常受 minimum ticket、费用和专业资源限制；大投资者更容易聘团队、议价和接触 direct opportunities，却可能受到 market impact、strategy capacity 与经理监督数量限制。

| 限制 | 检查什么？ | 为什么不等价？ |
| --- | --- | --- |
| Minimum investment | 拟投资金额是否达到产品门槛 | 达标只证明可参与，不证明适合 |
| Vehicle concentration | 投资占自身财富和产品总规模多少 | 一个门槛不高的产品仍可能装不下资金 |
| Strategy capacity | 策略能否在扩大规模后维持效果 | 低容量机会难以影响大机构总回报 |
| Governance resources | 能否选择、监督经理并管理 commitments | 多经理分散可能增加监督负担 |
| Mandate / regulation | 哪些资产或比例根本不允许 | 这是可行集合边界，不是 optimizer 的软偏好 |

**Intuition：** 为分散大型资产而不断增加 managers，可以缓解单个 manager capacity，却提高 due diligence 与监督要求。规模优势因此需要实施能力支撑，不能认为 AUM 越大越容易得到好结果。

法规、地域限制和 policy caps 应先写入可行集合。本 Topic 按虚构案例给定的规则分析，不推定任何现实国家当前的具体法规。

## Example · Titan 与 Fordhart：同一比例的两种规模约束

<p class="source-note">Source: Local Other AA / No.2025072102000052 — adapted；答案为推导。</p>

Titan AUM 10 million，10% PE 是 1 million，恰达到产品 minimum ticket。它能买到一只基金，却要承受自身财富 10% 集中和锁定，仍需检查支出。

Fordhart AUM 2 billion，10% PE 是 200 million；若目标基金总规模为 500 million，这笔资金占 vehicle 的 40%。5 million minimum 已不重要，产品容量与集中才是问题。

两个例子都不能只根据 “10%” 或 “minimum met” 得出适合结论；必须同时看 investor AUM、fund AUM 和 liquidity needs。

## CFA Language & Formula

::: info Formula · Know how to use
把政策比例还原为实际资金，再量化产品集中：

$$Investment\ Amount=AUM_{investor}\times w$$

$$Vehicle\ Share=\frac{Investment\ Amount}{AUM_{fund}}$$

$w$ 使用小数，investor AUM 与 fund AUM 不能混淆；minimum ticket 是金额，不是比例。先统一 million / billion 单位再比较。
:::

**Capacity** 是策略或产品能承受的规模；**access** 是可否进入；**liquidity** 是需要退出或支付时资金是否可得。达到其中一个条件，不自动满足另外两个。

## Connection

[Asset Classes](/cfa/asset-allocation/review/03-overview/step-04) 定义机会集，本步筛选是否可实施。[Liquidity Budget](/cfa/asset-allocation/review/05-constraints/step-02) 检查资金时点，[Governance](/cfa/asset-allocation/review/03-overview/step-01) 确定谁能批准与监督实际配置。

## Exam Focus

- **Exam Trigger — Discuss two reasons：** 每个理由写一个 case fact 和一个实施后果，避免两个理由只是同一事实改写。
- **Common Trap：** Minimum ticket 达标即适合；将 fund AUM 与 investor AUM 混淆；用高 expected return 推翻法定上限。
- **Boundary Condition：** 长期没有提款也不能取消 mandate 的资产限制；可达性、capacity、concentration 和 liquidity 可能同时绑定。
- **Constructed Response：** “The proposed $200m commitment is 40% of the vehicle, creating concentration/capacity concerns.” 是具体证据与影响。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other AA，No.2025072102000052-2 — adapted；答案为推导。</p>

Fordhart has $2bn; a proposed 10% allocation targets a $500m private-equity fund. **Discuss** one implementation concern.

::: tip Answer & Reasoning
**Conclusion:** The proposed investment creates vehicle concentration and capacity concerns.

**Scoring Points:**

- Commitment = $2bn × 10% = $200m.
- $200m is 40% of the $500m fund; the $5m minimum is not binding.

**Minimum Passing Answer:** The $200m allocation would represent 40% of the vehicle, creating concentration and potential capacity issues; meeting the minimum does not establish suitability.

**Exam Takeaway：** 配置比例必须变成金额，再分别检验产品、策略、治理与授权限制。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-size)

</div>
