# Deliverable 1 — Executive Research Summary

**Project:** OurOwn — grocery & everyday-essentials commerce, Northern Nigeria
**Prepared:** 30 October 2026 · All sources accessed 28–30 October 2026
**Basis:** Desk research + quantitative modelling. No customer interviews, no supplier confirmations, no code audit were available for this research (see evidence-gap register).

---

## 1. The commercial opportunity

Nigeria's total retail market was **₦25.4 trillion (~US$19.0 billion) in 2025** (Euromonitor, via Practical Ecommerce, 1 Sept 2026), of which retail **e-commerce is only ₦492 billion (~US$368 million)** and **online food/grocery is ~US$95 million (ECDB, 2025)** — online grocery is roughly **0.5% of the retail base and 0–5% of food retail**. This is a penetration bet, not a share-grab.

The Kano-specific opening is structural, not demographic:

- **No major delivery incumbent is in Kano.** Glovo's Nigerian footprint is Lagos, Abuja, Port Harcourt and Ibadan (Techeconomy, 6 Oct 2026; glovoapp.com/en/ng/kano returns 404). PricePally covers Lagos/Abuja/Ibadan/PH. Chowdeck's public city list does not confirm Kano. Jumia Food and Bolt Food are shut nationally.
- **Kano is a top-3 connectivity market:** 9.03 million active internet subscriptions — 3rd highest of any state after Lagos and Ogun (NBS, Q4 2023) — in a metro of ~4.9 million people.
- **Kano is where the goods already are:** Dawanau International Grains Market (10,000+ shops, 600+ warehouses) plus Kano-manufactured FMCG (Mamuda/Pop Cola, Ghadco distribution, NBC Challawa, Seven-Up Zaria Road) give a local sourcing advantage no Lagos competitor has.
- **Local online competitors are sub-scale:** Sahad Stores (brick-and-mortar + unclear e-commerce), Sadaraki (~260 Instagram followers), Kano Food Express (500+ app downloads), plus WhatsApp micro-merchants.

## 2. The most important evidence

| Finding | Why it matters | Source (date) |
|---|---|---|
| **GoLemon (Lagos) shut down July 2026** despite *positive contribution per order*; avg basket ₦43,700; cause = insufficient order density vs fixed costs | The exact model OurOwn proposes (owned inventory, own fulfilment) failed in a market 10× denser than Kano | TechCabal, 29 Jul 2026 |
| **Blinkit — world's largest grocery dark-store operator, ~2,400 stores — runs at ~0.3% adjusted EBITDA on order value** | Grocery margin structurally trends toward zero even at Indian density; 5% gross margin must cover everything below the gross line | Eternal Q4 FY26 results (secondary, Oct 2026) |
| **Chowdeck: profitable, 11 cities, ₦1.5bn/month of groceries — but grocery is only 11% of its business, bolted onto an existing food-delivery demand base** | Grocery delivery works as an extension of proven density, not as a first act | TechCrunch 11 Aug 2025; Technext Jul 2026 |
| **NBS CPI: food inflation 19.59% vs headline 14.63% (Sept 2026)** — cost of goods inflating faster than wages/CPI | A 5% margin is a shrinking target; price-list staleness destroys it | NBS via press, Oct 2026 (snippet-level, headline confirmed on TradingEconomics) |
| **Informal channels = 78–95% of FMCG volume; open markets set prices (Dawanau, Singer Market)** | OurOwn's real competitor is the kiosk and "send someone to the market", not an app | DALA/NielsenIQ 2026; USDA FAS GAIN NI2024-0014 (snippet) |
| **Modelled contribution per order is negative for every ₦5,000 basket and every margin ≤8% unless delivery is batched and/or a fee is charged** | Minimum basket + delivery pricing are the two levers that decide viability | See Deliverable 6 |
| **Payment reality: webhook ≠ settlement; NIBSS switch failures (May 2026); "I paid but no order" is the normal failure mode** | Payment verification/reconciliation is a launch-day requirement, not a Phase-2 feature | Paystack post-mortem 2019; TheCable 13 May 2026 (snippet) |

## 3. The most serious risks (top 5)

1. **Order-density failure (GoLemon's death).** Owned inventory + fixed cost + too few orders per km². Mitigation: one dense polygon, scheduled batch windows, minimum basket, rented delivery capacity, kill rule.
2. **Margin arithmetic.** At 5% gross margin, a ₦10,000 order generates ₦500 gross profit against ~₦1,900 of payment + packaging + delivery + losses (base assumptions). 5% cannot work alone; 8–10%+ with a ₦10,000+ minimum basket and batched delivery is the break-even zone.
3. **No validated demand.** Zero interviews, zero live orders, no Kano e-grocery data exists publicly. The single biggest uncertainty is whether Kano customers will order groceries online at all, and at what price.
4. **Cash & working-capital risk.** Alerzo (₦5bn loan, Mareva injunction, Jan 2026) shows what happens when inventory/fleet is funded with expensive naira debt; GoLemon shows what happens when funding stops. Do not finance stock with 30%+ debt.
5. **Trust, COD and failed deliveries.** COD/failed-delivery rejection rates of 20–30% are industry-reported (Selligate, unattributed primary); perishables refused on delivery are a write-off, not a return.

## 4. Viability of the initial owned-inventory model

**Conditionally viable — but not as originally sketched.** Owned inventory works *only* if:

- **Minimum basket ≥ ₦10,000** (ideally ₦15,000 for free delivery) — below that, contribution is negative at any realistic margin.
- **Gross margin ≥ 8–10% blended**, not 5%. A 5% margin is negative-contribution at ₦5,000–₦20,000 baskets unless delivery cost falls to ~₦600/order through batching.
- **Delivery is batched** (scheduled windows, multiple drops per trip) and **charged** — either as a visible fee (₦800–₦1,200) or recovered through a minimum-basket rule.
- **Assortment is narrow and local:** staples, grains, oils, Kano-manufactured FMCG (Ghadco/Mamuda portfolio, NBC drinks) where landed cost beats Lagos-based competitors — ambient-first, no cold chain in phase 1.
- **Fixed cost stays tiny** until density is proven: no owned fleet, no dark-store arms race, no city #2.

The founders' three-stage path (owned → supplier network → marketplace) is directionally sound and matches what survived elsewhere, **but the marketplace stage must be gated on explicit evidence thresholds** (see Deliverable 11, section 6).

## 5. Main questions that remain unanswered

1. Will Kano customers pay for online grocery delivery at all? (No public data exists; 30-day pilot required.)
2. What delivery fee/basket-size combination converts? (A/B test required.)
3. Can OurOwn actually buy at wholesale prices below Singer Market carton prices, net of transport? (Supplier quotes required.)
4. Will Ghadco/Mamuda supply a new, uncapitalised retailer, and on what terms? (Direct outreach required.)
5. What is the real per-drop delivery cost from a Kano 3PL or rider? (Mystery-shop quotes required.)
6. Which payment provider settles cheapest at ₦8,000–₦20,000 baskets? (Paystack vs Monnify A/B in sandbox + live pilot.)
7. Is the Afrizen Capital operating shell adequate for PSP onboarding, contracts and liability? (Lawyer + PSP onboarding check.)
8. Is repacking/pre-portioning of staples in scope? (Decides whether NAFDAC manufacturer registration attaches — must be answered in writing before selling.)

## 6. Recommended next steps (7-day version)

1. **Freeze scope:** one polygon in Kano metro (2–3 core LGAs), ~60–100 SKUs, ambient goods, minimum basket ₦10,000, scheduled delivery windows.
2. **Collect real prices:** 1 day at Singer Market + Dawanau + Ghadco (46 Tafawa Balewa Rd) to build the SKU-level margin table (Deliverable 6 template).
3. **Get delivery quotes:** mystery-shop GIG Logistics Kano (3 branches), Fez Kano hub, and 3 local dispatch riders for a 5kg ambient bag within 10km of Sabon Gari.
4. **Test payment:** Paystack sandbox + ₦1,000 live transaction; confirm settlement timing to the Afrizen account in writing.
5. **Talk to 10 customers** using the interview script in Deliverable 11 — behaviour, not "would you use this app".
6. **Answer the compliance eight** (Deliverable 9, section 10) with a Nigerian lawyer — entity, objects clause, NAFDAC repacking, rider classification, NDPC registration.
7. **Decide go/no-go** against the pilot thresholds in Deliverable 11 before committing inventory capital.

---

**Read next:** [13-decision-framework.md](13-decision-framework.md) for direct answers to the 17 decision questions; [06-unit-economics-workbook-spec.md](06-unit-economics-workbook-spec.md) for the margin arithmetic.
