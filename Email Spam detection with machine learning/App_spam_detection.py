import streamlit as st
import pickle
import time,string,nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

st.set_page_config(page_title="Email/sms Spam classifier",page_icon=":envelope_with_arrow:",layout="wide")

@st.cache_data
def getmodels():
    model=pickle.load(open('spam_detection_LSVM.pkl','rb'))
    vector=pickle.load(open('Vectorizer.pkl','rb'))
    return model,vector
model,vector=getmodels()

st.title('Email/SMS  Spam Classifier ')
st.divider()

with st.sidebar:
    st.title('Sample inputs')

    st.subheader('inputs for spam:')
    st.text('WINNER!! As a valued network customer you have been selected to receivea �900 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only.,,,')
    st.text('spam,"URGENT! You have won a 1 week FREE membership in our �100,000 Prize Jackpot! Txt the word: CLAIM to No: 81010 T&C www.dbuk.net LCCLTD POBOX 4403LDNW1A7RW18",,,')

    st.subheader('inputs for ham (not spam):')
    st.text('ham,I HAVE A DATE ON SUNDAY WITH WILL!!,,,')
    st.text('ham,As per your request "Melle Melle (Oru Minnaminunginte Nurungu Vettam)"has been set as your callertune for all Callers. Press *9 to copy your friends Callertune,,,')

def preprocess(text):

    #case convertion
    text=text.lower()
    #token generation
    text=nltk.word_tokenize(text)

    #removing special characters
    x=[]
    for i in text:
        if i.isalnum():
            x.append(i)

    #removing stop words
    text=x[:]
    y=[]
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    #stemming
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)            



with st.form('Enter msg'):
    inpsms=st.text_area('Enter the message')
    inptrans=preprocess(inpsms)
    inp_vector=vector.transform([inptrans])
    sub=st.form_submit_button('Predict')
    if sub:
        if inptrans!="":
            pred=model.predict(inp_vector)
            with st.spinner('Predicting'):
                time.sleep(1)
            if pred[0]==1:    
                st.header('Spam ')
            else:
                st.header('Not Spam')  
        else:
            st.subheader('please enter the Msg')            
                





footer = """
<style>
    .footer-table {
        display: flex;
        align-items: center;
        gap: 10px;
    }
</style>

<div class="footer-table">
    <h4>Made with &#10084; by PURAM HAREESH</h4>
    <a href='https://www.linkedin.com/in/hareesh-puram-21344a23b'><h6>LinkedIn</h6></a>
    <a href='https://github.com/Hareeshpuram'><h6>GitHub</h6></a>
</div>
"""

st.write(footer, unsafe_allow_html=True)

hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            header {visibility:hidden;}
            </style>
            """
st.markdown(hide_st_style,unsafe_allow_html=True)


