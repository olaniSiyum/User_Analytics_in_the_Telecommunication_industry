import sys
sys.path.insert(0, './script')

import streamlit as st
from multiapp import MultiApp
from notebook import user_overview, user_engagement, user_experience
# import your app modules here

st.set_page_config(page_title="TellCo Telecom Analytics", layout="wide")

app = MultiApp()


st.sidebar.markdown("""
# TellCo's User Analytics
### Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
### Modifications
\t- Page Folder Based Access
\t- Presentation changed to SideBar
""")

# Add all your application here
app.add_app("User Overview Analysis", user_overview.app)
app.add_app("User Engagement Analysis", user_engagement.app)
app.add_app("User Experience Analysis", user_experience.app)

# The main app
app.run()
