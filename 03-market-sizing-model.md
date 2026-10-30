# Deliverable 3 — Market-Sizing Model (TAM / SAM / SOM)

**Date:** 30 Oct 2026 · Every formula, input, source and assumption shown. Hypothetical inputs are marked **[H]**, sourced inputs **[S]**, derived values **[D]**.

> ⚠️ **No public source contains any Kano e-grocery figure.** This model is built bottom-up from population data and stated assumptions. Confidence is **Low-to-Medium** throughout; the purpose is to bound the problem and expose which inputs the pilot must measure.

---

## 1. Definitions

- **TAM** — total annual grocery spend by households in the Kano metropolitan area (all channels). It is *not* OurOwn's market; it is the pool.
- **SAM** — the portion OurOwn can actually serve: households inside pilot delivery zones, reachable digitally, willing and able to buy groceries online.
- **SOM** — what OurOwn could plausibly capture within 12 months given conversion, repeat rate, delivery capacity and marketing.

---

## 2. TAM — Kano metropolitan grocery spend

**Formula:** `TAM = metro households × monthly grocery spend per household × 12`

Inputs:

| Input | Value | Basis | Tag |
|---|---|---|---|
| Kano metro population | 4,910,000 (2022) | citypopulation.de agglomeration from NPC/NBS | [S] |
| Household size | 6.0–6.5 persons | Nigeria avg ~5.2 (NBS NLSS); Northern states larger — range assumption | [H] |
| Metro households | **755,000–820,000** | 4.91m ÷ 6.0–6.5 | [D] |
| Monthly grocery spend (food-at-home + household essentials) | **₦30,000–₦60,000** | Anchored to NBS 2019: ₦47,500/month household food (2019 naira, NLSS 2018/19), CPI-escalated ~3× then discounted 30–40% for (a) Kano's below-average income, (b) excluding food-away-from-home | [H] — **the weakest input; no Kano expenditure survey obtained** |

**Result:**

| Scenario | Calculation | TAM |
|---|---|---|
| Conservative | 755,000 × ₦30,000 × 12 | **₦272bn/yr** |
| Base | 785,000 × ₦45,000 × 12 | **₦424bn/yr** |
| Optimistic | 820,000 × ₦60,000 × 12 | **₦590bn/yr** |

**Cross-check (top-down):** Kano metro ≈ 2.2% of Nigeria's population in a low-income state; applying 1.5–2.0% to Nigeria's ₦25.4trn total retail (Euromonitor 2025) gives ₦380–510bn — consistent with the range above. **Use ₦270–590bn, mid ₦420bn, as TAM with Low confidence.**

**Limitations:** household size and Kano-specific spend are unmeasured; NLSS 2022/23 wave (not 2019) should replace the anchor when obtained; inflation between now and use of the model erodes naira values.

---

## 3. SAM — households OurOwn can actually serve

**Formula:** `SAM = zone households × reachable share × monthly spend × 12`

A single Kano dark store/dispatch hub realistically serves a **5–8 km radius** in dense core LGAs. Pilot zone = parts of **Nasarawa, Dala, Kano Municipal, Gwale, Fagge** (the contiguous urban block: 3.53m people across these 8 LGAs; a 3-LGA slice ≈ 1.1–1.4m people).

| Input | Value | Basis | Tag |
|---|---|---|---|
| Zone households | **180,000–240,000** | ~1.15–1.4m people ÷ 6.0–6.5 | [D]/[H] |
| Reachable share | **25–35%** | Has smartphone (Kano: 9.0m internet subs/15.5m state pop suggests high but incomplete reach), within zone, willing to transact online. **No source exists — this is exactly what the pilot measures** | [H] |
| Effective spend via platform | Use full ₦30k–60k spend for reachable households as the *ceiling*; realistic platform share of their grocery spend in year 1 is far lower (see SOM) | | |

| Scenario | Calculation | SAM (upper bound of reachable spend) |
|---|---|---|
| Conservative | 180,000 × 25% × ₦30,000 × 12 | **₦162bn/yr** |
| Base | 210,000 × 30% × ₦45,000 × 12 | **₦340bn/yr** |
| Optimistic | 240,000 × 35% × ₦60,000 × 12 | **₦605bn/yr** |

**Important honesty note:** these SAM numbers say "spend that is theoretically reachable", **not** spend OurOwn can win. Conversion to an actual online-grocery habit in a market where online grocery is <1% of food retail is the real discount — applied in SOM. Presenting ₦340bn as "our market" would be misleading; **the defensible statement is: "reachable household spend in the pilot zone is in the low hundreds of billions of naira; our realistic capture is a fraction of one percent of it."**

---

## 4. SOM — realistic 12-month capture

**Formula:** `SOM = active ordering customers × orders per customer per month × AOV × 12`

| Scenario | Active customers | Orders/customer/mo | AOV | Annual revenue | Orders/day |
|---|---|---|---|---|---|
| **Conservative** | 250–300 | 1.0 | ₦8,000 | **₦24–29m** | ~9–11 |
| **Base** | 550–650 | 1.2 | ₦9,000 | **₦59–70m** | ~22–26 |
| **Optimistic** | 1,000–1,200 | 1.3 | ₦10,000 | **₦125–144m** | ~43–52 |

Sanity anchors:
- Base ≈ the founders' **₦60m** target (≈ 17–26 orders/day). Optimistic ≈ **₦100m+** (≈ 45/day).
- GoLemon (Lagos, far denser) got to "tens of thousands of orders" over ~2.5 years then died of density — so the optimistic column requires **repeat-purchase rates nobody has measured**, plus delivery cost control.
- 87% cart abandonment and ~1.5% session conversion (ECDB) imply marketing must drive large traffic or — realistically in Kano — **referral/WhatsApp/radio-driven direct orders**.

**Share of SAM won (base):** ₦65m ÷ ₦340bn ≈ **0.02%** — small, which is why the opportunity is plausible; **share of *actual online grocery* demand matters more**: Nigeria's whole online grocery is ~US$95m (~₦130bn); Kano's slice is unknown but plausibly single-digit ₦bn — so a ₦65m OurOwn would be a rounding error nationally but a real player locally.

---

## 5. Sensitivity — what moves SOM most

Ranked by impact (own analysis, from the model):

1. **Orders per customer per month** (1.0 → 2.0 doubles SOM): retention is the swing factor.
2. **AOV** (₦8k → ₦15k: +87% revenue with same orders): minimum-basket policy is the strongest single lever.
3. **Reachable/willing share** (25% → 35%): trust and delivery reliability, not advertising.
4. **Fixed-cost discipline:** does not change SOM but changes whether SOM is profitable (Deliverable 6).

## 6. Data needed to improve confidence (in priority order)

1. **Actual AOV and order frequency** from a live pilot (replaces two [H] inputs at once).
2. **Kano household expenditure data** — NBS NLSS 2022/23 state tables / GHS Panel Wave 5 (PDFs at nigerianstat.gov.ng).
3. **Reachable-household count per ward** — Kano State Bureau of Statistics / NPC; or field enumeration of the pilot zone.
4. **EFInA A2F microdata** (free on request) cut to North-West/Kano for payment-behaviour inputs.
5. **Competitor order density** — mystery-shop Sahad/Sadaraki/KFE; interview riders on actual drops/day by cluster.
