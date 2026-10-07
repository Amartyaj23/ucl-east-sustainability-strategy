"""Turn sdg_matrix.csv into a heatmap PNG (measures down the side, SDG targets across the top).

Usage:  python3 make_heatmap.py
Reads:  sdg_matrix.csv   (cell value 2 = direct link, 1 = supporting link, 0 = none)
Writes: images/sdg_heatmap.png
Needs:  pandas and matplotlib only.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # draw to a file, no window needed
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
import pandas as pd

HERE = Path(__file__).resolve().parent
CSV = HERE / "sdg_matrix.csv"
OUT = HERE / "images" / "sdg_heatmap.png"

# One-hue blue ramp, light to dark (steps 250 and 600 of the blue sequential ramp).
SURFACE = "#fcfcfb"
NONE = "#f0efec"
SUPPORT = "#86b6ef"
DIRECT = "#184f95"
INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#898781"

GOAL_NAMES = {
    "3": "Good health",
    "6": "Clean water",
    "7": "Energy",
    "9": "Industry",
    "11": "Cities",
    "12": "Consumption",
    "13": "Climate",
    "15": "Land / nature",
}


def main() -> None:
    df = pd.read_csv(CSV)
    sdg_cols = [c for c in df.columns if c.startswith("SDG ")]
    grid = df[sdg_cols].to_numpy()
    n_rows, n_cols = grid.shape
    labels = [f"{r.measure_id}  {r.measure}" for r in df.itertuples()]
    targets = [c.replace("SDG ", "") for c in sdg_cols]
    goals = [t.split(".")[0] for t in targets]

    fig, ax = plt.subplots(figsize=(11.5, 9.2), facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    cmap = ListedColormap([NONE, SUPPORT, DIRECT])
    ax.imshow(grid, cmap=cmap, vmin=0, vmax=2, aspect="auto")

    ax.set_xlim(-0.5, n_cols - 0.46)  # tiny margin so the last column's edge is not clipped

    # 2px gaps between cells so neighbouring fills never touch.
    ax.set_xticks([x - 0.5 for x in range(n_cols + 1)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(n_rows + 1)], minor=True)
    ax.grid(which="minor", color=SURFACE, linewidth=2)
    ax.tick_params(which="both", length=0)

    ax.set_xticks(range(n_cols))
    ax.set_xticklabels(targets, fontsize=9.5, color=INK)
    ax.xaxis.tick_top()
    ax.set_yticks(range(n_rows))
    ax.set_yticklabels(labels, fontsize=9.5, color=INK)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Goal labels in a band above the target numbers.
    start = 0
    for i in range(1, n_cols + 1):
        if i == n_cols or goals[i] != goals[start]:
            mid = (start + i - 1) / 2
            ax.text(mid, -1.55, f"Goal {goals[start]}", ha="center", va="bottom",
                    fontsize=9.5, fontweight="bold", color=INK)
            ax.text(mid, -1.0, GOAL_NAMES[goals[start]], ha="center", va="bottom",
                    fontsize=7.2, color=INK_2)
            if start > 0:
                ax.plot([start - 0.5, start - 0.5], [-1.6, n_rows - 0.5],
                        color=MUTED, linewidth=0.6, alpha=0.5, clip_on=False)
            start = i

    # Thin rule between the five strategy sections.
    for i in range(1, n_rows):
        if df["section"].iloc[i] != df["section"].iloc[i - 1]:
            ax.axhline(i - 0.5, color=MUTED, linewidth=1.2, xmin=-0.5, clip_on=False)

    # Count of measures that serve each target, along the bottom.
    for j in range(n_cols):
        count = int((grid[:, j] > 0).sum())
        ax.text(j, n_rows - 0.1, str(count), ha="center", va="top", fontsize=9, color=INK_2)
    ax.text(-0.6, n_rows - 0.1, "Measures per target", ha="right", va="top", fontsize=9, color=INK_2)

    ax.legend(
        handles=[Patch(facecolor=DIRECT, label="Direct link"),
                 Patch(facecolor=SUPPORT, label="Supporting link"),
                 Patch(facecolor=NONE, label="No link")],
        loc="upper center", bbox_to_anchor=(0.5, -0.05), ncol=3, frameon=False,
        fontsize=9.5, labelcolor=INK,
    )
    fig.suptitle("Which UN SDG targets each measure serves", x=0.02, y=0.985,
                 ha="left", fontsize=14, fontweight="bold", color=INK)
    fig.text(0.02, 0.948, "UCL East neighbourhood strategy (student exercise). Link strength is the author's judgement.",
             ha="left", fontsize=9.5, color=INK_2)

    fig.subplots_adjust(left=0.30, right=0.98, top=0.855, bottom=0.10)
    OUT.parent.mkdir(exist_ok=True)
    fig.savefig(OUT, dpi=160, facecolor=SURFACE)
    print(f"Wrote {OUT.relative_to(HERE)}  ({n_rows} measures x {n_cols} SDG targets)")


if __name__ == "__main__":
    main()
