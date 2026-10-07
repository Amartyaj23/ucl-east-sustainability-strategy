# Sources and figure register

Research done on 7 October 2026. Every policy number, factor or date used anywhere in this repository is listed in Part B with the source it came from and how well I could check it.

**How I checked each figure**

| Code | Meaning |
|---|---|
| **Read** | I extracted the text of the official PDF and read the passage myself. |
| **Page** | I read the official web page through a page-summarising tool, not the raw text. Where possible I cross-checked it against a PDF marked "Read". |
| **Secondary** | Reported by a trade, vendor or search-result page only. Treated as unconfirmed. |

---

## Part A. Source list

### London Plan and Greater London Authority (GLA) guidance

| ID | Document | URL |
|---|---|---|
| S1 | London Plan 2021, Chapter 8 Green Infrastructure (Policies G5, G6, G7; Table 8.2) | https://www.london.gov.uk/programmes-strategies/planning/london-plan/the-london-plan-2021-online/chapter-8-green-infrastructure |
| S2 | London Plan 2021, Chapter 9 Sustainable Infrastructure (Policies SI 1, SI 2, SI 4, SI 5, SI 7, SI 12, SI 13) | https://www.london.gov.uk/programmes-strategies/planning/london-plan/the-london-plan-2021-online/chapter-9-sustainable-infrastructure |
| S3 | London Plan 2021, Chapter 3 Design (Policies D5, D6, D8) | https://www.london.gov.uk/programmes-strategies/planning/london-plan/the-london-plan-2021-online/chapter-3-design |
| S4 | London Plan 2021, Chapter 1 Good Growth (Policy GG3) | https://www.london.gov.uk/programmes-strategies/planning/london-plan/the-london-plan-2021-online/chapter-1-good-growth |
| S5 | GLA, *London Plan Guidance: Urban Greening Factor*, January 2023 (PDF) | https://www.london.gov.uk/media/99842/download |
| S6 | GLA, *London Plan Guidance: Whole Life-Cycle Carbon Assessments*, March 2022 (PDF) | https://www.london.gov.uk/sites/default/files/lpg_-_wlca_guidance.pdf |
| S7 | GLA, *London Plan Guidance: Circular Economy Statements*, March 2022 (PDF) | https://www.london.gov.uk/sites/default/files/circular_economy_statements_lpg_0.pdf |
| S8 | GLA, *Energy Assessment Guidance*, June 2022 (PDF) | https://www.london.gov.uk/sites/default/files/gla_energy_assessment_guidance_june_2022_0.pdf |
| S9 | GLA, "Referral process for LPAs" (what makes an application referable to the Mayor) | https://www.london.gov.uk/programmes-strategies/planning/planning-applications-and-decisions/referral-process-lpas |

### Building Regulations, overheating and carbon (national)

| ID | Document | URL |
|---|---|---|
| S10 | Approved Document O: Overheating, 2021 edition (PDF), requirement O1, Section 1, Section 2, Appendix C | https://assets.publishing.service.gov.uk/media/6218c5aad3bf7f4f0b29b624/ADO.pdf |
| S11 | GOV.UK landing page for Approved Document O (published 15 Dec 2021, last updated 15 Jun 2022) | https://www.gov.uk/government/publications/overheating-approved-document-o |
| S12 | CIBSE, TM59 (2017) *Design methodology for the assessment of overheating risk in homes* | https://www.cibse.org/knowledge-research/knowledge-portal/technical-memorandum-59-design-methodology-for-the-assessment-of-overheating-risk-in-homes |
| S13 | CIBSE, TM59 (2026) *Overheating risk in dwellings: a design stage methodology* | https://www.cibse.org/knowledge-research/knowledge-portal/tm59-overheating-risk-in-dwellings-a-design-stage-methodology-2026/ |
| S14 | EDSL TM59 Wizard documentation (software vendor restating the TM59 2017 pass criteria) | https://docs.edsl.net/TM59/TM59Report.html |
| S15 | MHCLG, Building Circular 01/2026, Future Homes and Buildings Standards (published 24 March 2026) | https://www.gov.uk/government/publications/the-future-homes-and-buildings-standards-building-circular-012026/the-future-homes-and-buildings-standards-building-circular-012026-letter |

### Biodiversity net gain

| ID | Document | URL |
|---|---|---|
| S16 | GOV.UK, *Understanding biodiversity net gain* | https://www.gov.uk/guidance/understanding-biodiversity-net-gain |
| S17 | Environment Act 2021, Schedule 14 (inserts Schedule 7A into the Town and Country Planning Act 1990) | https://www.legislation.gov.uk/ukpga/2021/30/schedule/14 |

### Local context

| ID | Document | URL |
|---|---|---|
| S18 | Newham Green and Water Infrastructure Strategy, section 4 (says Newham follows the London Plan UGF scores, no bespoke target) | https://www.newham.gov.uk/downloads/file/9504/eb062-newham-green-and-water-infrastructure-strategy-section-4-the-newham-context-2025-pdf- |

### UN Sustainable Development Goals (official pages)

| ID | Goal | URL |
|---|---|---|
| U3 | Goal 3 | https://sdgs.un.org/goals/goal3 |
| U6 | Goal 6 | https://sdgs.un.org/goals/goal6 |
| U7 | Goal 7 | https://sdgs.un.org/goals/goal7 |
| U9 | Goal 9 | https://sdgs.un.org/goals/goal9 |
| U11 | Goal 11 | https://sdgs.un.org/goals/goal11 |
| U12 | Goal 12 | https://sdgs.un.org/goals/goal12 |
| U13 | Goal 13 | https://sdgs.un.org/goals/goal13 |
| U15 | Goal 15 | https://sdgs.un.org/goals/goal15 |

---

## Part B. Figure register

### Urban Greening Factor (used in `ugf_calculator.py`)

| Figure | Value | Source | Check |
|---|---|---|---|
| UGF target, predominantly residential | 0.4 | S5 para 1.1.2; S1 Policy G5 | Read (S5) |
| UGF target, predominantly commercial (excluding B2/B8) | 0.3 | S5 para 1.1.2 and footnote 1; S1 | Read (S5) |
| Which target applies to mixed use | Use class with the most floorspace | S5 para 3.2.2 | Read |
| Calculation | (sum of area × factor) ÷ total site area | S5 para 3.2.1 | Read |
| Site area | Red-line boundary, retained cover included | S5 para 3.2.2 | Read |
| Green walls | Vertical area counted but not added to site area | S5 para 3.2.2, Table A1.1 | Read |
| Tree canopy and what lies beneath | Canopy scored in its own right; features underneath also scored | S5 para 3.2.2, Table A1.1 | Read |
| Roofs under PV | Green roof area under PV cells is still counted | S5 Table A1.1 | Read |
| Newham target | Follows London Plan, no bespoke score | S18 | Secondary (search-result text; I did not read the adopted Local Plan) |

**Surface-cover factors** (London Plan Table 8.2, reproduced as Table 3.1 in S5, January 2023). All values read in S5 and confirmed against S1.

| Surface-cover type | Factor |
|---|---|
| Semi-natural vegetation (trees, woodland, species-rich grassland) | 1.0 |
| Wetland or open water (semi-natural, not chlorinated) | 1.0 |
| Intensive green roof or vegetation over structure, substrate at least 150 mm | 0.8 |
| Standard trees in connected pits, soil volume at least two-thirds of mature canopy area | 0.8 |
| Extensive green roof, substrate at least 80 mm (or 60 mm beneath vegetation blanket) | 0.7 |
| Flower-rich perennial planting | 0.7 |
| Rain gardens and other vegetated sustainable drainage | 0.7 |
| Hedges (line of mature shrubs one or two shrubs wide) | 0.6 |
| Standard trees in pits with less than two-thirds of mature canopy area as soil | 0.6 |
| Green wall (modular system or climbers rooted in soil) | 0.6 |
| Groundcover planting | 0.5 |
| Amenity grassland (species-poor, regularly mown) | 0.4 |
| Extensive green roof of sedum mat or other lightweight system not meeting GRO Code 2014 | 0.3 |
| Water features (chlorinated) or unplanted detention basins | 0.2 |
| Permeable paving | 0.1 |
| Sealed surfaces (concrete, asphalt, waterproofing, stone) | 0.0 |

### Carbon

| Figure | Value | Source | Check |
|---|---|---|---|
| Major development should be net zero-carbon; energy hierarchy be lean, be clean, be green, be seen | Policy SI 2 A | S2 | Page |
| Minimum on-site reduction beyond Building Regulations | 35% (10% homes and 15% non-residential through energy efficiency alone) | S2 Policy SI 2 C; S8 paras 1.4 and 5.2 | Page (S2), Read (S8 confirms 35%) |
| 10% and 15% efficiency-only figures | 10% homes, 15% non-residential | S2 Policy SI 2 C | Page only (not seen in S8) |
| Whole life-cycle carbon assessment for referable applications | Policy SI 2 F | S2; S6 front matter and para 1.1.1 | Read (S6) |
| WLC assessment stages | Pre-application, planning submission (RIBA 2/3), post-construction | S6 para 2.3 | Read |
| WLC benchmark, homes | A1–A5 below 850; B–C below 350; A–C below 1,200 kgCO₂e/m² GIA | S6 Table A2.1 | Read |
| WLC aspirational benchmark, homes | A1–A5 below 500; B–C below 300; A–C below 800 | S6 Table A2.1 | Read |
| WLC benchmark, offices | A1–A5 below 950; B–C below 450; A–C below 1,400 | S6 Table A2.1 | Read |
| WLC aspirational benchmark, offices | A1–A5 below 600; B–C below 370; A–C below 970 | S6 Table A2.1 | Read |
| Aspirational benchmarks are 40% below the benchmarks | 40% | S6 para A2.1.3 | Read |
| Energy use intensity to aim for | Homes 35, offices 55 kWh/m²/yr (GIA) | S8 Table 4, para 7.13 | Read |
| Space heating demand to aim for | 15 kWh/m²/yr (homes and offices) | S8 Table 4 | Read |
| Carbon offset price | £95 per tonne CO₂, over 30 years | S8 para 6.4 | Read |
| Future Homes Standard published | 24 March 2026 | S15 | Page |
| Future Homes Standard in force | 24 March 2027 (24 September 2027 for higher-risk building work) | S15 | Page |
| New requirement L3: on-site renewable electricity for new dwellings | — | S15 | Page |
| Referable to the Mayor: 150-home threshold | 150 homes | not confirmed (see Part D) | **Unverified** |
| GLA referral page lists a new category for 50 or more homes, effective 11 May 2026 | 50 homes | S9 | Page |

### Circular economy

| Figure | Value | Source | Check |
|---|---|---|---|
| Referable applications submit a Circular Economy Statement | Policy SI 7 B | S2; S7 | Page (S2), Read (S7) |
| Construction and demolition waste reused, recycled or recovered | 95% | S2 SI 7 A; S7 | Page (S2), Read (S7 quotes it) |
| Excavation waste put to beneficial use | 95% | S2 SI 7 A; S7 | Page (S2), Read (S7) |
| Municipal waste recycling by 2030 | 65% | S2 SI 7 A; S7 | Page (S2), Read (S7) |
| Zero biodegradable or recyclable waste to landfill by | 2026 | S2 SI 7 A | Page |
| Business waste recycling by 2030 (London Environment Strategy Policy 7.2.2) | 75% | S7 para 4.8.1 | Read |
| Aim for recycled or reused content, by value, whole building | At least 20% | S7 para 4.7.6 (an aim, not a hard limit) | Read |
| Bill of Materials covers materials making up at least this share of cost | 80% | S7 para 4.7.7 | Read |
| Explore retention of existing buildings before demolition | — | S7 para 2.4.5 | Read |
| Pre-demolition audit strongly encouraged at pre-application | — | S7 paras 4.6.7, 4.6.13 | Read |
| End-of-life strategy, BIM or material passporting | — | S7 para 4.7.11 | Read |

### Biodiversity and greening

| Figure | Value | Source | Check |
|---|---|---|---|
| Biodiversity gain objective | At least 10% above pre-development value | S17 Schedule 7A para 2; S16 | Page (both agree) |
| Mandatory for major development from | 12 February 2024 | S16 | Page |
| Habitat creation and enhancement maintained for | At least 30 years | S17 para 9(3); S16 | Page (both agree) |
| Statutory biodiversity metric must be used | — | S16 | Page |
| Order of delivery | On-site, then off-site, then statutory credits | S16 | Page |
| Biodiversity gain plan approved before development starts | — | S16 | Page |
| London Plan Policy G6 | "aim to secure net biodiversity gain" | S1 | Page |
| 0.2 ha exemption from 6 August 2026 | — | S16 | Page (does not affect this site, which is larger) |

### Overheating and resilience

| Figure | Value | Source | Check |
|---|---|---|---|
| Requirement O1: limit unwanted solar gains; adequate means to remove heat; mechanical cooling only where heat cannot otherwise be removed | — | S10 requirement O1 | Read |
| Two compliance routes | Simplified method; dynamic thermal modelling to CIBSE TM59 | S10 Sections 1 and 2 | Read |
| Postcodes E15 and E20 are in the "high risk" part of London | — | S10 Appendix C, Table C1 | Read |
| Part O limits on TM59 modelling | Windows start opening at 22°C, fully open at 26°C | S10 para 2.6 | Read |
| Blinds, curtains and foliage may not be counted | — | S10 paras 2.8, 2.9 | Read |
| Cooling hierarchy, six steps | Reduce heat entering; minimise internal heat; manage heat with thermal mass; passive ventilation; mechanical ventilation; active cooling | S2 Policy SI 4 B; S8 para 8.2 | Page (S2), Read (S8) |
| Pass DSY1 weather year; DSY2 and DSY3 must be mitigated as far as practical | — | S8 paras 8.14, 8.16 | Read |
| Non-residential overheating tested to CIBSE TM52 with TM49 weather data | — | S8 Table 6 | Read |
| TM59 (2017) naturally ventilated homes: hours 1 K above the adaptive limit not more than 3% of May–September occupied hours | 3%, 1 K | S14 (restates S12) | Secondary |
| TM59 (2017) bedrooms: above 26°C for not more than 1% of annual night hours | 1%, 26°C | S14 | Secondary |
| TM59 (2017) is still required for Part O compliance; TM59 (2026) is recommended | — | S13 | Page |
| TM59 (2026) published July 2026; new bedroom criterion; 2050s weather data; ceiling-fan guidance | July 2026 | S13 | Page (new bedroom thresholds not verified) |
| Mains water use in homes | 105 litres per person per day or less (up to 5 litres for outdoors excluded) | S2 Policy SI 5 | Page |
| Greenfield runoff rates unless demonstrably impracticable | — | S2 Policy SI 13 | Page |

### Health and wellbeing

| Figure | Value | Source | Check |
|---|---|---|---|
| GG3: assess health impacts, for example by Health Impact Assessment; use Healthy Streets Approach | — | S4 Policy GG3 C, D | Page |
| SI 1: development must be at least Air Quality Neutral | — | S2 Policy SI 1 B | Page |
| D6: private outdoor space | 5 m² for 1–2 person homes, plus 1 m² per extra occupant | S3 Policy D6 | Page (also quoted by council documents in search results) |
| D6: maximise dual aspect homes | — | S3 Policy D6 | Page |
| D5: highest standards of accessible and inclusive design | — | S3 Policy D5 | Page |

---

## Part C. UN SDG target wording used in `sdg_matrix.csv`

Wording copied from the official goal pages above. Several targets carry a deadline (2020) that has now passed; I use them as a statement of direction.

| Target | Wording |
|---|---|
| 3.4 | By 2030, reduce by one third premature mortality from non-communicable diseases through prevention and treatment and promote mental health and well-being |
| 3.9 | By 2030, substantially reduce the number of deaths and illnesses from hazardous chemicals and air, water and soil pollution and contamination |
| 6.3 | By 2030, improve water quality by reducing pollution, eliminating dumping and minimizing release of hazardous chemicals and materials, halving the proportion of untreated wastewater and substantially increasing recycling and safe reuse globally |
| 6.4 | By 2030, substantially increase water-use efficiency across all sectors and ensure sustainable withdrawals and supply of freshwater to address water scarcity and substantially reduce the number of people suffering from water scarcity |
| 7.2 | By 2030, increase substantially the share of renewable energy in the global energy mix |
| 7.3 | By 2030, double the global rate of improvement in energy efficiency |
| 9.4 | By 2030, upgrade infrastructure and retrofit industries to make them sustainable, with increased resource-use efficiency and greater adoption of clean and environmentally sound technologies and industrial processes, with all countries taking action in accordance with their respective capabilities |
| 11.1 | By 2030, ensure access for all to adequate, safe and affordable housing and basic services and upgrade slums |
| 11.3 | By 2030, enhance inclusive and sustainable urbanization and capacity for participatory, integrated and sustainable human settlement planning and management in all countries |
| 11.5 | By 2030, significantly reduce the number of deaths and the number of people affected and substantially decrease the direct economic losses relative to global gross domestic product caused by disasters, including water-related disasters, with a focus on protecting the poor and people in vulnerable situations |
| 11.6 | By 2030, reduce the adverse per capita environmental impact of cities, including by paying special attention to air quality and municipal and other waste management |
| 11.7 | By 2030, provide universal access to safe, inclusive and accessible, green and public spaces, in particular for women and children, older persons and persons with disabilities |
| 11.b | By 2020, substantially increase the number of cities and human settlements adopting and implementing integrated policies and plans towards inclusion, resource efficiency, mitigation and adaptation to climate change, resilience to disasters, and develop and implement, in line with the Sendai Framework for Disaster Risk Reduction 2015-2030, holistic disaster risk management at all levels |
| 12.2 | By 2030, achieve the sustainable management and efficient use of natural resources |
| 12.5 | By 2030, substantially reduce waste generation through prevention, reduction, recycling and reuse |
| 12.7 | Promote public procurement practices that are sustainable, in accordance with national policies and priorities |
| 13.1 | Strengthen resilience and adaptive capacity to climate-related hazards and natural disasters in all countries |
| 13.2 | Integrate climate change measures into national policies, strategies and planning |
| 15.1 | By 2020, ensure the conservation, restoration and sustainable use of terrestrial and inland freshwater ecosystems and their services, in particular forests, wetlands, mountains and drylands, in line with obligations under international agreements |
| 15.5 | Take urgent and significant action to reduce the degradation of natural habitats, halt the loss of biodiversity and, by 2020, protect and prevent the extinction of threatened species |
| 15.9 | By 2020, integrate ecosystem and biodiversity values into national and local planning, development processes, poverty reduction strategies and accounts |

---

## Part D. What I could not verify

1. **Referral threshold.** The GLA page (S9) confirms that referable applications are defined by the Mayor of London Order 2008 and lists a new 50-home category from 11 May 2026. I did not read the Order itself, so I have not confirmed the older 150-home threshold. A scheme of about 300 homes is above either figure, so the strategy treats it as referable.
2. **Local plan.** I did not read Newham's adopted Local Plan. S18 says Newham follows the London Plan UGF scores. Which borough a real site near UCL East would fall in is an assumption.
3. **TM59 criteria.** I did not read TM59 (2017) itself. The 3% and 1% criteria come from a software vendor's restatement (S14). The numerical thresholds of the new bedroom criterion in TM59 (2026) are not verified; trade press reports numbers, which I have not used.
4. **Single-source London Plan wording.** The SI 1, SI 2 (10%/15% split), SI 5, SI 12, SI 13, D5, D6, D8 and GG3 wording comes from GLA web pages read through a summarising tool. Corroboration from a second source is noted in Part B where I found one.
5. **Future Homes Standard.** Only the dates and requirement L3 are confirmed. I did not verify the carbon-reduction percentage.
