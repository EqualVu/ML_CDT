# %%
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

#Load Excel File
df = pd.read_csv('D:\\Study stuff\\Machine Learning\\datasets\\advertising.csv')

#Display Basic Information
print(df.head())
print(df.describe())


# %%
# Preprocess the data
df = df.dropna()  # Handle missing values
df = pd.get_dummies(df, drop_first=True)  # Encode categorical variables

x = df[['TV','Radio','Newspaper']]
y = df['Sales']

# %%
# Split the data
z = df.iloc[:, :]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# %%
# Train the classification model
model = SVR(kernel='linear') #other kernel like 'rbf', 'poly'
model.fit(x_train, y_train)


# %%
# Make predictions and evaluate the model
y_pred = model.predict(x_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# %%
# Predict sales
new_data = pd.DataFrame({
    'TV': [100],
    'Radio': [25],
    'Newspaper': [20]
})
predicted_sales = model.predict(new_data)
print(f'Predicted Sales: {predicted_sales[0]}')

# Show in streamlit
st.title('Predict Sales in Streamlit')
st.header('by =')
st.markdown('[My GitHub](https://github.com/EqualVu/ML_CDT/tree/baihoctuan/t4)')

st.divider()
n_tv = st.number_input('Input TV Advertising Budget', value=100, min_value=0)
n_radio = st.number_input('Input Radio Advertising Budget', value=25, min_value=0)
n_news = st.number_input('Input Newspaper Advertising Budget', value=20, min_value=0)
if st.button('Predict'):
    new_data = pd.DataFrame({
        'TV': [n_tv],
        'Radio': [n_radio],
        'Newspaper': [n_news]
})
predicted_sales = model.predict(new_data)

st.divider()
st.success(f'Predicted Sales: {predicted_sales[0]:.2f}')