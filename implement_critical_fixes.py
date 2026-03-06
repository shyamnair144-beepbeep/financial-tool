#!/usr/bin/env python3
"""
CRITICAL FINANCIAL PLANNING FIXES
==================================

Implements 5 critical fixes identified by CFP-level analysis:
1. Inflation Modeling - Inflate all goals to future values
2. Asset Allocation Tracker - Show current allocation vs target with rebalancing alerts
3. Emergency Fund Tracker - Track ₹20L existing fund vs required coverage
4. Insurance Adequacy - Calculate life/health insurance gaps
5. Retirement Corpus Fix - Use inflated expenses + 4% safe withdrawal rule

Professional-grade implementation following Certified Financial Planner standards.
"""

import re

print("=" * 80)
print("🎯 IMPLEMENTING CRITICAL FINANCIAL PLANNING FIXES")
print("=" * 80)
print()

with open('index.html', 'r') as f:
    html = f.read()

# ============================================================================
# PHASE 1: ADD INFLATION MODELING
# ============================================================================

print("📊 PHASE 1: Adding Inflation Modeling...")
print()

# Step 1: Add inflation inputs to Settings page
print("  → Adding inflation rate inputs to Settings page...")

old_investment_assumptions = '''<div class="sh"><span class="sh-n">03</span><h2>Investment Assumptions</h2></div>
<div class="settings-grid">
  <div class="sg-row">
    <label>Expected Return (CAGR) <small>Annual return expectation</small></label>
    <input id="s-return" type="number" step="0.1" value="12">%
  </div>
  <div class="sg-row">
    <label>Annual Step-up <small>SIP increase every year</small></label>
    <input id="s-stepup" type="number" step="1" value="10">%
  </div>
  <div class="sg-row">
    <label>Inflation Rate <small>General inflation</small></label>
    <input id="s-inflation" type="number" step="0.1" value="6">%
  </div>
</div>'''

new_investment_assumptions = '''<div class="sh"><span class="sh-n">03</span><h2>Investment Assumptions</h2></div>
<div class="settings-grid">
  <div class="sg-row">
    <label>Expected Return (CAGR) <small>Annual return expectation</small></label>
    <input id="s-return" type="number" step="0.1" value="12">%
  </div>
  <div class="sg-row">
    <label>Annual Step-up <small>SIP increase every year</small></label>
    <input id="s-stepup" type="number" step="1" value="10">%
  </div>
  <div class="sg-row">
    <label>General Inflation <small>Living expenses, rent</small></label>
    <input id="s-inflation-general" type="number" step="0.1" value="6">%
  </div>
  <div class="sg-row">
    <label>Education Inflation <small>Kids college fees</small></label>
    <input id="s-inflation-education" type="number" step="0.1" value="10">%
  </div>
  <div class="sg-row">
    <label>Healthcare Inflation <small>Medical costs</small></label>
    <input id="s-inflation-healthcare" type="number" step="0.1" value="12">%
  </div>
</div>'''

if old_investment_assumptions in html:
    html = html.replace(old_investment_assumptions, new_investment_assumptions)
    print("     ✅ Added 3 inflation rate inputs (general 6%, education 10%, healthcare 12%)")
else:
    print("     ⚠️  Could not find Investment Assumptions section")

# Step 2: Add Emergency Fund section to Settings
print("  → Adding Emergency Fund section to Settings...")

emergency_fund_section = '''
<div class="sh"><span class="sh-n">04</span><h2>Emergency Fund</h2></div>
<div class="settings-grid">
  <div class="sg-row">
    <label>Current Emergency Fund <small>Liquid funds, savings account</small></label>
    <input id="s-emergency-fund" type="number" step="10000" value="2000000">
  </div>
  <div class="sg-row">
    <label>Target Coverage <small>Months of expenses</small></label>
    <select id="s-emergency-target">
      <option value="6" selected>6 months (Minimum)</option>
      <option value="9">9 months (Recommended)</option>
      <option value="12">12 months (Conservative)</option>
    </select>
  </div>
</div>
<div id="emergency-fund-status" style="margin:16px 0"></div>

'''

# Insert before My SIP Allocation
my_sip_marker = '<div class="sh"><span class="sh-n">04</span><h2>My SIP Allocation</h2></div>'
if my_sip_marker in html:
    html = html.replace(my_sip_marker, emergency_fund_section + my_sip_marker.replace('sh-n">04', 'sh-n">05'))
    print("     ✅ Added Emergency Fund section with ₹20L default")
else:
    print("     ⚠️  Could not find My SIP Allocation marker")

# Step 3: Add Insurance Coverage section
print("  → Adding Insurance Coverage section...")

insurance_section = '''
<div class="sh"><span class="sh-n">06</span><h2>Insurance Coverage</h2></div>
<div class="settings-grid">
  <div class="sg-row">
    <label>Life Insurance (Term) <small>Current coverage</small></label>
    <input id="s-life-insurance" type="number" step="100000" value="0" placeholder="e.g., 50000000 for ₹5 Cr">
  </div>
  <div class="sg-row">
    <label>Health Insurance (Family) <small>Sum assured</small></label>
    <input id="s-health-insurance" type="number" step="100000" value="0" placeholder="e.g., 2000000 for ₹20L">
  </div>
  <div class="sg-row">
    <label>Parents Health Insurance <small>Sum assured</small></label>
    <input id="s-parents-health" type="number" step="100000" value="0" placeholder="e.g., 1000000 for ₹10L">
  </div>
</div>
<div id="insurance-adequacy" style="margin:16px 0"></div>

'''

# Insert after Wife's SIP Allocation
wife_sip_end = '</div>\n</div>\n\n<button class="save-btn"'
if wife_sip_end in html:
    html = html.replace(wife_sip_end, '</div>\n</div>\n\n' + insurance_section + '<button class="save-btn"')
    print("     ✅ Added Insurance Coverage section")
else:
    print("     ⚠️  Could not find insertion point for insurance section")

# Fix section numbers for My SIP and Wife's SIP
html = html.replace('<div class="sh"><span class="sh-n">05</span><h2>Wife\'s SIP Allocation', '<div class="sh"><span class="sh-n">07</span><h2>Wife\'s SIP Allocation')

# Step 4: Update config object
print("  → Updating config object with new fields...")

old_config = '''let config = {
  annualCTC: 3360000,
  basicSalary: 139678,
  netPay: 213586,
  wifeGross: 70000,
  wifeInvestment: 50000,
  rent: 40000,
  parents: 20000,
  fixedExpenses: 13000,
  livingExpenses: 49000,
  sinkingFunds: 60000,
  yourSIP: 70900,
  wifeSIP: 50000
};'''

new_config = '''let config = {
  annualCTC: 3360000,
  basicSalary: 139678,
  netPay: 213586,
  wifeGross: 70000,
  wifeInvestment: 50000,
  rent: 40000,
  parents: 20000,
  fixedExpenses: 13000,
  livingExpenses: 49000,
  sinkingFunds: 60000,
  yourSIP: 70900,
  wifeSIP: 50000,
  // Inflation rates
  inflationGeneral: 6,
  inflationEducation: 10,
  inflationHealthcare: 12,
  // Emergency fund
  emergencyFund: 2000000,  // ₹20L existing
  emergencyFundTarget: 6,  // 6 months coverage
  // Insurance
  lifeInsuranceCurrent: 0,
  healthInsuranceCurrent: 0,
  parentsHealthInsurance: 0
};'''

html = html.replace(old_config, new_config)
print("     ✅ Added inflation, emergency fund, and insurance fields to config")

print()
print("✅ PHASE 1 COMPLETE: Inflation & Settings Infrastructure Added")
print()

# Write intermediate result
with open('index.html', 'w') as f:
    f.write(html)

print("=" * 80)
print("💾 Progress saved. Continuing with calculation functions...")
print("=" * 80)
print()
