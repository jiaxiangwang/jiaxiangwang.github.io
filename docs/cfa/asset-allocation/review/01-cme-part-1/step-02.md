---
title: "Step 2 — 区分 Trend Growth 与周期增长"
pageClass: cfa-study
outline: [2, 2]
prev: false
next: false
sidebarTitle: "02 · 趋势增长与盈利边界"
study: {"section": "Review Course", "module": "CME Part 1", "moduleLink": "/cfa/asset-allocation/review/01-cme-part-1/", "step": 2, "total": 6, "topic": "Asset Allocation", "topicLink": "/cfa/asset-allocation/", "category": "CORE", "categoryLink": "/cfa/review/#core", "system": "review"}
studyNav: {"previous": {"label": "← Previous", "title": "把经济观点变成可检验的 Capital Market Expectations", "link": "/cfa/asset-allocation/review/01-cme-part-1/step-01"}, "map": {"label": "Learning Map", "title": "CME Part 1", "link": "/cfa/asset-allocation/review/01-cme-part-1/"}, "next": {"label": "Next Step →", "title": "从 Business Cycle 识别政策和资产方向", "link": "/cfa/asset-allocation/review/01-cme-part-1/step-03"}}
---

# 区分 Trend Growth 与周期增长

::: info 本步目标
能区分趋势与周期，用劳动和生产率估计长期增长，并检验股票回报预测是否依赖不可持续的估值扩张。
:::

## Why · 为什么长期 CME 不能直接外推最近的 GDP？

季度 GDP 受需求、库存和政策刺激影响，而长期 SAA 关心经济能够持续创造多少真实产出。若把一次强劲复苏直接外推，会把 **cyclical growth** 当作 **trend growth**，进而高估长期盈利与资产回报。

本步先恢复供给能力，再把它接到名义盈利。这样可以检验股票回报预测中的增长假设，而不是只背一个 GDP 分解式。

## Core & Intuition · 有效劳动 × 生产率，再检查利润份额

长期真实增长来自两件事：投入多少有效劳动，以及每单位劳动创造多少产出。人口、劳动参与率与工时影响 labor input；资本深化、技术、教育和制度影响 labor productivity。

随后才把经济增长连接到企业盈利：**真实增长 → 加入通胀 → 名义经济增长 → 检查企业利润占 GDP 的比例 → 检查每股口径**。利润份额稳定时，aggregate corporate earnings 的长期增长可由名义 GDP 提供锚；shares outstanding 的变化还会影响每股盈利。

**Intuition：** 全市场利润如果永远比经济增长更快，利润占 GDP 的比例就会不断上升，最终产生不合理结果。个别公司可以抢占份额，因此“某家公司高增长”不能用来证明“全市场永远高于 GDP 增长”。同样，股价可以短期受 P/E 扩张支持，但倍数不能无限扩张。

成熟经济的历史趋势可以作为起点。发展中经济的追赶、人口或制度变化更可能改变未来生产能力，需要更谨慎地调整历史外推。判断冲击时，要问它是否持久改变劳动、资本或生产率；需求刺激本身不足以证明趋势提高。

## Example · 把 9% 的股票预测拆开

<p class="source-note">Source: Local 原版书 CME / Cambo / No.2021052701000002 — adapted；答案为推导。</p>

Cambo 的输入是 labor growth 0.5%、productivity growth 1.3%、inflation 2.2%、dividend yield 2.8%，预测股票年回报 9%；利润份额不变。

先得到真实趋势增长 1.8%，再得到名义增长约 4.0%。若股数不变，增长与股息合计支持约 6.8% 回报，剩余 2.2 个百分点来自 P/E contribution。这个结果既是计算答案，也是合理性检查：若把 9% 当作永久假设，就需要解释估值扩张为何能一直持续。

## CFA Language & Formula

::: info Formula · Must memorize
经济含义是“更多劳动 + 每单位劳动更高产出”；小幅增长率可相加：

$$g_{real\ GDP}\approx g_{labor\ input}+g_{labor\ productivity}$$

$$g_{nominal\ GDP}\approx g_{real\ GDP}+\pi$$

输入要保持同一时间尺度，且不能把 nominal labor-productivity growth 再加一次通胀。
:::

**Know how to use：** 在本地 Cambo 的稳定利润份额、股数不变假设下，$\Delta(P/E)\approx E(R_e)-D/P-g_{nominal\ earnings}$。它说明剩余回报来自 repricing，不代表所有题目都能忽略发行或回购。

**Trend growth** 回答可持续供给能力；**business cycle** 回答实际产出围绕趋势的波动。Real risk-free yields 也受真实增长机会与储蓄需求影响，但不是每期都精确等于真实 GDP growth。

## Connection

[Business Cycle](/cfa/asset-allocation/review/01-cme-part-1/step-03) 决定短期偏离，[Grinold–Kroner](/cfa/asset-allocation/review/02-cme-part-2/step-02) 把增长进一步接到股息、股数和估值。两者共同帮助判断一项回报假设应进入长期 SAA，还是只适合短期 TAA。

## Exam Focus

- **Exam Trigger — Calculate / Justify：** 先算真实与名义增长，再分离经营增长和估值贡献。
- **Common Trap：** 把 GDP growth 当作全部 equity return，遗漏 dividend yield；或把生产率与通胀重复计入。
- **Boundary Condition：** 利润份额、市场覆盖的企业或股数改变时，aggregate GDP growth 与 EPS growth 不能直接画等号。
- **Constructed Response：** 说明“长期不合理”的机制，应写利润份额或 P/E 无法无限上升，不能仅写“预测太乐观”。

> **Quick Recall：** 利润份额稳定时，全市场盈利能否永久高于名义 GDP 增长？\
> **Answer: No.** 否则利润占经济的比重会持续上升。

## Immediate Practice

<div class="review-practice">

<p class="source-note">Source: Local 原版书 CME，No.2021052701000002-1 — adapted；答案为推导。</p>

Labor growth is 0.5%, productivity growth 1.3%, inflation 2.2%, and dividend yield 2.8%. Expected equity return is 9.0%; profit share and shares outstanding are unchanged. **Calculate** the implied P/E contribution.

::: tip Answer & Reasoning
**Conclusion:** The implied P/E contribution is 2.2 percentage points annually.

**Scoring Points:**

- Nominal earnings growth ≈ 0.5% + 1.3% + 2.2% = 4.0%.
- P/E contribution ≈ 9.0% − 2.8% − 4.0% = 2.2%.

**Minimum Passing Answer:** $\Delta(P/E)=9.0-2.8-(0.5+1.3+2.2)=2.2\%$.

**Exam Takeaway：** 先分经营增长和估值扩张，再判断长期可持续性。
:::

</div>

<div class="study-actions">

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-growth)

</div>
