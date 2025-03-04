import requests as rq
import json
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql

# Fetching data using requests
response = rq.get('https://jsonplaceholder.typicode.com/comments')

# Checking if the response is successful
if response.status_code == 200:
    json_data = response.json()  # Convert response to JSON format
    
    # Saving the data as JSON file
    with open('review.json', 'w') as file:
        json.dump(json_data, file, indent=4)
    
    print("Data fetched and saved successfully!")

    # Loading the data from the JSON file
    with open('review.json', 'r') as file:
        data = json.load(file)

    # Extracting the relevant fields from the first 5 entries
    for review in data[:5]:  
        print(f"\n\bName: {review['name']},\n \bEmail: {review['email']},\n \bBody: {review['body']} \n")
    
    #Load Restaurant Sales data
    sales_df = pd.read_csv('restaurant_sales.csv')
    
    #Convert date column to datetime-format
    sales_df['date'] = pd.to_datetime(sales_df['date'])

    #Handling the missing values using Numpy
    sales_df.replace("", np.nan, inplace= True)

    #Adding a new column 'day_of_week' based on date
    sales_df['day_of_week'] = sales_df['date'].dt.day_name()
    
    # Identify VIP customers (Customers spending more than $500 in total)
    vip_customers = sales_df.groupby("customer_id")["total_bill"].sum()
    vip_customers = vip_customers[vip_customers > 500].index.tolist()

    # Add a new column 'VIP' (True if the customer is in the VIP list)
    sales_df["VIP"] = sales_df["customer_id"].isin(vip_customers)

    disc = {customer_id: random.randint(5, 20) for customer_id in vip_customers}
    
    # Computing discounted bills using a lambda function
    sales_df['Discounted_Bill'] = sales_df.apply(
        lambda row: row['total_bill'] * (1 - disc.get(row['customer_id'], 0) / 100),
        axis=1
        )
    
    #Re-inserting the values back into csv file
    sales_df.to_csv('restaurant_sales.csv', index = False)
    # Grouping the sales data by date and summing the total bill
    sales_trend = sales_df.groupby('date')['total_bill'].sum()

    # Line plot showing the total sales trend over time
    plt.figure(figsize=(12, 6))
    plt.plot(sales_trend.index, sales_trend.values, marker='o', label='Total Sales')

    # Formatting
    plt.title('Line Plot Showing the Trend in Sales Over Time', fontsize=20, fontweight='bold')
    plt.xlabel('Dates', fontsize=12)
    plt.ylabel('Total Sales', fontsize=12)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.legend()
    plt.grid(True, alpha=0.5)
    plt.show()

    #Relationship between Total Bill and tips
    sns.scatterplot(data = sales_df, x = 'total_bill', y = 'tip')
    plt.title('Relationship between Total Bill and Tips')
    plt.grid(True, alpha=0.5)
    plt.show()

    #Correlation matrix
    corr_matrix = sales_df.select_dtypes(include= ['number']).corr()

    #Heatmap using the correlation matrix
    sns.heatmap(corr_matrix, annot= True, cmap= 'coolwarm', linewidths= 0.5)
    plt.title('Correlation matrix of sales data')
    plt.show()

    try:
        # Establish connection
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="P@why@1d",
            database="mydatabase"
            )
        cursor = conn.cursor()
        # Define query
        query = """
        INSERT INTO restaurant_performance 
        (Customer_id, Food_Category, Date, WeekDay, Total_Bill, Tip, Discounted_Bill) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Convert date column to datetime.date before looping
        sales_df['date'] = sales_df['date'].dt.date

        # Insert values
        for _, row in sales_df.iterrows():
            cursor.execute(query, (
                row['customer_id'],
                row['food_category'],
                row['date'],
                row['day_of_week'],
                row['total_bill'],
                row['tip'],
                row['Discounted_Bill']
                ))
        
        # Commit transaction
        conn.commit()

        if cursor:
            cursor.close()

        if conn:
            conn.close()

    
    except pymysql.MySQLError as err:
        print(f"Error: {err}")

        

else:
    print(f"Failed to fetch data! Status Code: {response.status_code}")
