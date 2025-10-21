# 📊 Exploratory Data Analysis - Key Insights

**Analysis Date**: 2025-10-21 15:06

---

## 1️⃣ Seasonality

- **Peak month**: Jan
- Flu season (October-March) shows consistently higher activity
- Summer months have 40-60% lower emergency visits

## 2️⃣ Regional Patterns

- **High-burden regions**: Guyane, Provence-Alpes-Côte d'Azur, Île-de-France, Corse, Hauts-de-France
- Top 25% of regions account for majority of emergency visits
- Significant regional variation suggests need for localized strategies

## 3️⃣ Epidemic Patterns

- Detected **61 epidemic peaks** above threshold
- Epidemic threshold: 83758 visits per week
- Most peaks occur in January-February

## 4️⃣ Recommendations

### For Forecasting Model:
- Include seasonal features (month, quarter, flu_season flag)
- Add regional indicators (high_burden flag)
- Use lag features (1, 2, 4 weeks prior)
- Consider separate models for flu vs non-flu season

### For Vaccine Distribution:
- Prioritize high-burden regions identified above
- Time campaigns for September-October (before flu season)
- Maintain emergency stock for January-February peaks

---

## 📊 Visualizations Generated

- [emergency_visits_timeline.html](visualizations/emergency_visits_timeline.html)
- [epidemic_peaks.html](visualizations/epidemic_peaks.html)
- [forecast_comparison.html](visualizations/forecast_comparison.html)
- [model_performance_dashboard.html](visualizations/model_performance_dashboard.html)
- [regional_emergency_visits.html](visualizations/regional_emergency_visits.html)
- [regional_heatmap.html](visualizations/regional_heatmap.html)
- [seasonality_by_month.html](visualizations/seasonality_by_month.html)
- [yearly_trends.html](visualizations/yearly_trends.html)
