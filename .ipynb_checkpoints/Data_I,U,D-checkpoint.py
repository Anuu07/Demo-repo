import streamlit as st
import pymysql
import pandas as pd

# Database connection function
def get_connection():
    return pymysql.connect(host="localhost", user="root", password="Samiksha@14", database="project")

# Insert employee function
def insert_employee(emp_id, name, email,salary, joining_date):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO employee VALUES (%s, %s,%s, %s, %s)"
        cursor.execute(query, (emp_id, name, email,salary, joining_date))
        conn.commit()
        return "Record inserted successfully!"
    except pymysql.MySQLError as e:
        conn.rollback()
        return f"SQL Error: {str(e)}"
    finally:
        cursor.close()
        conn.close()
# Update employee function
def update_employee(emp_id, name, email,salary, joining_date):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "UPDATE employee SET ename = %s, salary = %s, doj = %s,email=%s WHERE empid = %s"
        cursor.execute(query, (name, salary, joining_date,email, emp_id))
        conn.commit()
        return "Record updated successfully!"
    except pymysql.MySQLError as e:
        conn.rollback()
        return f"SQL Error: {str(e)}"
    finally:
        cursor.close()
        conn.close()

# Delete employee function
def delete_employee(emp_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "DELETE FROM employee WHERE empid = %s"
        cursor.execute(query, (emp_id,))
        conn.commit()
        return "Record deleted successfully!"
    except pymysql.MySQLError as e:
        conn.rollback()
        return f"SQL Error: {str(e)}"
    finally:
        cursor.close()
        conn.close()
# Fetch all employees function
def fetch_all_employees():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM employee"
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    except pymysql.MySQLError as e:
        return f"SQL Error: {str(e)}"
    finally:
        cursor.close()
        conn.close()

# Streamlit app configuration
st.title("Employee Database Manager")

# Navigation menu
menu = ["Insert", "Update", "Delete", "Show All"]
choice = st.sidebar.selectbox("Menu", menu)

# Insert functionality
if choice == "Insert":
    st.subheader("Insert New Employee")
    with st.form("insert_form"):
        emp_id = st.number_input("Employee ID", min_value=1, step=1)
        name = st.text_input("Employee Name")
        email = st.text_input("Email")
        salary = st.number_input("Salary", min_value=0.0, step=1000.0)
        joining_date = st.date_input("Joining Date")
        submitted = st.form_submit_button("Insert Record")

    if submitted:
        result = insert_employee(emp_id, name, email, joining_date, salary)
        st.write(result)

# Update functionality
elif choice == "Update":
    st.subheader("Update Employee Record")
    with st.form("update_form"):
        emp_id = st.number_input("Employee ID", min_value=1, step=1)
        name = st.text_input("New Name")
        email = st.text_input("Email")
        salary = st.number_input("New Salary", min_value=0.0, step=1000.0)
        joining_date = st.date_input("New Joining Date")
        submitted = st.form_submit_button("Update Record")

    if submitted:
        result = update_employee(emp_id, name, email,salary, joining_date)
        st.write(result)

# Delete functionality
elif choice == "Delete":
    st.subheader("Delete Employee Record")
    with st.form("delete_form"):
        emp_id = st.number_input("Employee ID", min_value=1, step=1)
        submitted = st.form_submit_button("Delete Record")

    if submitted:
        result = delete_employee(emp_id)
        st.write(result)

# Show all functionality
elif choice == "Show All":
    st.subheader("All Employee Records")
    records = fetch_all_employees()
    if records:
        df = pd.DataFrame(records, columns=["ID", "Name", "Email", "Joining Date","Salary"])
        #print(df)
        st.dataframe(df.style.format({"Salary": "${:,.2f}","Joining Date": lambda x: x.strftime("%Y-%m-%d")}))
    else:
        st.write("No records found.")