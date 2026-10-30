# Deliverable 6 — Financial & Unit-Economics Workbook Specification

**Spreadsheet-ready tables.** All **hypothetical inputs are labelled [H]** and must be replaced with quotations and observed data. Verified published figures are **[V]** with source. **No output here is a forecast.**

---

## 0. Sheet 0 — Input register (replace before trusting any output)

| Input | Base value used here | Type | How to verify |
|---|---|---|---|
| Payment processing | 1.5% + ₦100, capped ₦2,000 per transaction | **[V]** Paystack published Nigeria local rate (support.paystack.com, Oct 2026) | Compare live invoices from chosen PSP |
| Packaging per order | ₦250 | **[H]** | Quote bag/box suppliers (Kano) |
| Delivery cost, single drop | ₦1,200 | **[H]** anchored on observed Nigerian band ₦1,000–₦1,700 | Mystery-shop 3PL/rider quotes (Deliverable 11, A5) |
| Delivery cost, batched (3+ drops/trip) | ₦600 | **[H]** derived from ₦350–600 variable floor | Rider interviews + trip timing |
| Delivery fee charged | ₦0 / ₦800 / ₦1,000 scenarios | **[H]** | A/B pilot (Deliverable 11, A6) |
| Losses (spoilage + returns + failed delivery) | 2% of revenue | **[H]** | Track from order 1; COD rejection assumed 10–20% prepaid, 20–30% COD |
| Discounts/promotions | 0% base; 3% promo scenario | **[H]** | Actual promo calendar |
| Blended gross margin | 5% / 8% / 10% / 12% / 15% scenarios | **[H]** founders' 5% is unvalidated | SKU margin table (Sheet 1) |
| Fixed opex (pilot) | ₦750,000/month illustrative | **[H]** real payroll/rent quotes required | Actual commitments |
| Operating days | 365 (delivery 7 days) / 300 (6 days/week) | **[H]** GIG Kano is closed Sundays — if using such 3PL, 300 | Policy decision |

---

## 1. Sheet 1 — Product cost & selling price (SKU level)

Columns: `SKU | Category | Unit | Supplier | Carton price | Units/carton | Unit cost | Transport to store (₦/unit) | Landed cost | Selling price | Gross profit ₦ | Gross margin % | Market benchmark price (Singer/Dawanau) | Price index vs market | NAFDAC no. | Expiry date | Days-to-expiry at receipt | Reorder?`

Rule: `Landed cost = (carton price + transport + breakage allowance) ÷ units/carton`. Flag any SKU where `Gross margin% < 8%` or `Price index > 1.10` (dearer than the market).

## 2. Sheet 2 — Basket-level profitability (the model behind this deliverable)

Formula chain per order:

```
Gross profit      = basket × margin%
Payment cost      = MIN(basket × 1.5% + ₦100, ₦2,000)
Packaging         = ₦250
Delivery cost     = ₦1,200 single-drop  |  ₦600 batched
Discounts         = basket × promo rate (0 base)
Losses            = basket × 2%
Delivery fee in   = ₦0 | ₦800 | ₦1,000
Contribution      = gross profit + fee − payment − packaging − delivery − discounts − losses
```

### Table 2a — Single-drop delivery (₦1,200), **no delivery fee** (free delivery embedded)

| Basket | 5% | 8% | 10% | 12% | 15% |
|---|---|---|---|---|---|
| ₦5,000 | −1,475 | −1,325 | −1,225 | −1,125 | −975 |
| ₦10,000 | −1,400 | −1,100 | −900 | −700 | −400 |
| ₦20,000 | −1,250 | −650 | −250 | **+150** | +750 |
| ₦30,000 | −1,100 | −200 | **+400** | +1,000 | +1,900 |

### Table 2b — Single-drop delivery (₦1,200), **₦1,000 fee collected**

| Basket | 5% | 8% | 10% | 12% | 15% |
|---|---|---|---|---|---|
| ₦5,000 | −475 | −325 | −225 | −125 | +25 |
| ₦10,000 | −400 | −100 | **+100** | +300 | +600 |
| ₦20,000 | −250 | **+350** | +750 | +1,150 | +1,750 |
| ₦30,000 | −100 | **+800** | +1,400 | +2,000 | +2,900 |

### Table 2c — **Batched delivery (₦600), ₦800 fee** (recommended operating model)

| Basket | 5% | 8% | 10% | 12% | 15% |
|---|---|---|---|---|---|
| ₦5,000 | −75 | +75 | +175 | +275 | +425 |
| ₦10,000 | 0 | **+300** | +500 | +700 | +1,000 |
| ₦20,000 | +150 | +750 | +1,150 | +1,550 | +2,150 |
| ₦30,000 | +300 | +1,200 | +1,800 | +2,400 | +3,300 |

**Reading of the model:**
1. **At the founders' 5% margin, delivery is the whole problem**: only batched delivery + a fee makes even ₦5,000–₦10,000 baskets work, and contribution (−75 to +300) cannot fund fixed costs at pilot volumes.
2. **Break-even zone: ≥8–10% blended margin, ≥₦10,000 basket, batched delivery, fee charged** → ₦300–₦700 contribution/order.
3. Free-delivery-only (Table 2a) requires baskets ≥₦20,000 at ≥12% — viable only for stock-up missions, hence **minimum basket policy**.
4. Never present Table 2b/2c outputs as forecasts — inputs are hypothetical.

## 3. Sheet 3 — Delivery pricing strategies compared

| | Strategy 1: separate fee | Strategy 2: embedded in price | Strategy 3: free above minimum basket |
|---|---|---|---|
| Mechanics | ₦800–₦1,000 fee shown at checkout | +10–12% on every price to recover ₦1,200 | Fee ₦0 if basket ≥ ₦15,000; ₦1,000 below |
| Contribution effect (₦10k basket, 10%) | +₦100 with fee (Table 2b) | Breakeven only if price uplift ≈ cost; but **prices now ~12% above market** → conversion loss | Neutral on small orders; funds fee from ₦1.5k gross profit at ₦15k |
| Trust/compliance | ✅ transparent — matches FCCPC "all disclosures before payment" | ❌ undisclosed charge = trust & regulatory risk if discovered | ✅ clear rule, strong conversion lever (Chowdeck's ₦3,000 bar) |
| Competitive effect | Fee is visible friction | Visibly dearer than kiosk/market → kills price comparison | Rewards bulk — aligns with economics |
| Verdict | **Adopt for orders < ₦15,000** | **Reject** while customers price-compare | **Adopt for orders ≥ ₦15,000** |

**Recommended hybrid:** minimum basket **₦10,000**; delivery **included free at ≥₦15,000**, **₦800–₦1,000 below**; scheduled batch windows. Never call delivery "free" if it is hidden in an above-market price — say "free delivery on orders of ₦15,000+".

## 4. Sheet 4 — Payment provider comparison & weighted scorecard

**Published fees (Oct 2026, official pages):**

| Provider | Local card/transfer | Intl | Virtual account | Settlement | Splits/marketplace | Public docs |
|---|---|---|---|---|---|---|
| Paystack | 1.5% + ₦100 (cap ₦2,000; ₦100 waived <₦2,500) | 3.9% + ₦100 | 1% cap ₦300 | **T+1 contractual** | Multi-split, delayed settlement (best documented) | Extensive |
| Flutterwave | 2% (1.4+0.6) **+ 7.5% VAT** ≈ 2.15% | 4.8% | yes | next day | Subaccounts; merchant bears chargebacks | Strong |
| Monnify | 1.5% cap ₦2,000 | 4% | ₦500 flat (confirm) | **T+0 by 22:00 + 3 express/day** | max 5 splits, manual enablement + indemnity | Good |
| Paga | **not published** | — | Paga account numbers | not published | none documented | Dated (SHA-512, IP whitelisting) |
| PayGate (Upperlink) | **not published** | USD settlement offered | — | not published | none found | **none public** |

**Weighted scorecard (weights = founders' priorities; scores 1–5, evidence-based, October 2026):**

| Criterion (weight) | Paystack | Flutterwave | Monnify | Paga | PayGate |
|---|---|---|---|---|---|
| Cost at ₦8k–₦20k baskets (25%) | 3 | 3 | **5** | 2 | 2 |
| Settlement speed / cashflow (20%) | 3 | 4 | **5** | 2 | 2 |
| Docs & integration quality (15%) | **5** | 4 | 4 | 2 | 1 |
| Marketplace readiness Stage 3 (15%) | **5** | 4 | 3 | 1 | 1 |
| Reconciliation/virtual accounts (10%) | **5** | 4 | 4 | 3 | 1 |
| Transparency of published terms (10%) | **5** | **5** | **5** | 1 | 1 |
| Support/reliability reputation (5%) | 4 | 3 | 4 | 3 | 1 |
| **Weighted total** | **4.10** | **3.75** | **4.30** | 2.05 | 1.35 |

**Recommendation (criterion-driven, not popularity):** **Pilot = Paystack OR Monnify**, decided by measured AOV: AOV <₦6,000 → Monnify (no ₦100 flat fee); AOV ≥₦6,000 and Stage-3 marketplace plans → Paystack. Keep Flutterwave as redundancy. **Paga and PayGate: RFP only — request written fee schedule, settlement SLA, API docs before any evaluation.** Never claim any provider is "best" beyond these criteria.

**Sandbox/live testing procedure:** (1) sandbox: charge every method (card, transfer, USSD, VA), kill webhooks deliberately, confirm server-side verify recovers; (2) duplicate-payment test: same reference retried → single fulfilment; (3) refund test on a live ₦2,000 order → confirm days-to-refund; (4) **settlement test**: ₦5,000 live charge → confirm T+1 credit on Afrizen's bank statement and reconcile against dashboard; (5) run for ≥2 weeks including a weekend.

## 5. Sheet 5 — Monthly fixed operating expenses (pilot, illustrative [H])

| Item | ₦/month | Note |
|---|---|---|
| 2 staff (ops + customer service) | 300,000 | actual payroll quotes required; federal min wage ₦70,000 |
| Store/pick space rent + service charge | 100,000 | Kano location-dependent; + LGA tenement |
| Rider/delivery partnership (prepaid float) | 150,000 | if not per-drop |
| Software/tools/PSP monthly costs | 25,000 | hosting, SMS/WhatsApp, analytics |
| Utilities/backup power | 50,000 | grid unreliability |
| Marketing (radio spot + WhatsApp) | 75,000 | SCIMDER: radio is Kano's mass channel |
| Contingency | 50,000 | |
| **Total** | **₦750,000** | |

**Break-even:** at contribution ₦300/order → **2,500 orders/month (~83/day)**; at ₦700/order → **1,071/month (~36/day)**. *This is why batching + minimum basket + 8–10% margin are non-negotiable.*

## 6. Sheet 6 — Sales scenarios & break-even (Deliverable 2, Area G restated)

| Target | AOV | Orders/yr | Orders/mo | Orders/day (300 op. days) | Gross profit @10% |
|---|---|---|---|---|---|
| ₦60m | 5,000 | 12,000 | 1,000 | 40 | ₦6.0m |
| ₦60m | 10,000 | 6,000 | 500 | 20 | ₦6.0m |
| ₦60m | 15,000 | 4,000 | 333 | 13 | ₦6.0m |
| ₦100m | 10,000 | 10,000 | 833 | 33 | ₦10.0m |
| ₦100m | 15,000 | 6,667 | 556 | 22 | ₦10.0m |
| ₦100m | 20,000 | 5,000 | 417 | 17 | ₦10.0m |

Variable costs per Tables 2a–c consume most of gross profit; **₦100m sales ≈ ₦3–8m contribution at modelled inputs — NOT ₦100m profit.**

## 7. Sheet 7 — Working capital & monthly cash flow (template)

Rows: Opening cash · Inventory purchases (prepay) · Delivery top-ups · PSP settlement received (T+1) · Payroll · Rent · Marketing · Net cash flow · Closing cash · **Days of inventory cover · Cash tied up in stock**.
Key rules: (a) T+1 settlement means yesterday's sales fund today's stock; (b) never let inventory cover exceed the cash runway; (c) Alerzo warning — no high-rate naira debt for inventory.

## 8. Sheet 8 — Refunds, returns, spoilage log

`Order ID | Reason (wrong/expired/short-delivery/refused/COD-failed) | Value | Recoverable Y/N | Credit given | Rider/supplier responsible | % of revenue (target <2%)`

## 9. Sheet 9 — Discount & promotion tracker

`Campaign | Dates | Discount value | Uplift in orders (vs baseline) | CAC effect | Contribution after promo` — because promotions must be evaluated on **incremental contribution**, not gross sales.

## 10. Sheet 10 — Dashboard definitions (daily/weekly review)

Orders/day · AOV · Contribution/order · Repeat-purchase rate (30-day) · On-time delivery % · Availability % (SKUs in stock at order time) · Failed-delivery % · Complaints/order · Cash in bank · Inventory days. (Definitions and cadence in Deliverable 11 §7.)
