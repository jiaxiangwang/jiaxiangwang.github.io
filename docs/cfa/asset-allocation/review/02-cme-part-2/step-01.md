---
title: "Step 1 — 将 Yield、Risk Premium 与实现回报分开"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "01 · 债券收益率、溢价与持有期限"
study: {"section": "Review Course", "module": "CME Part 2", "moduleLink": "/cfa/asset-allocation/review/02-cme-part-2/", "step": 1, "total": 5}
studyNav: {"previous": {"label": "← Previous", "title": "Overview", "link": "/cfa/asset-allocation/review/02-cme-part-2/"}, "map": {"label": "Learning Map", "title": "CME Part 2", "link": "/cfa/asset-allocation/review/02-cme-part-2/"}, "next": {"label": "Next Step →", "title": "从盈利、分红与估值拆解 Equity Return", "link": "/cfa/asset-allocation/review/02-cme-part-2/step-02"}}
---

# 将 Yield、Risk Premium 与实现回报分开

::: info 本步目标
能从正确的无风险基准搭建债券回报，再用投资期限与 Macaulay Duration 判断价格风险和再投资风险的主导关系。
:::

## Why · 为什么“收益率更高”既可能是机会，也可能是风险变差？

债券的报价 yield 补偿多种风险，不同期限、信用和流动性的债券不能直接比较。信用恶化可能使 required yield 上升，却同时压低现有价格；投资者是否获利，还取决于持有期限、卖出价格与再投资。

本步按两个层次复习：先问“为什么要求这个回报”，再问“在投资者的 horizon 内怎样实现回报”。这样能避免把 building-block expectation、YTM 和 realized return 当成同一个数字。

## Core & Intuition · 风险补偿与持有期回报分开看

Building block approach 从真实无风险利率出发，依次加入 expected inflation、term、credit 和 liquidity premiums。比较长期公司债与短期国债时，差额同时含期限、信用和流动性补偿；比较同期限国债与公司债时，才更接近额外信用/流动性补偿。

持有期回报则来自收入与价格变化。利率上升会压低存量债券价格，却提高 coupons 的再投资收益。哪个作用更重要，取决于投资期限相对于现金流平均回收时间。

| Horizon 与 Macaulay Duration | 哪种风险更重要？ | 单次利率上升的典型影响 |
| --- | --- | --- |
| $H<D_M$ | Price risk | 卖出较早，再投资增益不足，价格损失更占主导 |
| $H\approx D_M$ | 两项近似平衡 | 在简化条件下，实现回报接近初始 yield |
| $H>D_M$ | Reinvestment risk | 较长再投资期使更高利率的收入效应更占主导 |

**Intuition：** 同一只债券，对三年后需要用钱的人与十年后需要用钱的人，不是同一种利率风险。Duration 需要与 horizon 一起读，不能只把利率上升叫坏消息。

Emerging market debt 还要检查 ability to pay 与 willingness to pay：税基、债务、外汇储备和短期外债影响支付能力；制度和政治意愿影响是否支付。更高 yield 不能替代这些检查。

## Example · 高收益债是否符合组合的买入门槛？

<p class="source-note">Source: Local 原版书 CME / No.2020012102000002 — adapted；答案为推导。</p>

投资者拟等权加入一年国债、十年国债与十年 BBB 公司债，要求整个新增组合相对一年国债的 premium 至少为 1.5%。一年国债的 nominal rate 为 1%，term premium 1%，credit premium 0.75%，liquidity premium 0.55%。

三种回报分别是 1.0%、2.0% 和 3.3%；等权组合为 2.1%，相对基准 premium 只有 1.1%，不达到门槛。即使公司债单独有 2.3% 额外补偿，也不能替代题目要求的**组合**门槛。这说明计算之后还要回到投资规则。

## CFA Language & Formula

::: info Formula · Know how to use
风险补偿框架的经济含义是，投资者为真实时间价值、购买力损失及额外风险分别要求回报：

$$E(R)\approx r_{real}+\pi_e+TP+CP+LP$$

若已给 nominal risk-free rate，它包含 expected inflation，不能再加一次。题干中的百分比与 basis points 应先统一；75 bp = 0.75%。该式是本地题的简化 building-block framework，不能作为任意期限 realized return 的保证。
:::

**Macaulay Duration** 用于与 horizon 比较；**Modified Duration** 用于价格的一阶敏感度：$\Delta P/P\approx-D_{mod}\Delta y$（**Know how to use**）。$\Delta y$ 用小数，20 bp = 0.002；不要用 $D_M$ 直接代入 modified-duration 价格式。

## Connection

利率方向来自 [Policy Mix](/cfa/asset-allocation/review/01-cme-part-1/step-05)，但本步将它转换成投资者 horizon 内的风险。[Liability-relative allocation](/cfa/asset-allocation/review/04-principles/step-05) 进一步把资产现金流和利率暴露与负债匹配。

## Exam Focus

- **Exam Trigger — Calculate / Determine：** 先确认基准为 real 还是 nominal、期限是否匹配，再按题干投资规则比较。
- **Common Trap：** 重复加 inflation；用单只债券的 spread 回答等权组合门槛；或把 higher required return 等同于 higher attractiveness。
- **Boundary Condition：** Duration-horizon 抵消使用单次小幅平行利率变化、给定现金流等简化条件。曲线扭转、违约和多次利率冲击会改变结论。
- **Constructed Response：** 写“horizon is shorter than Macaulay duration, so price risk dominates reinvestment risk”，已同时给出比较依据与结论。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local Other CME，No.2025060303000022 — adapted；答案为推导。</p>

A fixed-rate bond has Macaulay duration 5 years; the investor's horizon is 3 years. Realized return is **most likely**:


<div class="review-options">

A. More sensitive to price changes than reinvestment income.

B. Unchanged because the two effects exactly offset.

C. More sensitive to reinvestment income than price changes.



</div>

::: tip Answer & Reasoning
**Answer: A.** 3 年内收入再投资不足以抵消较远现金流的价格敏感度。

**Exam Takeaway：** 收益率解释要求补偿；投资期限决定价格与再投资作用怎样进入实现回报。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-bonds)

</div>
