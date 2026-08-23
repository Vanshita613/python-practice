import streamlit as st
st.write("hello world")  #display text



st.write("This is a simple Streamlit app that demonstrates how to use Streamlit for building web applications. You can add more features and functionalities as needed.")



st.markdown("## this is large heading")   #large heading

st.markdown("# this is small heading")   #small heading


number=st.slider("pick a number", min_value=1, max_value=9)  # adds a slider
st.write(f'You picked {number}')

check=st.checkbox("agree the terms!")
if check:
    st.write("you aggredd!")

st.image("streamlit_hero.jpg" )



bias=st.selectbox("select your bias:", ["jay","niki", "arisu","huta","keeho","intak"])
st.write(f"you selected: {bias}")
st.success("damnn u have great bias!")


