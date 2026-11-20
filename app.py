import streamlit as st

st.title("🏥 TWIN TOWERS HOSPITAL")
st.write("Made by Muzhumathi - Diabetes & Triage App")

name = st.text_input("Patient Name")
temp = st.number_input("Enter Temperature", value=98.6)
disease = st.selectbox("Disease", ["Diabetes", "Fever", "Cold", "Other"])
fees = st.number_input("Fees", value=500)

if st.button("CHECK PATIENT"):
    st.write("---")
    st.write("Patient: {name}")
    
    if temp >= 102:
        st.error(" HIGH RISK! Emergency Ward NOW!")
    elif temp >= 100:
        st.warning("⚠️ MEDIUM RISK - See in 30 mins")
    else:
        st.success("✅ NORMAL - Can Wait")
    
    if disease == "Diabetes":
        st.info("💊 Diabetes Patient - Send to Diabetes Ward")
    
    st.write("Total Fees to Pay: Rs. {fees}")
    st.balloons()
