import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import db
import yaml
 

from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'] 
    )
    
    try:
        authenticator.login()
    except Exception as e:
            st.error(e)
            
    if st.session_state.get('authentication_status'):
            authenticator.logout()
            st.write(f'Welcome *{st.session_state["name"]}*')
            st.title('Some content')
    elif st.session_state.get('authentication_status') is False:
            st.error('Username/password is incorrect')
    elif st.session_state.get('authentication_status') is None:
            st.warning('Please enter your username and password')
