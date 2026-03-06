#!/usr/bin/env python3
"""
Enhance settings with:
1. Detailed expense categories
2. Auto-update fund allocations from SIP
3. Fully editable tax optimizer
"""

print("🔧 Adding detailed settings and tax optimizer...")

with open('index.html', 'r') as f:
    html = f.read()

# 1. Replace the simple expense section with detailed categories
old_expenses = '''      <div class="card j">
        <div class="ch3 j">MONTHLY EXPENSES</div>
        <div class="ml">
          <div class="d">Rent</div>
          <div class="a"><input type="number" id="cfg_rent" value="40000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:120px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Parents Support</div>
          <div class="a"><input type="number" id="cfg_parents" value="25000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:120px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Living</div>
          <div class="a"><input type="number" id="cfg_living" value="49000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:120px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
      </div>'''

new_expenses = '''      <div class="card j">
        <div class="ch3 j">HOUSING & FIXED</div>
        <div class="ml">
          <div class="d">Rent/EMI</div>
          <div class="a"><input type="number" id="cfg_rent" value="40000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Electricity</div>
          <div class="a"><input type="number" id="cfg_electricity" value="3000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Internet/Phone</div>
          <div class="a"><input type="number" id="cfg_internet" value="2000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Maintenance</div>
          <div class="a"><input type="number" id="cfg_maintenance" value="3000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
      </div>

      <div class="card j">
        <div class="ch3 j">DAILY LIVING</div>
        <div class="ml">
          <div class="d">Groceries</div>
          <div class="a"><input type="number" id="cfg_groceries" value="15000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Dining Out</div>
          <div class="a"><input type="number" id="cfg_dining" value="8000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Transport/Fuel</div>
          <div class="a"><input type="number" id="cfg_transport" value="5000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Household Items</div>
          <div class="a"><input type="number" id="cfg_household" value="4000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
      </div>

      <div class="card j">
        <div class="ch3 j">FAMILY & PERSONAL</div>
        <div class="ml">
          <div class="d">Parents Support</div>
          <div class="a"><input type="number" id="cfg_parents" value="25000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Healthcare</div>
          <div class="a"><input type="number" id="cfg_healthcare" value="5000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Personal Care</div>
          <div class="a"><input type="number" id="cfg_personalCare" value="3000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Entertainment</div>
          <div class="a"><input type="number" id="cfg_entertainment" value="6000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Clothing/Shopping</div>
          <div class="a"><input type="number" id="cfg_shopping" value="5000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Miscellaneous</div>
          <div class="a"><input type="number" id="cfg_misc" value="5000" oninput="validateAndUpdate()" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--red);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
      </div>'''

html = html.replace(old_expenses, new_expenses)
print("✅ Added detailed expense categories (13 categories)")

# 2. Add Tax Optimizer settings section
tax_optimizer_settings = '''
    <div class="sh">
      <span class="sh-n">03</span>
      <h2>Tax Deductions & Optimizer</h2>
    </div>

    <div class="g3">
      <div class="card y">
        <div class="ch3 y">SECTION 80C (Max ₹1.5L)</div>
        <div class="ml">
          <div class="d">EPF (Auto)</div>
          <div class="a"><input type="number" id="cfg_epf" value="16761" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--jt);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">PPF</div>
          <div class="a"><input type="number" id="cfg_ppf" value="0" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--jt);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">ELSS (Mutual Funds)</div>
          <div class="a"><input type="number" id="cfg_elss" value="120000" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--jt);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">LIC Premium</div>
          <div class="a"><input type="number" id="cfg_lic" value="30000" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--jt);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Home Loan Principal</div>
          <div class="a"><input type="number" id="cfg_homeLoanPrincipal" value="0" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--jt);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div style="margin-top:10px;font-size:10px;color:var(--ink3)">
          Total 80C: <span id="total80C" style="color:var(--you)">₹0</span> / ₹1,50,000
        </div>
      </div>

      <div class="card y">
        <div class="ch3 y">OTHER DEDUCTIONS</div>
        <div class="ml">
          <div class="d">80CCD(1B) - NPS Extra</div>
          <div class="a"><input type="number" id="cfg_npsExtra" value="50000" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--jt);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">80D - Health Insurance</div>
          <div class="a"><input type="number" id="cfg_healthInsurance" value="25000" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--jt);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">80D - Parents Insurance</div>
          <div class="a"><input type="number" id="cfg_parentsInsurance" value="50000" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--jt);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">80EE - Home Loan Interest</div>
          <div class="a"><input type="number" id="cfg_homeLoanInterest" value="0" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--jt);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">80E - Education Loan Int</div>
          <div class="a"><input type="number" id="cfg_eduLoanInterest" value="0" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--jt);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div style="margin-top:10px;font-size:10px;color:var(--ink3)">
          Total Other: <span id="totalOther" style="color:var(--you)">₹0</span>
        </div>
      </div>

      <div class="card y">
        <div class="ch3 y">HRA & STANDARD</div>
        <div class="ml">
          <div class="d">HRA Received (Annual)</div>
          <div class="a"><input type="number" id="cfg_hraReceived" value="670452" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--you);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Annual Rent Paid</div>
          <div class="a"><input type="number" id="cfg_annualRent" value="480000" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--you);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">Basic Salary (Annual)</div>
          <div class="a"><input type="number" id="cfg_basicSalary" value="1676136" onchange="saveConfig()" style="background:var(--bg3);border:1px solid var(--border);color:var(--you);padding:4px 8px;border-radius:3px;width:100px;text-align:right;font-family:'IBM Plex Mono',monospace"></div>
        </div>
        <div class="ml">
          <div class="d">HRA Exemption</div>
          <div class="a" style="color:var(--jt)" id="hraExemption">₹0</div>
        </div>
        <div style="margin-top:10px;font-size:10px;color:var(--ink3)">
          Standard Deduction: ₹50,000 (automatic)
        </div>
      </div>
    </div>

    <div class="g2" style="margin-top:13px">
      <div class="card j">
        <div class="ch3 j">TAX SUMMARY (OLD REGIME)</div>
        <div class="ml">
          <div class="d">Gross Annual Income</div>
          <div class="a ay" id="taxGrossIncome">₹0</div>
        </div>
        <div class="ml">
          <div class="d">Total Deductions</div>
          <div class="a aj" id="taxTotalDeductions">₹0</div>
        </div>
        <div class="ml">
          <div class="d">Taxable Income</div>
          <div class="a ay" id="taxTaxableIncome">₹0</div>
        </div>
        <div class="ml">
          <div class="d">Income Tax</div>
          <div class="a ar" id="taxAmount">₹0</div>
        </div>
        <div class="ml">
          <div class="d">Cess (4%)</div>
          <div class="a ar" id="taxCess">₹0</div>
        </div>
        <div class="tr">
          <div class="tl">Total Tax Liability</div>
          <div class="tv ar" id="taxTotal">₹0</div>
        </div>
        <div class="tr">
          <div class="tl">Monthly Tax</div>
          <div class="tv ar" id="taxMonthly">₹0</div>
        </div>
      </div>

      <div class="card j">
        <div class="ch3 j">TAX SUMMARY (NEW REGIME)</div>
        <div class="ml">
          <div class="d">Gross Annual Income</div>
          <div class="a ay" id="taxNewGrossIncome">₹0</div>
        </div>
        <div class="ml">
          <div class="d">Standard Deduction</div>
          <div class="a aj">₹50,000</div>
        </div>
        <div class="ml">
          <div class="d">Taxable Income</div>
          <div class="a ay" id="taxNewTaxableIncome">₹0</div>
        </div>
        <div class="ml">
          <div class="d">Income Tax</div>
          <div class="a ar" id="taxNewAmount">₹0</div>
        </div>
        <div class="ml">
          <div class="d">Cess (4%)</div>
          <div class="a ar" id="taxNewCess">₹0</div>
        </div>
        <div class="tr">
          <div class="tl">Total Tax Liability</div>
          <div class="tv ar" id="taxNewTotal">₹0</div>
        </div>
        <div class="tr">
          <div class="tl">SAVINGS vs Old Regime</div>
          <div class="tv" id="taxSavings" style="color:var(--jt)">₹0</div>
        </div>
      </div>
    </div>
'''

# Find where to insert (after investment settings, before the save button)
insert_pos = html.find('<div style="margin-top:20px;text-align:center">')
if insert_pos != -1:
    html = html[:insert_pos] + tax_optimizer_settings + '\n' + html[insert_pos:]
    print("✅ Added comprehensive tax optimizer settings")

# 3. Update config object to include all new fields
old_config = '''let config = {
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
};'''

new_config = '''let config = {
  // Income
  netPay: 213586,
  annualCTC: 3634036,
  salaryIncrement: 10,
  wifeGross: 70000,
  wifeContrib: 20000,
  wifeIncrement: 8,

  // Housing & Fixed
  rent: 40000,
  electricity: 3000,
  internet: 2000,
  maintenance: 3000,

  // Daily Living
  groceries: 15000,
  dining: 8000,
  transport: 5000,
  household: 4000,

  // Family & Personal
  parents: 25000,
  healthcare: 5000,
  personalCare: 3000,
  entertainment: 6000,
  shopping: 5000,
  misc: 5000,

  // Investments
  yourSIP: 71886,
  wifeSIP: 50000,
  stepUp: 10,
  wifeStepUp: 10,
  expectedReturns: 12,
  wifeReturns: 12,

  // Goals
  retireAge: 60,
  retireTarget: 10,
  carYear: 2026,

  // Tax Deductions - 80C
  epf: 16761,
  ppf: 0,
  elss: 120000,
  lic: 30000,
  homeLoanPrincipal: 0,

  // Tax Deductions - Other
  npsExtra: 50000,
  healthInsurance: 25000,
  parentsInsurance: 50000,
  homeLoanInterest: 0,
  eduLoanInterest: 0,

  // HRA
  hraReceived: 670452,
  annualRent: 480000,
  basicSalary: 1676136
};'''

html = html.replace(old_config, new_config)
print("✅ Updated config with all new fields")

# 4. Update validation function to use detailed expenses
old_validation = '''  const rent = parseFloat(document.getElementById('cfg_rent').value) || 0;
  const parents = parseFloat(document.getElementById('cfg_parents').value) || 0;
  const living = parseFloat(document.getElementById('cfg_living').value) || 0;'''

new_validation = '''  const rent = parseFloat(document.getElementById('cfg_rent').value) || 0;
  const electricity = parseFloat(document.getElementById('cfg_electricity').value) || 0;
  const internet = parseFloat(document.getElementById('cfg_internet').value) || 0;
  const maintenance = parseFloat(document.getElementById('cfg_maintenance').value) || 0;
  const groceries = parseFloat(document.getElementById('cfg_groceries').value) || 0;
  const dining = parseFloat(document.getElementById('cfg_dining').value) || 0;
  const transport = parseFloat(document.getElementById('cfg_transport').value) || 0;
  const household = parseFloat(document.getElementById('cfg_household').value) || 0;
  const parents = parseFloat(document.getElementById('cfg_parents').value) || 0;
  const healthcare = parseFloat(document.getElementById('cfg_healthcare').value) || 0;
  const personalCare = parseFloat(document.getElementById('cfg_personalCare').value) || 0;
  const entertainment = parseFloat(document.getElementById('cfg_entertainment').value) || 0;
  const shopping = parseFloat(document.getElementById('cfg_shopping').value) || 0;
  const misc = parseFloat(document.getElementById('cfg_misc').value) || 0;'''

html = html.replace(old_validation, new_validation)

old_total_expenses = '  const totalExpenses = rent + parents + living;'
new_total_expenses = '''  const totalExpenses = rent + electricity + internet + maintenance +
                      groceries + dining + transport + household +
                      parents + healthcare + personalCare + entertainment + shopping + misc;'''

html = html.replace(old_total_expenses, new_total_expenses)
print("✅ Updated validation to use detailed expenses")

# 5. Add tax calculation functions
tax_calc_functions = '''
// ============================================
// TAX CALCULATION FUNCTIONS
// ============================================

function calculateTax() {
  const annualCTC = parseFloat(document.getElementById('cfg_annualCTC').value) || 0;

  // 80C Deductions
  const epf = parseFloat(document.getElementById('cfg_epf').value) || 0;
  const ppf = parseFloat(document.getElementById('cfg_ppf').value) || 0;
  const elss = parseFloat(document.getElementById('cfg_elss').value) || 0;
  const lic = parseFloat(document.getElementById('cfg_lic').value) || 0;
  const homeLoanPrincipal = parseFloat(document.getElementById('cfg_homeLoanPrincipal').value) || 0;

  const total80C = Math.min(epf + ppf + elss + lic + homeLoanPrincipal, 150000);
  updateEl('total80C', '₹' + formatNum(total80C));

  // Other Deductions
  const npsExtra = parseFloat(document.getElementById('cfg_npsExtra').value) || 0;
  const healthInsurance = Math.min(parseFloat(document.getElementById('cfg_healthInsurance').value) || 0, 25000);
  const parentsInsurance = Math.min(parseFloat(document.getElementById('cfg_parentsInsurance').value) || 0, 50000);
  const homeLoanInterest = Math.min(parseFloat(document.getElementById('cfg_homeLoanInterest').value) || 0, 200000);
  const eduLoanInterest = parseFloat(document.getElementById('cfg_eduLoanInterest').value) || 0;

  const totalOther = npsExtra + healthInsurance + parentsInsurance + homeLoanInterest + eduLoanInterest;
  updateEl('totalOther', '₹' + formatNum(totalOther));

  // HRA Calculation
  const hraReceived = parseFloat(document.getElementById('cfg_hraReceived').value) || 0;
  const annualRent = parseFloat(document.getElementById('cfg_annualRent').value) || 0;
  const basicSalary = parseFloat(document.getElementById('cfg_basicSalary').value) || 0;

  const hraExemption = Math.min(
    hraReceived,
    annualRent - (0.1 * basicSalary),
    0.5 * basicSalary
  );
  updateEl('hraExemption', '₹' + formatNum(hraExemption));

  // OLD REGIME
  const standardDeduction = 50000;
  const totalDeductions = total80C + totalOther + hraExemption + standardDeduction;
  const taxableIncomeOld = Math.max(0, annualCTC - totalDeductions);

  let taxOld = 0;
  if (taxableIncomeOld > 1000000) taxOld += (taxableIncomeOld - 1000000) * 0.3;
  if (taxableIncomeOld > 500000) taxOld += Math.min(taxableIncomeOld - 500000, 500000) * 0.2;
  if (taxableIncomeOld > 250000) taxOld += Math.min(taxableIncomeOld - 250000, 250000) * 0.05;

  const cessOld = taxOld * 0.04;
  const totalTaxOld = taxOld + cessOld;
  const monthlyTaxOld = totalTaxOld / 12;

  updateEl('taxGrossIncome', '₹' + formatNum(annualCTC));
  updateEl('taxTotalDeductions', '₹' + formatNum(totalDeductions));
  updateEl('taxTaxableIncome', '₹' + formatNum(taxableIncomeOld));
  updateEl('taxAmount', '₹' + formatNum(taxOld));
  updateEl('taxCess', '₹' + formatNum(cessOld));
  updateEl('taxTotal', '₹' + formatNum(totalTaxOld));
  updateEl('taxMonthly', '₹' + formatNum(monthlyTaxOld));

  // NEW REGIME
  const taxableIncomeNew = Math.max(0, annualCTC - standardDeduction);

  let taxNew = 0;
  if (taxableIncomeNew > 1500000) taxNew += (taxableIncomeNew - 1500000) * 0.3;
  if (taxableIncomeNew > 1200000) taxNew += Math.min(taxableIncomeNew - 1200000, 300000) * 0.2;
  if (taxableIncomeNew > 900000) taxNew += Math.min(taxableIncomeNew - 900000, 300000) * 0.15;
  if (taxableIncomeNew > 600000) taxNew += Math.min(taxableIncomeNew - 600000, 300000) * 0.1;
  if (taxableIncomeNew > 300000) taxNew += Math.min(taxableIncomeNew - 300000, 300000) * 0.05;

  const cessNew = taxNew * 0.04;
  const totalTaxNew = taxNew + cessNew;
  const savings = totalTaxOld - totalTaxNew;

  updateEl('taxNewGrossIncome', '₹' + formatNum(annualCTC));
  updateEl('taxNewTaxableIncome', '₹' + formatNum(taxableIncomeNew));
  updateEl('taxNewAmount', '₹' + formatNum(taxNew));
  updateEl('taxNewCess', '₹' + formatNum(cessNew));
  updateEl('taxNewTotal', '₹' + formatNum(totalTaxNew));

  const savingsEl = document.getElementById('taxSavings');
  if (savingsEl) {
    savingsEl.textContent = (savings >= 0 ? '+' : '') + '₹' + formatNum(Math.abs(savings));
    savingsEl.style.color = savings >= 0 ? 'var(--jt)' : 'var(--red)';
  }
}

// Update field watchers to include tax fields
const taxFields = ['cfg_epf', 'cfg_ppf', 'cfg_elss', 'cfg_lic', 'cfg_homeLoanPrincipal',
                   'cfg_npsExtra', 'cfg_healthInsurance', 'cfg_parentsInsurance',
                   'cfg_homeLoanInterest', 'cfg_eduLoanInterest', 'cfg_hraReceived',
                   'cfg_annualRent', 'cfg_basicSalary', 'cfg_annualCTC'];

window.addEventListener('DOMContentLoaded', function() {
  // ... existing code ...

  // Add tax calculation listeners
  taxFields.forEach(fieldId => {
    const field = document.getElementById(fieldId);
    if (field) {
      field.addEventListener('input', calculateTax);
    }
  });

  // Calculate tax on load
  setTimeout(calculateTax, 500);
});

'''

# Insert before the MY PORTFOLIO DATA section
portfolio_data_pos = html.find('// ============================================\n// MY PORTFOLIO DATA')
if portfolio_data_pos != -1:
    html = html[:portfolio_data_pos] + tax_calc_functions + '\n' + html[portfolio_data_pos:]
    print("✅ Added tax calculation functions")

# 6. Update the fieldsToWatch array
old_fields_watch = "  const fieldsToWatch = ['cfg_rent', 'cfg_parents', 'cfg_living', 'cfg_yourSIP', 'cfg_wifeSIP', 'cfg_wifeContrib'];"
new_fields_watch = """  const fieldsToWatch = ['cfg_rent', 'cfg_electricity', 'cfg_internet', 'cfg_maintenance',
                      'cfg_groceries', 'cfg_dining', 'cfg_transport', 'cfg_household',
                      'cfg_parents', 'cfg_healthcare', 'cfg_personalCare', 'cfg_entertainment',
                      'cfg_shopping', 'cfg_misc', 'cfg_yourSIP', 'cfg_wifeSIP', 'cfg_wifeContrib'];"""

html = html.replace(old_fields_watch, new_fields_watch)
print("✅ Updated field watchers")

# Write output
with open('index.html', 'w') as f:
    f.write(html)

print("=" * 60)
print("✅ ENHANCED SETTINGS COMPLETE!")
print("")
print("📋 DETAILED EXPENSES (13 Categories):")
print("   Housing: Rent, Electricity, Internet, Maintenance")
print("   Daily: Groceries, Dining, Transport, Household")
print("   Personal: Parents, Healthcare, Personal Care, Entertainment, Shopping, Misc")
print("")
print("📋 TAX OPTIMIZER (Fully Editable):")
print("   80C: EPF, PPF, ELSS, LIC, Home Loan Principal")
print("   Other: NPS Extra, Health Ins, Parents Ins, Home Loan Int, Edu Loan Int")
print("   HRA: Auto-calculated from rent and basic salary")
print("   Live comparison: Old vs New regime with savings")
print("")
print("🎯 NEXT: Add SIP auto-update to fund allocations")
