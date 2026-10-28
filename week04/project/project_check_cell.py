# ===================== SSCM 2026 · GROUP PROJECT CHECK CELL · v1.0 =====================
# Copy this cell into your notebook UNCHANGED and run it after your baseline run.
# It needs two names defined earlier in your notebook:
#   DATA_DIR = the folder that holds your CSV files, e.g. DATA_DIR = "my_product_data"
#   baseline = your baseline results: one dictionary per seed (a list of 10), or one
#              dictionary with the means over the seeds. Keys (all numbers):
#     weeks_simulated      weeks in the run (52)
#     hours_simulated      clock hours of the run; the same clock as avg_hours_on_line
#     units_started        units that entered the line
#     units_finished       units that left the last station
#     key_components_used  key components taken from stock into the line
#     avg_units_on_line    time-average of units between start and finish
#     avg_hours_on_line    average hours from start to finish of a finished unit
#     cost_per_unit_eur    one-year total cost divided by units finished
# The grader runs the original of this cell on your files. Do not edit it.
import hashlib, math, os, datetime
import pandas as pd

CHECK_VERSION = "1.0"
REQUIRED = {
    "products.csv": ["product_id", "product_name", "frame_material", "mass_kg", "list_price_eur"],
    "bom.csv": ["product_id", "component_id", "component_name", "qty_per_unit", "mass_kg",
                "unit_cost_eur", "supplier_id", "added_at_workcenter"],
    "workcenters.csv": ["workcenter_id", "workcenter_name", "seq", "num_servers", "shift_hours",
                        "days_per_week", "availability", "process_time_cv", "fixed_cost_eur_week"],
    "routing.csv": ["product_id", "seq", "workcenter_id", "process_time_min", "setup_time_min"],
    "process_environment.csv": ["workcenter_id", "kw_running", "kw_idle", "waste_kg_per_unit",
                                "water_l_per_unit"],
    "suppliers.csv": ["supplier_id", "supplier_name", "country", "component_id", "unit_price_eur",
                      "promised_lead_days", "lead_time_mean_days", "lead_time_sd_days",
                      "capacity_per_month", "min_per_month", "kg_co2e_per_unit", "location_id"],
    "locations.csv": ["location_id", "name", "type", "country", "lat", "lon"],
    "network_lanes.csv": ["lane_id", "origin_id", "destination_id", "mode_id", "distance_km",
                          "transit_days_mean", "transit_days_sd"],
    "freight_rates.csv": ["lane_id", "mode_id", "rate_eur_per_shipment", "rate_eur_per_tkm",
                          "min_charge_eur"],
    "sources.csv": ["file", "row_id", "column", "value", "source_type", "source_or_calculation",
                    "sanity_check"],
}
MAY_BE_BLANK = {("bom.csv", "supplier_id")}           # parts not bought from a modelled supplier
MAY_BE_NEGATIVE = {("locations.csv", "lat"), ("locations.csv", "lon")}
KEYS = ["weeks_simulated", "hours_simulated", "units_started", "units_finished",
        "key_components_used", "avg_units_on_line", "avg_hours_on_line", "cost_per_unit_eur"]

def _cell_fingerprint():
    try:
        return hashlib.sha256(get_ipython().user_ns["_ih"][-1].strip().encode()).hexdigest()[:12]
    except Exception:
        return "n/a"

def _runs():
    b = globals().get("baseline")
    runs = b if isinstance(b, (list, tuple)) else [b]
    if b is None or not runs:
        raise ValueError("no `baseline` defined: run your baseline first")
    for i, r in enumerate(runs, 1):
        missing = [k for k in KEYS if k not in r]
        if missing:
            raise ValueError(f"baseline run {i} lacks {missing}")
        for k in KEYS:
            if not isinstance(r[k], (int, float)) or not math.isfinite(r[k]) or r[k] < 0:
                raise ValueError(f"baseline run {i}: {k} = {r[k]!r} is not a number ≥ 0")
        if r["units_finished"] <= 0 or r["hours_simulated"] <= 0 or r["weeks_simulated"] <= 0:
            raise ValueError(f"baseline run {i}: units_finished, hours and weeks must be > 0")
    return runs

def _verdict(name, ok, lines):
    print(f"{'PASS' if ok else 'FAIL'}  {name}")
    for line in lines:
        print("      " + line)
    return ok

data, results = {}, {}
folder = globals().get("DATA_DIR", ".")
h = hashlib.sha256()

# ---- T1 Format ----------------------------------------------------------------------
problems = []
for fname, cols in REQUIRED.items():
    path = os.path.join(folder, fname)
    if not os.path.exists(path):
        problems.append(f"{fname}: file missing in {folder!r}")
        continue
    h.update(open(path, "rb").read())
    df = pd.read_csv(path)
    df.columns = [str(c) for c in df.columns]
    data[fname] = df
    lacking = [c for c in cols if c not in df.columns]
    if lacking:
        problems.append(f"{fname}: column(s) missing or misspelt: {lacking}")
    if len(df) == 0:
        problems.append(f"{fname}: no rows")
    for c in [c for c in cols if c in df.columns]:
        blanks = df[c].isna() | (df[c].astype(str).str.strip() == "")
        if blanks.any() and (fname, c) not in MAY_BE_BLANK:
            problems.append(f"{fname}: {c} is empty in row(s) {list(df.index[blanks] + 2)}")
        num = pd.to_numeric(df[c], errors="coerce")
        if (num < 0).any() and (fname, c) not in MAY_BE_NEGATIVE:
            problems.append(f"{fname}: {c} is negative in row(s) {list(df.index[num < 0] + 2)}")
if "workcenters.csv" in data and "availability" in data["workcenters.csv"]:
    av = pd.to_numeric(data["workcenters.csv"]["availability"], errors="coerce")
    if ((av <= 0) | (av > 1) | av.isna()).any():
        problems.append("workcenters.csv: availability must be a share between 0 and 1")
if "routing.csv" in data and "process_time_min" in data["routing.csv"]:
    if (pd.to_numeric(data["routing.csv"]["process_time_min"], errors="coerce") <= 0).any():
        problems.append("routing.csv: every process_time_min must be above 0")
results["T1"] = _verdict("T1 Format", not problems,
                         problems[:12] + (["… and more"] if len(problems) > 12 else [])
                         or ["all 10 files present, columns exact, no blanks or negatives"])

# ---- baseline numbers for T2–T5 -------------------------------------------------------
try:
    runs = _runs()
    base_error = None
except Exception as e:
    runs, base_error = [], str(e)
if base_error:
    for t in ["T2 Capacity", "T3 Little's Law", "T4 Flow balance", "T5 Margin"]:
        results[t[:2]] = _verdict(t, False, [base_error])
else:
    try:
        prod = data["products.csv"].iloc[0]
        pid = prod["product_id"]
        wc = data["workcenters.csv"].set_index("workcenter_id")
        rt = data["routing.csv"]
        rt = rt[rt["product_id"] == pid]
        minutes = rt.groupby("workcenter_id")["process_time_min"].sum()
        unknown = [w for w in minutes.index if w not in wc.index]
        avail_min_week = (wc["num_servers"] * wc["shift_hours"] * 60 * wc["days_per_week"]
                          * wc["availability"])
        # ---- T2 Capacity: load offered by the units started, per station
        lines, ok = [], not unknown and len(minutes) > 0
        if unknown:
            lines.append(f"routing.csv names stations not in workcenters.csv: {unknown}")
        worst = {}
        for r in runs:
            for w, m in minutes.items():
                if w in wc.index:
                    share = r["units_started"] * m / (avail_min_week[w] * r["weeks_simulated"])
                    worst[w] = max(worst.get(w, 0), share)
        for w, share in worst.items():
            flag = "  <- 100 % or more" if share >= 1 else ""
            lines.append(f"{w} {wc.loc[w, 'workcenter_name']}: busy {share:.1%} of available time{flag}")
            ok = ok and share < 1
        results["T2"] = _verdict("T2 Capacity", ok, lines)
        # ---- T3 Little's Law: L = λ × W, within 10 %
        lines, ok = [], True
        for i, r in enumerate(runs, 1):
            lam = r["units_finished"] / r["hours_simulated"]
            lw = lam * r["avg_hours_on_line"]
            gap = abs(r["avg_units_on_line"] - lw) / lw if lw > 0 else float("inf")
            ok = ok and gap <= 0.10
            if (gap > 0.10 and len(lines) < 3) or i == 1:
                lines.append(f"run {i}: L = {r['avg_units_on_line']:.2f}  vs  λ×W = {lam:.3f}/h × "
                             f"{r['avg_hours_on_line']:.2f} h = {lw:.2f}  (gap {gap:.1%})")
        results["T3"] = _verdict("T3 Little's Law", ok, lines + [f"{len(runs)} run(s) checked"])
        # ---- T4 Flow balance
        bom = data["bom.csv"]
        bom = bom[bom["product_id"] == pid]
        keys = bom[bom["component_id"].isin(data["suppliers.csv"]["component_id"])]
        lines, ok = [], len(keys) == 1
        if len(keys) != 1:
            lines.append(f"expected one key component (in bom.csv and suppliers.csv), found {len(keys)}")
        else:
            q = float(keys["qty_per_unit"].iloc[0])
            n_opt = int((data["suppliers.csv"]["component_id"] == keys["component_id"].iloc[0]).sum())
            if n_opt < 2:
                lines.append(f"note: only {n_opt} sourcing option in suppliers.csv (the brief asks for two)")
            for i, r in enumerate(runs, 1):
                s, f, u = r["units_started"], r["units_finished"], r["key_components_used"]
                good = f <= s + 0.5 and f * q - 0.5 <= u <= s * q + 0.5
                ok = ok and good
                if not good or i == 1:
                    lines.append(f"run {i}: started {s:,.0f}, finished {f:,.0f}, key components used "
                                 f"{u:,.0f} (allowed {f*q:,.0f} to {s*q:,.0f})")
        results["T4"] = _verdict("T4 Flow balance", ok, lines)
        # ---- T5 Margin
        price = float(prod["list_price_eur"])
        material = float((bom["qty_per_unit"] * bom["unit_cost_eur"]).sum())
        costs = [r["cost_per_unit_eur"] for r in runs]
        lines = [f"cost per unit {min(costs):,.2f} to {max(costs):,.2f} EUR vs list price {price:,.2f} EUR"]
        if min(costs) < material:
            lines.append(f"warning: below the material cost alone ({material:,.2f} EUR per unit)")
        results["T5"] = _verdict("T5 Margin", max(costs) < price, lines)
    except Exception as e:
        for t in ["T2 Capacity", "T3 Little's Law", "T4 Flow balance", "T5 Margin"]:
            if t[:2] not in results:
                results[t[:2]] = _verdict(t, False, [f"could not run: {e}"])

print("-" * 78)
print(f"{sum(results.values())} of 5 tests passed  ·  {'ALL PASS' if all(results.values()) and len(results) == 5 else 'NOT YET'}")
print(f"check cell v{CHECK_VERSION} · cell {_cell_fingerprint()} · data {h.hexdigest()[:12]} · "
      f"{datetime.datetime.now():%Y-%m-%d %H:%M}")
# ======================= end of check cell · do not edit above ==========================
