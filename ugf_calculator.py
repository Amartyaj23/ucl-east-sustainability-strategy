"""Urban Greening Factor (UGF) calculator, using the London Plan's surface-cover factors.

Usage:  python3 ugf_calculator.py
Writes: images/ugf_result.png, and prints the table and score.
Needs:  pandas and matplotlib only.

Method (GLA, London Plan Guidance: Urban Greening Factor, January 2023, para 3.2.1):
    UGF = sum(area of each surface-cover type x its factor) / total site area

Factors: London Plan 2021 Policy G5, Table 8.2 (reproduced as Table 3.1 of the GLA guidance).
Targets: 0.4 for predominantly residential, 0.3 for predominantly commercial (GLA guidance para 1.1.2).
Full citations are in docs/sources.md.

The site layout below is ILLUSTRATIVE and invented for this student exercise. Edit LAYOUT to test your own.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
OUT = HERE / "images" / "ugf_result.png"

# --- London Plan Table 8.2: surface-cover factors (docs/sources.md, Part B) ---------------------
FACTORS = {
    "Semi-natural vegetation": 1.0,
    "Wetland or open water (semi-natural)": 1.0,
    "Intensive green roof (150 mm+ substrate)": 0.8,
    "Standard trees, soil volume >= 2/3 of canopy area": 0.8,
    "Extensive green roof (80 mm+ substrate)": 0.7,
    "Flower-rich perennial planting": 0.7,
    "Rain gardens / vegetated drainage": 0.7,
    "Hedges": 0.6,
    "Standard trees, soil volume < 2/3 of canopy area": 0.6,
    "Green wall": 0.6,
    "Groundcover planting": 0.5,
    "Amenity grassland": 0.4,
    "Extensive green roof (sedum mat)": 0.3,
    "Water features (chlorinated)": 0.2,
    "Permeable paving": 0.1,
    "Sealed surfaces": 0.0,
}
TARGET_RESIDENTIAL = 0.4
TARGET_COMMERCIAL = 0.3

# --- Illustrative scheme (all areas in m2; assumptions, not survey data) -----------------------
SITE_AREA = 20_000  # red-line boundary, 2.0 ha
RESIDENTIAL_GIA = 27_000  # about 300 homes
WORKSPACE_GIA = 6_000

# Areas measured in plan. These must add up to SITE_AREA.
PLAN_LAYOUT = [
    # roofs (building footprint = 9,000 m2)
    ("Intensive green roof (150 mm+ substrate)", 800),
    ("Extensive green roof (80 mm+ substrate)", 3_600),
    ("Sealed surfaces", 4_600),  # plant, cores, terraces (roof)
    # ground level (11,000 m2)
    ("Sealed surfaces", 5_200),  # streets, paths, hardstanding
    ("Permeable paving", 1_500),
    ("Amenity grassland", 1_100),
    ("Groundcover planting", 600),
    ("Hedges", 150),
    ("Flower-rich perennial planting", 900),
    ("Rain gardens / vegetated drainage", 700),
    ("Semi-natural vegetation", 700),
    ("Wetland or open water (semi-natural)", 150),
]

# Extra layers that the GLA method scores in their own right and does NOT add to site area:
#  - tree canopy (what lies under it is still scored separately), measured as projected canopy
#  - green walls, measured on the vertical plane
CANOPY_PER_TREE = 30  # m2 at maturity, assumed (must not exceed the nursery's published maximum)
EXTRA_LAYOUT = [
    ("Standard trees, soil volume >= 2/3 of canopy area", 50 * CANOPY_PER_TREE),  # 50 trees
    ("Standard trees, soil volume < 2/3 of canopy area", 30 * CANOPY_PER_TREE),  # 30 trees
    ("Green wall", 600),  # on podium and boundary walls
]


def target_score(residential_gia: float, commercial_gia: float) -> tuple[float, str]:
    """Use class with the most floorspace decides the target (GLA guidance para 3.2.2)."""
    if residential_gia >= commercial_gia:
        return TARGET_RESIDENTIAL, "predominantly residential"
    return TARGET_COMMERCIAL, "predominantly commercial"


def calculate(plan_layout, extra_layout, site_area):
    plan_total = sum(area for _, area in plan_layout)
    if plan_total != site_area:
        raise ValueError(f"Plan areas add up to {plan_total} m2, but the site is {site_area} m2")
    rows = []
    for kind, layout in (("plan", plan_layout), ("extra layer", extra_layout)):
        for name, area in layout:
            factor = FACTORS[name]  # KeyError here means a surface type that is not in Table 8.2
            rows.append({"Surface cover": name, "Counted as": kind, "Area (m2)": area,
                         "Factor": factor, "Score (area x factor)": area * factor})
    table = pd.DataFrame(rows)
    # merge identical surface types (e.g. roof and ground sealed surfaces) for display
    table = (table.groupby(["Surface cover", "Counted as", "Factor"], as_index=False)
             [["Area (m2)", "Score (area x factor)"]].sum()
             .sort_values(["Score (area x factor)", "Factor"], ascending=False, ignore_index=True))
    score = table["Score (area x factor)"].sum() / site_area
    return table, score


def draw(table, score, target, label):
    ink, ink2, surface, blue, light_blue = "#0b0b0b", "#52514e", "#fcfcfb", "#184f95", "#86b6ef"
    contrib = table[table["Score (area x factor)"] > 0].copy()
    contrib["points"] = contrib["Score (area x factor)"] / SITE_AREA
    contrib = contrib.sort_values("points")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7.4), facecolor=surface,
                                   gridspec_kw={"height_ratios": [1, 4.2], "hspace": 0.35})
    for ax in (ax1, ax2):
        ax.set_facecolor(surface)
        for side in ("top", "right", "left"):
            ax.spines[side].set_visible(False)
        ax.spines["bottom"].set_color("#c3c2b7")
        ax.tick_params(colors=ink2, length=0)

    ax1.barh([0], [score], color=blue, height=0.5)
    ax1.axvline(target, color=ink, linewidth=2)
    ax1.text(target + 0.01, 0.34, f"London Plan target {target:.1f} ({label})", ha="left", va="bottom",
             fontsize=9.5, color=ink)
    ax1.text(score / 2, 0, f"UGF {score:.2f}", ha="center", va="center", color="white",
             fontsize=12, fontweight="bold")
    ax1.set_xlim(0, 0.6)
    ax1.set_ylim(-0.4, 0.9)
    ax1.set_yticks([])
    ax1.set_title("Illustrative UCL East layout: Urban Greening Factor", loc="left", fontsize=13,
                  fontweight="bold", color=ink, pad=14)

    ax2.barh(contrib["Surface cover"], contrib["points"], color=light_blue, height=0.62)
    for y, (p, a) in enumerate(zip(contrib["points"], contrib["Area (m2)"])):
        ax2.text(p + 0.002, y, f"{p:.3f}   ({a:,.0f} m2)", va="center", fontsize=8.5, color=ink2)
    ax2.set_xlim(0, contrib["points"].max() * 1.45)
    ax2.set_xlabel(f"Contribution to the score (area x factor / {SITE_AREA:,} m2 site)", color=ink2,
                   fontsize=9.5)
    for lab in ax2.get_yticklabels():
        lab.set_fontsize(9)
        lab.set_color(ink)
    fig.text(0.01, 0.005, "Factors: London Plan 2021 Table 8.2. Areas are invented for this student exercise.",
             fontsize=8, color=ink2)
    OUT.parent.mkdir(exist_ok=True)
    fig.savefig(OUT, dpi=160, facecolor=surface, bbox_inches="tight")


def main() -> None:
    table, score = calculate(PLAN_LAYOUT, EXTRA_LAYOUT, SITE_AREA)
    target, label = target_score(RESIDENTIAL_GIA, WORKSPACE_GIA)

    pd.set_option("display.width", 140)
    print(table.to_string(index=False, float_format=lambda v: f"{v:,.1f}"))
    print()
    print(f"Site area:        {SITE_AREA:,} m2 (plan areas checked: they add up)")
    total = table["Score (area x factor)"].sum()
    print(f"UGF score:        {total:,.0f} / {SITE_AREA:,} = {total / SITE_AREA:.4f}  (about {score:.2f})")
    print(f"Target:           {target:.1f} ({label}: {RESIDENTIAL_GIA:,} m2 homes vs {WORKSPACE_GIA:,} m2 workspace)")
    verdict = "MEETS" if score >= target else "DOES NOT MEET"
    print(f"Result:           {verdict} the London Plan target (margin {score - target:+.3f})")

    draw(table, score, target, label)
    print(f"Wrote {OUT.relative_to(HERE)}")


if __name__ == "__main__":
    main()
