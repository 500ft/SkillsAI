#!/usr/bin/env python3
"""Report overlapping text artists in a matplotlib figure. Import and call before fig.savefig().

    from overlap_check import check
    check(fig, "figure 3")      # prints collisions; returns count

Use as a gate: assert check(fig) == 0 before saving. Tick-label vs axis-label pairs are listed
separately so you can accept them deliberately.
"""
import itertools

def _texts(fig):
    out = []
    for ax in fig.axes:
        for t in ax.texts: out.append(("text", t))
        out.append(("xlabel", ax.xaxis.label)); out.append(("ylabel", ax.yaxis.label)); out.append(("title", ax.title))
        for t in ax.get_xticklabels() + ax.get_yticklabels(): out.append(("tick", t))
        leg = ax.get_legend()
        if leg:
            for t in leg.get_texts(): out.append(("legend", t))
    for t in fig.texts: out.append(("figtext", t))
    return [(k, t) for k, t in out if t.get_visible() and t.get_text().strip()]

def check(fig, name="figure", verbose=True):
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    items = [(k, t, t.get_window_extent(r)) for k, t in _texts(fig)]
    hard, soft = [], []
    for (ka, ta, ba), (kb, tb, bb) in itertools.combinations(items, 2):
        if ba.overlaps(bb):
            pair = (ka, ta.get_text()[:30], kb, tb.get_text()[:30])
            tick_vs_label = ("tick" in (ka, kb)) and ({"xlabel", "ylabel"} & {ka, kb})
            (soft if tick_vs_label else hard).append(pair)
    if verbose:
        print(f"[{name}] hard collisions: {len(hard)}  (tick-vs-axis-label: {len(soft)})")
        for p in hard: print("   ", p)
    return len(hard)
