#!/usr/bin/env python3
"""
Analyze current projection quality and suggest improvements
"""

import re

with open('index.html', 'r') as f:
    html = f.read()

print("=" * 70)
print("PROJECTION QUALITY ANALYSIS")
print("=" * 70)

# Find the calculateMonthlyProjection function
projection_func = re.search(r'function calculateMonthlyProjection\(.*?\n(.*?)\n  return months;', html, re.DOTALL)

if projection_func:
    func_body = projection_func.group(1)
    
    print("\n🔍 CURRENT PROJECTION METHOD:\n")
    
    # Check for NAV simulation
    if 'simulatedNAV' in func_body or 'Math.random()' in func_body:
        print("❌ PROBLEM 1: Using RANDOM/SIMULATED NAV")
        print("   Current: nav = currentNAV * (0.95 + Math.random() * 0.15)")
        print("   Issue: Random volatility, not based on historical patterns")
        print("")
    
    # Check for growth assumptions
    if '0.12' in func_body or '12%' in html:
        print("❌ PROBLEM 2: ASSUMED growth rates (12%, 15%, etc.)")
        print("   Current: Hardcoded growth assumptions")
        print("   Issue: Not based on actual fund performance")
        print("")
    
    # Check for historical data usage
    if 'history' not in func_body or 'historical' not in func_body.lower():
        print("❌ PROBLEM 3: NOT using historical NAV data")
        print("   Current: No historical data analysis")
        print("   Issue: Projections not validated against past performance")
        print("")

print("\n" + "=" * 70)
print("WHAT WE SHOULD DO - PROFESSIONAL APPROACH")
print("=" * 70)

print("""
✅ 1. FETCH HISTORICAL NAV DATA (Last 15 years)
   - MFApi.in provides full NAV history
   - Get actual NAV for each fund from 2010-2025
   - Calculate real returns: 1Y, 3Y, 5Y, 10Y, 15Y

✅ 2. CALCULATE ACTUAL FUND PERFORMANCE
   For each fund:
   - Absolute returns (what ₹10K became)
   - CAGR (Compound Annual Growth Rate)
   - Volatility (standard deviation)
   - Best/Worst year
   - Rolling returns

✅ 3. USE REALISTIC PROJECTIONS
   Instead of random: Use historical patterns
   - If Parag Parikh gave 18% CAGR (2010-2025)
   - Project: 15-18% for future (conservative)
   - Add realistic volatility from historical data

✅ 4. SHOW VALIDATION
   Display for each fund:
   - "Based on 15-year historical data"
   - "Actual CAGR (2010-2025): 17.2%"
   - "Projected CAGR: 15% (conservative)"
   - "Confidence: Historical avg ± volatility"

✅ 5. SCENARIO ANALYSIS
   Show 3 scenarios:
   - Best case: Historical best 5-year period
   - Base case: Historical 15-year CAGR
   - Worst case: Historical worst 5-year period
""")

print("\n" + "=" * 70)
print("CURRENT STATUS")
print("=" * 70)

print("""
❌ Current: VAGUE & OVERWHELMING
   - Random NAV simulation
   - Assumed growth rates
   - No historical validation
   - User can't trust numbers

✅ Should be: DATA-DRIVEN & VALIDATED
   - Real historical NAV
   - Actual fund performance
   - Conservative projections
   - User can verify
""")

print("\n" + "=" * 70)
print("RECOMMENDATION")
print("=" * 70)

print("""
🎯 IMPROVE PROJECTIONS WITH HISTORICAL DATA

Would you like me to:

1. Fetch 15-year historical NAV for all 10 funds
2. Calculate actual CAGR, volatility, returns
3. Use real data for projections (not random)
4. Show "Based on X years historical data"
5. Add scenario analysis (best/base/worst case)
6. Display fund performance cards with real returns

This will make your tool PROFESSIONAL and TRUSTWORTHY.
The projections will be realistic, not vague guesses.

Say "yes" and I'll implement historical data-driven projections!
""")

