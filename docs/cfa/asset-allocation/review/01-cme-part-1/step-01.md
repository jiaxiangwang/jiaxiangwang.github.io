---
title: "Step 1 — 把经济观点变成可检验的 Capital Market Expectations"
---

# Step 1 — 把经济观点变成可检验的 Capital Market Expectations

## 先定义预测要服务的决策

Capital Market Expectations (CME) 是对资产收益、风险与相关性的**条件性预期**。它不是单一股市点位预测。SAA 需要长期且互相一致的输入；TAA 需要较短期的观点。先问投资者是谁、哪些资产、什么期限，才能判断数据与模型是否有用。

复习时按这条工作链恢复：**定义所需预期与期限 → 检查历史记录 → 选方法 → 选可靠数据 → 解读当前环境 → 形成一致的预期 → 将实现结果反馈给预测过程**。本地 Wuyan Case 已完成中间几项，考试会要求补首尾，而不是换一个更复杂的模型。

## 为什么显著关系可能没有投资价值？

足球成绩与股市回报偶然相关，重复筛选足够多变量后，总能找到“显著”结果：这就是 **data-mining bias**。经济机制、样本外稳定性和合理性检查应先于信任统计显著性。Correlation 本身不能证明 causation，也未必提供先行预测能力。

| 问题 | 为什么失真 | 应对思路 |
| --- | --- | --- |
| Survivorship bias | 只看存活基金会漏掉失败记录 | 尽量使用含退出样本的数据 |
| Appraisal smoothing | 估值更新慢，观察波动被压低 | 检查序列相关，谨慎使用风险/相关性 |
| Time-period bias / regime change | 扩大样本可能把不同制度混在一起 | 先检查结构稳定性，再决定样本窗口 |
| Availability / anchoring / status quo | 印象、起点或原配置主导判断 | 用书面假设、替代情景和反馈约束判断 |

更多数据减少 sampling error 的同时，可能增加旧制度污染。不能把“20 年优于 10 年”当成无条件规则。

## Forecasting tools 是互补关系

Econometric / structural models 保持变量之间的逻辑一致，并能考察政策情景；代价是模型设定复杂、参数与输入误差、可能产生 false precision。Leading indicators 简洁及时，但可能给 false signals，且历史先后关系会变。Checklist 灵活，缺点是判断主观、跨时点一致性较弱。

**Exam Trigger — Explain / Discuss：** 写出具体失真机制与影响；只写“有 bias”不能说明为何输入不可靠。**Common Trap：** 把经济变量与回报的同期相关误读为可预测未来回报。

## Immediate Practice

Source: Local Other CME，No.2025060303000001 — adapted；答案为推导。

An analyst finds a significant relation between soccer results and equity returns after extensive data searches, without an economic rationale. Which bias is **most likely**?

A. Anchoring.\
B. Status quo.\
C. Data mining.

**Answer: C.** 多次搜寻后选中显著关系，而非由经济机制提出并验证假设。

## Connection

CME 的估计误差会在 MVO 中被放大；使用稳健配置方法之前，先处理输入本身的质量。

[减少 MVO 输入误差造成的极端权重](/cfa/asset-allocation/review/04-principles/step-02) · [让 Variance–Covariance Matrix 反映真实风险](/cfa/asset-allocation/review/02-cme-part-2/step-05)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-framework)

---

[← Previous](/cfa/asset-allocation/review/01-cme-part-1/) · [Learning Map](/cfa/asset-allocation/review/01-cme-part-1/) · [Next Step →](/cfa/asset-allocation/review/01-cme-part-1/step-02)
