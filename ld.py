import streamlit as st
import sympy as sp

# Title of the webpage will be Passion
st.title('Passion')

# Create a selectbox for the menu
menu = st.selectbox('Menu', ['Find limit of a function', 'Find derivative of a function'])

x = sp.symbols('x')

if menu == 'Find limit of a function':
    limit_point_str = st.text_input("Enter the limit point")
    expression_str = st.text_input("Enter the expression")

    if st.button('Calculate Limit'):
        try:
            limit_point = sp.simplify(limit_point_str)
            expression = sp.simplify(expression_str)
            result = sp.limit(expression, x, limit_point)
            st.write("Limit as x approaches(",limit_point,"):- ",result)
        except Exception as e:
            st.error(f'Error: {str(e)}')

elif menu == 'Find derivative of a function':
    fs = st.text_input("Enter a function")

    if st.button('Calculate Derivative'):
        try:
            f = sp.simplify(fs)
            df = sp.diff(f, x)
            simplified_df = sp.simplify(df)
            st.write("Derivative:- ", simplified_df)
        except Exception as e:
            st.error(f'Error: {str(e)}')
