import streamlit as st
import sympy as sp

# Title of the webpage will be Passion
st.title('Limits And Derivatives')

# Create a selectbox for the menu
menu = st.sidebar.selectbox('Menu', ['Find limit of a function', 'Find derivative of a function'])

x = sp.symbols('x')

# Keypad buttons for mathematical symbols and operators
keypad_buttons = [
    '1', '2', '3', '+', '-',
    '4', '5', '6', '*', '/',
    '7', '8', '9', '(', ')',
    'sin', 'cos', 'tan', '0', 'x',
    'exp', '^2', 'sqrt', 'backspace', 'Clear'
]

if 'expression_input' not in st.session_state:
    st.session_state.expression_input = ""

expression_input = st.session_state.expression_input

for i in range(0, len(keypad_buttons), 5):
    row = st.columns(5)
    for j in range(5):
        if i + j < len(keypad_buttons):
            button = keypad_buttons[i + j]
            if button == 'Backspace':
                row[j].button(button, key=f'key_{i+j}', help=f'Click to remove the last character from the expression', on_click=lambda: st.session_state.update(expression_input=expression_input[:-1]))
            elif button == 'Clear':
                row[j].button(button, key=f'key_{i+j}', help=f'Click to clear the expression', on_click=lambda: st.session_state.update(expression_input=""))
            else:
                row[j].button(button, key=f'key_{i+j}', help=f'Click to add {button} to the expression', on_click=lambda b=button: st.session_state.update(expression_input=expression_input + b + '(') if b in {'x', 'sin', 'cos', 'tan', 'exp', 'sqrt'} else st.session_state.update(expression_input=expression_input + b))

# Concatenate the clicked buttons to form the expression
expression = expression_input

# Display the current expression
st.write("Current Expression:", expression)

if menu == 'Find limit of a function':
    limit_point_str = st.text_input("Enter the limit point")
    if st.button('Calculate Limit'):
        try:
            limit_point = sp.simplify(limit_point_str)
            result = sp.limit(sp.sympify(expression), x, limit_point)
            st.write(f"Limit as x approaches {sp.latex(limit_point)}:", result)
        except Exception as e:
            st.error(f'Error calculating limit: {str(e)}')

elif menu == 'Find derivative of a function':
    if st.button('Calculate Derivative'):
        try:
            df = sp.diff(sp.sympify(expression), x)
            simplified_df = sp.simplify(df)
            st.write("Derivative:", simplified_df)
        except Exception as e:
            st.error(f'Error calculating derivative: {str(e)}')
