#!/usr/bin/env python3
"""
Verify that parameter changes propagate to all dependent pages
"""

import re

with open('index.html', 'r') as f:
    html = f.read()

print("=" * 70)
print("DATA FLOW VERIFICATION")
print("=" * 70)

# Check saveConfig function
print("\n1. SETTINGS SAVE FUNCTION:")

save_config = re.search(r'function saveConfig\(\).*?\n}', html, re.DOTALL)
if save_config:
    func_body = save_config.group(0)
    
    # Check if it refreshes dependent pages
    refreshes = [
        ('refreshMyPortfolio', 'My Portfolio'),
        ('refreshWifePortfolio', 'Wife Portfolio'),
        ('renderMonthlyProjections', 'Monthly Projections'),
        ('renderDashboardCharts', 'Dashboard'),
        ('renderRetirementCharts', 'Retirement'),
        ('renderKidsCharts', 'Kids Education')
    ]
    
    for func_name, page_name in refreshes:
        if func_name in func_body:
            print(f"   ✅ Refreshes {page_name}")
        else:
            print(f"   ❌ MISSING: {page_name} not refreshed")
else:
    print("   ❌ saveConfig function not found!")

# Check if fund data is linked to settings
print("\n2. FUND DATA LINKAGE:")

# Check if yourFunds array is static or dynamic
funds_def = re.search(r'const yourFunds\s*=\s*\[', html)
if funds_def:
    print("   ⚠️  WARNING: yourFunds is CONST (hardcoded)")
    print("   Need to update SIP values from settings")
else:
    print("   ✅ yourFunds is dynamic")

# Check if there's a function to sync settings with fund data
sync_funcs = ['updateFundSIPs', 'syncFundsFromSettings', 'loadSIPFromSettings']
found_sync = False
for func in sync_funcs:
    if func in html:
        print(f"   ✅ Found sync function: {func}")
        found_sync = True

if not found_sync:
    print("   ❌ MISSING: No function to sync settings → fund data")

print("\n3. DEPENDENCY CHAIN:")
print("   Settings → yourFunds[].monthlySIP → Monthly Projections")
print("   Settings → config.yourSIP → Dashboard")
print("   Settings → config.netPay → Cash Flow")

# Check localStorage usage
print("\n4. PERSISTENCE:")
if "localStorage.setItem('financialConfig'" in html:
    print("   ✅ Config saved to localStorage")
else:
    print("   ❌ Config NOT saved to localStorage")

if "localStorage.setItem('myFundsSIP'" in html:
    print("   ✅ Fund SIPs saved to localStorage")
else:
    print("   ❌ Fund SIPs NOT saved to localStorage")

print("\n" + "=" * 70)
print("RECOMMENDATION")
print("=" * 70)

print("""
To ensure ALL pages update when you change parameters:

1. Settings page inputs should update:
   - config object (income, expenses, etc.)
   - yourFunds array (SIP amounts)
   - wifeFunds array (SIP amounts)

2. saveConfig() should call:
   - saveFundsData() - sync settings → funds
   - refreshMyPortfolio() - update My Portfolio
   - refreshWifePortfolio() - update Wife Portfolio  
   - renderMonthlyProjections() - update Monthly Projections
   - renderDashboardCharts() - update Dashboard
   - renderAllCharts() - update all other charts

3. All pages should READ from:
   - config object (single source of truth)
   - yourFunds/wifeFunds arrays (dynamic)

Let me check if this is implemented...
""")

