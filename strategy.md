# Sustainability strategy: a mixed-use neighbourhood near UCL East

*A student exercise, not a real commission. The brief, site and all targets are my own assumptions. Policy figures are cited in [docs/sources.md](docs/sources.md); codes like S6 refer to that file. Each measure is mapped to a UN Sustainable Development Goal (SDG) target in [sdg_matrix.csv](sdg_matrix.csv). That mapping is my judgement, not an official classification.*

## Brief and assumptions

About 300 homes (about 27,000 m² gross internal area, GIA) and about 6,000 m² of workspace on a 2.0 ha site near UCL East, Queen Elizabeth Olympic Park, Stratford (postcode area E20). Homes are the largest use, so the scheme counts as "predominantly residential". I assume it is a "major" and "referable" application, meaning large enough that the Mayor of London reviews it. That triggers extra reports on whole life carbon and circular economy. The rules used are the London Plan 2021, GLA guidance, Building Regulations and the Environment Act 2021. I have not run any energy or ecology models, so every target is a design intention, not a prediction.

## 1. Carbon (operational and embodied)

**Policy.** London Plan Policy SI 2 says major developments should be net zero-carbon, following an energy hierarchy: be lean (use less), be clean, be green (renewables) and be seen (monitor results). They must cut on-site carbon by at least 35% beyond Building Regulations, with 10% (homes) or 15% (non-residential) from efficiency alone. Any shortfall is paid into a borough fund; the GLA suggests £95 per tonne of CO₂ over 30 years [S2, S8]. Referable schemes must also submit a whole life carbon assessment (SI 2 F) and compare it with GLA benchmarks in kgCO₂e per m² GIA [S6]:

| | Homes | Workspace (office benchmark) |
|---|---|---|
| Construction, A1–A5 | under 850 (aspirational 500) | under 950 (aspirational 600) |
| Whole life, A–C | under 1,200 (aspirational 800) | under 1,400 (aspirational 970) |

The GLA also asks schemes to aim for energy use of 35 kWh/m²/yr in homes and 55 in offices, with space heating of 15 [S8]. The Future Homes Standard takes effect on 24 March 2027 and adds a requirement for on-site renewable electricity in new homes [S15].

**Measures**
- **C1 All-electric, fabric-first buildings.** No gas; heavy insulation, airtight construction and heat-recovery ventilation. *Target:* energy use at most 35 kWh/m²/yr (homes) and 55 (workspace); space heating at most 15. *SDG 7.3, 9.4, 11.b, 13.2.*
- **C2 Heat pumps and solar roofs.** Electric heat pumps, with solar panels sharing roofs with green roofs. *Target:* at least 35% on-site carbon cut beyond Building Regulations; any shortfall to net zero paid at £95 per tonne. *SDG 7.2, 9.4, 13.2.*
- **C3 Be seen monitoring.** Meter every home and workspace unit and publish measured against predicted energy use yearly. *Target:* measured use within 20% of design (my own figure). *SDG 7.3, 13.2.*
- **C4 Low-carbon structure and materials.** Compare structural options (timber hybrid, low-cement concrete, reused steel) by carbon at concept stage; require product environmental declarations. *Target:* A1–A5 at most 500 kgCO₂e/m² (homes) and 600 (workspace), the GLA aspirational levels. *SDG 9.4, 12.2, 13.2.*
- **C5 Whole life carbon assessment, three times.** At pre-application, planning submission and after construction, independently checked [S6]. *Target:* A–C at most 800 (homes) and 970 (workspace). *SDG 11.b, 12.2, 13.2.*

**SDG targets served:** 7.2, 7.3, 9.4, 11.b, 12.2, 13.2.

## 2. Circular economy

**Policy.** London Plan Policy SI 7 asks referable schemes to aim to be net zero-waste and to submit a Circular Economy Statement. Targets: 95% of construction and demolition waste reused, recycled or recovered; 95% of excavation waste put to beneficial use; 65% municipal waste recycling by 2030; and no biodegradable or recyclable waste to landfill by 2026 [S2]. The GLA guidance says to explore keeping existing buildings before demolishing, to aim for at least 20% recycled or reused content by value, and to plan how the building can be taken apart at the end of its life [S7]. It also notes a 75% business waste recycling goal for 2030 [S7].

**Measures**
- **R1 Retain first, audit before demolition.** Test keeping every existing structure before any demolition, and commission a pre-demolition audit of reusable materials. *Target:* 95% of demolition waste reused, recycled or recovered. *SDG 12.2, 12.5, 13.2.*
- **R2 Recycled and reused content.** Track a Bill of Materials covering at least 80% of cost. *Target:* at least 20% recycled or reused content by value (the GLA's aim). *SDG 9.4, 12.2, 12.5.*
- **R3 Design for disassembly.** Bolted rather than glued connections, a repeating structural grid, and a digital "material passport" for each element. *Target:* passports covering elements worth at least 80% of cost. *SDG 11.3, 12.2, 12.5.*
- **R4 Waste on site and in use.** Reuse excavated soil on site where possible; shared bin stores sized for separated recycling. *Target:* 95% beneficial use of excavation waste; 65% recycling of household waste and 75% of workspace waste by 2030. *SDG 11.6, 12.5.*

**SDG targets served:** 9.4, 11.3, 11.6, 12.2, 12.5, 13.2.

## 3. Biodiversity net gain and greening

**Policy.** Since 12 February 2024, major developments in England must deliver at least 10% biodiversity net gain: the site's habitat value after building must exceed its value before by 10%, measured with the statutory biodiversity metric and maintained for 30 years. Gains should come on site first, then off site, with national credits as a last resort [S16, S17]. London Plan Policy G5 requires an Urban Greening Factor (UGF): each surface type scores from 0 (sealed paving) to 1 (semi-natural vegetation), weighted by area and divided by site area. The London Plan targets are 0.4 for predominantly residential and 0.3 for predominantly commercial schemes [S1, S5]. Policy G6 asks for net biodiversity gain [S1]. Newham reportedly uses the London Plan scores [S18]; I did not read its Local Plan.

**Measures**
- **B1 Baseline survey and metric.** Survey existing habitats before any clearance and run the statutory metric from the first design stage. *Target:* at least 10% net gain, mostly on site; 30-year management plan. *SDG 15.1, 15.5, 15.9.*
- **B2 Urban Greening Factor.** Design the landscape against the UGF from the first sketch. *Target:* UGF of at least 0.4. [`ugf_calculator.py`](ugf_calculator.py) tests an illustrative layout. *SDG 11.7, 13.1, 15.9.*
- **B3 Habitat patches linked to the Olympic Park.** Native meadow, wetland edge and flower-rich planting arranged as stepping stones. *Target:* at least 850 m² of semi-natural vegetation and wetland. *SDG 11.7, 15.1, 15.5.*
- **B4 Trees and biodiverse roofs.** Well-sized soil pits so trees reach full size; extensive green roofs with deep substrate. *Target:* 80 new trees (at least 50 with soil volume of two-thirds of canopy area or more) and 3,600 m² of green roof with at least 80 mm substrate. *SDG 11.6, 13.1, 15.5.*

**SDG targets served:** 11.6, 11.7, 13.1, 15.1, 15.5, 15.9.

## 4. Overheating and climate resilience

**Policy.** Building Regulations Part O (Approved Document O) requires new homes to limit solar heat gain and remove excess heat, using mechanical cooling only where other means are not enough. Compliance is by a simplified method or by computer modelling to CIBSE TM59 [S10]. E15 and E20 are in Part O's "high risk" London postcode list [S10]. London Plan Policy SI 4 sets a cooling hierarchy in six steps: reduce heat entering, reduce internal heat, use thermal mass, passive ventilation, mechanical ventilation, then active cooling last [S2, S8]. The GLA expects homes to pass the standard design summer year (DSY1) and to reduce risk as far as practical in the hotter DSY2 and DSY3 years [S8]. TM59 (2017) tests that living rooms, kitchens and bedrooms do not run more than 1 K over their comfort limit for more than 3% of summer occupied hours, and that bedrooms stay under 26°C for all but 1% of the night hours (as restated by a software vendor, not read in the original [S14]). A revised TM59 appeared in July 2026 with a new bedroom test and 2050s weather; Part O still requires the 2017 edition [S13]. Policy SI 13 requires surface water runoff at greenfield rates unless demonstrably impracticable, and SI 5 requires homes to use 105 litres or less of mains water per person per day [S2].

**Measures**
- **O1 Passive-first homes.** Dual-aspect layouts, fixed external shading, limited glazing, and no air conditioning in homes. *Target:* 100% of homes pass TM59 (2017) in DSY1, using Part O's modelling limits. *SDG 3.4, 11.1, 11.b, 13.1.*
- **O2 Extreme-heat stress test.** Re-run models in DSY2, DSY3 and the TM59 (2026) 2050s year; give residents a heat plan. *Target:* every failing room has documented fixes (shading, vents, fans); no home left without a plan. *SDG 3.4, 11.5, 11.b, 13.1.*
- **O3 Cool workspace.** Follow the same hierarchy for offices, tested to TM52 [S8]. *Target:* workspace passes TM52 with reported cooling demand. *SDG 7.3, 11.b, 13.1.*
- **O4 Rain gardens and sustainable drainage.** Manage rain where it falls. *Target:* runoff at or below greenfield rate; at least 700 m² of rain gardens. *SDG 6.3, 11.5, 13.1, 15.1.*
- **O5 Water efficiency.** Low-flow fittings and rainwater reuse for irrigation. *Target:* at most 105 litres per person per day in homes. *SDG 6.4, 11.b.*

**SDG targets served:** 3.4, 6.3, 6.4, 7.3, 11.1, 11.5, 11.b, 13.1, 15.1.

## 5. Health and wellbeing

**Policy.** London Plan Policy GG3 asks developers to assess health impacts, for example through a Health Impact Assessment, and to use the Healthy Streets Approach [S4]. Policy SI 1 requires schemes to be at least "air quality neutral" [S2]. Policy D6 asks for 5 m² of private outdoor space for one- to two-person homes plus 1 m² for each extra person, and says to maximise dual-aspect homes [S3]. Policy D5 asks for the highest standards of inclusive design [S3].

**Measures**
- **H1 Health Impact Assessment.** Run it at pre-application with local health teams and publish the actions. *Target:* assessment submitted; every identified harm has a named mitigation. *SDG 3.4, 11.3.*
- **H2 Clean air.** No on-site combustion (no gas boilers or diesel generators); a dust and emissions plan for construction. *Target:* air quality neutral. *SDG 3.9, 11.6.*
- **H3 Homes with outdoor space and light.** Every home gets a balcony or garden; dual aspect wherever possible. *Target:* 100% of homes meet the D6 outdoor-space minimum. *SDG 3.4, 11.1.*
- **H4 Inclusive green public realm.** Step-free, shaded, open-access courtyards and paths linking to the Olympic Park. *Target:* every home has a step-free route to public green space within 200 m (my own figure). *SDG 3.4, 11.3, 11.7.*

**SDG targets served:** 3.4, 3.9, 11.1, 11.3, 11.6, 11.7.

## What I could not verify

- **Referral status.** I did not read the Mayor of London Order, so the "referable" assumption rests on the scheme's size, not the legal threshold [S9].
- **Local rules.** I did not read Newham's Local Plan, and a real site's borough is itself an assumption [S18].
- **TM59.** I did not read TM59 itself. The 2017 criteria come from a vendor's restatement, and I could not confirm the thresholds of the 2026 bedroom test [S13, S14].
- **Future Homes Standard.** Only its dates and the renewable-electricity requirement are confirmed [S15].
- **Policy wording.** Several London Plan policies (SI 1, SI 5, SI 13, D5, D6, GG3) were read through web pages summarised by a tool, not from the full document [S2–S4].
- **SDG deadlines.** Targets 11.b, 15.1, 15.5 and 15.9 carry a 2020 deadline that has passed; I treat them as direction, not a test.

## Ideas for later

Embodied-carbon modelling with a real tool; a heat-network connection study; a cost plan; a survey of the actual site's ecology.
