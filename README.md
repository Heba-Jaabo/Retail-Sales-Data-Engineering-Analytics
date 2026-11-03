# Retail Sales Data Engineering, Advanced Analytics & Power BI Dashboard

An end-to-end Data Engineering and Analytics project focused on designing a relational database architecture, running advanced analytical SQL queries, conducting statistical Exploratory Data Analysis (EDA) in Python, and building an interactive dashboard in Power BI.

---

## 🚀 Project Overview
This project models the complete data lifecycle for retail sales transactions:
1. **Data Architecture & Relational Engineering (Star Schema):** Structured raw transaction data into a robust **Star Schema** using SQLite, isolating entities into dimension tables (`Dim_Customers`, `Dim_Products`) and a factual table (`Fact_Sales`).
2. **Advanced SQL Insights:** Applied advanced SQL queries using **Window Functions** (e.g., `ROW_NUMBER`, `RANK`) and **Common Table Expressions (CTEs)** to analyze revenue distributions and category performance.
3. **Statistical EDA (Python):** Conducted correlation analysis using Pandas, Matplotlib, and Seaborn to compute feature dependencies and generate a high-resolution **Correlation Heatmap**.
4. **Interactive Power BI Dashboard:** Built a clean visual dashboard featuring Key Performance Indicators (KPIs), category breakdowns, and dynamic interactive slicers for business analysis.

---

## 🛠️ Tech Stack
* **Language & Analysis:** Python (Pandas, NumPy, Matplotlib, Seaborn)
* **Database & Querying:** SQLite3, SQL (Star Schema, Window Functions, CTEs, Aggregations)
* **Business Intelligence:** Power BI Desktop (Interactive KPI Cards, Column Charts, Visual Slicers)
* **Tools & Environment:** VS Code, Git, GitHub

---

## 📁 Repository Structure
```text
├── retail_sales_dataset.csv          # Original raw dataset
├── retail_store_advanced.db         # Engineered SQLite database (Star Schema)
├── p.py                             # Data pipeline, database setup & SQL execution script
├── correlation_heatmap.py           # Statistical analysis & heat map generator
├── sales_insights.png               # EDA visualization charts
├── correlation_heatmap.png          # High-resolution correlation heat map
├── retail_sales_dashboard.pbix      # Interactive Power BI Dashboard file
└── README.md                        # Complete project documentation
