# 📊 Exploratory Data Analysis - Key Insights

**Analysis Date**: 2025-10-22 10:38

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

- [regional_emergency_visits.html](visualization/regional_emergency_visits.html)
- [yearly_trends.html](visualization/yearly_trends.html)
- [regional_demand.html](visualization/regional_demand.html)
- [learning_curves.html](visualization/learning_curves.html)
- [model_diagnostics_dashboard.html](visualization/model_diagnostics_dashboard.html)
- [model_comparison.html](visualization/model_comparison.html)
- [epidemic_peaks.html](visualization/epidemic_peaks.html)
- [forecast_comparison.html](visualization/forecast_comparison.html)
- [feature_importance_analysis.html](visualization/feature_importance_analysis.html)
- [seasonality_by_month.html](visualization/seasonality_by_month.html)
- [emergency_visits_timeline.html](visualization/emergency_visits_timeline.html)
- [regional_heatmap.html](visualization/regional_heatmap.html)
- [model_r2_comparison.html](visualization/model_r2_comparison.html)
- [allocation_by_region.html](visualization/allocation_by_region.html)
- [coverage_by_region.html](visualization/coverage_by_region.html)
