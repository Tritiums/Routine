from scipy import stats

x=[47.7, 34.5, 41.6, 34.1, 36.3, 45.2, 49.2, 34.0, 44.2, 40.5, 41.5, 32.2]
y=[49.7, 57.2, 48.3, 59.1, 47.7, 57.5, 56.6, 50.5, 56.7, 43.5, 51.8, 56.9]
z=[84.4, 70.1, 68.0, 73.7, 75.5, 80.3, 82.9, 79.1, 63.2, 71.1, 69.6, 72.4]

anova_result=stats.f_oneway(x,y,z)

print('ANOVA is: ',anova_result)