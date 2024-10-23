from flask import Flask, render_template, url_for, request
from model.classifier import Model
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("homepage.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        data = {}

        # Retrieve form data
        customer_age = int(request.form["Customer_Age"])
        dependent_count = int(request.form["Dependent_count"]) 
        education_level =  request.form["Education_Level"]
        income_category =  request.form["Income_Category"]
        card_category =  request.form["Card_Category"]
        months_on_book = int(request.form["Months_on_book"]) 
        total_relationship_count = int(request.form["Total_Relationship_Count"]) 
        months_inactive_12_mon = int(request.form["Months_Inactive_12_mon"]) 
        contacts_count_12_mon = int(request.form["Contacts_Count_12_mon"]) 
        credit_limit = float(request.form["Credit_Limit"]) 
        total_revolving_bal = int(request.form["Total_Revolving_Bal"]) 
        avg_open_to_buy = float(request.form["Avg_Open_To_Buy"]) 
        total_amt_chng_q4_q1 = float(request.form["Total_Amt_Chng_Q4_Q1"]) 
        total_trans_amt = int(request.form["Total_Trans_Amt"]) 
        total_trans_ct = int(request.form["Total_Trans_Ct"]) 
        total_ct_chng_q4_q1 = float(request.form["Total_Ct_Chng_Q4_Q1"]) 
        avg_utilization_ratio = float(request.form["Avg_Utilization_Ratio"]) 
        gender = request.form["Gender"]
        marital_status = request.form["Marital_Status"]

        data = {'Customer_Age':customer_age, 
                'Dependent_count': dependent_count, 
                'Education_Level' :education_level, 
                'Income_Category' :income_category,
                'Card_Category' :card_category, 
                'Months_on_book' :months_on_book, 
                'Total_Relationship_Count' :total_relationship_count,
                'Months_Inactive_12_mon' :months_inactive_12_mon, 
                'Contacts_Count_12_mon' :contacts_count_12_mon, 
                'Credit_Limit' :credit_limit,
                'Total_Revolving_Bal' :total_revolving_bal,
                'Avg_Open_To_Buy' :avg_open_to_buy, 
                'Total_Amt_Chng_Q4_Q1' :total_amt_chng_q4_q1,
                'Total_Trans_Amt' :total_trans_amt,
                'Total_Trans_Ct' : total_trans_ct, 
                'Total_Ct_Chng_Q4_Q1' :total_ct_chng_q4_q1,
                'Avg_Utilization_Ratio' : avg_utilization_ratio, 
                'Gender' : gender, 
                'Marital_Status': marital_status
                }
        
        df = pd.DataFrame(data, index=[0])
        # Log the input for debugging
        # print(customer_age, dependent_count, education_level, income_category, "ce sont mes data")

        # Pass all the inputs to your prediction function
        prediction = Model.Churner(df)

        return render_template("form.html", prediction=prediction)
    else:
        return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
