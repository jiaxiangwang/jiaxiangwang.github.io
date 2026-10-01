---
title: "Step 6 — 把 Probability、Horizon 与 Funding Cost 连起来"
---

# Step 6 — 把 Probability、Horizon 与 Funding Cost 连起来

## 高平均回报不等于高目标成功率

Goals-based allocation 为每个目标明确金额、horizon、priority 和 required success probability，再选择 sub-portfolio。计算 funding cost 时使用该期限与概率下的 **minimum expectation return**，而非无条件平均回报。

**Know how to use：** 若将年化回报近似看作独立、正态且适合简单年化处理，可作直觉近似 $r_{min}(p,T)\approx\mu-z_p\sigma/\sqrt T$。它不替代题干表格或更可靠多期分布模型；非正态、现金流与相关序列会改变结果。

更高 $p$ 使 lower-tail return 更低；同 $p$ 下更长期限可能减轻年化噪声，但不能消除 shortfall 或 sequence risk。单一年末目标以匹配 $r_{min}$ 折现：

**Must memorize：**

$$PV_{goal}=\frac{FV_{goal}}{(1+r_{min})^T}$$

同一目标下，符合 success rate 的 $r_{min}$ 越高，所需初始资本越少。不能先选最高 expected return portfolio 再声称最便宜。

## 单期目标：Roy Safety-First Ratio

如果目标是下一年回报至少达到 $R_L$，在可按相同正态模型比较的 return distributions 下，可最大化 **Roy Safety-First Ratio**：

**Know how to use：**

$$SFR=\frac{E(R_p)-R_L}{\sigma_p}$$

分子是超过最低目标的 buffer，分母是噪声；标准化 buffer 越大，shortfall probability 越低。$R_L$ 不是默认 risk-free rate；只有目标恰为 $r_f$ 时才与 Sharpe 相同。非正态或分布形状不同，仅凭该 ratio 不能精确比较概率，应看完整 lower-tail distribution。

Shipman 要从 $900,000$ 支出 $54,000$ 且不损本金，所以 $R_L=6\%$。三个 portfolio 的 ratios 为 $(10.5-6)/20=0.225$、$(9-6)/13=0.2308$、$(7.75-6)/10=0.175$；第二个更有可能达标，而非最高均值或最低波动的组合。

这个单期思路与多期目标的 minimum expectation return 相接：两者都把风险相对实际目标表达，不能把平均 return 当成功率。

## 多个支出用现金流现值

若未来 $N$ 年每年**期初**支出，第一笔为 $C_0$、通胀 $g$、适用折现率 $r$：

**Know how to use：**

$$PV=C_0\sum_{t=0}^{N-1}\left(\frac{1+g}{1+r}\right)^t$$

期末开始则改时点。立即支出的第一笔不能再折现一年；future nominal lump sum 不应再多加通胀。

## Armstrong Case 的完整选择逻辑

Goal 1（5 年/85%）对应表中最高 minimum return 为 C 4.4%；Goal 2（10 年/99%）为 B 2.2%；Goal 3（25 年/75%）为 D 7.5%。分别计算现值，再加总与 8 million 资本比较；剩余按客户指令投 A。若预算不够，应调整目标、概率、期限或追加资金，不能直接升高风险就假称达标。

**Exam Trigger — Select / Justify / Construct：** 先在正确 horizon/probability row 中选最大 $r_{min}$，再折现并算权重。**Common Trap：** 均值 9%、需要 85% 成功率，直接用 9% 折现；或把每个目标成功率当所有目标联合成功率。

> Quick Recall：required success probability 上升，funding cost 通常怎样变？\
> **Answer: Higher。** lower-tail discount rate 下降，需要更多初始资金。

## Immediate Practice

Source: Local Other AA，No.2025072102000011 — adapted；答案为推导。

A portfolio has mean return 9% and volatility 15%. The client wants an 85% probability of reaching a five-year goal. The discount rate is **most likely**:

A. Below 9%.\
B. Equal to 9%.\
C. Above 9%.

**Answer: A.** 高于 50% 的成功概率需要用更保守的 lower-tail return，而不是均值。

## Connection

目标框架来自 risk definition；inflation 形成未来支出，simulation 检查多期及联合 shortfall，taxes 决定净回报口径。

[选择与目标一致的 Risk Definition](/cfa/asset-allocation/review/03-overview/step-03) · [用 Scenario / Monte Carlo 检查路径与目标风险](/cfa/asset-allocation/review/04-principles/step-03) · [用 After-tax Exposure 进行配置与 Asset Location](/cfa/asset-allocation/review/05-constraints/step-04)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-goals)

---

[← Previous](/cfa/asset-allocation/review/04-principles/step-05) · [Learning Map](/cfa/asset-allocation/review/04-principles/) · [Next Step →](/cfa/asset-allocation/review/04-principles/step-07)
