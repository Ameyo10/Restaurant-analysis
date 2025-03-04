# 🍽️ Restaurant Performance & Customer Behavior Analysis  

## **📝 Problem Statement**  
A restaurant chain wants to analyze its **sales, customer behavior, and operational efficiency** using data from multiple sources.  
This project focuses on **fetching, cleaning, analyzing, and visualizing** restaurant data to extract meaningful insights.  

---

## **🔹 Task Breakdown**  

### **1️⃣ Fetch Customer Reviews & Ratings (requests, json, os, files)**  
- Use the `requests` module to fetch **customer review data** from a public API:  
  🔗 [API Link](https://jsonplaceholder.typicode.com/comments)  
- Save the data as a JSON file (`reviews.json`).  
- Load and extract **relevant fields** (`name, email, and review body`).  

### **2️⃣ Load and Clean Restaurant Sales Data (pandas, numpy, datetime, files)**  
- Read **`restaurant_sales.csv`** into a **Pandas DataFrame**.  
- Convert the **date column** to `datetime` format.  
- Handle **missing values** using NumPy (`numpy.nan` replacement).  
- Add a new column **"day_of_week"** based on the date.  

### **3️⃣ Analyze Customer Spending Behavior (math, random, dictionary)**  
- Create a **dictionary** storing random customer discounts (`5% to 20%`) for VIP customers.  
- Compute **discounted bills** using mathematical functions.  

### **4️⃣ Data Visualization & Insights (matplotlib, seaborn)**  
- 📈 **Line Plot:** Total sales trend over time (`matplotlib`).  
- 🔹 **Scatter Plot:** Relationship between **total bill and tips** (`seaborn`).  
- 🔥 **Heatmap:** Correlation matrix of **sales data**.  

### **5️⃣ Store Analyzed Data into MySQL Database (mysql-connector-python)**  
- Create a **MySQL table `restaurant_performance`** if it doesn’t exist.  
- Insert **cleaned and aggregated data** into MySQL for further analysis.  

---

## **📂 Provided Files for This Task**  
📌 `restaurant_sales.csv` → Contains columns: `date, total_bill, tip, customer_id, food_category`  
📌 `menu.json` → Contains **menu items and their prices**  
📌 `reviews.json` → **Fetched from API**  

---

## **🚀 How to Run the Project?**  

### **🔹 Prerequisites**  
Ensure you have the following **Python libraries installed**:  
```bash
pip install pandas numpy matplotlib seaborn mysql-connector-python requests
