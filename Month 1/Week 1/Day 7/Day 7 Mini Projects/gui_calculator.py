import os
import streamlit as st
import calculator_extended as calc  # Import the extended calculator module

# Set up the Streamlit page
st.title("Streamlit Calculator with History")
st.markdown("Use this app to perform calculations and view history from the log file.")

# --- Calculation Section ---
st.header("Perform Calculation")

# Input fields for binary operations
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("First Number (a)", value=0.0)
with col2:
    num2 = st.number_input("Second Number (b)", value=0.0)

operation = st.selectbox(
    "Select Operation",
    list(calc.binary_ops.keys()) + list(calc.unary_ops.keys())
)

result = None
error = None

if st.button("Calculate"):
    try:
        if operation in calc.binary_ops:
            # Handle binary operations
            func = calc.binary_ops[operation]
            result = func(num1, num2)
        elif operation in calc.unary_ops:
            # Handle unary operations (using num1 only)
            func = calc.unary_ops[operation]
            result = func(num1)
            
        st.success(f"Result of {operation}({num1}{', ' + str(num2) if operation in calc.binary_ops else ''}) = **{result}**")
        
    except (ZeroDivisionError, ValueError) as e:
        st.error(f"Calculation Error: {e}")

# --- History Section ---
st.header("Calculation History")

if st.button("Show/Refresh History"):
    # The history function prints directly to the console in the original script,
    # so we'll adapt it to read the file and display in Streamlit.
    try:
        if not os.path.exists(calc.LOG_FILE):
             st.info("No log file found yet.")
        else:
            with open(calc.LOG_FILE, 'r') as f:
                history_content = f.read()
            st.text_area("calculator.log Content", history_content, height=300)
    except Exception as e:
        st.error(f"Error reading log file: {e}")