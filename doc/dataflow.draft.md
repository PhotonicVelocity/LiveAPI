# Data Flow — draft

```
                ┌────────────────────────────────────────────────────────┐
                │   Stage 1 — CAPTURE              (inside Ableton Live) │
                │   driver:  tools/run_pipeline.py                       │
                │   runs:    tools/apicapture/APICapture.py              │
                │            ├─ scripts/CaptureModule.py                 │
                │            ├─ scripts/PropertyProbe.py                 │
                │            └─ scripts/DeviceProbe.py                   │
                └────────────────────────────────────────────────────────┘
                                          │
                  stubs/<v>/pipeline/LiveTree.raw.json
                  stubs/<v>/pipeline/LiveClasses.json
                                          ▼
                ┌────────────────────────────────────────────────────────┐
                │   Stage 2 — PARSE  →  seed YAML in SOT format          │
                │   tools/parse/parse_apicapture_results.py  (reshape)   │
                └────────────────────────────────────────────────────────┘
                                          │
                  stubs/<v>/reports/seed/<Module>.yaml
                                          │
                                          ▼
                ┌────────────────────────────────────────────────────────┐
                │   Stage 3 — COMPARE      (seed YAML  vs  SOT)          │
                │   tools/parse/compare_seed_vs_sot.py    (new)          │
                └────────────────────────────────────────────────────────┘
                                          │
                          stubs/<v>/reports/drift.md
                                          │
                              (human reads → edits SOT)
                                          │
                                          ▼
   ┌──────────────────────────────────────────────────────────────────────┐
   │                       doc/lom/<Module>.yaml                          │
   │                                                                      │
   │             HAND-CURATED SOT  —  never machine-written               │
   │                                                                      │
   │   Mirrors the seed shape, plus per-field override + confidence       │
   │   + source. Holds authored prose and hypothesis claims.              │
   │   Order/structure drives reference page layout.                      │
   └──────────────────────────────────────────────────────────────────────┘
                                          │
              ┌───────────────────────────┴───────────────────────────┐
              ▼                                                       ▼
   ┌──────────────────────────────────┐         ┌──────────────────────────────────┐
   │  Stage 4a — STUBS                │         │  Stage 4b — REFERENCE PAGES      │
   │  tools/generate/generate_stubs.py│         │  tools/generate/                 │
   │                                  │         │    generate_reference.py         │
   │  → stubs/<v>/Live/*.pyi          │         │  → web/.../modules/*.mdx         │
   └──────────────────────────────────┘         └──────────────────────────────────┘
                                                              │
                                                              ▼
                                                ┌──────────────────────────────────┐
                                                │  Stage 5 — SITE BUILD            │
                                                │  npm run build (web/)            │
                                                │  Astro / Starlight integration   │
                                                │  → web/dist/ → GitHub Pages      │
                                                └──────────────────────────────────┘


   ┌──────────────────────────────────────────────────────────────────┐
   │ (future) HYPOTHESIS VERIFICATION                                 │
   │ reads claims in doc/lom/<Module>.yaml, probes a running Live     │
   │ → stubs/<v>/reports/hypotheses.md                                │
   │ (human reads → edits SOT)                                        │
   └──────────────────────────────────────────────────────────────────┘
```
