import tkinter as tk
from tkinter import messagebox
import joblib

def predict_loan():
    # Get input values from GUI
    gender = gender_var.get()
    married = married_var.get()
    dependents = dependents_var.get()
    education = education_var.get()
    self_employed = self_employed_var.get()
    applicant_income = float(applicant_income_entry.get())
    coapplicant_income = float(coapplicant_income_entry.get())
    loan_amount = float(loan_amount_entry.get()) if loan_amount_entry.get() else None
    loan_term = int(loan_term_entry.get())
    credit_history = credit_history_var.get()
    property_area = property_area_var.get()
    
    # Handle missing loan_amount value
    if loan_amount is None:
        # Generate a random value between 1000 and 5000
        loan_amount = random.randint(1000, 5000)
        # Update the GUI with the random loan amount
        loan_amount_entry.delete(0, tk.END)
        loan_amount_entry.insert(0, loan_amount)
    
    # Load trained model
    model = joblib.load('F:/My Projects/LPrediction/pklFiles/RandomForestClassifier_loan_prediction_model.pkl')
    
    # Make prediction
    prediction = model.predict([[gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, 
                                  loan_amount, loan_term, credit_history, property_area]])
    
    # Update output label with prediction
    output_label.configure(text="Loan Status: {}".format(prediction[0]))

# Load the machine learning model
# model = joblib.load('F:/My Projects/LPrediction/pklFiles/RandomForestClassifier_loan_prediction_model.pkl')


# # Create a function to make the loan prediction
# def predict_loan():
#     gender = gender_var.get()
#     married = married_var.get()
#     dependents = dependents_var.get()
#     education = education_var.get()
#     self_employed = self_employed_var.get()
#     applicant_income = float(applicant_income_entry.get())
#     coapplicant_income = float(coapplicant_income_entry.get())
#     loan_amount = float(loan_amount_entry.get())
#     loan_term = float(loan_term_entry.get())
#     credit_history = credit_history_var.get()
#     property_area = property_area_var.get()

#     # Make the loan prediction
#     prediction = model.predict([[gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_term, credit_history, property_area]])

#     # Display the loan prediction result
#     messagebox.showinfo('Loan Prediction', f'The loan prediction is {prediction[0]}')

# Create the GUI
root = tk.Tk()
root.title('Loan Prediction')

# Create the input fields
gender_var = tk.StringVar(value='Male')
tk.Label(root, text='Gender').grid(row=0, column=0)
tk.OptionMenu(root, gender_var, 'Male', 'Female').grid(row=0, column=1)

married_var = tk.StringVar(value='No')
tk.Label(root, text='Married').grid(row=1, column=0)
tk.OptionMenu(root, married_var, 'No', 'Yes').grid(row=1, column=1)

dependents_var = tk.StringVar(value='0')
tk.Label(root, text='Dependents').grid(row=2, column=0)
tk.OptionMenu(root, dependents_var, '0', '1', '2', '3+').grid(row=2, column=1)

education_var = tk.StringVar(value='Not Graduate')
tk.Label(root, text='Education').grid(row=3, column=0)
tk.OptionMenu(root, education_var, 'Not Graduate', 'Graduate').grid(row=3, column=1)

self_employed_var = tk.StringVar(value='No')
tk.Label(root, text='Self Employed').grid(row=4, column=0)
tk.OptionMenu(root, self_employed_var, 'No', 'Yes').grid(row=4, column=1)

applicant_income_entry = tk.Entry(root)
tk.Label(root, text='Applicant Income').grid(row=5, column=0)
applicant_income_entry.grid(row=5, column=1)

coapplicant_income_entry = tk.Entry(root)
tk.Label(root, text='Coapplicant Income').grid(row=6, column=0)
coapplicant_income_entry.grid(row=6, column=1)

loan_amount_entry = tk.Entry(root)
tk.Label(root, text='Loan Amount').grid(row=7, column=0)
loan_amount_entry.grid(row=7, column=1)

loan_term_entry = tk.Entry(root)
tk.Label(root, text='Loan Term').grid(row=8, column=0)
loan_term_entry.grid(row=8, column=1)

credit_history_var = tk.StringVar(value='1')
tk.Label(root, text='Credit History').grid(row=9, column=0)
tk.OptionMenu(root, credit_history_var, '0','1').grid(row=9, column=1)

property_area_var = tk.StringVar(value='Urban')
tk.Label(root, text='Property Area').grid(row=10, column=0)
tk.OptionMenu(root, property_area_var, 'Rural', 'Semiurban', 'Urban').grid(row=10, column=1)

predict_button = tk.Button(root, text='Predict', command=predict_loan)
predict_button.grid(row=11, column=0, columnspan=2)

root.mainloop()
