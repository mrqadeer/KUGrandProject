import streamlit as st 
st.set_page_config("KU-ML",page_icon="💹",layout='wide')
import pandas as pd
import pickle 
with open("models\model.pkl",'rb') as file:
    model=pickle.load(file)
def main():
    st.header("KU Machine Learning")
    st.divider()
    col1=st.columns(5)
    col2=st.columns(5)
    # Age Income	Home	Emp_length	Intent	Amount	Rate	Percent_income	Default	Cred_length
    with col1[0]:
        age=st.number_input("Enter Age",min_value=2,max_value=99,key='age')
    with col1[1]:
        income=st.number_input("Enter Income",key='income')
        
    with col1[2]:
        home=st.text_input("Enter Home",placeholder='OWN,MORTGAGE, RENT, OTHER',key='home')
    with col1[3]:
        emp_length=st.number_input("Enter Employment Length",key='emp_length')
        
    with col1[4]:
        intent=st.text_input("Enter Loan Intension",placeholder='EDUCATION,MEDICAL,VENTURE,PERSONAL,HOMEIMPROVEMENT,DEBTCONSOLIDATION',key='intent')
    with col2[0]:
        amount=st.number_input("Enter Amount")
    with col2[1]:
        rate=st.number_input("Enter Rate")
        
        
    with col2[2]:
        perc_income=st.number_input("Enter Income Percentage",placeholder='income percentage')
    with col2[3]:
        default=st.text_input("Enter Default",placeholder='Y or N')
        
    with col2[4]:
        cred_length=st.number_input("Enter Credit Length",placeholder='credit lenght')
    
    # features names
    columns=['Age','Income','Home',
    'Emp_length',
    'Intent',
    'Amount',
    'Rate',
    'Percent_income',
    'Default',
    'Cred_length']
    data=[[age],[income],[home],[emp_length],[intent],[amount],[rate],[perc_income],[default],[cred_length]]
    inputs=pd.DataFrame(dict(zip(columns,data)))
    predict=st.button("Predict")
    if predict:
        predictions=prediction(inputs)[0]
        if predictions==1:
            st.write(f"Predicted: {predictions}")
            st.success("Congratulations you have got loan.")
        else:
            st.write(f"Predicted: {predictions}")
            st.error("Sorry you are not eligible for loan.")
def prediction(inputs):
    predictions=model.predict(inputs)
    return predictions
if __name__=="__main__":
    main()