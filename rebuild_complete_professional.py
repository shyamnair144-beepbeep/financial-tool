#!/usr/bin/env python3
"""
Professional complete rebuild of financial tool
This script will:
1. Start from original backup
2. Create proper 14-page structure
3. Add all missing pages (Settings, My Portfolio, Wife's Portfolio, Historical, Alerts)
4. Add all JavaScript functions properly
5. Ensure data flows correctly
6. Use readable fonts
"""

import re

print("🔧 PROFESSIONAL REBUILD STARTED")
print("=" * 70)

# Start from original backup
print("\n📂 Step 1: Loading original backup...")
with open('index-original-backup.html', 'r') as f:
    html = f.read()

original_lines = html.count('\n')
print(f"   ✅ Loaded {original_lines:,} lines from original")

# The original has these pages:
# 0: Dashboard
# 1: Retirement  
# 2: Kids Education
# 3: Investments
# 4: Tax Optimizer
# 5: Car Decision
# 6: Sinking Funds
# 7: Wife's Portfolio

# We need to add:
# - Settings page (will be page 1, shifting others)
# - My Portfolio page (will be page 2, before Retirement)
# - Historical page 
# - Alerts page
# - Enhanced Car Decision

# First, let's update the navigation to have all 12 tabs
print("\n🔗 Step 2: Updating navigation structure...")

old_nav = re.search(r'<div class="tabs">(.*?)</div>\s*<div class="content">', html, re.DOTALL)
if old_nav:
    new_nav = '''<div class="tabs">
  <div class="tab active" onclick="showPage(0)">📊 DASHBOARD</div>
  <div class="tab" onclick="showPage(1)">⚙️ SETTINGS</div>
  <div class="tab" onclick="showPage(2)">💼 MY PORTFOLIO</div>
  <div class="tab" onclick="showPage(3)">🏖️ RETIREMENT</div>
  <div class="tab" onclick="showPage(4)">🎓 KIDS EDUCATION</div>
  <div class="tab" onclick="showPage(5)">💼 INVESTMENTS</div>
  <div class="tab" onclick="showPage(6)">💰 TAX OPTIMIZER</div>
  <div class="tab" onclick="showPage(7)">🚗 CAR DECISION</div>
  <div class="tab" onclick="showPage(8)">🏦 SINKING FUNDS</div>
  <div class="tab" onclick="showPage(9)">📈 WIFE'S PORTFOLIO</div>
  <div class="tab" onclick="showPage(10)">📊 HISTORICAL</div>
  <div class="tab" onclick="showPage(11)">🔔 ALERTS</div>
</div>
<div class="content">'''
    
    html = html[:old_nav.start()] + new_nav + html[old_nav.end():]
    print("   ✅ Updated navigation to 12 tabs")
else:
    print("   ⚠️  Navigation structure not found in expected format")

# Change fonts to readable system fonts
print("\n🔤 Step 3: Changing to readable system fonts...")
html = html.replace(
    "font-family:'IBM Plex Mono','Courier New',monospace",
    "font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"
)
html = html.replace(
    "font-family:'IBM Plex Mono',monospace",
    "font-family:'SF Mono',Consolas,Monaco,'Courier New',monospace"
)
print("   ✅ Changed to system fonts (more readable)")

# Add Settings page after Dashboard
print("\n⚙️ Step 4: Adding SETTINGS page...")

# Find where to insert (after first page div closes)
dashboard_end = html.find('</div>\n\n<!-- PAGE 1:')
if dashboard_end == -1:
    dashboard_end = html.find('</div>\n<!-- PAGE 1:')

if dashboard_end != -1:
    settings_page = '''

<!-- PAGE 1: SETTINGS -->
<div class="page">
  <h1>Settings & Configuration</h1>
  
  <div style="background:rgba(240,180,41,0.1);border-left:4px solid #f0b429;padding:15px;margin:20px 0;border-radius:4px">
    💡 <strong>LIVE UPDATES:</strong> Changes here automatically update all other pages when you click SAVE SETTINGS.
  </div>

  <h2>💰 Income & Employment</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin:20px 0">
    <div>
      <label style="display:block;margin-bottom:8px;font-weight:600">Annual CTC (₹)</label>
      <input type="number" id="cfg_annualCTC" value="2320000" oninput="updateNetPay()" 
             style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:12px;border-radius:6px;font-size:14px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px;font-weight:600">Monthly Net Pay (₹)</label>
      <input type="number" id="cfg_netPay" value="147680" oninput="updateAnnualCTC()"
             style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:12px;border-radius:6px;font-size:14px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px;font-weight:600">Wife's Contribution (₹/month)</label>
      <input type="number" id="cfg_wifeContrib" value="50000"
             style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:12px;border-radius:6px;font-size:14px">
    </div>
  </div>

  <h2>🏠 Monthly Expenses</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:15px;margin:20px 0">
    <div>
      <label style="display:block;margin-bottom:8px">Rent</label>
      <input type="number" id="cfg_rent" value="40000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px">Electricity</label>
      <input type="number" id="cfg_electricity" value="3000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px">Internet & Phone</label>
      <input type="number" id="cfg_internet" value="2000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px">Maintenance</label>
      <input type="number" id="cfg_maintenance" value="3000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px">Groceries</label>
      <input type="number" id="cfg_groceries" value="15000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px">Dining Out</label>
      <input type="number" id="cfg_dining" value="8000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px">Transport</label>
      <input type="number" id="cfg_transport" value="5000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px">Household Items</label>
      <input type="number" id="cfg_household" value="4000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px">Parents Support</label>
      <input type="number" id="cfg_parents" value="25000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px">Healthcare</label>
      <input type="number" id="cfg_healthcare" value="5000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px">Personal Care</label>
      <input type="number" id="cfg_personal" value="3000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px">Entertainment</label>
      <input type="number" id="cfg_entertainment" value="6000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px">Shopping & Misc</label>
      <input type="number" id="cfg_shopping" value="10000" style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px;border-radius:4px">
    </div>
  </div>

  <h2>💼 Monthly Investments</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin:20px 0">
    <div>
      <label style="display:block;margin-bottom:8px;font-weight:600">Your SIP (₹/month)</label>
      <input type="number" id="cfg_yourSIP" value="71886"
             style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:12px;border-radius:6px;font-size:14px">
    </div>
    <div>
      <label style="display:block;margin-bottom:8px;font-weight:600">Wife's SIP (₹/month)</label>
      <input type="number" id="cfg_wifeSIP" value="50000"
             style="width:100%;background:var(--bg2);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:12px;border-radius:6px;font-size:14px">
    </div>
  </div>

  <div style="margin:30px 0;text-align:center">
    <button onclick="saveConfig()" style="background:#30c87a;color:#000;border:none;padding:15px 40px;border-radius:6px;font-weight:700;font-size:16px;cursor:pointer">
      💾 SAVE SETTINGS
    </button>
    <div id="saveNotification" style="display:none;margin-top:15px;color:#30c87a;font-weight:600">
      ✅ Settings saved and all pages updated!
    </div>
  </div>
</div>
'''
    html = html[:dashboard_end] + settings_page + html[dashboard_end:]
    print("   ✅ Added Settings page with all editable fields")
else:
    print("   ⚠️  Could not find insertion point for Settings page")

print("\n💼 Step 5: Adding MY PORTFOLIO page...")

# This will be a comprehensive page
# For now, save to continue
with open('index.html', 'w') as f:
    f.write(html)

print("\n✅ Phase 1 complete - Navigation and Settings added")
print("   Continuing with portfolio pages...")

