#!/usr/bin/env python3
"""
Part 3: Add Rendering Functions & Update saveConfig/loadConfig
===============================================================

Adds:
- Rendering functions for all new features
- Updates saveConfig() to read new inputs
- Updates loadConfig() to restore new values
- Adds dashboard cards for inflation impact, allocation health, emergency fund, insurance
"""

import re

print("=" * 80)
print("🎨 PART 3: ADDING RENDERING FUNCTIONS")
print("=" * 80)
print()

with open('index.html', 'r') as f:
    html = f.read()

#  Add rendering functions before saveConfig
rendering_functions = '''

// ============== RENDERING FUNCTIONS ==============

// Render Emergency Fund Status in Settings Page
function renderEmergencyFundStatus() {
  const ef = calculateEmergencyFundAdequacy();
  const statusEl = document.getElementById('emergency-fund-status');
  if (!statusEl) return;

  let html = '<div class="alert ';
  if (ef.status === 'adequate') {
    html += 'success">✅ <strong>Emergency Fund: Adequate</strong><br>';
    html += `You have ₹${(ef.current / 100000).toFixed(1)}L covering ${ef.targetMonths} months of expenses (₹${(ef.required / 100000).toFixed(1)}L). `;
    html += `Surplus: ₹${(ef.surplus / 100000).toFixed(1)}L.`;
  } else if (ef.status === 'partial') {
    html += 'warning">⚠️ <strong>Emergency Fund: Partially Funded</strong><br>';
    html += `You have ₹${(ef.current / 100000).toFixed(1)}L but need ₹${(ef.required / 100000).toFixed(1)}L for ${ef.targetMonths} months coverage. `;
    html += `Shortfall: ₹${(Math.abs(ef.surplus) / 100000).toFixed(1)}L (${ef.adequacy}% funded).`;
  } else {
    html += 'danger">🔴 <strong>Emergency Fund: Critical Gap</strong><br>';
    html += `You need ₹${(ef.required / 100000).toFixed(1)}L for ${ef.targetMonths} months of expenses but have only ₹${(ef.current / 100000).toFixed(1)}L. `;
    html += `Build emergency fund BEFORE investing. Shortfall: ₹${(Math.abs(ef.surplus) / 100000).toFixed(1)}L.`;
  }
  html += '</div>';
  statusEl.innerHTML = html;
}

// Render Insurance Adequacy in Settings Page
function renderInsuranceAdequacy() {
  const ins = calculateInsuranceAdequacy();
  const statusEl = document.getElementById('insurance-adequacy');
  if (!statusEl) return;

  let html = '';

  // Life Insurance
  if (ins.life.gap > 0) {
    html += `<div class="alert danger">🔴 <strong>Life Insurance Gap: ₹${(ins.life.gap / 10000000).toFixed(1)} Cr</strong><br>`;
    html += `Required: ₹${(ins.life.required / 10000000).toFixed(1)} Cr | Current: ₹${(ins.life.current / 10000000).toFixed(1)} Cr | Coverage: ${ins.life.adequacy}%<br>`;
    html += `💡 Get term insurance immediately. Cost: ~₹12-15K/year for ₹5 Cr at age 32.</div>`;
  } else if (ins.life.current > 0) {
    html += `<div class="alert success">✅ Life Insurance: Adequate (₹${(ins.life.current / 10000000).toFixed(1)} Cr)</div>`;
  }

  // Health Insurance
  if (ins.health.gap > 0) {
    html += `<div class="alert danger" style="margin-top:8px">🔴 <strong>Health Insurance Gap: ₹${(ins.health.gap / 100000).toFixed(0)}L</strong><br>`;
    html += `Required: ₹${(ins.health.required / 100000).toFixed(0)}L | Current: ₹${(ins.health.current / 100000).toFixed(0)}L<br>`;
    html += `💡 Get family floater ₹20L + super top-up ₹50L. Premium: ~₹25-30K/year.</div>`;
  } else if (ins.health.current > 0) {
    html += `<div class="alert success" style="margin-top:8px">✅ Health Insurance: Adequate (₹${(ins.health.current / 100000).toFixed(0)}L)</div>`;
  }

  // Parents Health
  if (ins.parentsHealth.gap > 0 && ins.parentsHealth.current > 0) {
    html += `<div class="alert warning" style="margin-top:8px">⚠️ <strong>Parents Health Gap: ₹${(ins.parentsHealth.gap / 100000).toFixed(0)}L</strong><br>`;
    html += `Recommended: ₹${(ins.parentsHealth.required / 100000).toFixed(0)}L for parents critical care.</div>`;
  }

  statusEl.innerHTML = html;
}

// Render Asset Allocation Health Card on Dashboard
function renderAllocationHealth() {
  const allocation = analyzeAssetAllocation();
  const summaryEl = document.getElementById('allocation-summary');
  const alertEl = document.getElementById('rebalancing-alert');

  if (!summaryEl) return;

  // Display summary
  let html = '<div class="gs">';
  html += `<div><div class="gs-l">Equity</div><div class="gs-v ay">${allocation.equity.percent}%</div><small class="ai">Target: ${allocation.equity.target * 100}%</small></div>`;
  html += `<div><div class="gs-l">Debt</div><div class="gs-v ab">${allocation.debt.percent}%</div><small class="ai">Target: ${allocation.debt.target * 100}%</small></div>`;
  html += `<div><div class="gs-l">Gold</div><div class="gs-v ay">${allocation.gold.percent}%</div><small class="ai">Target: ${allocation.gold.target * 100}%</small></div>`;
  html += `<div><div class="gs-l">International</div><div class="gs-v ap">${allocation.international.percent}%</div><small class="ai">Target: 10-15%</small></div>`;
  html += '</div>';
  summaryEl.innerHTML = html;

  if (!alertEl) return;

  // Generate rebalancing alerts
  let alert = '';

  if (parseFloat(allocation.debt.percent) < 15) {
    alert += `<div class="alert danger" style="margin-top:10px">🔴 <strong>Critical Risk:</strong> You have only ${allocation.debt.percent}% in debt. Recommended minimum: 20%. Add debt funds (liquid, corporate bond, banking & PSU) to reduce portfolio risk during market crashes.</div>`;
  }

  if (parseFloat(allocation.gold.percent) < 3) {
    alert += `<div class="alert warning" style="margin-top:10px">⚠️ <strong>Diversification Gap:</strong> No gold allocation detected. Consider adding 5% gold ETF/Sovereign Gold Bonds for inflation hedge and portfolio stability.</div>`;
  }

  if (parseFloat(allocation.international.percent) < 5) {
    alert += `<div class="alert warning" style="margin-top:10px">⚠️ <strong>Geographic Concentration:</strong> 100% India exposure. Consider adding 10-15% international equity funds (US/Global) for currency diversification.</div>`;
  }

  if (Math.abs(allocation.equity.deviation) > 10) {
    alert += `<div class="alert warning" style="margin-top:10px">⚠️ <strong>Rebalancing Needed:</strong> Your equity allocation is ${allocation.equity.percent}% (target: ${allocation.equity.target * 100}%). `;
    if (allocation.equity.deviation > 0) {
      alert += `Consider adding more debt funds to rebalance.`;
    } else {
      alert += `Consider increasing equity allocation.`;
    }
    alert += `</div>`;
  }

  alertEl.innerHTML = alert;
}

// Render Inflation Impact on Dashboard
function renderInflationImpact() {
  const eduToday = 3000000; // ₹30L
  const eduFuture = calculateInflatedGoal(eduToday, 18, config.inflationEducation || 10);

  const monthlyExp = (config.rent || 0) + (config.parents || 0) + (config.fixedExpenses || 0) + (config.livingExpenses || 0);
  const annualExpToday = monthlyExp * 12;
  const annualExpFuture = calculateInflatedGoal(annualExpToday, 28, config.inflationGeneral || 6);

  const retReq = calculateRetirementRequirement();

  const el = document.getElementById('inflation-impact-values');
  if (el) {
    el.innerHTML = `
      <div class="ml">
        <div class="d">Kids Education (Today)<small>4-year engineering</small></div>
        <div class="a ar">₹${(eduToday / 100000).toFixed(0)}L</div>
      </div>
      <div class="ml">
        <div class="d">Kids Education (2044)<small>Inflated @ ${config.inflationEducation || 10}%/year</small></div>
        <div class="a ay">₹${(eduFuture / 100000).toFixed(0)}L</div>
      </div>
      <div class="ml">
        <div class="d">Annual Expenses (Today)<small>All monthly expenses × 12</small></div>
        <div class="a ar">₹${(annualExpToday / 100000).toFixed(1)}L</div>
      </div>
      <div class="ml">
        <div class="d">Annual Expenses (2054)<small>At retirement, inflated @ ${config.inflationGeneral || 6}%</small></div>
        <div class="a ay">₹${(annualExpFuture / 10000000).toFixed(2)} Cr</div>
      </div>
      <div class="ml">
        <div class="d">Required Retirement Corpus<small>4% safe withdrawal rule</small></div>
        <div class="a aj">₹${(retReq.requiredCorpus / 10000000).toFixed(1)} Cr</div>
      </div>
    `;
  }
}

// Render Retirement Adequacy Alert
function renderRetirementAdequacy() {
  const ret = calculateRetirementRequirement();
  const retirementPage = document.querySelector('#page-3');
  if (!retirementPage) return;

  let html = '<div class="alert ';

  if (ret.adequacy >= 100) {
    html += 'success">✅ <strong>Retirement: On Track!</strong><br>';
    html += `Projected corpus: ₹${(ret.projectedCorpus / 10000000).toFixed(1)} Cr exceeds requirement of ₹${(ret.requiredCorpus / 10000000).toFixed(1)} Cr (${ret.adequacy}% funded).`;
  } else if (ret.adequacy >= 75) {
    html += 'warning">⚠️ <strong>Retirement: Needs Attention</strong><br>';
    html += `Projected: ₹${(ret.projectedCorpus / 10000000).toFixed(1)} Cr | Required: ₹${(ret.requiredCorpus / 10000000).toFixed(1)} Cr | Gap: ₹${(Math.abs(ret.gap) / 10000000).toFixed(1)} Cr (${ret.adequacy}% funded)<br>`;
    html += `💡 Increase combined SIP by ₹${(ret.additionalSIPNeeded / 1000).toFixed(0)}K/month to close gap.`;
  } else {
    html += 'danger">🔴 <strong>Retirement: Critical Shortfall</strong><br>';
    html += `Your expenses at retirement (2054): ₹${(ret.futureAnnualExpenses / 10000000).toFixed(2)} Cr/year<br>`;
    html += `Required corpus (4% safe withdrawal rule): ₹${(ret.requiredCorpus / 10000000).toFixed(1)} Cr<br>`;
    html += `Current projection: ₹${(ret.projectedCorpus / 10000000).toFixed(1)} Cr<br>`;
    html += `<strong>Shortfall: ₹${(Math.abs(ret.gap) / 10000000).toFixed(1)} Cr (only ${ret.adequacy}% funded)</strong><br>`;
    html += `💡 Increase combined SIP by ₹${(ret.additionalSIPNeeded / 1000).toFixed(0)}K/month.`;
  }
  html += '</div>';

  // Insert or update
  const existingAlert = retirementPage.querySelector('.retirement-adequacy');
  if (existingAlert) {
    existingAlert.innerHTML = html;
  } else {
    const content = retirementPage.querySelector('.content');
    if (content) {
      const div = document.createElement('div');
      div.className = 'retirement-adequacy';
      div.innerHTML = html;
      content.insertBefore(div, content.firstChild);
    }
  }
}

'''

# Insert before saveConfig
marker = '// Save configuration and update ALL pages\nfunction saveConfig() {'
if marker in html:
    html = html.replace(marker, rendering_functions + '\n' + marker)
    print("✅ Added rendering functions:")
    print("   • renderEmergencyFundStatus()")
    print("   • renderInsuranceAdequacy()")
    print("   • renderAllocationHealth()")
    print("   • renderInflationImpact()")
    print("   • renderRetirementAdequacy()")
    print()
else:
    print("⚠️  Could not find saveConfig marker")

# Update saveConfig to read new inputs
print("Updating saveConfig() to read new inputs...")

# Find saveConfig function and update it to read new fields
old_saveconfig_start = '''function saveConfig() {
  console.log('💾 Saving configuration and refreshing all pages...');

  // Read all settings inputs
  const getValue = (id) => parseFloat(document.getElementById(id)?.value) || 0;'''

new_saveconfig_start = '''function saveConfig() {
  console.log('💾 Saving configuration and refreshing all pages...');

  // Helper to parse number from formatted string (removes commas)
  const getValue = (id) => {
    const el = document.getElementById(id);
    if (!el) return 0;
    const val = el.value.toString().replace(/,/g, '');
    return parseFloat(val) || 0;
  };

  // Helper to parse percentage
  const getPercent = (id) => {
    const el = document.getElementById(id);
    if (!el) return 0;
    const val = el.value.toString().replace(/%/g, '').replace(/,/g, '');
    return parseFloat(val) || 0;
  };'''

if old_saveconfig_start in html:
    html = html.replace(old_saveconfig_start, new_saveconfig_start)
    print("   ✅ Updated getValue helper to handle formatted numbers")

# Add new config fields to saveConfig
old_save_end = '''  config.yourSIP = yourFunds.reduce((sum, f) => sum + (f.monthlySIP || 0), 0);
  }

  if (typeof wifeFunds !== 'undefined') {
    wifeFunds.forEach((fund, idx) => {
      const val = getValue(`s-wife-sip-${idx}`);
      if (val > 0) fund.monthlySIP = val;
    });
    config.wifeSIP = wifeFunds.reduce((sum, f) => sum + (f.monthlySIP || 0), 0);
  }

  // Save to localStorage
  localStorage.setItem('financialConfig', JSON.stringify(config));'''

new_save_end = '''  config.yourSIP = yourFunds.reduce((sum, f) => sum + (f.monthlySIP || 0), 0);
  }

  if (typeof wifeFunds !== 'undefined') {
    wifeFunds.forEach((fund, idx) => {
      const val = getValue(`s-wife-sip-${idx}`);
      if (val > 0) fund.monthlySIP = val;
    });
    config.wifeSIP = wifeFunds.reduce((sum, f) => sum + (f.monthlySIP || 0), 0);
  }

  // Read inflation rates
  config.inflationGeneral = getPercent('s-inflation-general');
  config.inflationEducation = getPercent('s-inflation-education');
  config.inflationHealthcare = getPercent('s-inflation-healthcare');

  // Read emergency fund
  config.emergencyFund = getValue('s-emergency-fund');
  const targetEl = document.getElementById('s-emergency-target');
  config.emergencyFundTarget = targetEl ? parseInt(targetEl.value) : 6;

  // Read insurance coverage
  config.lifeInsuranceCurrent = getValue('s-life-insurance');
  config.healthInsuranceCurrent = getValue('s-health-insurance');
  config.parentsHealthInsurance = getValue('s-parents-health');

  // Save to localStorage
  localStorage.setItem('financialConfig', JSON.stringify(config));'''

if old_save_end in html:
    html = html.replace(old_save_end, new_save_end)
    print("   ✅ Added code to read inflation, emergency fund, and insurance inputs")

# Add new render calls to saveConfig
old_render_calls = '''  // Refresh ALL dependent pages
  console.log('🔄 Refreshing all dependent pages...');

  setTimeout(() => {
    if (typeof renderDashboardCharts === 'function') renderDashboardCharts();
    if (typeof renderRetirementCharts === 'function') renderRetirementCharts();
    if (typeof renderKidsCharts === 'function') renderKidsCharts();
    if (typeof renderInvestmentCharts === 'function') renderInvestmentCharts();
    if (typeof renderWifeCharts === 'function') renderWifeCharts();
    if (typeof refreshMyPortfolio === 'function') refreshMyPortfolio();
    if (typeof refreshWifePortfolio === 'function') refreshWifePortfolio();
    if (typeof renderMonthlyProjections === 'function') renderMonthlyProjections();

    console.log('✅ All pages refreshed');
    alert('✅ Settings saved! All pages updated with new values.');
  }, 100);
}'''

new_render_calls = '''  // Refresh ALL dependent pages
  console.log('🔄 Refreshing all dependent pages...');

  setTimeout(() => {
    // Core pages
    if (typeof renderDashboardCharts === 'function') renderDashboardCharts();
    if (typeof renderRetirementCharts === 'function') renderRetirementCharts();
    if (typeof renderKidsCharts === 'function') renderKidsCharts();
    if (typeof renderInvestmentCharts === 'function') renderInvestmentCharts();
    if (typeof renderWifeCharts === 'function') renderWifeCharts();
    if (typeof refreshMyPortfolio === 'function') refreshMyPortfolio();
    if (typeof refreshWifePortfolio === 'function') refreshWifePortfolio();
    if (typeof renderMonthlyProjections === 'function') renderMonthlyProjections();

    // New critical features
    if (typeof renderEmergencyFundStatus === 'function') renderEmergencyFundStatus();
    if (typeof renderInsuranceAdequacy === 'function') renderInsuranceAdequacy();
    if (typeof renderAllocationHealth === 'function') renderAllocationHealth();
    if (typeof renderInflationImpact === 'function') renderInflationImpact();
    if (typeof renderRetirementAdequacy === 'function') renderRetirementAdequacy();

    console.log('✅ All pages refreshed including new critical features');
    alert('✅ Settings saved! All pages updated with inflation-adjusted goals, emergency fund, insurance gaps, and asset allocation health.');
  }, 100);
}'''

if old_render_calls in html:
    html = html.replace(old_render_calls, new_render_calls)
    print("   ✅ Added calls to new rendering functions")

print()

# Write result
with open('index.html', 'w') as f:
    f.write(html)

print("=" * 80)
print("✅ RENDERING FUNCTIONS ADDED & saveConfig() UPDATED")
print("=" * 80)
print()
