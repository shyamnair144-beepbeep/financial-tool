#!/usr/bin/env python3
"""
Comprehensive verification of the entire financial tool
Focus on:
1. Navigation structure
2. Investment start date (April 2026)
3. JavaScript functions
4. Data integrity
"""

import re
from datetime import datetime

with open('index.html', 'r') as f:
    html = f.read()

print("=" * 70)
print("COMPREHENSIVE VERIFICATION")
print("=" * 70)

errors = []
warnings = []
successes = []

# 1. NAVIGATION CHECK
print("\n📋 1. NAVIGATION STRUCTURE")
nav_tabs = re.findall(r'onclick="showPage\((\d+)\)">([^<]+)</div>', html)
print(f"   Total tabs found: {len(nav_tabs)}")

expected_tabs = [
    (0, 'Dashboard'),
    (1, 'Settings'),
    (2, 'My Portfolio'),
    (3, 'Retirement'),
    (4, 'Kids Education'),
    (5, 'Investments'),
    (6, 'Tax Optimizer'),
    (7, 'Car Decision'),
    (8, 'Sinking Funds'),
    (9, "Wife's Portfolio"),
    (10, 'Historical'),
    (11, 'Monthly Projections'),
    (12, 'Alerts')
]

for expected_num, expected_name in expected_tabs:
    found = any(int(num) == expected_num and expected_name.lower() in name.lower() 
                for num, name in nav_tabs)
    page_exists = f'id="page-{expected_num}"' in html
    
    if found and page_exists:
        successes.append(f"Tab {expected_num}: {expected_name}")
    elif found and not page_exists:
        errors.append(f"Tab {expected_num}: Navigation exists but page div missing")
    elif not found:
        errors.append(f"Tab {expected_num}: {expected_name} - Navigation missing")

# 2. INVESTMENT START DATE CHECK
print("\n📅 2. INVESTMENT START DATE VERIFICATION")

# Check for April 2026 references
april_2026_refs = re.findall(r"['\"]2026-04['\"]", html)
print(f"   Found {len(april_2026_refs)} references to '2026-04'")

# Check specific functions
start_date_patterns = [
    (r"new Date\(['\"]2026-04-01['\"]", "April 2026 start date"),
    (r"startDate.*2026-04", "Start date variable"),
]

for pattern, desc in start_date_patterns:
    matches = re.findall(pattern, html, re.IGNORECASE)
    if matches:
        successes.append(f"Start date: {desc} found ({len(matches)} times)")
    else:
        warnings.append(f"Start date: {desc} not found")

# Check if there are any current date references that might override
current_date_refs = re.findall(r"new Date\(\)", html)
print(f"   Found {len(current_date_refs)} 'new Date()' calls (should handle April 2026 start)")

# 3. FUND DATA CHECK
print("\n💰 3. FUND DATA VERIFICATION")

# Your funds
your_funds_section = re.search(r'const yourFunds\s*=\s*\[(.*?)\];', html, re.DOTALL)
if your_funds_section:
    your_funds_data = your_funds_section.group(1)
    your_funds_count = len(re.findall(r'\{[^}]*name:', your_funds_data))
    print(f"   Your funds: {your_funds_count} funds defined")
    
    if your_funds_count == 8:
        successes.append("Your portfolio: 8 funds correctly defined")
    else:
        errors.append(f"Your portfolio: Expected 8 funds, found {your_funds_count}")
else:
    errors.append("Your portfolio: yourFunds array not found")

# Wife's funds
wife_funds_section = re.search(r'const wifeFunds\s*=\s*\[(.*?)\];', html, re.DOTALL)
if wife_funds_section:
    wife_funds_data = wife_funds_section.group(1)
    wife_funds_count = len(re.findall(r'\{[^}]*name:', wife_funds_data))
    print(f"   Wife's funds: {wife_funds_count} funds defined")
    
    if wife_funds_count == 2:
        successes.append("Wife's portfolio: 2 funds correctly defined")
    else:
        errors.append(f"Wife's portfolio: Expected 2 funds, found {wife_funds_count}")
else:
    errors.append("Wife's portfolio: wifeFunds array not found")

# 4. CRITICAL FUNCTIONS CHECK
print("\n⚙️  4. CRITICAL FUNCTIONS")

critical_functions = [
    'showPage',
    'saveConfig',
    'calculateCarOptions',
    'renderMonthlyProjections',
    'fetchNAV',
    'calculateMonthlyProjection',
    'calculateXIRR',
    'calculateTax'
]

for func in critical_functions:
    if f'function {func}' in html or f'async function {func}' in html:
        successes.append(f"Function: {func}()")
    else:
        errors.append(f"Function: {func}() MISSING")

# 5. MONTHLY PROJECTIONS SPECIFIC CHECKS
print("\n📊 5. MONTHLY PROJECTIONS FEATURE")

mp_elements = [
    ('yourFundCards', 'Your fund cards container'),
    ('yourMasterChart', 'Your master chart'),
    ('yourMonthlyTableBody', 'Your monthly table'),
    ('wifeFundCards', 'Wife fund cards container'),
    ('wifeMasterChart', 'Wife master chart'),
    ('wifeMonthlyTableBody', 'Wife monthly table'),
]

for elem_id, desc in mp_elements:
    if f'id="{elem_id}"' in html:
        successes.append(f"Monthly Projections: {desc}")
    else:
        errors.append(f"Monthly Projections: {desc} MISSING")

# 6. JAVASCRIPT SYNTAX CHECK
print("\n🔍 6. JAVASCRIPT QUALITY")

script_match = html.match(r'<script>(.*?)</script>', re.DOTALL)
if script_match:
    js_code = script_match.group(1)
    
    # Count braces
    open_braces = js_code.count('{')
    close_braces = js_code.count('}')
    
    if open_braces == close_braces:
        successes.append(f"JavaScript: Braces balanced ({open_braces} pairs)")
    else:
        errors.append(f"JavaScript: Brace mismatch ({open_braces} open, {close_braces} close)")
    
    # Check for common errors
    if '$ {' in js_code:
        warnings.append("JavaScript: Found '$ {' spacing (should be '${' for template literals)")
    
    js_lines = js_code.split('\n')
    js_size_kb = len(js_code) / 1024
    
    print(f"   JavaScript size: {js_size_kb:.1f} KB")
    print(f"   JavaScript lines: {len(js_lines)}")

# 7. CHART.JS CHECK
print("\n📈 7. CHART.JS INTEGRATION")

if 'Chart.js' in html or 'chart.js' in html.lower():
    successes.append("Chart.js: Library included")
else:
    errors.append("Chart.js: Library NOT included")

# Check for chart rendering
chart_renders = re.findall(r'new Chart\(', html)
print(f"   Chart instances: {len(chart_renders)} charts created")

# SUMMARY
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print(f"\n✅ SUCCESSES: {len(successes)}")
for s in successes[:10]:  # Show first 10
    print(f"   • {s}")
if len(successes) > 10:
    print(f"   ... and {len(successes) - 10} more")

if warnings:
    print(f"\n⚠️  WARNINGS: {len(warnings)}")
    for w in warnings:
        print(f"   • {w}")

if errors:
    print(f"\n❌ ERRORS: {len(errors)}")
    for e in errors:
        print(f"   • {e}")
else:
    print("\n✨ NO CRITICAL ERRORS FOUND")

# FINAL VERDICT
total_checks = len(successes) + len(warnings) + len(errors)
success_rate = (len(successes) / total_checks * 100) if total_checks > 0 else 0

print("\n" + "=" * 70)
print(f"QUALITY SCORE: {len(successes)}/{total_checks} ({success_rate:.0f}%)")

if errors:
    print("⚠️  STATUS: NEEDS FIXES")
elif warnings:
    print("⚠️  STATUS: GOOD (minor warnings)")
else:
    print("✅ STATUS: EXCELLENT - PRODUCTION READY")

print("=" * 70)

