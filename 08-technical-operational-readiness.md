# Deliverable 8 — Technical & Operational Readiness Assessment

**Scope:** moving OurOwn from a Google AI Studio prototype (founder-reported features) to a reliable operating platform. **No code audit has been performed** — nothing below should be read as "OurOwn's code does/doesn't do X". Items requiring direct inspection are marked **🔍 inspect**.

**Verified context (Oct 2026):** Nigerian outages have no published ₦ costs (Paystack's 2019 post-mortem is qualitative) → instrument your own telemetry. Nigerian network reality: design for the 10th percentile (<1 Mbps, 300–800 ms RTT); Android 84.2% share, Tecno/Infinix low-RAM dominant (StatCounter Sept 2026). Payment failure modes are channel-specific (Paystack status page shows Verve-only degradation windows during Interswitch maintenance).

---

## 1. Launch-readiness checklist

Classification: **🔴 Must have before launch · 🟡 Must have before scaling · ⚪ Can wait.**

### Product catalogue & inventory
- 🔍 **🔍 inspect** SKU catalogue with stable IDs, unit of measure, NAFDAC number, batch/expiry captured at receipt — *prototype has "product identifiers + spreadsheet import"; verify uniqueness, encoding, and import validation*
- 🔍 🔍 **Price accuracy**: price change workflow, effective timestamps, audit of last price change (price errors = instant loss at 8–10% margin)
- 🔍 🔴 **Live stock count at order time** (overselling is a customer-trust event): stock decremented at order placement, not delivery; low-stock alerts
- 🔴 Stock-opportunity handling: out-of-stock → refund or substitute **with customer pre-approval**
- 🟡 Multi-location stock (store + pickup point) — later
- ⚪ Supplier PO module, auto-reorder — later

### Checkout & payments
- 🔴 **Server-side payment verification** — webhook is an optimisation, never the source of truth: poll the PSP `verify` endpoint keyed by unique `order_reference` (Paystack 2019 outage: notifications failed while money moved)
- 🔴 **Idempotency**: same reference retried → one charge, one fulfilment; dedupe webhooks by event ID
- 🔴 **State machine**: `PAYMENT_PENDING → PAID_UNFULFILLED → PACKED → DISPATCHED → DELIVERED → SETTLED` with `REFUND_QUEUED`, `FAILED` — no silent skips
- 🔴 **Duplicate-payment protection**: customer retry path must reuse the reference or auto-refund the duplicate within 24h 🔍 **🔍 inspect**
- 🔴 **Amount-match handling** for pay-with-transfer (under/over payment queue — customers will send ₦20,000 for a ₦19,850 order)
- 🔴 **Reconciliation job** every 15–30 min: PSP API ↔ DB ↔ fulfilment, with an ops queue for unmatched credits; daily settlement report vs bank credit
- 🔴 **Refund flow** with SLA stated in T&Cs; grocery rules: wrong/expired/damaged always refunded; hygiene-sealed goods non-returnable (disclosed pre-payment)
- 🔴 Hosted checkout only — **never store card data** (PCI SAQ A path; confirm with PSP in writing under v4.0.1 rules) 🔍 **🔍 inspect**
- 🟡 Per-channel health/fallback (card → transfer → USSD ordering re-weighted at runtime)
- 🟡 Virtual account per repeat customer (reconciliation speed)
- ⚪ Saved cards, BNPL, loyalty wallet

### Order processing & fulfilment
- 🔴 Order → pick list → pack → dispatch with timestamps; substitution policy enforced
- 🔴 **Confirmation call/WhatsApp before dispatch** for first orders and all COD (failed-delivery cost control)
- 🔴 Customer notifications at each state (SMS/WhatsApp — SMS as channel, not a security control)
- 🟡 Route/zone management, batch windows, rider assignment
- 🟡 Delivery proof (photo/PIN); failed-delivery reason codes feeding Sheet 8

### Admin, access, audit
- 🔴 Role-based access control (owner/ops/support) + **MFA on all admin accounts**
- 🔴 **Audit log** on price changes, refunds, order edits, user admin — immutable, retained
- 🔴 Daily backups of orders/customers/inventory **with tested restore** 🔍 **🔍 inspect**
- 🟡 Admin dashboard metrics wired to Deliverable 11 §7 definitions
- ⚪ Advanced analytics/BI

### Security
- 🔴 OWASP **ASVS Level 2** for storefront/checkout/account flows (v5.0.0, 30 May 2025): especially object-level authorisation on order IDs (customer A must not read customer B's address), cart price/quantity tampering, webhook signature verification
- 🔍 🔴 Penetration test or at minimum OWASP Top-10 checklist sign-off by an independent reviewer before launch
- 🔴 Secrets management (PSP keys never in the repo or client bundle) 🔍 **🔍 inspect**
- 🔴 Rate limiting + bot protection on login/OTP/order endpoints
- 🟡 Dependency/vulnerability scanning; incident-response runbook
- ⚪ Bug bounty

### Data protection (NDPA)
- 🔴 Privacy notice at checkout; consent capture (timestamped) for marketing and for sharing address/phone with riders
- 🔴 Data minimisation: no card data; mask phone numbers in support tooling; riders see only their stops
- 🔴 **NDPC registration assessment** (the >200-data-subjects/6-months threshold will be crossed early — see Deliverable 9; exact threshold text unverified)
- 🟡 Data-processing agreement templates (riders, 3PL, PSP, SMS); breach-notification procedure; annual audit return via licensed DPCO
- ⚪ Formal DPIA beyond the delivery/geolocation one (GAID audit template expects records)

### Monitoring & reliability
- 🔴 Uptime + error alerting on checkout, payment verify, order create
- 🔍 🔴 **Load test** the order flow at 10× expected peak (evening batch window) on low-end Android throttling
- 🟡 Per-channel payment success-rate dashboard; cart-abandonment instrumentation (baseline: 87% national)
- 🟡 Status page / customer-facing "we're verifying your payment" state instead of hard errors
- ⚪ Multi-region failover

### Reporting
- 🔴 Daily: orders, AOV, contribution, settlement received, failed payments, complaints
- 🟡 Weekly: repeat rate, on-time %, availability %, failed-delivery %, inventory days, cash position

---

## 2. Staged summary

| Stage | Contents |
|---|---|
| **Before first real customer order** | All 🔴 items in Checkout/Payments, stock-at-order, RBAC+MFA, audit log, backups+restore test, privacy notice, hosted checkout, verify+reconcile, refund flow, notifications, confirmation call process |
| **Before scaling past pilot** | 🟡 items: route/batching, per-channel fallback, virtual accounts, DPA + NDPC registration completion, pen test, load test, analytics |
| **Can wait** | ⚪: multi-location, BNPL, BI, bug bounty, marketplace vendor module (build only when Stage 3 gate passes) |

## 3. Explicitly out of scope of this assessment

No source code was reviewed; no security scan, load test, or payment-settlement test was run by this research. Founder-reported features (registration, location, cart, checkout, Paystack test, tracking, admin, inventory import) are treated as **unverified claims**.

## 4. 🔍 What must be tested directly (acceptance criteria)

1. **Duplicate payment**: submit the same order twice / retry mid-flow → exactly one charge, or automatic refund of the second within 24h.
2. **Webhook kill test**: disable webhook receiver → system still marks orders paid via polling, with no duplicates.
3. **Settlement**: ₦5,000 live charge → verify T+1 credit to bank matches dashboard within 1 kobo; run over a weekend.
4. **Refund**: live refund → days-to-customer recorded; matches T&Cs.
5. **Oversell**: set stock to 1, attempt purchase of 2 → blocked.
6. **AuthZ**: with two customer accounts, manipulate an order ID → 403/404, no data leak (ASVS 5.0 object-level auth).
7. **Admin takeover**: MFA enforced; audit log entries created for price change/refund/user changes.
8. **Backup restore**: restore yesterday's backup into a scratch environment; time it; count lost records.
9. **Load**: 50 concurrent checkouts on throttled 3G + low-end Android → no order loss, p95 < 5s for catalogue.
10. **Power/network loss**: kill connectivity mid-checkout → cart survives (offline-tolerant cart), no orphaned "paid" states.

## 5. Evidence base

Paystack status page (status.paystack.com) · Paystack 2019 outage post-mortem (paystack.com/blog/news-updates/august-9-outage) · TheCable NIBSS failures 13 May 2026 (snippet) · CBN Risk-Based Cybersecurity Framework 31 May 2024 (via Legal500, 18 Sep 2024) · NDPA/GAID regime (via Legal500, 21 Jan 2026) · OWASP ASVS 5.0.0 (30 May 2025) · PCI SSC SAQ A v4.0.1 updates (30 Jan 2025 blog, snippet) · Ookla Speedtest Nigeria Sept 2026 · StatCounter Nigeria Sept 2026 · Cybercrimes (Amendment) Act 2024 + suspended 0.5% levy (PLAC/KPMG snippets; **no "Cybersecurity Act 2025"/"NCSA" exists — do not cite one**).
