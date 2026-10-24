"""Simple financial model for the StepSure business concept.

Every input below is an ASSUMPTION (see Part 5 of the report for the basis of
each number). Change the inputs and re-run to see how results move:

    python3 reports/financial_model.py
"""

LAKH = 100_000

# ---- Assumptions (INR) -------------------------------------------------------
STATIONS_PER_CUSTOMER = 5            # average stations per paying plant
SUB_PER_STATION_YEAR = 2.4 * LAKH    # software subscription per station per year
HW_KIT_PRICE = 1.6 * LAKH            # station kit sold to customer (one-time)
HW_KIT_COST = 1.35 * LAKH            # our landed cost of the kit
ONBOARDING_FEE = 3.0 * LAKH          # one-time per customer (process digitisation)
ONBOARDING_COST = 1.5 * LAKH         # engineer time + travel per onboarding
SUB_COGS_RATE = 0.20                 # cloud, support, field visits as % of subscription

# Monthly fixed operating cost (salaries, rent, cloud, travel, admin)
OPEX_MONTH_PROTOTYPE = 4.8 * LAKH    # months 1-6: 5-person build team
OPEX_MONTH_LAUNCH = 7.6 * LAKH       # months 7-12: 7-person team incl. sales
FIXED_COST_YEAR_2_PLUS = 120.0 * LAKH  # 9-10 people from year 2

# One-time / year-1 items
CAPEX_YEAR_1 = 10.1 * LAKH           # dev stations, VR headsets, workstations
MARKETING_YEAR_1 = 29.0 * LAKH       # see Part 4 budget table
LEGAL_IP_YEAR_1 = 5.0 * LAKH         # incorporation, trademark, prior-art/FTO search
SOFTWARE_TOOLS_YEAR_1 = 2.0 * LAKH   # engine/SDK licences, CAD viewer, dev tools
CONTINGENCY_RATE = 0.10

# Year-1 revenue, base case: 2 paid pilots, 2 converted to small contracts
PILOT_PRICE = 7.0 * LAKH
YEAR_1_PILOTS = 2
YEAR_1_CONVERSIONS_ARR_RECOGNISED = 6.0 * LAKH  # partial-year subscription


def per_customer():
    sub = STATIONS_PER_CUSTOMER * SUB_PER_STATION_YEAR
    hw_rev = STATIONS_PER_CUSTOMER * HW_KIT_PRICE
    hw_cost = STATIONS_PER_CUSTOMER * HW_KIT_COST
    first_year_rev = sub + hw_rev + ONBOARDING_FEE
    first_year_gp = sub * (1 - SUB_COGS_RATE) + (hw_rev - hw_cost) + (ONBOARDING_FEE - ONBOARDING_COST)
    recurring_gp = sub * (1 - SUB_COGS_RATE)
    return sub, first_year_rev, first_year_gp, recurring_gp


def lakh(x):
    return f"{x / LAKH:,.1f} L"


def year_one_cash():
    opex = 6 * OPEX_MONTH_PROTOTYPE + 6 * OPEX_MONTH_LAUNCH
    subtotal = opex + CAPEX_YEAR_1 + MARKETING_YEAR_1 + LEGAL_IP_YEAR_1 + SOFTWARE_TOOLS_YEAR_1
    total = subtotal * (1 + CONTINGENCY_RATE)
    revenue = YEAR_1_PILOTS * PILOT_PRICE + YEAR_1_CONVERSIONS_ARR_RECOGNISED
    return opex, total, revenue


def main():
    opex, total, revenue = year_one_cash()
    print("Year 1 cash plan")
    print(f"  Fixed opex (6 months prototype + 6 months launch): {lakh(opex)}")
    print(f"  Total year-1 spend incl. capex, marketing, legal, tools, 10% contingency: {lakh(total)}")
    print(f"  Base-case year-1 revenue: {lakh(revenue)}")
    print(f"  Funding needed (spend - revenue): {lakh(total - revenue)}")
    print()
    sub, fy_rev, fy_gp, rec_gp = per_customer()
    print("Per customer (5 stations)")
    print(f"  Annual recurring revenue (ARR): {lakh(sub)}")
    print(f"  First-year revenue (ARR + hardware + onboarding): {lakh(fy_rev)}")
    print(f"  First-year gross profit: {lakh(fy_gp)}")
    print(f"  Recurring gross profit per year (year 2 onward): {lakh(rec_gp)}")
    print()
    fixed = FIXED_COST_YEAR_2_PLUS
    print(f"Scenarios (steady state, fixed cost {lakh(fixed)}/year)")
    print(f"  {'Customers':>9} {'ARR':>10} {'Rec. GP':>10} {'Op. profit':>11}")
    for n in (5, 10, 20):
        arr = n * sub
        gp = n * rec_gp
        print(f"  {n:>9} {lakh(arr):>10} {lakh(gp):>10} {lakh(gp - fixed):>11}")
    print()
    be = fixed / rec_gp
    print(f"Break-even customers (recurring GP only): {be:.1f}")
    print(f"Break-even stations: {be * STATIONS_PER_CUSTOMER:.0f}")


if __name__ == "__main__":
    main()
