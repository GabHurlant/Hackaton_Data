#  Exploratory Data Analysis - Key Insights

**Analysis Date**: 2025-10-22 12:12

---

## 1️ - Seasonality

- **Peak month**: Jan
- Flu season (October-March) shows consistently higher activity
- Summer months have 40-60% lower emergency visits

## 2️ - Regional Patterns

- **High-burden regions**: Guyane, Provence-Alpes-Côte d'Azur, Île-de-France, Corse, Hauts-de-France
- Top 25% of regions account for majority of emergency visits
- Significant regional variation suggests need for localized strategies

## 3️ - Epidemic Patterns

- Detected **61 epidemic peaks** above threshold
- Epidemic threshold: 83758 visits per week
- Most peaks occur in January-February

## 4️ - Recommendations

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

##  Visualizations Generated

- [allocation_by_region.html](visualizations/allocation_by_region.html)
- [coverage_by_region.html](visualizations/coverage_by_region.html)
- [dashboard_financial_impact.html](visualizations/dashboard_financial_impact.html)
- [dashboard_forecast_performance.html](visualizations/dashboard_forecast_performance.html)
- [dashboard_implementation_roadmap.html](visualizations/dashboard_implementation_roadmap.html)
- [dashboard_kpis.html](visualizations/dashboard_kpis.html)
- [dashboard_regional_priorities.html](visualizations/dashboard_regional_priorities.html)
- [dashboard_seasonal_timing.html](visualizations/dashboard_seasonal_timing.html)
- [emergency_visits_timeline.html](visualizations/emergency_visits_timeline.html)
- [epidemic_peaks.html](visualizations/epidemic_peaks.html)
- [feature_importance_analysis.html](visualizations/feature_importance_analysis.html)
- [forecast_comparison.html](visualizations/forecast_comparison.html)
- [learning_curves.html](visualizations/learning_curves.html)
- [model_comparison.html](visualizations/model_comparison.html)
- [model_diagnostics_dashboard.html](visualizations/model_diagnostics_dashboard.html)
- [model_performance_dashboard.html](visualizations/model_performance_dashboard.html)
- [model_r2_comparison.html](visualizations/model_r2_comparison.html)
- [regional_demand.html](visualizations/regional_demand.html)
- [regional_emergency_visits.html](visualizations/regional_emergency_visits.html)
- [regional_heatmap.html](visualizations/regional_heatmap.html)
- [seasonality_by_month.html](visualizations/seasonality_by_month.html)
- [yearly_trends.html](visualizations/yearly_trends.html)
