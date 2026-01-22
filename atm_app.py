import streamlit as st

st.title("🏧 ATM Machine")

# Session state (balance & login)
if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# LOGIN
if not st.session_state.logged_in:
    pin = st.text_input("Enter your PIN", type="password")

    if st.button("Login"):
        if pin == "1234":
            st.session_state.logged_in = True
            st.success("Login Successful ✅")
        else:
            st.error("Wrong PIN ❌")

# ATM MENU
else:
    st.success("Welcome to ATM")

    option = st.selectbox(
        "Choose an option",
        ["Check Balance", "Deposit", "Withdraw"]
    )

    # CHECK BALANCE
    if option == "Check Balance":
        st.info(f"💰 Current Balance: Rs {st.session_state.balance}")

    # DEPOSIT
    elif option == "Deposit":
        amount = st.number_input("Enter amount to deposit", min_value=1)
        if st.button("Deposit"):
            st.session_state.balance += amount
            st.success(f"✅ Rs {amount} deposited successfully")
            st.info("🧾 Receipt: Transaction Successful")

    # WITHDRAW
    elif option == "Withdraw":
        amount = st.number_input("Enter amount to withdraw", min_value=1)
        if st.button("Withdraw"):
            if amount <= st.session_state.balance:
                st.session_state.balance -= amount
                st.success(f"✅ Rs {amount} withdrawn successfully")
                st.info("🧾 Receipt: Please collect your cash")
            else:
                st.error("❌ Insufficient balance")

    # LOGOUT BUTTON
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.success("Logged out successfully 👋")
