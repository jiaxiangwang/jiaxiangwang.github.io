---
title: "Step 2 — 从盈利、分红与估值拆解 Equity Return"
---

# Step 2 — 从盈利、分红与估值拆解 Equity Return

## 两种方法解决不同问题

**Grinold–Kroner (G–K)** 拆预期回报从何而来；**Singer–Terhaar** 用全球整合程度解释均衡风险补偿是多少。前者是 cash-flow / valuation 分解，后者是 required-return framework。两者不能混为同一“选最高收益率市场”的模型。

### Grinold–Kroner：增长不等于全部回报

**Must memorize：**

$$E(R_e)\approx D/P+\pi+g_{real\ earnings}-\Delta S+\Delta(P/E)$$

$D/P$ 是 dividend yield；$\pi+g$ 是 aggregate nominal earnings growth；$\Delta S$ 是净股份数量增长，发行稀释减回报，repurchases 使 $\Delta S<0$；最后一项是 P/E 的**相对变化率**，不是倍数点数变化。

P/E 从 14.5 降至 14.0，相对变化 $14/14.5-1=-3.45\%$。预期 dividend yield 2.4%、通胀 2.3%、真实盈利增长 5%、股数不变，下一年回报近似 $2.4+2.3+5-3.45=6.25\%$。若扣当前匹配基准国债收益率 2.3%，得到 forward-looking equity-vs-bonds premium 约 3.95%。不能扣历史平均 yield 替代当前基准。

### Singer–Terhaar：总风险还是系统风险获补偿？

**Know how to use：** 全球完全整合时，只有与全球市场共变的风险得到补偿：

$$RP_i^{int}=\rho_{i,G}\sigma_i\frac{RP_G}{\sigma_G}$$

完全分割时可用本地市场 Sharpe ratio：$RP_i^{seg}=\sigma_i SR_i$。Partial integration 以题干给定整合权重 $\phi$ 组合两者：$RP_i=\phi RP_i^{int}+(1-\phi)RP_i^{seg}$。所求是 total return 时再加 $r_f$；不能把 premium 当 total return。

更充分整合通常降低不可分散风险的要求补偿，并可带来重估价格上涨；**transition gain** 与“整合之后较低的长期 required return”是不同问题。没有价格或预期实现收益时，不能仅凭所需风险溢价高低比较 valuation attractiveness。

**Exam Trigger — Calculate：** share repurchases 的符号、P/E 变化率、premium vs total return。**Boundary Condition：** 长期盈利受经济增长限制；governance、财产权与少数股东保护对 equities 尤其重要，因为其为 residual claims。

## Immediate Practice

Source: Local Other CME，No.2025060303000024 — adapted；答案为推导。

A fully integrated market has volatility 15%, correlation with global market 0.60, global Sharpe ratio 0.35 and risk-free rate 1.5%. Expected total return is:

A. 3.15%.\
B. 4.65%.\
C. 6.00%.

**Answer: B.** $RP=0.6\times15\%\times0.35=3.15\%$，再加 1.5%。A 漏掉 risk-free return。

## Connection

长期盈利输入接自 trend growth；全球整合和治理风险又影响 robust MVO 的预期与相关性假设。

[区分 Trend Growth 与周期增长](/cfa/asset-allocation/review/01-cme-part-1/step-02) · [减少 MVO 输入误差造成的极端权重](/cfa/asset-allocation/review/04-principles/step-02) · [区分 PPP 长期锚与 Capital Flows 短期力量](/cfa/asset-allocation/review/02-cme-part-2/step-04)

[Practice More Questions →](/cfa/asset-allocation/questions/#concept-equity)

---

[← Previous](/cfa/asset-allocation/review/02-cme-part-2/step-01) · [Learning Map](/cfa/asset-allocation/review/02-cme-part-2/) · [Next Step →](/cfa/asset-allocation/review/02-cme-part-2/step-03)
