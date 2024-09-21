#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. تست نرمالیتی (Normality Test)
# نصب کتابخانه‌های مورد نیاز
get_ipython().system('pip install pandas numpy scipy matplotlib seaborn')

# وارد کردن کتابخانه‌ها
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# ایجاد داده‌های واقعی‌تر برای تست نرمالیتی: دمای هوا در یک ماه
np.random.seed(42)
temperatures = [30, 32, 31, 33, 32, 30, 31, 30, 31, 32, 33, 34, 32, 33, 34, 32, 31, 33, 34, 35, 36, 37, 35, 34, 33, 32, 31, 30, 29, 28] 
temperatures = np.array(temperatures) + np.random.normal(0, 1, len(temperatures))  # اضافه کردن نویز به داده‌ها

# رسم هیستوگرام برای بررسی توزیع داده‌ها
plt.hist(temperatures, bins=10, edgecolor='k')
plt.title('Distribution of Daily Temperatures')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Frequency')
plt.show()

# انجام تست نرمالیتی
k2, p = stats.normaltest(temperatures)
print(f"Normality Test: Statistics={k2:.3f}, p-value={p:.3f}")
if p < 0.05:
    print("Data is not normally distributed.")
else:
    print("Data is normally distributed.")
    
    
    
    #2. تست همبستگی (Correlation Test)
    # ایجاد داده‌های واقعی‌تر برای تست همبستگی: قیمت بنزین و تعداد سفرهای خودرویی
np.random.seed(24)
gas_prices = [1.5, 1.6, 1.7, 1.8, 1.6, 1.5, 1.4, 1.3, 1.6, 1.7, 1.8, 1.9]
trips = [100, 98, 95, 90, 92, 94, 97, 99, 93, 91, 89, 88]

# اضافه کردن نویز به داده‌ها
gas_prices = np.array(gas_prices) + np.random.normal(0, 0.05, len(gas_prices))
trips = np.array(trips) + np.random.normal(0, 5, len(trips))

# رسم نمودار پراکندگی برای بررسی رابطه بین قیمت بنزین و تعداد سفرها
plt.scatter(gas_prices, trips)
plt.title('Scatter Plot of Gas Prices and Number of Trips')
plt.xlabel('Gas Price ($)')
plt.ylabel('Number of Trips')
plt.show()

# محاسبه ضریب همبستگی پیرسون
corr, p_value = stats.pearsonr(gas_prices, trips)
print(f"Correlation Test: Pearson's correlation = {corr:.3f}, p-value = {p_value:.3f}")




#3. تی‌تست (T-test)
# ایجاد داده‌های واقعی‌تر برای تی‌تست: میانگین زمان خواب دو گروه از دانشجویان
np.random.seed(6)
sleep_before_exams = np.random.normal(6, 0.5, 30)  # میانگین زمان خواب قبل از امتحانات
sleep_after_exams = np.random.normal(8, 0.6, 30)  # میانگین زمان خواب بعد از امتحانات

# رسم هیستوگرام مقایسه‌ای برای میانگین زمان خواب
plt.hist(sleep_before_exams, bins=10, alpha=0.5, label='Before Exams')
plt.hist(sleep_after_exams, bins=10, alpha=0.5, label='After Exams')
plt.title('Comparison of Sleep Duration Before and After Exams')
plt.xlabel('Sleep Duration (hours)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# انجام تی‌تست
t_stat, p_val = stats.ttest_ind(sleep_before_exams, sleep_after_exams)
print(f"T-test: t-statistic = {t_stat:.3f}, p-value = {p_val:.3f}")
if p_val < 0.05:
    print("There is a significant difference in the mean sleep duration before and after exams.")
else:
    print("There is no significant difference in the mean sleep duration before and after exams.")

    
    
    #4. آنووا (ANOVA)
    # ایجاد داده‌های واقعی‌تر برای آنووا: میانگین نمرات دانشجویان سه رشته مختلف
np.random.seed(9)
scores_science = np.random.normal(75, 10, 30)  # نمرات رشته علوم
scores_engineering = np.random.normal(80, 12, 30)  # نمرات رشته مهندسی
scores_arts = np.random.normal(70, 15, 30)  # نمرات رشته هنر

# رسم هیستوگرام برای مقایسه نمرات رشته‌های مختلف
plt.hist(scores_science, bins=10, alpha=0.5, label='Science')
plt.hist(scores_engineering, bins=10, alpha=0.5, label='Engineering')
plt.hist(scores_arts, bins=10, alpha=0.5, label='Arts')
plt.title('Comparison of Scores across Different Majors')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# انجام آنووا
f_stat, p_value_anova = stats.f_oneway(scores_science, scores_engineering, scores_arts)
print(f"ANOVA: F-statistic = {f_stat:.3f}, p-value = {p_value_anova:.3f}")
if p_value_anova < 0.05:
    print("There is a significant difference in the mean scores between the different majors.")
else:
    print("There is no significant difference in the mean scores between the different majors.")


# In[ ]:




