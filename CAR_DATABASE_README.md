# Car Database Management

## Overview
This car database contains **15 Petrol Automatic vehicles** suitable for company lease in the ₹16-20L on-road range (Bangalore).

## Update Schedule
- **Frequency**: Monthly (1st of every month)
- **Method**: GitHub Actions reminder + manual review
- **Automation**: Timestamp updates automatically, prices reviewed manually

## How It Works

### 1. Automated Monthly Check (GitHub Actions)
- Runs on 1st of every month at 2 AM IST
- Updates timestamp in `car-database.json`
- Serves as reminder to review prices

### 2. Manual Price Updates (When Needed)
When car prices change:
1. Go to [car-database.json](car-database.json) on GitHub
2. Click "Edit" button
3. Update changed prices
4. Commit changes

### 3. What to Update Monthly

Check these sources for price changes:
- [ZigWheels](https://www.zigwheels.com/new-cars)
- [CarWale](https://www.carwale.com/new-cars)
- Manufacturer websites

Update if:
- Ex-showroom price changed
- New variant launched
- Old variant discontinued
- Specifications changed

## Current Database (March 2026)

### Compact SUVs (₹12-17L)
1. Hyundai Venue (AT)
2. Maruti Brezza (AT)
3. Tata Nexon (AT)
4. Kia Sonet (AT)

### Mid-Size SUVs (₹17-26L)
5. Hyundai Creta (AT)
6. Kia Seltos (AT)
7. Maruti Grand Vitara (Hybrid AT)
8. Skoda Kushaq (AT)
9. MG Astor (CVT)
10. Toyota Hyryder (Hybrid AT)
11. Mahindra XUV700 (AT)

### Sedans (₹16-25L)
12. Honda City Hybrid (e-CVT)
13. Hyundai Verna (AT)
14. Volkswagen Virtus (AT)
15. Skoda Slavia (AT)

## On-Road Price Calculation

Formula for Bangalore:
```
On-Road = Ex-Showroom + RTO (13%) + Insurance (8%) + Other (2%)
On-Road = Ex-Showroom × 1.23
```

Other cities:
- Delhi: 1.19x
- Mumbai: 1.23x
- Chennai: 1.23x
- Hyderabad: 1.21x
- Pune: 1.23x

## Filter Criteria

All cars in database meet these criteria:
- ✅ Fuel: Petrol only
- ✅ Transmission: Automatic (AT/DCT/CVT/e-CVT)
- ✅ Availability: Currently on sale (March 2026)
- ✅ Target Range: ₹12-26L on-road (Bangalore)
- ✅ Suitability: Company lease eligible

## Manual Update Process

### Step-by-Step:

1. **Check ZigWheels for price changes:**
   ```
   https://www.zigwheels.com/hyundai-cars/creta/
   https://www.zigwheels.com/kia-cars/seltos/
   ... (check all 15 cars)
   ```

2. **Update car-database.json:**
   - Find the car entry
   - Update `exShowroom` price
   - Update variant prices if changed
   - Update `lastUpdated` date

3. **Commit changes:**
   ```
   git add car-database.json
   git commit -m "Update car prices - [Month Year]"
   git push
   ```

## Quick Price Check Template

Monthly checklist:
```
[ ] Hyundai Creta - Check ex-showroom: ₹14.5L (current)
[ ] Kia Seltos - Check ex-showroom: ₹14.2L (current)
[ ] Tata Nexon - Check ex-showroom: ₹11.2L (current)
[ ] Maruti Brezza - Check ex-showroom: ₹10.95L (current)
[ ] Skoda Kushaq - Check ex-showroom: ₹15.5L (current)
... (all 15 cars)
```

## Notes

- Car prices typically change every 3-6 months
- New model year launches happen around September-October
- Festive discounts (Oct-Nov, Feb-Mar) don't need database update
- Focus on ex-showroom price, tool calculates on-road automatically

## Troubleshooting

**If scraper fails (future implementation):**
- Fallback to manual update
- Database remains usable with last known prices
- Update manually using steps above

**If new car launches:**
- Add to `cars` array in car-database.json
- Follow existing structure
- Ensure Petrol Automatic variant only

---

*Last manual review: March 2026*
*Next review: April 2026 (automated reminder)*
