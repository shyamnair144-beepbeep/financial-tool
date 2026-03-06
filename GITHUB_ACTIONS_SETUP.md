# 🤖 GitHub Actions Setup for Live Market Data

**Problem**: Browser-based API calls blocked by CORS
**Solution**: Server-side data fetching via GitHub Actions

---

## ✅ What's Included

The workflow file `.github/workflows/fetch-market-data.yml` is ready and will:

1. **Run automatically** every day at 6:30 PM IST (after market close)
2. **Fetch live data** from Yahoo Finance and NSE APIs
3. **Create/update** `market-data.json` in your repository
4. **Commit and push** changes automatically
5. **Allow manual triggering** anytime from GitHub Actions tab

---

## 📋 Setup Steps

### **Step 1: Push the Workflow File**

```bash
cd /home/shyanair/financial-tool
git add .github/workflows/fetch-market-data.yml
git commit -m "Add GitHub Actions workflow for daily market data updates"
git push origin main
```

### **Step 2: Enable GitHub Actions (if not already enabled)**

1. Go to your repository: https://github.com/shyamnair144-beepbeep/financial-tool
2. Click **Settings** tab
3. Scroll to **Actions** → **General**
4. Under "Workflow permissions", select:
   - ✅ **Read and write permissions**
   - ✅ **Allow GitHub Actions to create and approve pull requests**
5. Click **Save**

### **Step 3: Manually Run First Time**

1. Go to **Actions** tab in your repository
2. Click "Fetch Market Data Daily" workflow
3. Click **Run workflow** dropdown (right side)
4. Click green **Run workflow** button
5. Wait ~30 seconds for completion
6. Verify `market-data.json` appears in your repository

### **Step 4: Verify It Works**

After the workflow runs, you should see:

1. **New file**: `market-data.json` in repository root
2. **Commit message**: "🤖 Auto-update market data - 2026-03-06 13:00 UTC"
3. **Green checkmark** on the Actions run

Then on your website:
1. Go to Market Indicators page
2. Click "🔄 Refresh Market Data"
3. Should show: "GitHub Actions (Daily Update)" as source
4. **No more CORS errors!**

---

## 📊 What Data Gets Fetched

The workflow fetches and saves:

```json
{
  "source": "GitHub Actions (Daily Update)",
  "timestamp": 1709737200000,
  "lastUpdated": "2026-03-06 13:00:00 UTC",
  "niftyPrice": 22000,        // Live from Yahoo/NSE
  "niftyChange": 0.5,         // Daily % change
  "niftyPE": 22.5,            // PE ratio from NSE
  "niftyPB": 4.2,             // PB ratio from NSE
  "indiaVIX": 15.5,           // Volatility index
  "repoRate": 6.5,            // RBI repo rate
  "cpiInflation": 5.1,        // CPI inflation
  "usdInr": 83.2,             // USD/INR rate
  "crudeOil": 75.0,           // Crude oil price
  "goldPrice": 62500,         // Gold price per 10g
  "note": "Auto-updated daily..."
}
```

---

## ⏰ Schedule

**Automatic runs**: Every day at **6:30 PM IST** (1:00 PM UTC)
**Manual runs**: Anytime via Actions tab

Why 6:30 PM IST?
- Market closes at 3:30 PM
- Gives 3 hours for all indices to settle
- Updated data ready for evening review

---

## 🔍 How to Check If It's Working

### **Method 1: GitHub Actions Tab**
1. Go to Actions tab
2. See "Fetch Market Data Daily" runs
3. Click latest run → View logs
4. Look for:
   ```
   ✅ Yahoo Finance data fetched: Nifty 22000
   ✅ market-data.json created with live data
   ✅ Market data pushed to repository
   ```

### **Method 2: Repository Root**
1. Check if `market-data.json` exists
2. Click file → View raw
3. Verify `lastUpdated` is recent

### **Method 3: Your Website**
1. Open financial tool
2. Go to Market Indicators page
3. Check "Last Updated" timestamp
4. Should say "GitHub Actions (Daily Update)"

---

## 🛠️ Troubleshooting

### **Issue: Workflow fails with "Permission denied"**
**Fix**: Enable write permissions in Settings → Actions → Workflow permissions

### **Issue: No market-data.json file created**
**Fix**: Check Actions logs for errors. Might be API rate limiting.

### **Issue: File created but website still shows default values**
**Fix**:
1. Hard refresh website (Ctrl+Shift+R)
2. Clear browser cache
3. Verify file URL works: https://shyamnair144-beepbeep.github.io/financial-tool/market-data.json

### **Issue: Yahoo Finance returns 0 or null**
**Fix**: Normal! Workflow has fallback values. NSE API will be tried next.

---

## 📝 Manual Testing Script

If you want to test the data fetch locally:

```bash
# Test Yahoo Finance API
curl -s 'https://query1.finance.yahoo.com/v8/finance/chart/%5ENSEI' | jq '.chart.result[0].meta.regularMarketPrice'

# Test NSE API
curl -s -H "User-Agent: Mozilla/5.0" 'https://www.nseindia.com/api/allIndices' | jq '.data[] | select(.index=="NIFTY 50")'
```

---

## 🎯 Next Steps

1. **Push the workflow** (Step 1 above)
2. **Run it manually** to test (Step 3 above)
3. **Wait for automatic run** tomorrow at 6:30 PM IST
4. **Monitor for a week** to ensure daily updates work

After 1 week of successful runs:
- Market data will update automatically
- No more CORS errors
- Always fresh data on your website

---

## ✨ Benefits

✅ **No CORS issues** - Runs server-side
✅ **Automatic daily updates** - Set and forget
✅ **Live market data** - Real Nifty prices, PE ratios
✅ **Free** - GitHub Actions free tier: 2000 minutes/month (this uses ~1 minute/day)
✅ **Reliable** - Runs even if your computer is off
✅ **Transparent** - All runs logged in Actions tab

---

*Setup complete! Your financial tool will now have fresh market data every evening.* 🚀
