# Deliverable 9 — Regulatory & Compliance Research Memorandum (Nigeria)

**Date rules were checked: 30 October 2026.** Research memorandum only — **not legal advice**. Items marked **[UNVERIFIED]** could not be confirmed on an official page (several official instruments are PDF-only and were not machine-readable). Every item in §10 requires confirmation by a qualified Nigerian lawyer/tax adviser.

---

## 1. Corporate status & structure (Afrizen Capital shell)

- **CAC / CAMA 2020** (cac.gov.ng, read Oct 2026): companies must file **annual returns** (first within 18 months of incorporation, annually thereafter — exact fee/penalty schedule for this company must be checked on the CAC portal; CAC's own annual-returns page 404'd, penalty figures in circulation are from advisers [UNVERIFIED]). CAC has been striking off non-filing companies.
- **Operating OurOwn under Afrizen Capital Limited — implications to confirm:**
  1. **Objects clause**: do Afrizen's MEMARTs cover *online retail, warehousing, logistics and marketplace operation*? Marketplace operation is frequently missing and may require an objects amendment. 🔍 lawyer.
  2. **Trading name**: if "OurOwn" differs from the registered name, confirm whether a separate business-name registration is needed and ensure the registered entity name appears on website, invoices, packaging (disclosure duty).
  3. **Contracts**: supplier and delivery contracts will be signed by Afrizen — fine at pilot, but plan the eventual transfer/assignment to a separate OurOwn company (novation clauses now are cheaper than renegotiation later).
  4. **Liability & insurance**: food-safety and consumer claims sit against Afrizen's balance sheet; confirm product-liability/public-liability insurance covers grocery resale.
  5. **PSP onboarding**: Paystack/Flutterwave/Monnify live mode requires **CAC certificate + directors' BVN/KYC + business bank account** — onboarding happens in Afrizen's name; ensure the settlement account and the trading entity match.
  6. **Employment/contractors**: riders and staff engaged under Afrizen — PAYE registration with **KIRS** (Kano) and pension (18% employer, ≥15 employees) per PwC (May 2026).
  7. **Tax records & invoicing**: Afrizen invoices carry VAT obligations (§2); keep OurOwn's books separately inside Afrizen (departmental P&L) for clean eventual transfer.
  8. **IP & data**: app/domain/trademark should be owned by the entity that will hold them long-term — decide now (Afrizen vs future OurOwn) to avoid assignment cost later.
  9. **Data protection**: Afrizen is the data controller for OurOwn customer data until a separate entity exists — name it in the privacy notice.
- **Recommendation:** for a 30-day pilot, operating under Afrizen is workable **provided** (a) objects/branding check is done, (b) PSP onboarding succeeds under Afrizen, (c) insurance covers the activity, (d) a separate OurOwn Ltd is incorporated before Stage 2 (marketplace), when vendor contracts and withholding duties appear.

## 2. Tax

- **FIRS no longer exists — now the Nigeria Revenue Service (NRS)** (nrs.gov.ng, read Oct 2026), under the 2025 tax-reform package (Nigeria Tax Act 2025 / NTA Administration Act 2025; commencement for the 2026 year of assessment [UNVERIFIED precise date — confirm]).
- **CIT** (PwC, 29 May 2026): **0% for small companies** (annual gross turnover ≤ ₦100m **and** fixed assets ≤ ₦250m); 30% otherwise; **Development Levy 4%** on assessable profits except small companies (replaces Tertiary Education Tax/NITDA/NASENI levies).
- **VAT 7.5%** with **basic food items zero-rated** (specific list) — a grocery basket is *partially* zero-rated: **do not charge 7.5% flat, and do not charge 0% flat.** Small businesses are exempt from *collecting* VAT (separate test from zero-rating). NRS may deploy an **Electronic Fiscal System (EFS)** requiring real-time/scheduled VAT returns [PwC].
- **Kano state (KIRS, kirs.gov.ng; Kano State & LG Revenue Administration (Consolidation & Codification) Law 2021 — gazette PDF not readable, section numbers [UNVERIFIED])**: PAYE, withholding tax, **business premises registration** for the store/warehouse, **tenement rate** (LGA), signage/advert permit, environmental/waste and fire/health permits for a food warehouse. ⚠️ There is **no "Kano Emira" levy** in any official source — do not budget a line item for it; the brief's term appears to be a confusion with KIRS.

## 3. Consumer protection (FCCPC)

(fccpc.gov.ng business obligations + e-commerce guidance, read Oct 2026)

- **Obligations now:** clear, jargon-free T&Cs + privacy policy hyperlinked prominently; **"all disclosures known before payment"** → **total price, delivery fee, service charges itemised before checkout completes**; no wrongful/deceptive advertising; product labelling (date/place of manufacture); **register sales promotions with the Commission** (⚠️ open question whether ordinary discounts count — confirm with lawyer); complaint redress mechanism with response times; product-safety/withdrawal (expired stock, recalls) with customer notification.
- **Enforcement climate:** FCCPC reports ~₦10bn recovered across 9,000+ complaints citing *misleading pricing and lack of redress* (press, snippet); live themes = pricing transparency, complaints handling, labelling. → The founders' idea of making delivery "appear free" must be implemented as **an explicit rule ("free delivery on orders ≥₦15,000")**, not an undisclosed mark-up.
- **Draft Consumer Protection Regulations 2026** (comments closed 4 May 2026) would add **online-platform duties** (incl. no manipulation of reviews/ratings) — **draft, not law** as of Oct 2026; monitor. A separate draft Sales Promotion Regulation 2026 would require registering each promotion before announcement.
- **No general e-commerce platform registry exists** — the DEON registry (2025) is lending-specific.

## 4. Data protection (NDPA 2023 / NDPC)

(ndpc.gov.ng, read Oct 2026)

- NDPA 2023 principles (s.29), data-subject rights (ss.34–38), registration of controllers/processors "of major importance" (s.44), **GAID 2025** directive (in force Sept 2025), annual compliance audit returns **due 31 March via a licensed DPCO**, penalties up to **₦10m or 2% of annual gross revenue** (higher tier) [Legal500, 21 Jan 2026].
- **Threshold:** commonly summarised as >200 data subjects in a rolling 6-month period — **exact text [UNVERIFIED, PDF-only]**. An online grocery capturing name/phone/address/order history will cross it early → **treat NDPC registration as required now**.
- **Duties:** lawful basis (contract necessity for fulfilment; **separate consent** for marketing SMS/WhatsApp and for sharing address/phone with riders); privacy notice at checkout; data minimisation; encryption + RBAC + admin MFA; breach notification (**72-hour figure [UNVERIFIED — confirm exact window]**); DPO where appropriate; documented cross-border transfer basis (most Nigerian startups host on AWS eu-west-1 → document it).
- **Marketplace stage:** controller/processor mapping with vendors and 3PL; DPAs; vendors receive only delivery-necessary data — enforced technically.

## 5. Food & product (NAFDAC)

(nafdac.gov.ng, read Oct 2026; Pre-packaged Food (Labelling) Regulations 2022 scope read from snippet — PDF not machine-readable)

- **Reselling registered packaged goods:** generally no product registration needed for OurOwn **as retailer** — obligations: stock only goods with valid NAFDAC numbers; sell within expiry; do not alter labels; no unapproved advertising/claims.
- ⚠️ **THE KEY QUESTION: repacking.** If OurOwn splits rice/beans/oil into own-branded packs, or sells prepared/fresh processed food, it becomes a **manufacturer/packer**: full product registration, labelling regime, food-handler medicals, SOPs, fumigation certificates, fees (micro-scale registration ₦36,737.50, 90 working days, 2-year listing). **Get a written answer before selling any repacked item.**
- **Marketplace stage:** vendor warranties (NAFDAC numbers displayed on listings), delisting/recall process; open question whether the platform counts as "distributor" for third-party listings — flag to lawyer.
- Penalties under the NAFDAC Act include fines, imprisonment, seizure/destruction, closure [amounts UNVERIFIED].

## 6. Electronic transactions & online contracts

- **No Nigerian "Electronic Transactions Act 2015" could be located.** The framework is: **Evidence Act 2011 s.84** (electronic records/signatures admissibility) + **CAMA 2020** + **FCCPA 2018** (s.73 unfair/misleading practices; ss.130/146 cited by counsel for refund/redress rights — exact wording [UNVERIFIED]) + **Cybercrimes Act 2015 as amended 2024** (assented 28 Feb 2024). A widely circulated "ETA 2023 s.16" citation in a Legal500 article could not be traced to a gazette — **do not rely on it**.
- **Operational requirements (defensible from FCCPC guidance):** pre-contract disclosure of total cost incl. delivery; review/confirm step before payment; written T&Cs with delivery windows, substitution policy, cancellation/refund timelines and who bears return cost; written order confirmation as the contract record; **no unqualified "no refunds" clause** (unfair-term risk).

## 7. Riders: employment vs contractors

- No Nigerian platform-work statute exists. NICN in *Oladapo Olatunji v Uber Technologies System Nigeria Ltd* (NICN/LA/546/2017) **declined to find an employment relationship** — the test is **control** (hours, tools, supervision, exclusivity), not the contract label.
- **Risk:** scheduled, uniformed, equipped, exclusively-used, disciplined riders look like employees → PAYE, pension (≥15 employees), Employees' Compensation 1%, minimum wage (federal ₦70,000; Kano figure ₦71,000 reported [UNVERIFIED]), unfair-dismissal exposure. Contractor status requires: own bike, own hours, other platforms allowed, per-trip pay, no exclusivity.
- **Insurance** for contractor riders is OurOwn's exposure (ECA won't apply) — get rider insurance or accept the liability knowingly. No Kano rider-specific regulation found [apparently none — confirm].

## 8. Marketplace stage — incremental obligations (only when Stage 3 gate passes)

1. FCCPC platform duties (draft regs likely to be gazetted) + liability allocation for vendor goods written into **both** vendor and customer T&Cs.
2. Tax: VAT on commissions; **withholding** on vendor settlements/rent; EFS-ready invoicing mapping [confirm with tax adviser].
3. NDPA: joint-controller mapping, DPAs, processor register.
4. NAFDAC: vendor warranties, listing-level NAFDAC numbers, recall escalation.
5. Vendor contracts: prohibited-products list, dispute ownership matrix, payout schedule.

## 9. Distinguishing the three tiers

| Tier | Items |
|---|---|
| **1. Applies now** | CAC annual returns; objects/branding check; CIT/VAT position; KIRS/LGA levies & permits; FCCPC price disclosure + T&Cs + complaint channel; NDPA duties + registration assessment; NAFDAC expiry/labelling discipline for resale; rider classification decision; insurance |
| **2. Conditional on how we operate** | NAFDAC manufacturer regime (repacking/prepared food); FCCPC sales-promotion registration (are our discounts "promotions"?); ECA/pension thresholds (headcount); VAT collection status (turnover) |
| **3. Marketplace stage** | Vendor contracts/WHT/VAT mapping; platform liability; joint-controller data model; NAFDAC platform-as-distributor question; draft-reg platform duties |

## 10. The eight questions for the lawyer (one meeting)

1. Do Afrizen's objects cover online retail + marketplace, and what does a business-name registration cost for "OurOwn"?
2. Which of our SKUs are zero-rated basic food items vs standard-rated? Do we qualify as a small company (CIT 0% + VAT-collection exemption)?
3. Does repacking/own-label make us a NAFDAC-registered manufacturer? (Get it in writing.)
4. Are our riders employees in substance? What contract + operating practices preserve contractor status, and what insurance do we need?
5. Which Kano/KIRS/LGA permits apply to a food warehouse and delivery operation (business premises, tenement, signage, environmental)?
6. Do our discounts require FCCPC sales-promotion registration? What is FCCPC's position on "free delivery" advertising?
7. What exact refund/returns wording satisfies FCCPA ss.130/146 for perishable goods?
8. NDPC: are we "of major importance" under the current threshold, what is the exact breach-notification window, and who signs the annual audit return?

---

### Sources read (30 Oct 2026)
cac.gov.ng · nrs.gov.ng · fccpc.gov.ng (business-obligations, e-commerce guidance, regulations library, digital-lending release) · ndpc.gov.ng · nafdac.gov.ng/our-services/msme · kirs.gov.ng · PwC Nigeria tax summaries (CIT 29 May 2026; Other taxes) · Legal500: KPMG on NRS Act 2025 (5 Aug 2024/2025), G. Elias on CBN framework (18 Sep 2024), Advocaat on NDPA audit regime (21 Jan 2026), Aarndale on e-commerce framework (flagged ETA citation), Manifield on platform work/*Olatunji v Uber*. Snippet-level: PLAC Cybercrimes (Amendment) Act 2024; KPMG/Andersen on suspended 0.5% levy; Dubawa/BBC debunk of "Cybercrimes Act 2025"; Fagge LGA tenement page (425); CAC annual-returns page (404). **PDF-only, not machine-readable: NDPC registration guidance + GAID 2025, NAFDAC Pre-packaged Food Labelling Regs 2022, FCCPC draft regs 2026, Kano State revenue law.**
