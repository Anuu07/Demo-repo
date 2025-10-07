import streamlit as st
import pymysql

def insert_employee(emp_id, name, email,salary, joining_date):
    """Function to insert an employee into the database."""
    conn = pymysql.connect(host="localhost", user="root", password="root", database="project")
    try:
        cursor = conn.cursor()
        query = "INSERT INTO employee VALUES (%s, %s,%s, %s, %s)"
        cursor.execute(query, (emp_id, name, email,  joining_date,salary))
        conn.commit()
        return "Record inserted successfully!"
    except pymysql.MySQLError as e:
        if conn:
            conn.rollback()
        return f"SQL Error: {str(e)}"
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Streamlit app configuration
st.title("Employee Database Manager")
st.write("Use this app to insert a new employee record into the database.")

# Form for employee details
with st.form("employee_form"):
    emp_id = st.number_input("Employee ID", min_value=1, step=1)
    name = st.text_input("Employee Name")
    email = st.text_input("Employee Email")
    salary = st.number_input("Salary", min_value=0.0, step=1000.0)
    joining_date = st.date_input("Joining Date")

    # Submit button
    submitted = st.form_submit_button("Insert Record")

if submitted:
    # Insert record into the database
    result = insert_employee(emp_id, name, email,salary, joining_date)
    st.write(result)