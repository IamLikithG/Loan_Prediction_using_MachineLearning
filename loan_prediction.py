from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from tkinter import *
import pandas as pd

# Load the data
data = pd.read_csv('F:\My Projects\LPrediction\Datasets\LoanApprovalPrediction.csv')

# Fill missing values
data.fillna(method='ffill', inplace=True)

# Encode categorical features
categorical_features = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
le = LabelEncoder()
for feature in categorical_features:
    data[feature] = le.fit_transform(data[feature])

# Split the data into independent and dependent variables
X = data.drop(columns=['Loan_Status'])
y = data['Loan_Status']

# Create a random forest classifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X, y)

# Create the GUI
root = Tk()
root.title('Loan Prediction')
root.geometry('500x300')

# Create the input fields and labels
gender = StringVar(root)
gender.set('Male')
gender_label = Label(root, text='Gender:')
gender_label.grid(row=0, column=0)
gender_menu = OptionMenu(root, gender, 'Male', 'Female')
gender_menu.grid(row=0, column=1)

married = StringVar(root)
married.set('No')
married_label = Label(root, text='Married:')
married_label.grid(row=1, column=0)
married_menu = OptionMenu(root, married, 'Yes', 'No')
married_menu.grid(row=1, column=1)

dependents = StringVar(root)
dependents.set('0')
dependents_label = Label(root, text='Dependents:')
dependents_label.grid(row=2, column=0)
dependents_menu = OptionMenu(root, dependents, '0', '1', '2', '3+')
dependents_menu.grid(row=2, column=1)

education = StringVar(root)
education.set('Graduate')
education_label = Label(root, text='Education:')
education_label.grid(row=3, column=0)
education_menu = OptionMenu(root, education, 'Graduate', 'Not Graduate')
education_menu.grid(row=3, column=1)

self_employed = StringVar(root)
self_employed.set('No')
self_employed_label = Label(root, text='Self Employed:')
self_employed_label.grid(row=4, column=0)
self_employed_menu = OptionMenu(root, self_employed, 'Yes', 'No')
self_employed_menu.grid(row=4, column=1)

applicant_income_label = Label(root, text='Applicant Income:')
applicant_income_label.grid(row=5, column=0)
applicant_income = Entry(root)
applicant_income.grid(row=5, column=1)

coapplicant_income_label = Label(root, text='Coapplicant Income:')
coapplicant_income_label.grid(row=6, column=0)
coapplicant_income = Entry(root)
coapplicant_income.grid(row=6, column=1)

loan_amount_label = Label(root, text='Loan Amount:')
loan_amount_label.grid(row=7, column=0)
loan_amount = Entry(root)
loan_amount.grid(row=7, column=1)

loan_term_label = Label(root, text='Loan Term:')
loan_term_label.grid(row=8, column=0)
loan_term = Entry(root)
loan_term.grid(row=8, column=1)

credit_history = StringVar(root)
credit_history.set('1')
credit_history_label = Label(root, text='Credit History:')
credit_history_label.grid(row=9, column=0)
credit_history_menu = OptionMenu(root, credit_history, '0', '1')
credit_history_menu.grid(row=9, column=1)

def predict_loan():
# Get the user input
    gender_val = gender.get()
    married_val = married.get()
    dependents_val = dependents.get()
    education_val = education.get()
    self_employed_val = self_employed.get()
    applicant_income_val = float(applicant_income.get())
    coapplicant_income_val = float(coapplicant_income.get())
    loan_amount_val = float(loan_amount.get())
    loan_term_val = float(loan_term.get())
    credit_history_val = credit_history.get()


    # Encode the user input
    gender_val = le.transform([gender_val])[0]
    married_val = le.transform([married_val])[0]
    dependents_val = le.transform([dependents_val])[0]
    education_val = le.transform([education_val])[0]
    self_employed_val = le.transform([self_employed_val])[0]

    # Make the prediction
    prediction = model.predict([[gender_val, married_val, dependents_val, education_val, self_employed_val, applicant_income_val, coapplicant_income_val, loan_amount_val, loan_term_val, credit_history_val]])

    # Show the prediction result
    if prediction[0] == 1:
        result = 'Approved'
    else:
        result = 'Rejected'
        
    result_label = Label(root, text=f'Loan Status: {result}', font=('Helvetica', 16))
    result_label.grid(row=11, column=0, columnspan=2)

    predict_button = Button(root, text='Predict', command=predict_loan)
    predict_button.grid(row=10, column=0, columnspan=2, pady=10)


root.mainloop()




