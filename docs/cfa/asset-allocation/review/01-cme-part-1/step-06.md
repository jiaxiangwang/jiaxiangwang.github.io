---
title: "Step 6 — 把国内宏观判断放进开放经济约束"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "06 · 开放经济恒等式与政策自由度"
study: {"section": "Review Course", "module": "CME Part 1", "moduleLink": "/cfa/asset-allocation/review/01-cme-part-1/", "step": 6, "total": 6, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "把 Monetary / Fiscal Policy 转成利率判断", "link": "/cfa/asset-allocation/review/01-cme-part-1/step-05"}, "map": {"label": "Learning Map", "title": "CME Part 1", "link": "/cfa/asset-allocation/review/01-cme-part-1/"}, "next": {"label": "Next Step →", "title": "Module Review", "link": "/cfa/asset-allocation/review/01-cme-part-1/review"}}
---

# 把国内宏观判断放进开放经济约束

::: info 本步目标
能在给定私人储蓄条件下判断净出口，并按各独立情景解释固定汇率、资本流动与货币政策的约束。
:::

## Why · 为什么国内政策预期还必须与汇率一致？

若一个国家维持可信的固定汇率并允许资本自由流动，却假设央行长期独立把利率定在完全不同的水平，资金流动会冲击这个汇率安排。这样的利率与汇率 CME 互相冲突。

本步用两张“约束图”保持一致性：一张追踪国民收入如何由私人、政府和外部部门分担；另一张检查汇率制度给货币政策留下多少自由度。

## Core & Intuition · 部门收支约束 + Impossible Trinity

第一层是部门恒等关系。政府增加支出或减税，需要由其他部门行为或外部余额变化对应。题目只有在固定了私人净储蓄后，才能直接从预算变化推到净出口。

第二层是 **impossible trinity**：长期不能同时维持固定汇率、自由资本流动和独立货币政策。资本可以自由移动且 peg 完全可信时，利率明显偏离会引发跨境资金流动，货币当局必须为维持汇率作出反应。

| 改变的条件 | 哪种联系发生变化？ | 推理重点 |
| --- | --- | --- |
| Restrict capital flows | 资本套利渠道受限 | 国内利率可更偏离锚国，但 peg 仍需管理 |
| Allow currency to float | 不再承诺固定比价 | 政策自主性提高，利差与汇率预期/风险补偿共同作用 |
| Peg loses credibility | 固定汇率不再被认为永远可信 | 预期贬值及风险补偿可使国内利率高于锚国 |

**Intuition：** 投资者比较的不是两国票面利率，而是计入汇率变化和风险后的回报。“利率相同”的结论依赖强条件，不是所有开放经济的普遍规律。

## Example · Hadpret：每个情景单独改变一个条件

<p class="source-note">Source: Local 原版书 CME / No.2021052701000003-3 — adapted；答案为推导。</p>

Eastland 目前把货币固定到 Northland，资本自由流动。题目要求分别讨论资本管制、浮动汇率，以及市场不再完全相信 peg 会永远维持。

第一个情景改变资金移动能力，第二个改变汇率承诺，第三个改变投资者对承诺的信任。回答必须每次从原始制度重新出发。若把三个变化叠加成同一个新制度，就无法说明每个条件的独立影响，也偏离 “Consider each scenario independently” 的要求。

## CFA Language & Formula

::: info Formula · Know how to use
恒等式追踪三部门的对应关系：

$$NX=(S-I)+(T-G)$$

$S-I$ 是 net private saving；$T-G$ 是 government budget surplus；$NX$ 是 net exports。在题干的部门口径下，若 $S-I=5$、$T-G=-3$，则 $NX=2$；赤字加深到 $T-G=-5$ 而私人净储蓄不变，$NX$ 变成 0。
:::

输入必须来自同一经济与同一期间。$T-G$ 下降包括 taxes 下调或 spending 增加；不要把更大的 deficit 当作更大的 surplus。现实中私人储蓄、投资和汇率会调整，因此固定私人净储蓄是应用方向判断的必要条件。

## Connection

[Currency CME](/cfa/asset-allocation/review/02-cme-part-2/step-04) 延续这条资本流动链，解释短期汇率为何可偏离 PPP。[Policy Mix](/cfa/asset-allocation/review/01-cme-part-1/step-05) 的利率判断也必须放在该国政策制度中，不能孤立外推。

## Exam Focus

- **Exam Trigger — Discuss each scenario independently：** 每条说明哪项制度条件改变，以及利率/汇率联系如何变化。
- **Common Trap：** 把“资本自由流动”单独当作利率相等的充分条件；或把三个独立情景一起应用。
- **Boundary Condition：** 固定汇率可信度、信用与流动性风险不同，都可形成利差。净出口的方向判断依赖题干固定 $S-I$。
- **Constructed Response：** “Capital controls weaken cross-border arbitrage, allowing domestic rates to diverge further from the anchor country's rates.” 给出机制即可，无需猜测未提供的具体利率。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other CME，No.2025060303000009 — adapted；答案为推导。</p>

Government spending rises and taxes fall; net private saving stays unchanged. Net exports **most likely**:


<div class="review-options">

A. Decrease.

B. Stay unchanged.

C. Increase.



</div>

::: tip Answer & Reasoning
**Answer: A.** $T-G$ 下降，在 $S-I$ 不变时 $NX$ 必须下降。

**Exam Takeaway：** 先列固定条件，再判断哪个部门或制度条件必须调整。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-international)

</div>
