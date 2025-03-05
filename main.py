import streamlit as st


r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 0.5])


nav_pages = ["Notes", "PMAQ"]
selected_page = st.sidebar.radio("Navigation", nav_pages)







# Display content based on the selected page
if selected_page == nav_pages[0]:
    st.subheader("Welcome to the OMS Latin Website!")
    st.write("Nil sine magnō labore — Nothing without great labor (Brooklyn)")


if selected_page == "My Cart":
    st.subheader("Your Cart")
    st.write("Check out the items in your cart here.")
