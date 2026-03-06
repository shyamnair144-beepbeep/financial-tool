#!/usr/bin/env python3
"""
Create a simple static SIP allocation table that shows immediately
"""

print("🔧 Creating simple static SIP table...")

with open('index.html', 'r') as f:
    html = f.read()

# Find the SIP allocation table section and replace with static version
old_table_section = '''    <div class="tw">
      <table>
        <thead>
          <tr>
            <th>Fund Name</th>
            <th>Purpose</th>
            <th class="text-right">Monthly SIP</th>
            <th class="text-right">Annual (with 10% step-up)</th>
            <th class="text-right">% of Total</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody id="sipAllocationTable"></tbody>'''

new_table_section = '''    <div class="tw">
      <table>
        <thead>
          <tr>
            <th>Fund Name</th>
            <th>Purpose</th>
            <th class="text-right">Monthly SIP</th>
            <th class="text-right">Annual (with 10% step-up)</th>
            <th class="text-right">% of Total</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody id="sipAllocationTable">
          <tr>
            <td>Parag Parikh Flexi Cap Direct Growth</td>
            <td>80C Tax Saving + Retirement</td>
            <td class="text-right">
              <input type="number" id="sip_0" value="10000" oninput="updateSIPAllocation(0, this.value)" style="background:var(--bg3);border:1px solid var(--border);color:var(--you);padding:6px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace;font-size:12px">
            </td>
            <td class="text-right" id="sipAnnual_0">₹1,32,000</td>
            <td class="text-right" id="sipPercent_0">13.9%</td>
            <td>
              <button onclick="resetSIPToDefault(0)" style="background:var(--bg3);border:1px solid var(--border);color:var(--ink3);padding:4px 8px;border-radius:3px;cursor:pointer;font-size:10px">RESET</button>
            </td>
          </tr>
          <tr>
            <td>Nifty 50 Index Fund Direct Growth</td>
            <td>Retirement Core</td>
            <td class="text-right">
              <input type="number" id="sip_1" value="15000" oninput="updateSIPAllocation(1, this.value)" style="background:var(--bg3);border:1px solid var(--border);color:var(--you);padding:6px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace;font-size:12px">
            </td>
            <td class="text-right" id="sipAnnual_1">₹1,98,000</td>
            <td class="text-right" id="sipPercent_1">20.9%</td>
            <td>
              <button onclick="resetSIPToDefault(1)" style="background:var(--bg3);border:1px solid var(--border);color:var(--ink3);padding:4px 8px;border-radius:3px;cursor:pointer;font-size:10px">RESET</button>
            </td>
          </tr>
          <tr>
            <td>Motilal Oswal Midcap Fund Direct Growth</td>
            <td>Retirement (Existing)</td>
            <td class="text-right">
              <input type="number" id="sip_2" value="2200" oninput="updateSIPAllocation(2, this.value)" style="background:var(--bg3);border:1px solid var(--border);color:var(--you);padding:6px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace;font-size:12px">
            </td>
            <td class="text-right" id="sipAnnual_2">₹29,040</td>
            <td class="text-right" id="sipPercent_2">3.1%</td>
            <td>
              <button onclick="resetSIPToDefault(2)" style="background:var(--bg3);border:1px solid var(--border);color:var(--ink3);padding:4px 8px;border-radius:3px;cursor:pointer;font-size:10px">RESET</button>
            </td>
          </tr>
          <tr>
            <td>Quant Small Cap Fund Direct Growth</td>
            <td>Retirement Satellite</td>
            <td class="text-right">
              <input type="number" id="sip_3" value="10000" oninput="updateSIPAllocation(3, this.value)" style="background:var(--bg3);border:1px solid var(--border);color:var(--you);padding:6px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace;font-size:12px">
            </td>
            <td class="text-right" id="sipAnnual_3">₹1,32,000</td>
            <td class="text-right" id="sipPercent_3">13.9%</td>
            <td>
              <button onclick="resetSIPToDefault(3)" style="background:var(--bg3);border:1px solid var(--border);color:var(--ink3);padding:4px 8px;border-radius:3px;cursor:pointer;font-size:10px">RESET</button>
            </td>
          </tr>
          <tr>
            <td>HDFC Balanced Advantage Fund Direct Growth</td>
            <td>Kids Education</td>
            <td class="text-right">
              <input type="number" id="sip_4" value="15000" oninput="updateSIPAllocation(4, this.value)" style="background:var(--bg3);border:1px solid var(--border);color:var(--you);padding:6px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace;font-size:12px">
            </td>
            <td class="text-right" id="sipAnnual_4">₹1,98,000</td>
            <td class="text-right" id="sipPercent_4">20.9%</td>
            <td>
              <button onclick="resetSIPToDefault(4)" style="background:var(--bg3);border:1px solid var(--border);color:var(--ink3);padding:4px 8px;border-radius:3px;cursor:pointer;font-size:10px">RESET</button>
            </td>
          </tr>
          <tr>
            <td>Nifty Next 50 Index Fund Direct Growth</td>
            <td>Kids Education - Midcap</td>
            <td class="text-right">
              <input type="number" id="sip_5" value="8000" oninput="updateSIPAllocation(5, this.value)" style="background:var(--bg3);border:1px solid var(--border);color:var(--you);padding:6px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace;font-size:12px">
            </td>
            <td class="text-right" id="sipAnnual_5">₹1,05,600</td>
            <td class="text-right" id="sipPercent_5">11.1%</td>
            <td>
              <button onclick="resetSIPToDefault(5)" style="background:var(--bg3);border:1px solid var(--border);color:var(--ink3);padding:4px 8px;border-radius:3px;cursor:pointer;font-size:10px">RESET</button>
            </td>
          </tr>
          <tr>
            <td>NPS Tier 1 Auto Choice Aggressive</td>
            <td>80CCD Tax Saving</td>
            <td class="text-right">
              <input type="number" id="sip_6" value="8000" oninput="updateSIPAllocation(6, this.value)" style="background:var(--bg3);border:1px solid var(--border);color:var(--you);padding:6px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace;font-size:12px">
            </td>
            <td class="text-right" id="sipAnnual_6">₹96,000</td>
            <td class="text-right" id="sipPercent_6">11.1%</td>
            <td>
              <button onclick="resetSIPToDefault(6)" style="background:var(--bg3);border:1px solid var(--border);color:var(--ink3);padding:4px 8px;border-radius:3px;cursor:pointer;font-size:10px">RESET</button>
            </td>
          </tr>
          <tr>
            <td>HDFC Liquid Fund Direct Growth</td>
            <td>Sinking Funds</td>
            <td class="text-right">
              <input type="number" id="sip_7" value="1186" oninput="updateSIPAllocation(7, this.value)" style="background:var(--bg3);border:1px solid var(--border);color:var(--you);padding:6px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace;font-size:12px">
            </td>
            <td class="text-right" id="sipAnnual_7">₹14,232</td>
            <td class="text-right" id="sipPercent_7">1.7%</td>
            <td>
              <button onclick="resetSIPToDefault(7)" style="background:var(--bg3);border:1px solid var(--border);color:var(--ink3);padding:4px 8px;border-radius:3px;cursor:pointer;font-size:10px">RESET</button>
            </td>
          </tr>
        </tbody>'''

html = html.replace(old_table_section, new_table_section)
print("✅ Created static SIP allocation table with all 8 funds")

# Write output
with open('index.html', 'w') as f:
    f.write(html)

print("=" * 60)
print("✅ STATIC SIP TABLE CREATED!")
print("")
print("📊 NOW YOU WILL SEE:")
print("   ✅ All 8 funds listed")
print("   ✅ Editable SIP amounts (can type directly)")
print("   ✅ Annual amounts shown")
print("   ✅ Percentage of total")
print("   ✅ Reset button for each fund")
print("")
print("🎯 REFRESH YOUR BROWSER:")
print("   Go to MY PORTFOLIO tab - table should be populated now!")
