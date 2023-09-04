def  main():
    #Import libraries
    import pandas as pd
    from PIL import Image
    import streamlit as st
    import matplotlib.pyplot as plt
    st.set_page_config(layout="wide")
    
    #List of countries
    Country_list=['Austria', 'AmericanSamoa', 'United Kingdom', 'Albania', 'Belgium', 'Afghanistan', 'Australia', 'Bahrain',
                                        'Azerbaijan', 'United Arab Emirates', 'New Zealand', 'United States', 'Argentina', 'Jordan', 'Canada', 'Brazil', 'Croatia',
                                        'India', 'Bangladesh', 'France', 'Indonesia', 'Egypt', 'Netherlands', 'Greenland', 'Bahamas', 'South Africa', 'Viet Nam', 'Comoros',
                                        'Portugal', 'Finland', 'Norway', 'Ireland', 'Anguilla', 'Spain', 'Burundi', 'Lebanon', 'Italy', 'Pakistan', 'Chile', 'China', 'Saudi Arabia',
                                         'Romania', 'Sweden', 'Tonga', 'Oman', 'Philippines', 'Sri Lanka', 'Sierra Leone', 'Ethiopia', 'Iran', 'Costa Rica', 'Germany', 'Mexico', 'Russia',
                                         'Armenia', 'Iceland', 'Nicaragua', 'Hong Kong', 'Japan', 'Ukraine', 'Kazakhstan', 'Uruguay', 'Serbia', 'Malaysia', 'Ecuador', 'Niger', 'Bolivia',
                                         'Aruba', 'Turkey', 'Nepal', 'Angola', 'Iraq', 'Czech Republic', 'Cyprus', 'Kuwait', 'Europe', 'Malta',
                                        'Bulgaria', 'Georgia', 'Syria', 'South Korea', 'Qatar', 'Latvia', 'Nigeria', 'U.S. Outlying Islands', 'Isle of Man', 'Libya',
                                        'Ghana', 'Bhutan', 'Others']

    #Dictionaries of user input variables
    ethnicity={'Hispanic': 0, 'Black': 1, 'White-European': 2, 'Middle Eastern ': 3, 'South Asian': 4, 'Others': 5, 'Latino': 6, 'Asian': 7, 'Pasifika': 8, 'Turkish': 9, 'others': 10}
    gender={'M':1, 'F':2}
    country= {'Austria': 0, 'AmericanSamoa': 1, 'United Kingdom': 2, 'Albania': 3, 'Belgium': 4, 'Afghanistan': 5, 'Australia': 6, 'Bahrain': 7, 'Azerbaijan': 8,
              'United Arab Emirates': 9, 'New Zealand': 10, 'United States': 11, 'Argentina': 12, 'Jordan': 13, 'Canada': 14, 'Brazil': 15, 'Croatia': 16, 'India': 17,
              'Bangladesh': 18, 'France': 19, 'Indonesia': 20, 'Egypt': 21, 'Netherlands': 22, 'Greenland': 23, 'Bahamas': 24, 'South Africa': 25, 'Viet Nam': 26, 'Comoros': 27,
              'Portugal': 28, 'Finland': 29, 'Norway': 30, 'Ireland': 31, 'Anguilla': 32, 'Spain': 33, 'Burundi': 34, 'Lebanon': 35, 'Italy': 36, 'Pakistan': 37, 'Chile': 38,
              'China': 39, 'Saudi Arabia': 40, 'Romania': 41, 'Sweden': 42, 'Tonga': 43, 'Oman': 44, 'Philippines': 45, 'Sri Lanka': 46, 'Sierra Leone': 47, 'Ethiopia': 48, 'Iran': 49,
              'Costa Rica': 50, 'Germany': 51, 'Mexico': 52, 'Russia': 53, 'Armenia': 54, 'Iceland': 55, 'Nicaragua': 56, 'Hong Kong': 57, 'Japan': 58, 'Ukraine': 59, 'Kazakhstan': 60,
              'Uruguay': 61, 'Serbia': 62, 'Malaysia': 63, 'Ecuador': 64, 'Niger': 65, 'Bolivia': 66, 'Aruba': 67, 'Turkey': 68, 'Nepal': 69, 'Angola': 70, 'Iraq': 71,
              'Czech Republic': 72, 'Cyprus': 73, 'Kuwait': 74, 'Europe': 75, 'Malta': 76, 'Bulgaria': 77, 'Georgia': 78, 'Syria': 79,
              'South Korea': 80, 'Qatar': 81, 'Latvia': 82, 'Nigeria': 83, 'U.S. Outlying Islands': 84, 'Isle of Man': 85, 'Libya': 86, 'Ghana': 87, 'Bhutan': 88, 'Others': 89}
    austism={'YES':1, 'NO':2}
    used_app_before={'YES':1, 'NO':2}
    jaundiced={'YES':1, 'NO':2}
    relation={'Parent': 0, 'Relative': 1, 'Self': 2, 'Health care professional': 3, 'Others': 4, 'self': 5}
    age_desc= {'12-16 years': 0, '12-15 years': 1, '18 and more': 2, '4-11 years': 3}
    
    
    
    #Instantiating Navigation Bar
    Menu=["Home", "Analytics", "Predictor"]
    page=st.sidebar.selectbox('Navigation Bar', Menu)

    #Setting up the home page for the web app
    if page=="Home":
        st.markdown("<h1 style='text-align: center; color: blue;'> AUTISM SPECTRUM DISORDER DETECTOR</h1>", unsafe_allow_html=True)
        st.write('\n')
        st.write('\n')
        st.markdown("##### Autism spectrum disorder (ASD) is a developmental disability caused by differences in the brain. Some people with ASD have \
                    a known difference, such as a genetic condition. Other causes are not yet known. Scientists believe there are multiple causes of ASD that act together to\
                    change the most common ways people develop. We still have much to learn about these causes and how they impact people with ASD.  Diagnosing autism\
                    spectrum disorder (ASD) however can be difficult because there is no medical test, like a blood test, to diagnose the disorder.\
                     Doctors look at the child’s developmental history and behavior to make a diagnosis.")
        image = Image.open('Dependecies/autism.jpg')
        col1, col2, col3 = st.columns([1,4,1])
        with col2:
            st.write('\n')
            st.write('\n')
            st.image(image, width=1000, use_column_width=True)
        st.write('\n')
        st.write('\n')
        
        st.markdown("<h1 style='text-align: center; color: black;'> We therefore build this product to help doctors better diagnose persons with ASD.</h1>", unsafe_allow_html=True)
         
        
        
    #Setting up the analytics page for the web app
    elif page=="Analytics":
        st.markdown("<h1 style='text-align: center; color: blue;'> DID YOU KNOW ? </h1>", unsafe_allow_html=True)
        image1 = Image.open('Dependecies/asd.png')
        image2 = Image.open('Dependecies/asd (1).png')
        image3 = Image.open('Dependecies/asd (3).png')
        image4 = Image.open('Dependecies/asd (4).png')
        image5 = Image.open('Dependecies/asd (6).png')
        image6 = Image.open('Dependecies/asd (7).png')
        image7 = Image.open('Dependecies/asd (8).png')
        col1, col2, col3= st.columns(3)
        col4, col5, col6= st.columns(3)
        col7, col8, col9= st.columns(3)
        
        col1.image(image1)
        col1.markdown('###### Number of those with and without ASD')
        
        col2.image(image2)
        col2.markdown('###### Age group distribution of the data shows that majority of the dataset comes from people with 18 yrs and above likley due to the fact that \
                               the disorder is often diagnosed latter in life.')

        
        col3.image(image3)
        col3.markdown('###### Ethnic group distribution of data shows that majority of the dataset comes from people who are white-europeans, followed by blacks')
        
        col4.image(image6)
        col4.markdown('###### 85% of the people in the dataset do not suffer Jaundice while 15% suffers Jaundice.')
        
        col5.image(image5)
        col5.markdown('###### Gender distribution of the data shows more male than females')
        
        col6.image(image7)
        col6.markdown('###### Majority of the people in the dataset have never used an App before for ASD detection.')

        col8.image(image4)
        col8.markdown('###### The dataset consist people from over 89 countries')
        
        
        
    #Setting up the Predictor page for the web app    
    elif page=="Predictor":
        sub_menu=["AQ-10 Questionnaire", "ASD Predictor"]
        page1=st.sidebar.selectbox('Navigation bar',sub_menu)

        #Setting up the AQ-10 Questionnaire page for the web app
        if page1=="AQ-10 Questionnaire":
             st.markdown("<h1 style='text-align: center; color: blue;'> AQ-10 Questionnaire</h1>", unsafe_allow_html=True)

             st.subheader('Adults')

             st.write('A1:  I often notice small sounds when others do no')
             st.write ('A2: I usually concentrate more on the whole picture, rather than the small details')
             st.write ('A3: I find it easy to do more than one thing at once')
             st.write ('A4: If there is an interruption, I can switch back to what I was doing very quickly')
             st.write ('A5:  I find it easy to ‘read between the lines’ when someone is talking to me')
             st.write ('A6: I know how to tell if someone listening to me is getting bored')
             st.write (' A7:When I’m reading a story I find it difficult to work out the characters’ intentions')
             st.write ('A8 : I like to collect information about categories of things (e.g., types of car, types of bird, types of train, types of plant, etc')
             st.write ('A9: I find it easy to work out what someone is thinking or feeling just by looking at their face')
             st.write ('A10: I find it difficult to work out people’s intentions')

             st.subheader('Adolescents')

             st.write('A1:  S/he notices patterns in things all the time')
             st.write ('A2: S/he usually concentrates more on the whole picture,rather than the small details')
             st.write ('A3: In a social group, s/he can easily keep track of several different people’s conversations')
             st.write ('A4: If there is an interruption, s/he can switch back to what s/he was doing very quickly')
             st.write ('A5:  S/he frequently finds that s/he doesn’t know how to keep a conversation going')
             st.write ('A6: S/he is good at social chitchat')
             st.write ('A7: When s/he was younger, s/he used to enjoy playing games involving pretending with other children')
             st.write ('A8 : S/he finds it difficult to imagine what it would be like to be someone else')
             st.write ('A9: S/he finds social situations easy')
             st.write ('A10: S/he finds it hard to make new friends')

             st.subheader('Children')

             st.write('A1: S/he often notices small sounds when others do not')
             st.write ('A2: S/he usually concentrates more on the whole picture, rather than the small details')
             st.write ('A3: In a social group, s/he can easily keep track of several different people’s conversations')
             st.write ('A4: S/he finds it easy to go back and forth between different activities')
             st.write ('A5:  S/he does not know how to keep a conversation going with his/her peers')
             st.write ('A6: S/he is good at social chit-chat')
             st.write ('A7: When s/he is reading a story, s/he finds it difficult to work out the characters’ intentions or feelings')
             st.write ('A8 :When s/he was in preschool, she used to enjoy playing games involving pretending with other children ')
             st.write ('A9: S/he finds it easy to work out what someone is thinking or feeling just by looking at their face')
             st.write ('A10: S/he finds it hard to make new friends')
            

        #Setting up the ASD Predictor page for the web app
        elif page1=="ASD Predictor":
            
        
            st.markdown("<h1 style='text-align: center; color: blue;'> AUTISM SPECTRUM DISORDER PREDICTOR</h1>", unsafe_allow_html=True)
            with st.form("my_form"):
                
                container_1=st.container()
                container_2=st.container()
                container_3=st.container()
                container_4=st.container()
                container_5=st.container()
                container_6=st.container()
                container_6=st.container()
                container_7=st.container()

           

                with container_1:
                    col1,col2,col3,col4,col5=st.columns(5)
                    A1_score=col1.radio("A1_ANSWER (Yes:1, No:0): ", (1, 0))
                    A2_score=col2.radio("A2_ANSWER (Yes:1, No:0): ", (1, 0))
                    A3_score=col3.radio("A3_ANSWER (Yes:1, No:0): ", (1, 0))
                    A4_score=col4.radio("A4_ANSWER (Yes:1, No:0): ", (1, 0))
                    A5_score=col5.radio("A5_ANSWER (Yes:1, No:0): ", (1, 0))

                with container_2:
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')

                with container_3:
                    col1,col2,col3,col4,col5=st.columns(5)
                    A6_score=col1.radio("A6_ANSWER (Yes:1, No:0): ", (1, 0))
                    A7_score=col2.radio("A7_ANSWER (Yes:1, No:0): ", (1, 0))
                    A8_score=col3.radio("A8_ANSWER (Yes:1, No:0): ", (1, 0))
                    A9_score=col4.radio("A9_ANSWER (Yes:1, No:0): ", (1, 0))
                    A10_score=col5.radio("A10_ANSWER (Yes:1, No:0): ", (1, 0))

                with container_4:
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')

                with container_5:
                    col1,col2,col3,col4 = st.columns(4) 
                    Jaundiced=col1.radio("JAUNDICED? : ", ('YES', 'NO'))
                    Gender= col2.radio("GENDER: ", ('M', 'F'))
                    Austism=col3.radio("AUSTISM: ", ('YES', 'NO'))
                    Used_App_Before=col4.radio("USED APP BEFORE? : ", ('YES', 'NO'))
                    

                with container_6:
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    st.write('\n')
                    
                    
                with container_7:
                    col1, col2, col3,col4,col5,col6= st.columns(6)
                    Result=col1.number_input('RESULT: ',min_value=0, step=1,max_value=10)
                    Age=col2.number_input('AGE: ',min_value=1, step=1)
                    Ethnicity=col3.selectbox("ETHNICITY: ", ['Hispanic', 'Black', 'White-European', 'Middle Eastern ', 'South Asian', 'Others', 'Latino', 'Asian', 'Pasifika', 'Turkish', 'others'])
                    Country=col4.selectbox('COUNTRY OF RESIDENCE: ', Country_list)
                    Relation=col5.selectbox('CURRENT RELATIVE: ', ['Parent', 'Relative', 'Self', 'Health care professional', 'Others', 'self'])
                    Age_Desc=col6.selectbox( 'AGE GROUP: ', ['12-16 years', '12-15 years', '18 and more', '4-11 years'])
                    
                    
                st.write('\n')
                submitted = st.form_submit_button("MAKE PREDICTION")

                
                
             #Setting up the Submission and result panel for ASD predictor   
            if submitted:
                variables=[A1_score, A2_score,A3_score, A4_score, A5_score, A6_score, A7_score, A8_score, A9_score, A10_score,Age, gender[Gender],
                           ethnicity[Ethnicity],jaundiced[Jaundiced],  austism[Austism], country[Country],used_app_before[Used_App_Before],Result,  
                           age_desc[Age_Desc], relation[Relation]]
                import numpy as np
                X = np.array(variables).reshape(1, -1)
                
                

                with st.spinner('RUNNING...'):
                    import pickle
                    import time
                    time.sleep(1)
                    model=pickle.load(open('Dependecies/ASD_model.sav', 'rb')) #Load in saved/trained model
                    pred=model.predict(X)[0]
                    prob=model.predict_proba(X)[0]

                st.write('\n')
                st.write('\n')
             
                
                #result panel for ASD predictor 
                with st.expander("VIEW RESULT"):
                    df1=pd.DataFrame(['AUTISTIC', 'NOT AUTISTIC'], columns=['Name'])
                    df2=pd.DataFrame(prob, columns=['Prob'])
                    df=pd.concat([df1, df2], axis=1)
                    labels=df['Name'].to_list()
                    values= df['Prob'].to_list()
                    fig=plt.figure(figsize = (7, 5))
                    plt.pie(values, labels=labels, autopct='%1.0f%%')
                    plt.title("Probability of ASD")
                    st.pyplot(fig)
                    
                    col1, col2, col3=st.columns([1,5,1])
                    if pred== 1:
                        col2.markdown('## MOST PROBABLE DIAGNOSIS: NOT AUTISTIC')
                    else:
                        col2.markdown('## MOST PROBABLE DIAGNOSIS: AUTISTIC')
                        
                    
      
                
                
            
            



import streamlit 
import sys
from streamlit.web import cli as stcli
if __name__ == '__main__':
    if streamlit._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
