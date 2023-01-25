import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('Fmodel.pkl', 'rb') 
predictor = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(country,year,location_type,cellphone_access,household_size,age_of_respondent,gender_of_respondent,relationship_with_head,marital_status,education_level,job_type):   
 
    # Making predictions 
    prediction = predictor.predict([[country,year,location_type,cellphone_access,household_size,age_of_respondent,gender_of_respondent,relationship_with_head,marital_status,education_level,job_type]])
     
    if prediction == 0:
        pred = 'Yes'
    else:
        pred = 'No'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit diabetes diagnosis ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction

    country = st.selectbox('Country',('Kenya', 'Rwanda', 'Tanzania', 'Uganda'))
    year = st.selectbox('Year',(2016,2017,2018))
    location_type = st.selectbox('location_type',('Urban','Rural'))
    cellphone_access = st.selectbox('cellphone_access',('No', 'Yes'))
    household_size = st.number_input('household_size')
    age_of_respondent = st.number_input('age_of_respondent')
    gender_of_respondent = st.selectbox('gender',('Female', 'Male'))
    relationship_with_head = st.selectbox('relationship_with_head',('Child', 'Other relative', 'Head of Household', 'Spouse','Other non-relatives','Parent'))
    marital_status = st.selectbox('marital_status',('Widowed', 'Divorced/Seperated', 'Widowed', 'Single/Never Married','Married/Living together'))
    education_level = st.selectbox('education_level',('Primary education', 'Secondary education', 'No formal education', 'Tertiary education'))
    job_type = st.selectbox('job_type',('Formally employed Private', 'Dont Know/Refuse to answer', 'Informally employed', 'Remittance Dependent'))

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(country,year,location_type,cellphone_access,household_size,age_of_respondent,gender_of_respondent,relationship_with_head,marital_status,education_level,job_type) 
        st.success('Your diagnosis is {}'.format(result))
             
if __name__=='__main__': 
    main()
