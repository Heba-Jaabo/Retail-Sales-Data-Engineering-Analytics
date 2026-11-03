import sqlite3
import pandas as pd

# 1. قراءة البيانات الأصلية
df = pd.read_csv('retail_sales_dataset.csv')

# 2. إنشاء الاتصال بقاعدة البيانات المتقدمة
conn = sqlite3.connect('retail_store_advanced.db')
cursor = conn.cursor()

# 3. تصميم وهندسة جداول الـ Star Schema
# أ. جدول العملاء (Dim_Customers)
dim_customers = df[['Customer ID', 'Gender', 'Age']].drop_duplicates().reset_index(drop=True)
dim_customers.to_sql('Dim_Customers', conn, if_exists='replace', index=False)

# ب. جدول المنتجات (Dim_Products)
dim_products = df[['Product Category', 'Price per Unit']].drop_duplicates().reset_index(drop=True)
dim_products.to_sql('Dim_Products', conn, if_exists='replace', index=False)

# ج. جدول المعاملات الأساسي (Fact_Sales)
fact_sales = df[['Transaction ID', 'Date', 'Customer ID', 'Product Category', 'Quantity', 'Total Amount']]
fact_sales.to_sql('Fact_Sales', conn, if_exists='replace', index=False)

print("تم تصميم وهندسة قاعدة البيانات (Star Schema) بنجاح وإعادة بناء الجداول!")

# ==========================================
# 4. تنفيذ استعلامات SQL متقدمة (Advanced SQL)
# ==========================================

print("\n--- 1. تحليل باستخدام Window Functions (ترتيب المعاملات حسب السعر ضمن كل فئة) ---")
query_window = """
SELECT 
    "Transaction ID",
    "Product Category",
    "Total Amount",
    ROW_NUMBER() OVER(PARTITION BY "Product Category" ORDER BY "Total Amount" DESC) as Rank_In_Category
FROM Fact_Sales
LIMIT 6;
"""
print(pd.read_sql(query_window, conn))


print("\n--- 2. تحليل باستخدام CTEs (المبيعات التراكمية أو المتوسطات المتقدمة) ---")
query_cte = """
WITH CategorySales AS (
    SELECT 
        "Product Category",
        SUM("Total Amount") AS Cat_Total
    FROM Fact_Sales
    GROUP BY "Product Category"
)
SELECT 
    "Product Category",
    Cat_Total,
    (Cat_Total * 100.0 / (SELECT SUM(Cat_Total) FROM CategorySales)) AS Sales_Percentage
FROM CategorySales
ORDER BY Cat_Total DESC;
"""
print(pd.read_sql(query_cte, conn))

conn.close()