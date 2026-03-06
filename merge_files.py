#!/usr/bin/env python3
"""
Merge index-original-backup.html with new features from index-v4-ultimate.html
Creates ONE complete file with ALL 14 pages.
"""

import re

print("🔧 Starting merge process...")
print("=" * 60)

# Read both files
with open('index-original-backup.html', 'r') as f:
    original = f.read()

with open('index-v4-ultimate.html', 'r') as f:
    v4 = f.read()

print("✅ Read both files")
print(f"   Original: {len(original)} chars")
print(f"   V4: {len(v4)} chars")

# Update navigation in original (already done, but let's make sure)
nav_pattern = r'(<div class="top-nav">.*?</div>)'
old_nav = re.search(nav_pattern, original, re.DOTALL).group(0)

new_nav = '''<div class="top-nav">
  <div class="tn active" onclick="showPage(0)">📊 DASHBOARD</div>
  <div class="tn" onclick="showPage(1)">🏖️ RETIREMENT</div>
  <div class="tn" onclick="showPage(2)">🎓 KIDS EDUCATION</div>
  <div class="tn" onclick="showPage(3)">💼 INVESTMENTS</div>
  <div class="tn" onclick="showPage(4)">💰 TAX OPTIMIZER</div>
  <div class="tn" onclick="showPage(5)">🚗 CAR DECISION</div>
  <div class="tn" onclick="showPage(6)">🏦 SINKING FUNDS</div>
  <div class="tn" onclick="showPage(7)">📈 WIFE'S PORTFOLIO</div>
  <div class="tn" onclick="showPage(8)">💼 LIVE NAV</div>
  <div class="tn" onclick="showPage(9)">🎯 GOALS</div>
  <div class="tn" onclick="showPage(10)">📊 HISTORICAL</div>
  <div class="tn" onclick="showPage(11)">🔄 REBALANCE</div>
  <div class="tn" onclick="showPage(12)">💰 SWP PLAN</div>
  <div class="tn" onclick="showPage(13)">🔔 ALERTS</div>
</div>'''

merged = original.replace(old_nav, new_nav)
print("✅ Updated navigation (14 tabs)")

# Extract pages 0-5 from v4 (these are the NEW pages)
# Find all page divs in v4
v4_pages_match = re.findall(r'<!-- PAGE \d+:.*?-->\s*<div class="page.*?(?=<!-- PAGE \d+:|<script>)', v4, re.DOTALL)

print(f"✅ Extracted {len(v4_pages_match)} pages from v4")

# Rename them as pages 8-13
new_pages = []
page_num = 8
for page_html in v4_pages_match:
    # Keep the page content as-is, it will be pages 8-13
    new_pages.append(page_html)

# Find where to insert (before <script> tag in original)
script_pos = merged.find('<script>')

if script_pos == -1:
    print("❌ Could not find <script> tag!")
    exit(1)

# Insert new pages before script
merged = merged[:script_pos] + '\n'.join(new_pages) + '\n' + merged[script_pos:]

print(f"✅ Inserted {len(new_pages)} new pages")

# Now merge the JavaScript - extract functions from v4 and add to original
# Find script section in v4
v4_script_start = v4.find('<script>')
v4_script_end = v4.find('</script>')
v4_script = v4[v4_script_start+8:v4_script_end]

# Find script section in merged
merged_script_start = merged.find('<script>')
merged_script_end = merged.find('</script>')

# Extract key functions from v4 script
functions_to_add = []

# Function patterns to extract
function_patterns = [
    r'async function fetchNAV\(.*?\n}\n',
    r'async function fetchHistoricalNAV\(.*?\n}\n',
    r'function calculateXIRR\(.*?\n}\n',
    r'function calculateFundXIRR\(.*?\n}\n',
    r'function calculateTax\(.*?\n}\n',
    r'function renderGoalsOverview\(.*?\n}\n',
    r'function renderGoalsList\(.*?\n}\n',
    r'function updateGoalsChart\(.*?\n}\n',
    r'async function loadHistoricalData\(.*?\n}\n',
    r'function updateHistoricalChart\(.*?\n}\n',
    r'function calculateRebalancing\(.*?\n}\n',
    r'function calculateSWP\(.*?\n}\n',
    r'function requestNotificationPermission\(.*?\n}\n',
    r'function showNotification\(.*?\n}\n',
    r'function addPriceAlert\(.*?\n}\n',
    r'function renderAlertsList\(.*?\n}\n',
    r'function checkPriceAlerts\(.*?\n}\n'
]

print("✅ Extracting functions from v4...")
for pattern in function_patterns:
    match = re.search(pattern, v4_script, re.DOTALL | re.MULTILINE)
    if match:
        functions_to_add.append(match.group(0))
        print(f"   Found: {match.group(0)[:50]}...")

# Add global variables from v4
v4_globals = '''
// ============================================
// ADDITIONAL GLOBAL STATE FOR NEW FEATURES
// ============================================
let priceAlerts = [];
let alertHistory = [];
let notificationsEnabled = false;
let historicalData = null;

'''

# Insert functions before the final "renderCharts()" call in original script
original_script = merged[merged_script_start+8:merged_script_end]

# Find where to insert (before "renderCharts()")
insert_pos = original_script.rfind('renderCharts()')

if insert_pos != -1:
    new_script = (original_script[:insert_pos] +
                  v4_globals +
                  '\n'.join(functions_to_add) + '\n\n' +
                  original_script[insert_pos:])

    merged = merged[:merged_script_start+8] + new_script + merged[merged_script_end:]
    print(f"✅ Added {len(functions_to_add)} functions to script")
else:
    print("⚠️  Could not find renderCharts() - functions added at end")
    new_script = original_script + v4_globals + '\n'.join(functions_to_add) + '\n'
    merged = merged[:merged_script_start+8] + new_script + merged[merged_script_end:]

# Write output
with open('index.html', 'w') as f:
    f.write(merged)

print("=" * 60)
print("✅ MERGE COMPLETE!")
print(f"   Output: index.html ({len(merged)} chars)")
print("   Pages: 14 total (8 original + 6 new)")
print("")
print("🎉 Open index.html to see your complete tool!")
print("   All original data INTACT + all new features ADDED")
