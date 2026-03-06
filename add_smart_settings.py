#!/usr/bin/env python3
"""
Add smart auto-calculation and validation to Settings page
"""

print("🔧 Adding smart settings features...")

with open('index.html', 'r') as f:
    html = f.read()

# Find the existing config JS section and replace it with enhanced version
old_js_start = html.find('// ============================================\n// CONFIGURATION MANAGEMENT')
old_js_end = html.find('// ============================================\n// MY PORTFOLIO DATA')

if old_js_start == -1 or old_js_end == -1:
    print("❌ Could not find config section!")
    exit(1)

enhanced_config_js = '''// ============================================
// CONFIGURATION MANAGEMENT WITH AUTO-CALC
// ============================================

let config = {
  netPay: 213586,
  annualCTC: 3634036,
  salaryIncrement: 10,
  wifeGross: 70000,
  wifeContrib: 20000,
  wifeIncrement: 8,
  rent: 40000,
  parents: 25000,
  living: 49000,
  yourSIP: 71886,
  wifeSIP: 50000,
  stepUp: 10,
  wifeStepUp: 10,
  expectedReturns: 12,
  wifeReturns: 12,
  retireAge: 60,
  retireTarget: 10,
  carYear: 2026
};

function loadConfig() {
  const saved = localStorage.getItem('financialConfig');
  if (saved) {
    config = JSON.parse(saved);
    // Populate form fields
    Object.keys(config).forEach(key => {
      const el = document.getElementById('cfg_' + key);
      if (el) el.value = config[key];
    });
  }
  validateAndUpdate();
}

function saveConfig() {
  // Read all form values
  Object.keys(config).forEach(key => {
    const el = document.getElementById('cfg_' + key);
    if (el) config[key] = parseFloat(el.value);
  });

  // Validate
  if (!validateAndUpdate()) {
    return; // Don't save if validation fails
  }

  // Save to localStorage
  localStorage.setItem('financialConfig', JSON.stringify(config));

  // Show notification
  const notif = document.getElementById('saveNotif');
  if (notif) {
    notif.style.display = 'block';
    setTimeout(() => { notif.style.display = 'none'; }, 3000);
  }

  console.log('✅ Config saved:', config);
}

// Auto-calculation when monthly income changes
function updateAnnualCTC() {
  const netPay = parseFloat(document.getElementById('cfg_netPay').value) || 0;
  // Rough conversion: Net Pay ≈ 76.4% of CTC (based on original ratio)
  const estimatedCTC = Math.round(netPay * 12 / 0.764);
  document.getElementById('cfg_annualCTC').value = estimatedCTC;
  config.annualCTC = estimatedCTC;
  validateAndUpdate();
}

// Auto-calculation when annual CTC changes
function updateNetPay() {
  const annualCTC = parseFloat(document.getElementById('cfg_annualCTC').value) || 0;
  // Rough conversion: Net Pay ≈ 76.4% of CTC
  const estimatedNetPay = Math.round((annualCTC * 0.764) / 12);
  document.getElementById('cfg_netPay').value = estimatedNetPay;
  config.netPay = estimatedNetPay;
  validateAndUpdate();
}

// Validation and warnings
function validateAndUpdate() {
  const netPay = parseFloat(document.getElementById('cfg_netPay').value) || 0;
  const wifeContrib = parseFloat(document.getElementById('cfg_wifeContrib').value) || 0;
  const rent = parseFloat(document.getElementById('cfg_rent').value) || 0;
  const parents = parseFloat(document.getElementById('cfg_parents').value) || 0;
  const living = parseFloat(document.getElementById('cfg_living').value) || 0;
  const yourSIP = parseFloat(document.getElementById('cfg_yourSIP').value) || 0;
  const wifeSIP = parseFloat(document.getElementById('cfg_wifeSIP').value) || 0;

  const totalIncome = netPay + wifeContrib;
  const totalExpenses = rent + parents + living;
  const totalInvestments = yourSIP + wifeSIP;
  const totalOutflow = totalExpenses + totalInvestments;

  // Clear previous warnings
  const existingWarning = document.getElementById('budgetWarning');
  if (existingWarning) existingWarning.remove();

  // Create warning container if needed
  let warningHTML = '';
  let hasError = false;

  if (totalOutflow > totalIncome) {
    hasError = true;
    const deficit = totalOutflow - totalIncome;
    warningHTML = `
      <div class="alert danger" id="budgetWarning" style="margin-top:20px">
        ⚠️ <strong>BUDGET DEFICIT: ₹${formatNum(deficit)}/month</strong><br><br>
        <div style="font-size:12px;margin-top:8px">
          <strong>Total Income:</strong> ₹${formatNum(totalIncome)}<br>
          <strong>Total Expenses:</strong> ₹${formatNum(totalExpenses)}<br>
          <strong>Total Investments:</strong> ₹${formatNum(totalInvestments)}<br>
          <strong>Total Outflow:</strong> ₹${formatNum(totalOutflow)}<br><br>
          You are spending ₹${formatNum(deficit)} more than you earn. Reduce expenses or investments!
        </div>
      </div>
    `;
  } else if (totalExpenses > totalIncome * 0.7) {
    warningHTML = `
      <div class="alert warning" id="budgetWarning" style="margin-top:20px">
        💡 <strong>HIGH EXPENSE RATIO</strong><br><br>
        <div style="font-size:12px;margin-top:8px">
          Your expenses are ${formatNum((totalExpenses/totalIncome)*100, 1)}% of income.
          Consider optimizing to free up more for investments.<br><br>
          <strong>Total Income:</strong> ₹${formatNum(totalIncome)}<br>
          <strong>Total Expenses:</strong> ₹${formatNum(totalExpenses)}<br>
          <strong>Available for Investments:</strong> ₹${formatNum(totalIncome - totalExpenses)}<br>
          <strong>Current Investments:</strong> ₹${formatNum(totalInvestments)} (${formatNum((totalInvestments/totalIncome)*100, 1)}% of income)
        </div>
      </div>
    `;
  } else {
    warningHTML = `
      <div class="alert success" id="budgetWarning" style="margin-top:20px">
        ✅ <strong>BUDGET HEALTHY</strong><br><br>
        <div style="font-size:12px;margin-top:8px">
          <strong>Total Income:</strong> ₹${formatNum(totalIncome)}<br>
          <strong>Total Expenses:</strong> ₹${formatNum(totalExpenses)} (${formatNum((totalExpenses/totalIncome)*100, 1)}%)<br>
          <strong>Total Investments:</strong> ₹${formatNum(totalInvestments)} (${formatNum((totalInvestments/totalIncome)*100, 1)}%)<br>
          <strong>Surplus:</strong> ₹${formatNum(totalIncome - totalOutflow)}/month
        </div>
      </div>
    `;
  }

  // Insert warning after the Investment Settings section
  const investmentSection = document.querySelector('.content .sh:nth-of-type(2)');
  if (investmentSection && investmentSection.parentNode) {
    const existingWarningDiv = document.getElementById('budgetWarning');
    if (existingWarningDiv) {
      existingWarningDiv.remove();
    }

    const warningDiv = document.createElement('div');
    warningDiv.innerHTML = warningHTML;

    // Find the button container and insert before it
    const buttonContainer = document.querySelector('.content > div[style*="text-align:center"]');
    if (buttonContainer) {
      buttonContainer.parentNode.insertBefore(warningDiv.firstElementChild, buttonContainer);
    }
  }

  return !hasError;
}

// Add event listeners for auto-calc
window.addEventListener('DOMContentLoaded', function() {
  const netPayInput = document.getElementById('cfg_netPay');
  const annualCTCInput = document.getElementById('cfg_annualCTC');

  if (netPayInput) {
    netPayInput.addEventListener('input', function() {
      // Don't auto-update CTC if user is manually editing it
      if (document.activeElement !== annualCTCInput) {
        updateAnnualCTC();
      }
    });
  }

  if (annualCTCInput) {
    annualCTCInput.addEventListener('input', function() {
      // Don't auto-update Net Pay if user is manually editing it
      if (document.activeElement !== netPayInput) {
        updateNetPay();
      }
    });
  }

  // Add validation listeners to all expense/investment fields
  const fieldsToWatch = ['cfg_rent', 'cfg_parents', 'cfg_living', 'cfg_yourSIP', 'cfg_wifeSIP', 'cfg_wifeContrib'];
  fieldsToWatch.forEach(fieldId => {
    const field = document.getElementById(fieldId);
    if (field) {
      field.addEventListener('input', validateAndUpdate);
    }
  });
});

'''

html = html[:old_js_start] + enhanced_config_js + html[old_js_end:]

print("✅ Enhanced configuration management")

# Now update the Settings page HTML to add onchange events
# Update the net pay input
html = html.replace(
    'id="cfg_netPay" value="213586" onchange="saveConfig()"',
    'id="cfg_netPay" value="213586" oninput="updateAnnualCTC()" onchange="saveConfig()"'
)

html = html.replace(
    'id="cfg_annualCTC" value="3634036" onchange="saveConfig()"',
    'id="cfg_annualCTC" value="3634036" oninput="updateNetPay()" onchange="saveConfig()"'
)

# Add oninput to expense fields for live validation
for field in ['cfg_rent', 'cfg_parents', 'cfg_living', 'cfg_yourSIP', 'cfg_wifeSIP', 'cfg_wifeContrib']:
    html = html.replace(
        f'id="{field}"',
        f'id="{field}" oninput="validateAndUpdate()"'
    )

print("✅ Added live validation to input fields")

# Update the save button text
html = html.replace(
    '<button onclick="saveConfig()"',
    '<button onclick="saveConfig()" id="saveBtn"'
)

# Write output
with open('index.html', 'w') as f:
    f.write(html)

print("=" * 60)
print("✅ SMART SETTINGS COMPLETE!")
print("")
print("📋 NEW FEATURES:")
print("   ✅ Monthly Net Pay ↔ Annual CTC auto-sync")
print("   ✅ Budget validation (warns if expenses > income)")
print("   ✅ Live recalculation as you type")
print("   ✅ Expense ratio analysis")
print("   ✅ Surplus/deficit calculation")
print("")
print("🎯 TRY IT:")
print("   1. Change Monthly Net Pay → Annual CTC updates")
print("   2. Change Annual CTC → Monthly Net Pay updates")
print("   3. Increase expenses beyond income → Red warning!")
print("   4. Keep it healthy → Green checkmark ✅")
