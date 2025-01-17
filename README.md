# Rock vs Mine Predictor

This is a machine learning-based web application built with **Streamlit** to predict whether an object is a **Rock** or a **Mine** based on 60 input features. The model is trained using a machine learning algorithm (logistic regression).

![image](https://github.com/user-attachments/assets/4ef1d29a-e734-40f4-9c11-c2aa4d5b4749)

![image](https://github.com/user-attachments/assets/cda8d763-0256-4017-b4e8-edd5ddfbca74)

## Features

- Input up to 60 features using a number input field.
- Automatically generate random values for all features with a click of a button.
- Predict the object type (Rock or Mine) based on the input values.

## Requirements

Before running the app, make sure to install the following dependencies:

- Python 3.x
- Streamlit
- Scikit-learn
- NumPy
- Pandas

### To install the requirements, run:

```bash
pip install -r requirements.txt
```

##Setup
Clone the repository:
```bash
git clone https://github.com/your-username/rock-vs-mine-predictor.git
cd rock-vs-mine-predictor
```
Install the necessary dependencies using:
```bash
pip install -r requirements.txt
```
Make sure the model file rock_vs_mine_model.pkl is in the root of the project directory.
You're all set! Now you can run the app by executing:
```bash
streamlit run app.py
```
