#!/usr/bin/env python3
"""
Debug and fix SIP allocation table not showing
"""

print("🔧 Debugging SIP allocation table...")

with open('index.html', 'r') as f:
    html = f.read()

# Add console logging and ensure function runs after DOM is ready
old_render_sip = '''function renderSIPAllocations() {
  const table = document.getElementById('sipAllocationTable');
  if (!table) return;

  table.innerHTML = '';
  let totalSIP = 0;

  myFunds.forEach((fund, idx) => {'''

new_render_sip = '''function renderSIPAllocations() {
  console.log('renderSIPAllocations called, myFunds length:', myFunds.length);
  const table = document.getElementById('sipAllocationTable');
  if (!table) {
    console.error('sipAllocationTable not found!');
    return;
  }

  console.log('Table found, populating with', myFunds.length, 'funds');
  table.innerHTML = '';
  let totalSIP = 0;

  myFunds.forEach((fund, idx) => {
    console.log('Adding fund:', fund.name, 'SIP:', fund.monthlySIP);'''

html = html.replace(old_render_sip, new_render_sip)

# Also ensure the initialization happens after everything is loaded
old_init_call = '''window.addEventListener('DOMContentLoaded', function() {
  loadConfig();
  loadSIPAllocations();
  renderSIPAllocations();
  refreshMyPortfolio();
  populateAlertFunds();'''

new_init_call = '''window.addEventListener('DOMContentLoaded', function() {
  console.log('DOM Content Loaded - Initializing...');
  loadConfig();
  loadSIPAllocations();

  // Delay SIP rendering slightly to ensure table exists
  setTimeout(() => {
    console.log('Attempting to render SIP allocations...');
    renderSIPAllocations();
  }, 100);

  refreshMyPortfolio();
  populateAlertFunds();'''

html = html.replace(old_init_call, new_init_call)

# Add a manual trigger button for debugging
manual_trigger = '''
    <div style="margin:15px 0;text-align:center">
      <button onclick="renderSIPAllocations()" class="btn btn-primary" style="padding:8px 20px;margin-right:10px">🔄 REFRESH TABLE</button>
      <button onclick="saveSIPAllocations()" class="btn btn-primary" style="padding:10px 30px">💾 SAVE SIP ALLOCATIONS</button>'''

html = html.replace(
    '<button onclick="saveSIPAllocations()" class="btn btn-primary" style="padding:10px 30px">💾 SAVE SIP ALLOCATIONS</button>',
    manual_trigger
)

print("✅ Added debug logging and refresh button")

# Write output
with open('index.html', 'w') as f:
    f.write(html)

print("=" * 60)
print("✅ DEBUG VERSION CREATED!")
print("")
print("🔍 TO DEBUG:")
print("   1. Open index.html in browser")
print("   2. Go to MY PORTFOLIO tab")
print("   3. Press F12 to open browser console")
print("   4. Click the 'REFRESH TABLE' button")
print("   5. Check console for errors/logs")
print("")
print("   If table still empty, send me the console output!")
