---
title: "Step 5 — 把 Monetary / Fiscal Policy 转成利率判断"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "05 · 政策组合与 Taylor Rule"
study: {"section": "Review Course", "module": "CME Part 1", "moduleLink": "/cfa/asset-allocation/review/01-cme-part-1/", "step": 5, "total": 6, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "区分预期通胀、意外通胀与 Deflation", "link": "/cfa/asset-allocation/review/01-cme-part-1/step-04"}, "map": {"label": "Learning Map", "title": "CME Part 1", "link": "/cfa/asset-allocation/review/01-cme-part-1/"}, "next": {"label": "Next Step →", "title": "把国内宏观判断放进开放经济约束", "link": "/cfa/asset-allocation/review/01-cme-part-1/step-06"}}
---

# 把 Monetary / Fiscal Policy 转成利率判断

::: info 本步目标
能区分货币与财政政策影响的渠道和期限，按题干给定版本计算 Taylor rule，并解释收益率曲线的条件性变化。
:::

## Why · 为什么两个“宽松”不能直接推出所有利率下降？

Monetary easing 通常先压低短端融资成本；fiscal expansion 通过减税、支出和借款改变需求与政府债券供给。它们支持增长，却不一定对每个期限的收益率产生同向效果。

如果只把政策贴上 loose / tight 标签，就会漏掉题干的关键：谁在改变需求，谁在改变短率，借款集中在哪个期限，市场如何调整增长与通胀预期。

## Core & Intuition · 先分渠道，再组合政策

先把政策拆开：**monetary policy → financing conditions / short rates**；**fiscal policy → demand / taxes / government borrowing**。随后再判断两者怎样影响整条曲线。

| Policy mix | 典型利率倾向 | 为什么？ |
| --- | --- | --- |
| Loose monetary + tight fiscal | 名义利率偏低 | 短端被压低，政府借款和需求压力较小 |
| Tight monetary + loose fiscal | 名义利率偏高 | 短端政策紧，财政需求和借款又提供上行压力 |
| Both loose / both tight | 不能无条件给出一个水平 | 短率、需求、债券供给与预期的渠道可能互相拉扯 |

**Intuition：** 曲线斜率是短端与长端的相对变化。央行降息，政府却通过长期发债融资，短端下降、长端相对得到支撑，就可产生 steepening；这个判断不要求长端绝对上升。

Taylor rule 是另一个层次：它把“中性的名义利率”与央行对通胀、经济过热的反应分开。经济高于趋势且通胀高于目标时，应在中性基准上加紧缩反应，而不是简单维持原短率。

## Example · Hadpret：降息与长期国债发行同时发生

<p class="source-note">Source: Local 原版书 CME / No.2021052701000003-2 — adapted；答案为推导。</p>

经济衰退中，央行将 ease monetary policy；政府计划大幅减税，并用 long-term government securities 融资赤字。

把两条链分开写：货币宽松压低短端；长期借款供给及复苏/通胀预期为长端提供相对支撑。合起来是典型的 yield-curve steepening。只说“两种政策都宽松，所以利率都下降”遗漏财政融资渠道；只说“发债使利率上涨”又遗漏短端的政策作用。

## CFA Language & Formula

::: info Formula · Know how to use
本地题采用 **growth-gap Taylor rule**。经济含义是中性名义基准加上两项政策反应：

$$i^*=r^*+\pi_e+0.5(\pi_e-\pi^*)+0.5(g_e-g_{trend})$$

| Input | 先确认口径 |
| --- | --- |
| $r^*$ | Neutral **real** policy rate；如果已给 nominal baseline，不重复加通胀 |
| $\pi_e,\pi^*$ | 预期通胀与目标通胀，差值使用 percentage points |
| $g_e,g_{trend}$ | 本题的增长偏离；不是 GDP level output gap |

例如 $r^*=2\%,\pi_e=4\%,\pi^*=3\%,g_e=5\%,g_{trend}=3\%$：基准为 6%，两个反应项为 0.5 与 1.0 个百分点，目标名义利率为 **7.5%**。
:::

**Neutral rate** 与 **target policy rate** 不能混为一谈。规则解释政策方向，并不是央行承诺；其他题若定义 output gap，应严格使用其给定口径。

## Connection

[Business Cycle](/cfa/asset-allocation/review/01-cme-part-1/step-03) 决定政策为什么反应，[Fixed-income CME](/cfa/asset-allocation/review/02-cme-part-2/step-01) 将收益率变化转换为价格与再投资影响。[开放经济约束](/cfa/asset-allocation/review/01-cme-part-1/step-06) 则解释一国政策自主性为何可能受汇率制度限制。

## Exam Focus

- **Exam Trigger — Calculate：** 先写 real / nominal baseline，再计算各 gap；不要一开始就把所有百分数相加。
- **Common Trap：** 将中性真实利率直接与名义市场利率比较，或把 growth gap 与 output level gap 互换。
- **Boundary Condition：** 金融稳定、利率下限和汇率制度会限制规则的执行；财政刺激不自动永久提高 trend growth。
- **Constructed Response：** 解释 steepening 时分别写短端政策与长端供给/预期，不需要断言所有长期收益率必涨。

> **Quick Recall：** 预期通胀比目标高 1 个百分点，本题的 inflation-gap adjustment 是多少？\
> **Answer: 0.5 个百分点。** 预期通胀本身还进入 nominal baseline，两项不能混淆。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other CME，No.2025060303000007 — adapted；答案为推导。</p>

Given the Taylor-rule inputs above, the target nominal policy rate is:


<div class="review-options">

A. 3.5%.

B. 4.5%.

C. 7.5%.



</div>

::: tip Answer & Reasoning
**Answer: C.** 基准 $2+4=6\%$，再加两个 gap 的反应共 1.5%。

**Exam Takeaway：** 先分真实与名义、短端与长端，再组合政策判断。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-policy)

</div>
