#!/usr/bin/env python3
"""
Part 2: Add Critical Calculation Functions
===========================================

Adds all the financial calculation functions needed for:
- Inflation-adjusted goals
- Real vs nominal returns
- Asset allocation analysis
- Emergency fund adequacy
- Insurance gap calculation
- Retirement corpus with 4% SWR
"""

print("=" * 80)
print("🔧 PART 2: ADDING CALCULATION FUNCTIONS")
print("=" * 80)
print()

with open('index.html', 'r') as f:
    html = f.read()

# Find where to insert functions (after calculateXIRR)
insertion_marker = '// ============== CONFIGURATION & DATA PERSISTENCE =============='

if insertion_marker not in html:
    print("⚠️  Marker not found, searching for alternative...")
    insertion_marker = 'function saveConfig() {'

calculation_functions = '''

// ============== INFLATION & GOAL CALCULATIONS ==============

// Calculate future value of a goal adjusted for inflation
function calculateInflatedGoal(currentValue, years, inflationRate) {
  if (!currentValue || !years || inflationRate === undefined) return currentValue || 0;
  return currentValue * Math.pow(1 + inflationRate / 100, years);
}

// Calculate required monthly SIP for inflation-adjusted goal
function calculateRequiredSIP(futureGoal, years, expectedReturn, stepUpRate = 10) {
  if (!futureGoal || !years) return 0;

  const months = years * 12;
  const monthlyReturn = (expectedReturn || 12) / 12 / 100;
  const monthlyStepUp = stepUpRate / 12 / 100;

  // Formula for SIP with step-up: FV = SIP × [((1+r)^n - (1+g)^n) / (r-g)]
  const numerator = Math.pow(1 + monthlyReturn, months) - Math.pow(1 + monthlyStepUp, months);
  const denominator = monthlyReturn - monthlyStepUp;

  if (Math.abs(denominator) < 0.0001) {
    // If rates are equal, use simple formula
    return futureGoal / (months * (1 + monthlyReturn) ** (months / 2));
  }

  const fvFactor = numerator / denominator;
  return futureGoal / fvFactor;
}

// Calculate real return (adjusted for inflation)
function calculateRealReturn(nominalReturn, inflationRate) {
  if (nominalReturn === undefined || inflationRate === undefined) return nominalReturn || 0;
  return ((1 + nominalReturn / 100) / (1 + inflationRate / 100) - 1) * 100;
}

// ============== DYNAMIC RETIREMENT PROJECTION ==============

function calculateRetirementProjection() {
  const startYear = 2026;
  const startAge = 32;
  const retirementAge = 60;
  const years = retirementAge - startAge; // 28 years

  const currentSIP = (config.yourSIP || 0) + (config.wifeSIP || 0); // Combined SIP
  const stepUpRate = 10; // 10% annual step-up
  const expectedReturn = 12; // 12% nominal CAGR
  const inflationRate = config.inflationGeneral || 6;

  const data = [];
  let totalInvested = 0;
  let corpus = 0;
  let monthlySIP = currentSIP;

  for (let i = 0; i <= years; i++) {
    const year = startYear + i;
    const age = startAge + i;

    // Annual contribution with step-up
    const annualContribution = monthlySIP * 12;
    totalInvested += annualContribution;

    // Corpus grows by return rate + new contribution
    corpus = corpus * (1 + expectedReturn / 100) + annualContribution;

    // Inflation-adjusted corpus (present value in today's money)
    const inflAdjCorpus = corpus / Math.pow(1 + inflationRate / 100, i);

    data.push({
      year: year,
      age: age,
      sip: Math.round(monthlySIP),
      contrib: Math.round(annualContribution),
      corpus: Math.round(corpus),
      inflAdj: Math.round(inflAdjCorpus)
    });

    // Apply step-up for next year
    monthlySIP = monthlySIP * (1 + stepUpRate / 100);
  }

  return data;
}

// ============== DYNAMIC KIDS EDUCATION PROJECTION ==============

function calculateKidsEducationProjection(childNumber) {
  const birthYear = childNumber === 1 ? 2026 : 2028;
  const targetAge = 18;
  const yearsToGoal = (birthYear + targetAge) - 2026;

  // Today's cost for 4-year engineering degree
  const currentCost = 3000000; // ₹30L today

  // Inflate to future value
  const inflationRate = config.inflationEducation || 10;
  const futureGoalCost = calculateInflatedGoal(currentCost, yearsToGoal, inflationRate);

  // Current SIP allocation (from funds with purpose: "Kids Education")
  const kidsFunds = (typeof yourFunds !== 'undefined') ?
                    yourFunds.filter(f => f.purpose && f.purpose.includes('Kids')) : [];
  const currentSIP = kidsFunds.reduce((sum, f) => sum + (f.monthlySIP || 0), 0);

  // Project corpus growth
  const data = [];
  let corpus = 0;
  let monthlySIP = currentSIP || 23000; // Default if no kids funds
  const expectedReturn = 12;

  for (let age = 0; age <= targetAge; age++) {
    const year = birthYear + age;
    const annualContribution = monthlySIP * 12;
    corpus = corpus * (1 + expectedReturn / 100) + annualContribution;

    data.push({ year, age, corpus: Math.round(corpus) });

    // Apply 10% step-up
    monthlySIP = monthlySIP * 1.1;
  }

  return {
    data: data,
    targetCost: futureGoalCost,
    currentSIP: currentSIP,
    projectedCorpus: corpus,
    surplus: corpus - futureGoalCost,
    adequacy: (corpus / futureGoalCost * 100).toFixed(0)
  };
}

// ============== ASSET ALLOCATION ANALYSIS ==============

function analyzeAssetAllocation() {
  const allocation = {
    equity: { amount: 0, target: 0.75, funds: [] },
    debt: { amount: 0, target: 0.20, funds: [] },
    gold: { amount: 0, target: 0.05, funds: [] },
    international: { amount: 0, target: 0.00, funds: [] }
  };

  if (typeof yourFunds === 'undefined') return allocation;

  // Categorize each fund based on name and type
  yourFunds.forEach(fund => {
    const monthlyAmount = fund.monthlySIP || 0;
    const name = (fund.name || '').toLowerCase();

    if (name.includes('balanced') || name.includes('hybrid')) {
      // Balanced/Hybrid funds: ~65% equity, 35% debt
      allocation.equity.amount += monthlyAmount * 0.65;
      allocation.debt.amount += monthlyAmount * 0.35;
      allocation.equity.funds.push(fund.name);
    } else if (name.includes('liquid') || name.includes('debt') || name.includes('bond')) {
      allocation.debt.amount += monthlyAmount;
      allocation.debt.funds.push(fund.name);
    } else if (name.includes('gold')) {
      allocation.gold.amount += monthlyAmount;
      allocation.gold.funds.push(fund.name);
    } else if (name.includes('international') || name.includes('global') || name.includes('usa')) {
      allocation.international.amount += monthlyAmount;
      allocation.international.funds.push(fund.name);
    } else {
      // Default: pure equity (index, flexi cap, mid cap, small cap, etc.)
      allocation.equity.amount += monthlyAmount;
      allocation.equity.funds.push(fund.name);
    }
  });

  // Calculate percentages
  const total = allocation.equity.amount + allocation.debt.amount +
                allocation.gold.amount + allocation.international.amount;

  if (total > 0) {
    allocation.equity.percent = (allocation.equity.amount / total * 100).toFixed(1);
    allocation.debt.percent = (allocation.debt.amount / total * 100).toFixed(1);
    allocation.gold.percent = (allocation.gold.amount / total * 100).toFixed(1);
    allocation.international.percent = (allocation.international.amount / total * 100).toFixed(1);

    // Calculate deviation from target
    allocation.equity.deviation = parseFloat(allocation.equity.percent) - (allocation.equity.target * 100);
    allocation.debt.deviation = parseFloat(allocation.debt.percent) - (allocation.debt.target * 100);
    allocation.gold.deviation = parseFloat(allocation.gold.percent) - (allocation.gold.target * 100);
  } else {
    allocation.equity.percent = "0.0";
    allocation.debt.percent = "0.0";
    allocation.gold.percent = "0.0";
    allocation.international.percent = "0.0";
  }

  return allocation;
}

// ============== EMERGENCY FUND CALCULATIONS ==============

function calculateEmergencyFundAdequacy() {
  const currentFund = config.emergencyFund || 0;
  const targetMonths = parseInt(config.emergencyFundTarget) || 6;

  // Calculate monthly expenses
  const monthlyExpenses = (config.rent || 0) + (config.parents || 0) +
                          (config.fixedExpenses || 0) + (config.livingExpenses || 0);

  const requiredFund = monthlyExpenses * targetMonths;
  const adequacy = requiredFund > 0 ? (currentFund / requiredFund * 100).toFixed(0) : 100;
  const surplus = currentFund - requiredFund;

  return {
    current: currentFund,
    required: requiredFund,
    adequacy: adequacy,
    surplus: surplus,
    monthlyExpenses: monthlyExpenses,
    targetMonths: targetMonths,
    status: adequacy >= 100 ? 'adequate' : (adequacy >= 50 ? 'partial' : 'critical')
  };
}

// ============== INSURANCE ADEQUACY CALCULATIONS ==============

function calculateInsuranceAdequacy() {
  // Life Insurance: 15x annual expenses (conservative CFP standard)
  const monthlyExpenses = (config.rent || 0) + (config.parents || 0) +
                          (config.fixedExpenses || 0) + (config.livingExpenses || 0);
  const annualExpenses = monthlyExpenses * 12;
  const lifeInsuranceRequired = annualExpenses * 15;
  const lifeInsuranceCurrent = config.lifeInsuranceCurrent || 0;
  const lifeInsuranceGap = lifeInsuranceRequired - lifeInsuranceCurrent;

  // Health Insurance: Minimum ₹20L for family (CFP recommendation)
  const healthInsuranceRequired = 2000000; // ₹20L minimum
  const healthInsuranceCurrent = config.healthInsuranceCurrent || 0;
  const healthInsuranceGap = healthInsuranceRequired - healthInsuranceCurrent;

  // Parents Health: Minimum ₹10L (considering age-related medical needs)
  const parentsHealthRequired = 1000000; // ₹10L
  const parentsHealthCurrent = config.parentsHealthInsurance || 0;
  const parentsHealthGap = parentsHealthRequired - parentsHealthCurrent;

  return {
    life: {
      required: lifeInsuranceRequired,
      current: lifeInsuranceCurrent,
      gap: lifeInsuranceGap,
      adequacy: lifeInsuranceRequired > 0 ? (lifeInsuranceCurrent / lifeInsuranceRequired * 100).toFixed(0) : 100
    },
    health: {
      required: healthInsuranceRequired,
      current: healthInsuranceCurrent,
      gap: healthInsuranceGap,
      adequacy: (healthInsuranceCurrent / healthInsuranceRequired * 100).toFixed(0)
    },
    parentsHealth: {
      required: parentsHealthRequired,
      current: parentsHealthCurrent,
      gap: parentsHealthGap,
      adequacy: (parentsHealthCurrent / parentsHealthRequired * 100).toFixed(0)
    }
  };
}

// ============== RETIREMENT CORPUS WITH 4% SAFE WITHDRAWAL RATE ==============

function calculateRetirementRequirement() {
  const currentAge = 32;
  const retirementAge = 60;
  const lifeExpectancy = 85;
  const yearsToRetirement = retirementAge - currentAge; // 28 years
  const yearsInRetirement = lifeExpectancy - retirementAge; // 25 years

  // Current annual expenses
  const monthlyExpenses = (config.rent || 0) + (config.parents || 0) +
                          (config.fixedExpenses || 0) + (config.livingExpenses || 0);
  const currentAnnualExpenses = monthlyExpenses * 12;

  // Inflate to retirement year using general inflation
  const inflationRate = config.inflationGeneral || 6;
  const futureAnnualExpenses = calculateInflatedGoal(
    currentAnnualExpenses,
    yearsToRetirement,
    inflationRate
  );

  // Safe withdrawal rate: 4% rule (widely accepted CFP standard)
  // Corpus needed = Annual expenses / 0.04
  const requiredCorpus = futureAnnualExpenses / 0.04;

  // Current projection from dynamic calculation
  const retirementData = calculateRetirementProjection();
  const projectedCorpus = retirementData[retirementData.length - 1].corpus;

  // Gap analysis
  const gap = requiredCorpus - projectedCorpus;
  const adequacy = requiredCorpus > 0 ? (projectedCorpus / requiredCorpus * 100).toFixed(0) : 100;

  // Calculate required additional monthly SIP to close gap
  const additionalSIPNeeded = gap > 0 ? calculateRequiredSIP(gap, yearsToRetirement, 12, 10) : 0;

  return {
    currentAnnualExpenses: currentAnnualExpenses,
    futureAnnualExpenses: futureAnnualExpenses,
    requiredCorpus: requiredCorpus,
    projectedCorpus: projectedCorpus,
    gap: gap,
    adequacy: adequacy,
    safeWithdrawalRate: 0.04,
    yearsToRetirement: yearsToRetirement,
    yearsInRetirement: yearsInRetirement,
    additionalSIPNeeded: Math.round(additionalSIPNeeded)
  };
}

'''

# Insert the functions before saveConfig
if insertion_marker in html:
    html = html.replace(insertion_marker, calculation_functions + '\n' + insertion_marker)
    print("✅ Added all calculation functions:")
    print("   • calculateInflatedGoal()")
    print("   • calculateRequiredSIP()")
    print("   • calculateRealReturn()")
    print("   • calculateRetirementProjection()")
    print("   • calculateKidsEducationProjection()")
    print("   • analyzeAssetAllocation()")
    print("   • calculateEmergencyFundAdequacy()")
    print("   • calculateInsuranceAdequacy()")
    print("   • calculateRetirementRequirement()")
    print()
else:
    print("⚠️  Could not find insertion marker")

# Write result
with open('index.html', 'w') as f:
    f.write(html)

print("=" * 80)
print("✅ CALCULATION FUNCTIONS ADDED SUCCESSFULLY")
print("=" * 80)
print()
