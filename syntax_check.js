const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// Extract JavaScript between <script> and </script>
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) {
  console.log('❌ No script tag found');
  process.exit(1);
}

const jsCode = scriptMatch[1];

// Basic syntax checks
let errors = [];

// Check for common syntax issues
const openBraces = (jsCode.match(/\{/g) || []).length;
const closeBraces = (jsCode.match(/\}/g) || []).length;
const openParens = (jsCode.match(/\(/g) || []).length;
const closeParens = (jsCode.match(/\)/g) || []).length;
const openBrackets = (jsCode.match(/\[/g) || []).length;
const closeBrackets = (jsCode.match(/\]/g) || []).length;

console.log('📊 Bracket Analysis:');
console.log(`  Braces: { ${openBraces} } ${closeBraces} ${openBraces === closeBraces ? '✅' : '❌'}`);
console.log(`  Parens: ( ${openParens} ) ${closeParens} ${openParens === closeParens ? '✅' : '❌'}`);
console.log(`  Brackets: [ ${openBrackets} ] ${closeBrackets} ${openBrackets === closeBrackets ? '✅' : '❌'}`);

if (openBraces !== closeBraces) errors.push(`Brace mismatch: ${openBraces} open, ${closeBraces} close`);
if (openParens !== closeParens) errors.push(`Paren mismatch: ${openParens} open, ${closeParens} close`);
if (openBrackets !== closeBrackets) errors.push(`Bracket mismatch: ${openBrackets} open, ${closeBrackets} close`);

// Check for key functions
const keyFunctions = [
  'showPage',
  'calculatePortfolioExpectedReturn',
  'calculateAlpha',
  'updateExpenseSummary',
  'updateBenchmarkSummary',
  'fetchAllFundHistoricalData'
];

console.log('\n🔍 Key Functions:');
keyFunctions.forEach(fn => {
  const regex = new RegExp(`function ${fn}\\s*\\(`, 'g');
  const matches = jsCode.match(regex);
  const count = matches ? matches.length : 0;
  console.log(`  ${fn}: ${count} ${count === 1 ? '✅' : (count === 0 ? '❌ MISSING' : '⚠️ DUPLICATE')}`);
  if (count !== 1) errors.push(`${fn}: found ${count} times (expected 1)`);
});

console.log('\n' + (errors.length === 0 ? '✅ All checks passed!' : `❌ Found ${errors.length} issues:`));
errors.forEach(e => console.log(`  - ${e}`));

process.exit(errors.length === 0 ? 0 : 1);
