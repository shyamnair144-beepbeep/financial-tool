#!/usr/bin/env python3
"""Analyze current HTML structure professionally"""

with open('index.html', 'r') as f:
    html = f.read()

print("=" * 70)
print("CURRENT HTML STRUCTURE ANALYSIS")
print("=" * 70)

# Find all pages
import re
pages_found = []
for match in re.finditer(r'<div class="page(?: active)?">', html):
    start = match.start()
    # Find the h1 or h2 after this
    snippet = html[start:start+500]
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', snippet)
    h2_match = re.search(r'<h2[^>]*>(.*?)</h2>', snippet)
    title = (h1_match.group(1) if h1_match else h2_match.group(1) if h2_match else "Unknown").strip()
    # Clean HTML tags
    title = re.sub(r'<[^>]+>', '', title)
    pages_found.append(title[:60])

print(f"\n📄 PAGES FOUND: {len(pages_found)}")
for i, page in enumerate(pages_found):
    print(f"   Page {i}: {page}")

# Find navigation tabs
nav_matches = list(re.finditer(r'onclick="showPage\((\d+)\)"[^>]*>([^<]+)</div>', html))
print(f"\n🔗 NAVIGATION TABS: {len(nav_matches)}")
for match in nav_matches:
    page_num = match.group(1)
    tab_name = match.group(2).strip()
    print(f"   Tab {page_num}: {tab_name}")

# Find JavaScript functions
functions = re.findall(r'function\s+(\w+)\s*\(', html)
print(f"\n⚙️  JAVASCRIPT FUNCTIONS: {len(functions)}")
for func in sorted(set(functions))[:20]:
    print(f"   • {func}()")
if len(set(functions)) > 20:
    print(f"   ... and {len(set(functions)) - 20} more")

# Check for key elements
key_elements = [
    ('sipTotal', 'SIP Total display'),
    ('sipAllocationTable', 'SIP Allocation Table'),
    ('myFunds', 'My Funds data'),
    ('wifeFunds', 'Wife Funds data'),
    ('carExShowroom', 'Car price input'),
    ('cfg_annualCTC', 'Annual CTC setting'),
]

print(f"\n🔍 KEY ELEMENTS CHECK:")
for elem_id, desc in key_elements:
    exists = elem_id in html
    status = "✅" if exists else "❌"
    print(f"   {status} {desc} ({elem_id})")

print("\n" + "=" * 70)
print(f"FILE SIZE: {len(html):,} characters, {html.count(chr(10)):,} lines")
print("=" * 70)
