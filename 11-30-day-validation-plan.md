# Deliverable 11 — Practical 30-Day Market-Validation Plan

**Objective:** determine, within 30 days and before committing inventory capital, whether OurOwn can generate repeat purchases at positive contribution in one Kano polygon.
**Timing:** days are calendar days from kickoff. Owner columns assume a 2-person team. **All thresholds below are labelled hypotheses until validated.**

---

## Phase 1 — Days 1–7: Interviews & price collection

### A1 — Customer interviews (behaviour-based, not opinion)

- **Objective:** establish how target customers actually bought groceries in the last 2 weeks, what it cost them, and whether they have ever paid for delivery.
- **Method:** in-person interviews at 3 locations (one core urban neighbourhood, BUK perimeter, an institutional buyer cluster). Screening: did household groceries in last 7 days.
- **Sample:** **30 interviews** (20 households/professionals, 5 students, 5 institutional buyers: caterer/school/office).
- **Data to collect:** last purchase — where, what, how much, how they carried it, what annoyed them; delivery experience history; whether they have ever paid for a delivery and how much; willingness to place a *real* order today (ask for the order, not permission); payment preference (transfer-before vs pay-on-delivery); app vs WhatsApp.
- **Output:** transcript table; ≥3 recurring verbatim pain points; % who accept the live-order ask.
- **Decision:** **Hypothesis threshold:** if ≥8/30 show a recent paid-delivery precedent or accept a live order → continue; if ≤3 → pause and re-position (B2B-first or market-pickup model).

### A2 — Customer survey (n=100)

- **Objective:** quantify the interview signals.
- **Method:** short intercept survey (10 questions max), administered in Hausa/English.
- **Sample:** 100 respondents across the 3 locations.
- **Key questions (all behavioural):** last 3 grocery purchases (place, value, frequency); monthly grocery spend band; who does the shopping; transport cost/time to market per trip; ever paid delivery? how much; would they prepay ₦500 to a bank transfer for a ₦10k order; preferred delivery window.
- **Output:** spend distribution, delivery-fee acceptance curve by basket size, prepayment acceptance %.
- **Decision:** informs minimum-basket and fee setting (Deliverable 6 §3).

### A3 — Supplier meetings & price collection (days 2–5)

- **Objective:** replace every hypothetical cost with a written quote.
- **Method:** walk-in meetings — **Ghadco (46 Tafawa Balewa Rd)**, **Mamuda distributor line**, NBC Challawa depot; then Singer Market + Dawanau for benchmark carton prices. Template: [05-supplier-research-pack.md](05-supplier-research-pack.md) §3.
- **Sample:** ≥6 suppliers, ≥40 SKUs priced twice (direct vs market).
- **Output:** Sheet 1 populated with real landed costs; price index vs market; supplier comparison table.
- **Decision:** **Hypothesis:** ≥60% of target SKUs show modelled gross margin ≥8% at market-competitive prices → assortment confirmed; if staples only clear 3–5%, the assortment shifts to high-frequency local lines and the margin target is renegotiated upward.

### A4 — Competitor price & mystery-shop audit (days 3–7)

- **Objective:** real prices, fees and delivery promises where no public data exists.
- **Method:** price a 15-item basket at Sahad Stores, a neighbourhood kiosk, and one open market; mystery-shop Sahad/Sadaraki/KFE/BiteExpress for delivery fee, min order, delivery time (place a real small order each).
- **Output:** benchmark basket table; competitor fee/time card.
- **Decision:** OurOwn's launch price list must be within **±5% of the benchmark basket** (hypothesis) or the value proposition fails.

---

## Phase 2 — Days 8–21: Infrastructure & payment testing

### A5 — Delivery quotations & trial (days 8–12)

- **Objective:** real per-drop cost in the pilot polygon.
- **Method:** mystery-shop GIG Logistics Kano (3 centres), Fez Kano hub, and ≥3 local dispatchers (Safiyya, CC Delivery, Flexy Movers, CETRAH) with the same brief: 5kg ambient bag, 5km, within 24h; interview ≥5 riders on daily fuel, drops/day, fee/drop, COD experience.
- **Output:** per-drop cost card (quote vs rider reality); batch-feasibility map (cluster density of interview addresses).
- **Decision:** **Hypothesis:** batched cost ≤₦700/drop within polygon → proceed with batch model; if quotes cluster >₦1,200 with no batching possible → raise minimum basket to ₦15,000 or pause.

### A6 — Payment provider testing (days 8–15)

- **Objective:** verified settlement, not just checkout.
- **Method:** Paystack **and** Monnify sandbox integration (parallel); run the 5-test battery from [06-unit-economics-workbook-spec.md](06-unit-economics-workbook-spec.md) §4 — incl. a **₦5,000 live charge each** with bank-statement confirmation of settlement timing; ask both providers in writing: refund SLA, webhook retry schedule, virtual-account pricing.
- **Output:** completed scorecard with real numbers; chosen PSP.
- **Decision:** PSP selected only if live settlement confirmed ≤T+1 and reconciliation matches to the kobo.

### A7 — Technology readiness sprint (days 8–21)

- **Objective:** close the 🔴 pre-launch items ([08-technical-operational-readiness.md](08-technical-operational-readiness.md) §1).
- **Method:** independent technical review of the prototype (🔍 code + security checklist), fix payment verification/idempotency/reconciliation, RBAC+MFA, backups+restore test.
- **Output:** readiness sign-off sheet with the 10 acceptance tests passed.
- **Decision:** **No real customer orders accepted until all 🔴 items pass.** No exceptions.

---

## Phase 3 — Days 16–30: Micro live pilot

### A8 — Small live ordering pilot (days 16–30)

- **Scope:** one polygon, **~60 SKUs**, minimum basket ₦10,000, batched windows (2–3 slots/day), prepaid transfer, fee ₦800 (<₦15k) / free (≥₦15k). Demand generation: referral list from interviews + radio mention + WhatsApp broadcast — **no paid ads** (measures organic pull).
- **Sample/target:** **100 completed orders** over 15 days (≈7/day; **hypothesis threshold: ≥5/day for the final 8 consecutive days**).
- **Data to collect per order:** source channel, basket, fee paid, payment method, time to confirm, dispatch→delivery minutes, on-time %, failed/refused, substitution, complaints, second-order within 14 days.
- **Output:** the first real unit-economics sheet (actual contribution/order, not modelled).

### A9 — Repeat-order tracking (days 16–30+)

- **Method:** day-7 and day-14 reorder follow-up (WhatsApp call + ₦200 reorder credit); cohort table of first-100.
- **Decision:** **Hypothesis threshold: ≥30% of first-time buyers reorder within 14 days** → demand signal; 15–30% → investigate friction before scaling; <15% → stop or pivot.

### A10 — Unit-economics analysis (days 26–30)

- **Method:** replace every [H] input in Deliverable 6 with observed values; re-run all three delivery-pricing strategies on real data; compute contribution/order, CAC (if any channel measurable), and days-to-break-even at fixed ₦750k.
- **Output:** go/no-go memo with the real model.
- **Decision:** see §6.

---

## 4. Week-by-week schedule

| Days | Interviews | Prices/suppliers | Delivery | Payments | Tech | Pilot |
|---|---|---|---|---|---|---|
| 1–7 | A1 (30), A2 (100) | A3 (6 suppliers), A4 audit | — | — | review starts | — |
| 8–14 | follow-ups | quote reconciliation | A5 quotes + rider interviews | A6 sandbox + live tests | 🔴 fixes | soft launch prep |
| 15–21 | — | — | route batching | settlement confirmed | 10 acceptance tests | **pilot starts (day 16)** |
| 22–30 | — | — | measured cost/drop | reconciled daily | monitoring | pilot runs; A9 cohorts; A10 analysis |

## 5. Data capture (every activity)

Interview/survey: consent noted, transcripts stored with IDs. Prices: quote validity dates. Orders: CSV with the fields in A8. All inputs feed [06-unit-economics-workbook-spec.md](06-unit-economics-workbook-spec.md) sheets.

## 6. Go / Modify / Pause thresholds (all **hypotheses until validated**)

**GO (scale past pilot) if, by day 30:**
1. ≥100 completed orders, ≥5/day sustained over the final 8 days, **and**
2. AOV ≥ ₦10,000, **and**
3. Modelled **contribution/order positive on observed costs** (not hypotheticals), **and**
4. 14-day repeat rate ≥30%, **and**
5. On-time delivery ≥85% and failed deliveries ≤10%, **and**
6. ≥1 supplier on written terms incl. expiry/returns clause.

**MODIFY (extend 30 days, one change only) if:** orders 50–99 or repeat 15–30% or contribution marginally negative but diagnosable (fee too low, batch size small). Pick one lever: fee, minimum basket, or zone density.

**PAUSE (stop inventory capital) if:** <50 completed orders, or repeat <15%, or contribution clearly negative at every basket/fee combination tried, or payment settlement unreconciled, or supplier terms unobtainable. **A pause is a success: it costs 30 days, not 18 months** (GoLemon, Copia, Twiga lessons).

## 7. Pilot dashboard (daily/weekly review)

| Metric | Definition | How measured | Frequency |
|---|---|---|---|
| Customers reached | Unique contacts shown offer | Channel-tagged links/lists | Daily |
| First-time customers | First completed order | Order DB | Daily |
| Completed orders | Paid & delivered | Order DB | Daily |
| AOV | Revenue ÷ completed orders | Order DB | Daily |
| Gross margin % | (Price − landed cost) ÷ price, basket-weighted | Sheet 1 × orders | Weekly |
| Contribution/order | Deliverable 6 §2 chain with actuals | Workbook | Weekly |
| Repeat-purchase rate | % ordering again within 14 days | Cohort table | Weekly |
| Order cancellation rate | Cancelled ÷ paid | Order DB | Daily |
| On-time delivery % | Within slot ÷ dispatched | Dispatch timestamps | Daily |
| Product availability % | SKUs in stock ÷ SKUs wanted | Pick-list misses | Weekly |
| Complaints | Count + type, per 100 orders | Support log | Daily |
| CAC | Spend ÷ attributed first orders | Channel tracking | Weekly |
| Cash in inventory | Stock value at cost | Stock count | Weekly |
| Cash available | Bank balance | Bank | Daily |

## 8. What each activity decides

A1/A2 → *whether to proceed at all and to whom* · A3 → *real assortment and margin* · A4 → *price positioning* · A5 → *delivery model and minimum basket* · A6 → *PSP choice* · A7 → *launch permission* · A8/A9 → *demand and retention reality* · A10 → *scale, modify or pause*.
