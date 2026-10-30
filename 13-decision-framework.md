# Deliverable 13 — Decision Framework: Direct Answers to the Founders' 17 Questions

**Rule applied:** every answer states the reasoning, the supporting evidence, the uncertainty, and the next action. Where evidence was insufficient, the answer is a concrete test rather than an opinion.

---

**1. Should OurOwn launch first in Kano, and why?**
**Yes.** Kano has no delivery incumbent (Glovo /kano → 404; PricePally/Chowdeck absent; Jumia Food and Bolt Food dead nationally), it is a top-3 connectivity market (9.03m internet subs), and it is the founders' home advantage plus the sourcing hub (Dawanau, Singer, Ghadco, Mamuda, NBC Challawa) — a landed-cost edge no Lagos competitor can match. *Uncertainty:* zero Kano e-grocery demand data exists. *Next action:* Days 1–30 validation plan; go/no-go on its thresholds.

**2. Which customer segment first?**
**Households in 2–3 core urban LGAs doing weekly stock-up (₦10k+ baskets)** as the revenue base, **simultaneously pursuing 3–5 institutional buyers** (caterers/offices/schools) as the density shortcut — bulk, prepaid, no consumer CAC. Students (BUK) only via batched campus drops once routing works. *Evidence:* baskets ₦10k+ are the only contribution-positive zone (Deliverable 6); B2B has no public competition evidence but zero demand evidence either → 5 interviews in week 1 (A1).

**3. Which initial products?**
**60–100 ambient SKUs:** staples and grains (Dawanau), oils, confectionery/biscuits (Ghadco/Mamuda), beverages incl. Pop Cola (NBC Challawa/Ghadco), detergent/household (Too Clean, OK Plast), shelf-stable juices. **No chilled/frozen in phase 1** (no cold chain: <1,000 reefers nationally). Include items where OurOwn can beat the market index, exclude price-transparent branded items that only clear 3–5% unless they drive basket size. *Next action:* Sheet 1 margin table from real quotes (A3).

**4. How to source?**
Three-lane: (a) **direct from Ghadco/Mamuda/NBC depot** for Kano-made goods (freight ≈ 0); (b) **cash-and-carry at Singer/Dawanau** for everything else, arbitraging daily; (c) never budget from published "distributor terms" — none exist. Buy the lower *landed* cost per SKU; written returns/expiry clauses on every supplier account. Detail: [05-supplier-research-pack.md](05-supplier-research-pack.md).

**5. What evidence before approaching large distributors for commercial terms?**
(1) 40+ SKU price benchmark vs market; (2) 100+ completed orders proving order frequency; (3) a legal entity/objects confirmation so you can sign; (4) a 90-day volume projection with real cohort data; (5) premises/invoice capability (CAC, VAT position). Distributors sell to *routes*, not ideas — bring evidence you are a route.

**6. Can a 5% gross margin work?**
**Not on the modelled assumptions.** At 5%, contribution is negative for every ₦5k–₦10k basket and only reaches +₦150–₦300 at ₦20k–₦30k with batched delivery and a fee. 5% also funds nothing for fixed costs at pilot volumes. **What must change:** blended gross margin to **8–10%** (category mix: local lines 10–15%, price-sensitive branded 5–8%), minimum basket ₦10,000, delivery fee ≥₦800 below ₦15,000, batching to ₦600/order. With those, contribution is +₦300–₦700/order — still demanding (break-even ≈ 1,071–2,500 orders/month at ₦750k fixed cost). Full arithmetic: Deliverable 6.

**7. What order value makes delivery economically sensible?**
Single-drop: **≥₦15,000** (contribution turns positive at 8–10% with a ₦1,000 fee). Batched: **≥₦10,000** works (≈+₦300–₦500). Below ₦10,000 delivery is structurally loss-making regardless of fee shown. Hence the hard **minimum basket ₦10,000**.

**8. Delivery: separate, embedded, or free-above-threshold?**
**Hybrid: free above ₦15,000, visible ₦800–₦1,000 fee below it, minimum basket ₦10,000.** Separately charged is transparent and FCCPC-safe; free-above-threshold rewards exactly the baskets that fund it (Chowdeck trained the market with a ₦3,000 bar); **full embedding rejected** — +10–12% price to recover delivery makes OurOwn visibly dearer than the market and duplicates the trust/compliance risk of an undisclosed charge. Never call delivery free if it is hidden above market price. Model: Deliverable 6 §3.

**9. Which payment provider for the pilot, and on what evidence?**
**Paystack or Monnify**, chosen by measured AOV: Monnify if AOV <₦6,000 (no ₦100 flat fee; T+0 settlement), Paystack if ≥₦6,000 or marketplace is near (best docs, T+1 contractual, multi-split). Evidence required before choosing: completed scorecard (Deliverable 6 §4) **including a live ₦5,000 settlement test to the Afrizen bank account** and written answers on refund SLA/webhook retries. Paga and PayGate: no published pricing — RFP-only, not pilot-ready. Flutterwave: redundancy (2%+VAT is the most expensive local rate).

**10. Which technology features are essential before accepting real customer orders?**
All 🔴 items in [08-technical-operational-readiness.md](08-technical-operational-readiness.md) §1 — non-negotiable core: server-side payment verification + reconciliation, idempotency/duplicate-payment protection, stock decremented at order, order state machine with notifications, refund flow, RBAC+MFA+audit logs, tested backups, privacy notice/consent, hosted checkout (no card data), and the 10 acceptance tests passed. Everything else (marketplace module, subscriptions, advanced analytics) waits.

**11. What should founders measure in the first 30 days?**
Daily: orders, AOV, contribution/order, failed payments, on-time %. Weekly: 14–30-day repeat rate, availability %, failed-delivery %, complaints/100 orders, cash in bank, inventory days, payment-method mix, source channel. Plus the plan-specific outputs: 30 interviews, 100-order micro-pilot cohort, real per-drop cost, 40-SKU price index. Dashboard: Deliverable 11 §7.

**12. Under what conditions introduce third-party vendors?**
Gate (all must hold): **contribution-positive for 3 consecutive months; 30-day repeat ≥35%; fulfilment SLA ≥90%; working capital ≥3 months; legal entity + objects for marketplace; PSP splits enabled (Paystack multi-split); vendor T&Cs + NAFDAC warranties + DPAs drafted.** Market evidence: marketplaces survived where owned grocery died (Jumia) — but only after trust infrastructure existed. Introduce 3–5 *invited* vendors first, not open registration.

**13. What must be true before expanding to Kaduna, Jigawa, Katsina?**
(1) Kano polygon contribution-positive at full cost for 3 consecutive months; (2) repeat ≥35% with no decay; (3) supply spine confirmed in the new city (distributor or haulage cost per unit benchmarked); (4) dedicated local operator (not remote management); (5) 3 months of new-city working capital **without debt**; (6) delivery partner SLA verified on the ground. Alerzo rule: profitable-in-two-cities was the beginning of its collapse, not proof of scale.

**14. What must be true before Abuja?**
Same as Q13, **plus** independent verification of the founders' claimed delivery partner (coverage, pricing, SLA in writing — currently an unverified claim), and Abuja's different economics (higher basket, higher rent, established competition from Glovo/Chowdeck/PricePally). Abuja is a *competitor market*, Kano is a *white-space market* — the entry logic differs; do not expand to "match" it before Kano is a machine.

**15. What evidence justifies the ₦60m/₦100m targets?**
₦60m = 500 orders/month at ₦10k (17/day); ₦100m = 833/month (28/day). Justification requires: measured AOV ≥₦10k, measured 30-day repeat ≥30%, acquisition channel delivering ≥28 orders/day at CAC below contribution, and delivery capacity at that volume with ≥85% on-time. **If the 30-day pilot shows ≥5/day sustained with positive contribution and repeat ≥30%, the targets become credible scaling arithmetic; without that data they are slogans.** Remember: ₦100m sales ≈ ₦3–8m contribution at modelled inputs — not ₦100m profit.

**16. Three biggest reasons the business could fail?**
1. **Order-density shortfall** — positive per-order economics, insufficient orders per km² (GoLemon's exact death; Copia's).
2. **Margin collapse under real costs** — 5% gross margin + single-drop delivery + small baskets + failed deliveries = negative contribution; compounded by food inflation (19.59%) outrunning prices.
3. **Trust failure at first contact** — an unreconciled payment, a failed delivery, or a spoiled substitution in a market where e-commerce is the #1 fraud channel kills word-of-mouth, which is the only affordable acquisition channel in Kano.
*(Runners-up: funding run-out forcing debt (Alerzo); premature multi-city expansion.)*

**17. What should founders do in the next seven days?**
1. **Day 1:** decide the pilot polygon and write the operating policy (min basket ₦10k, fee rule, batch windows, prepaid-first) — one page, binding.
2. **Days 1–3:** book supplier meetings — Ghadco (46 Tafawa Balewa Rd, 0916 255 5650), Mamuda distributor line, NBC Challawa; prepare the 40-SKU quote sheet.
3. **Days 2–5:** run 10 customer interviews (script in Deliverable 11 §A1) — behaviour, live-order ask.
4. **Days 3–5:** mystery-shop delivery: GIG Kano's 3 centres, Fez Kano hub, 3 local dispatchers — one identical brief, get per-drop quotes.
5. **Days 3–7:** Paystack + Monnify sandbox, ₦5,000 live settlement test each; written questions on refunds/webhooks.
6. **Days 1–7 (parallel):** lawyer meeting with the eight questions (Deliverable 9 §10); independent technical review kickoff (Deliverable 8 §4).
7. **Day 7:** score everything against the Day-7 checkpoint in Deliverable 11 — continue, modify, or stop. **Do not buy inventory before Day 7.**

---

*Every recommendation above is only as good as the evidence cited in Deliverables 1–12. The three most load-bearing inputs — Kano AOV, Kano delivery cost, Kano repeat rate — are all unmeasured; the 30-day plan exists to measure them before capital is committed.*
