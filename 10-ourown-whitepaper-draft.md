# OurOwn — Whitepaper (Working Draft v0.1)

**Version:** 0.1 — working draft for founder review, 30 October 2026
**Prepared from:** independent desk research + quantitative modelling (see [README.md](README.md))
**Status:** *This is a working draft, not a final investment document.* Current capabilities are marked **[Now]**; proposals are **[Planned]**. OurOwn has **no verified customer demand, no signed supplier partnerships, no completed live orders, and no audited technology** as of this date — nothing below should be read as claiming otherwise.

---

## 1. Executive summary

OurOwn [Planned] is a grocery and everyday-essentials commerce platform for Northern Nigeria, launching in Kano. Nigeria's retail market is ₦25.4 trillion (2025, Euromonitor) but online grocery is only ~US$95 million — under 0.5% — and **no major delivery platform operates in Kano**. OurOwn's thesis: a local-first, Kano-native operator with local sourcing (Dawanau, Singer, Ghadco/Mamuda, NBC Challawa), a narrow high-frequency assortment, batched scheduled delivery and prepaid-first payments can build a profitable grocery business where imported models (Jumia Food, GoLemon, Copia, Twiga) failed. The core risks — order density, thin margins, and unvalidated demand — are addressed by a minimum-basket policy, an 8–10% blended-margin target (vs the originally discussed 5%), a one-polygon launch, and a 30-day validation gate before capital commitment.

## 2. The problem OurOwn seeks to solve

Household grocery shopping in Kano costs time: a bulk stock-up means a half-day market trip, haggling, carrying heavy loads, and price opacity. Neighbourhood kiosks solve convenience but at marked-up, non-comparable prices with limited assortment. Digital options are absent: Glovo, Chowdeck and PricePally do not serve Kano; micro-operators (Sadaraki, KFE) have no catalogue, SLA or scale. Meanwhile 90%+ of FMCG volume moves through informal channels with 4+ margin layers — the digitisation opportunity is real but unproven.

## 3. Market context

Nigeria 2025: retail ₦25.4trn/$19.0bn; retail e-commerce ₦492bn/$368m (+29%); online food $95m with 87–87.5% cart abandonment (ECDB). Inflation rebased Jan 2025; **Sept 2026 headline 14.63% but food 19.59%** — grocery costs rising faster than wages. FX ≈ ₦1,333–1,347/$. FMCG is 78–95% informal by volume. *(Euromonitor/ECDB/NBS, accessed Oct 2026.)*

## 4. The Nigerian grocery retail landscape

Chain: manufacturer → master distributor → market wholesaler → kiosk → consumer, with modern trade bypassing layers. Open market = 78–85% of volume; supermarkets 2–8%; e-commerce <1%. USDA: ~70% of food shopping informal; open-air markets 72% of retail sales. Manufacturers never publish MOQ or credit — terms are negotiated. Lagos dominates modern trade (>1,400 supermarkets); outside Lagos/Abuja/PH, distribution is wholesale + informal (DALA, 2026).

## 5. Northern Nigeria market opportunity

Kano State: 15.5m (2022 projection), **metro 4.91m** — Nigeria's largest state, top-3 internet market (9.03m subs). MPI 66.3% — mass-market, price-sensitive demand; food-insecurity epicentre (Cadre Harmonisé: 27.2m Crisis-or-worse, Oct–Dec 2025). Yet Kano is a **supply hub**: Dawanau (~42km², 10,000+ shops) and local FMCG plants give same-city sourcing no southern competitor has. **No public Kano e-grocery data exists** — the opportunity must be validated, not assumed.

## 6. Target customers and their needs

Priority order (hypotheses to test, Deliverable 11):
1. **Households in core urban LGAs** — weekly stock-up, ₦10k–30k baskets, time-poor.
2. **Institutional buyers** (schools, caterers, offices) — bulk, prepaid, recurring; under-competed, no public evidence anyone serves them well.
3. **Students/young workers (BUK: 39,979 students)** — small evening baskets, price-sensitive; economics only work with batched campus drops.
Not targeted at launch: chilled/frozen (no cold chain), ultra-small top-ups (negative contribution).

## 7. Value proposition

**"Market prices without the market trip — delivered on a schedule you can count on."** Four pillars, each evidence-backed: (1) local landed cost; (2) fixed, transparent prices with receipts; (3) batched same/next-day windows with named riders; (4) replacement guarantee. Not claimed: cheapest prices (the market's price is public and lower), 10-minute delivery (economically fatal — GoLemon/Blinkit evidence).

## 8. Initial owned-inventory business model [Now → Stage 1]

Buy at wholesale (Ghadco/Mamuda, NBC Challawa, Singer/Dawanau), hold a **narrow 60–100 SKU ambient assortment**, sell via web/WhatsApp/app, deliver in batched windows. Operating rules adopted from the unit-economics model: **minimum basket ₦10,000; free delivery ≥₦15,000, ₦800–₦1,000 below; blended gross margin target 8–10%** (5% rejected — see §18); prepaid-first; one delivery polygon.

## 9. Supplier and distribution strategy

Verified counterparties: **Ghadco Nigeria Ltd** (Kano HQ, 5+ categories, 250+ vehicles) and **Mamuda Beverages/Pop Cola** (open distributor invitation, FSSC 22000 plant), plus NBC Challawa and 7-Up Zaria Rd depots; open-market arbitrage daily against Singer/Dawanau. Written price lists, MOQ, and **expiry/returns clauses** required before first purchase order (no manufacturer publishes terms). Full pack: [05-supplier-research-pack.md](05-supplier-research-pack.md).

## 10. Pricing and revenue model

Revenue lines: (1) retail gross margin (8–10% blended target); (2) delivery fee below ₦15,000; (3) [Planned, Stage 3] vendor commissions/commission marketplace; (4) [Planned] placement/promotions; (5) [Planned] subscription pass after density. Pricing rule: re-index weekly against market benchmarks; supplier quote validity ≤7 days.

## 11. Delivery and fulfilment model

Outsourced initially (pilot risk reduction): GIG Logistics Kano (3 centres — note Sunday closure), Fez Kano hub (2026), local dispatch riders; **Kwik has retreated to Lagos-only** — do not contract on old assumptions. Batched scheduled windows (≥3 drops/trip target → ₦600/order), confirmation call before dispatch, prepaid-first, failed-delivery reason codes. Metrics tracked from order 1: cost/drop, on-time %, failed %, returns %.

## 12. Technology architecture and capabilities

Founder-reported prototype [Now, **unverified**]: registration, location, search, cart, checkout, Paystack test, tracking, admin, inventory import. Production requirements [Planned]: server-side payment verification + reconciliation (webhook ≠ settlement — Paystack 2019; NIBSS May 2026), idempotent order references, RBAC + MFA + audit logs, ASVS Level 2 security, tested backups, low-end Android + 3G-first performance (Android 84.2% share), NDPA-compliant consent/privacy. Full checklist: [08-technical-operational-readiness.md](08-technical-operational-readiness.md).

## 13. Payment and transaction operations

Pilot choice: **Paystack or Monnify**, decided on measured AOV (Paystack: docs, T+1, best marketplace splits; Monnify: cheapest small tickets, T+0 settlement). Paga/PayGate: no public pricing — RFP only. Procedures: sandbox kill-tests, duplicate-payment test, live settlement test to Afrizen's account before launch, daily reconciliation. Settlement ≠ on-screen success.

## 14. Customer acquisition and retention

Kano channel mix (evidence: SCIMDER 2024 — 51% radio listenership; Meta/Public First 2026; PalmPay referral ₦250): **radio (Hausa, morning/evening) + WhatsApp ordering + referral credits (₦500, gated on first delivered order)**; digital paid as supplement (Nigeria CPMs cheap but cold-traffic CAC ≈ ₦8k–22k uneconomic against ₦10k baskets). Retention via reliability, reorder reminders, and B2B accounts. Subscriptions deferred until cluster density (Chowpass geo-fencing precedent).

## 15. Future third-party vendor marketplace [Planned — gated]

Stage gate before any vendor onboarding: Kano pilot **contribution-positive for 3 consecutive months, 30-day repeat rate ≥35%, fulfilment SLA ≥90%**. Then: Paystack subaccount splits, vendor T&Cs with NAFDAC warranties, DPAs, liability matrix, withholding/VAT mapping. Market lesson: marketplaces survived where owned inventory died (Jumia) — but only with trust infrastructure first.

## 16. Expansion strategy

Sequence: **Kano polygon → Kano metro → Kaduna/Jigawa/Katsina → Abuja (only after partner verification)**. Gates: contribution-positive at full cost for 3 months; repeat ≥35%; delivery SLA ≥90%; working capital for 3 months of new-city inventory. Alerzo/Copia rule: expansion killed the profitable two-city business.

## 17. Financial assumptions and unit economics

Modelled (hypothetical inputs, [06-unit-economics-workbook-spec.md](06-unit-economics-workbook-spec.md)): contribution/order at batched ₦600 + ₦800 fee + 10% margin = **+₦175/₦5k, +₦500/₦10k, +₦1,150/₦20k, +₦1,800/₦30k**. Break-even ≈ 1,071–2,500 orders/month vs ₦750k fixed cost. Sales targets decomposed: **₦60m = 500 orders/month @₦10k; ₦100m = 833/month @₦10k** — year-1-to-2 objectives, not launch-month ambitions. ₦100m sales ≠ ₦100m profit: at modelled inputs, ₦3–8m contribution.

## 18. Risks and mitigations

Top five (full SWOT/TOWS: [07-swot-tows.md](07-swot-tows.md)): (1) **density failure** → one polygon, batch windows, min basket, kill rule; (2) **margin arithmetic** → 8–10% blended, fee charged, SKU-level discipline; (3) **unvalidated demand** → 30-day gate before inventory capital; (4) **working capital** → no high-rate debt (Alerzo: ₦5bn → Mareva injunction), staged spend; (5) **trust/COD** → prepaid-first, confirmation calls, replacement guarantee (fraud data: e-commerce is Nigeria's #1 fraud channel, NIBSS 2025).

## 19. Legal and compliance considerations

Operating under Afrizen Capital pending incorporation of OurOwn Ltd; objects/branding check required. Taxes: NRS (ex-FIRS), CIT 0% possible (small company), VAT 7.5% with **basic food zero-rated**. FCCPC: all fees disclosed pre-payment; promotion registration question open. NDPA registration likely required from launch. NAFDAC: resale of registered goods OK — **repacking would trigger manufacturer registration**. Riders: contractor status turns on control (*Olatunji v Uber*). Full memo: [09-regulatory-compliance-memo.md](09-regulatory-compliance-memo.md). *Professional advice required on all eight questions listed there.*

## 20. Implementation roadmap

| Phase | Days | Focus | Exit gate |
|---|---|---|---|
| 0 — Validate | 1–30 | Interviews, price collection, supplier/delivery/payment quotes, micro-pilot ([11-30-day-validation-plan.md](11-30-day-validation-plan.md)) | ≥8/30 interviews show recent pain; 5+ orders/day for 2 weeks; positive modelled contribution/order on real quotes |
| 1 — Launch | 31–90 | One polygon, 60–100 ambient SKUs, batched windows, prepaid-first, all 🔴 readiness items | ≥15 orders/day @ ≥₦10k AOV; on-time ≥85%; repeat ≥25% |
| 2 — Density | 91–180 | Second cluster in metro; B2B accounts; radio+referral scale | Contribution-positive 3 consecutive months; repeat ≥35% |
| 3 — Platform | 181+ | Marketplace vendors (gated), Kaduna/Jigawa pilots, subscription pass | Gates in §15/§16 |

## 21. Key performance indicators

**Daily:** orders, AOV, contribution/order, failed payments, on-time %. **Weekly:** 30-day repeat rate, availability %, failed-delivery %, complaints/order, cash in bank, inventory days, CAC (where measurable). **Monthly:** contribution after fixed cost, supplier price index vs market, cohort retention. Definitions in [11-30-day-validation-plan.md](11-30-day-validation-plan.md) §7.

## 22. Evidence gaps and assumptions

The seven mandatory gaps (no customer interviews; no verified TAM; Glovo narrative unverified; suppliers prospective; financial model hypothetical; technology unaudited; Afrizen/OurOwn structure unreviewed) plus all others discovered are catalogued in [12-assumptions-evidence-gap-register.md](12-assumptions-evidence-gap-register.md). **Material unknowns:** Kano AOV, Kano delivery WTP, repeat rates, Ghadco terms, Kano-specific e-grocery demand — each has a named verification task and owner.

## 23. References and source notes

Full source lists appear per deliverable. Principal sources: Euromonitor (2025 retail/e-commerce), ECDB (2025 online food), DALA/NielsenIQ (2026 FMCG/channel), USDA FAS GAIN NI2024-0014 (2024), NBS (CPI Sept 2026, MPI 2022, internet subs Q4 2023, NLSS 2019), citypopulation.de/NPC (2022 projections), TechCabal (GoLemon 29 Jul 2026; Copia 30 Sep 2026), TechCrunch (Chowdeck 11 Aug 2025; Jumia Food 14 Dec 2023), Techeconomy (Glovo 6 Oct 2026), Delivery Hero (16 Jul 2026), ghadconigeria.com, mamudagroup.com, support.paystack.com, monnify.com/pricing, flutterwave.com/ng/pricing, fccpc.gov.ng, ndpc.gov.ng, nafdac.gov.ng, nrs.gov.ng, cac.gov.ng, SCIMDER/Premium Times (Feb 2025), NIBSS/Punch (2026), Paystack status + 2019 post-mortem, OWASP ASVS 5.0. All accessed 28–30 Oct 2026; snippet-only sources flagged in the relevant deliverable.

## 24. Closing statement for reviewers

This draft is deliberately written to be **challenged**. Where evidence was absent it says so; where the founders' assumptions (5% margin, free delivery, ₦100m target, Glovo narrative) did not survive contact with data, it says that too — with the arithmetic. The next version of this whitepaper should replace hypothetical inputs with real quotes and pilot data from the 30-day plan.

---

*Sources for every claim above are cited in the supporting deliverables. Prepared as independent research; not investment, legal or financial advice.*
