import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. قراءة ملف البيانات
df = pd.read_csv('retail_sales_dataset.csv')

# 2. حساب مصفوفة الارتباط الإحصائي للأعمدة العددية (العمر، الكمية، سعر الوحدة، الإجمالي)
numeric_df = df[['Age', 'Quantity', 'Price per Unit', 'Total Amount']]
correlation_matrix = numeric_df.corr()

print("--- مصفوفة الارتباط الإحصائي (Correlation Matrix) ---")
print(correlation_matrix)

# 3. تصميم وتوليد خريطة الارتباط الحرارية (Correlation Heatmap)
sns.set_theme(style="white")
plt.figure(figsize=(8, 6))

# رسم الـ Heatmap مع إظهار الأرقام بدقة
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, cbar=True)

plt.title("Advanced Correlation Heatmap - Retail Sales", fontsize=14, fontweight='bold')

# حفظ الصورة بدقة عالية لتضاف إلى مستودع GitHub
plt.savefig("correlation_heatmap.png", dpi=300)
print("\nتم إنشاء وحفظ خريطة الارتباط الحرارية بنجاح باسم correlation_heatmap.png!")

plt.show()