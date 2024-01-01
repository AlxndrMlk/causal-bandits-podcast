import requests
from string import Template

import streamlit as st

# Constants
YT_TEMPL_URL = 'https://raw.githubusercontent.com/AlxndrMlk/causal-bandits-podcast/main/templates/yt-desc-temp.txt'

# Get the template
r = requests.get(YT_TEMPL_URL)
templ = Template(r.text)

# APP
# Title 
st.title('Causal Bandits Podcast - Episode Info')
st.subheader('Fill in the detalis')

# Get the data
# Date
date_obj = st.date_input('Recording date')
rec_year = date_obj.year
rec_month = date_obj.strftime('%B')[:3]
rec_day = date_obj.day

# Location
rec_city = st.text_input('Recording city')
rec_country = st.text_input('Recording country')

# Episode details
episode_headline = st.text_input('Episode headline')
episode_descr = st.text_area('Episode description')

# Guest details
guest_name = st.text_input('Guest\'s first name')
guest_info = st.text_area('Guest info')

# Guest contact
guest_twitter = st.text_input('Guest Twitter')
guest_linkedin = st.text_input('Guest LinkedIn')
guest_www = st.text_input('Guest WWW')

# Episode links
episode_links = st.text_area('Episode links')

# Fill the template 
filled = templ.safe_substitute(
    REC_MONTH=rec_month,
    REC_DAY=rec_day,
    REC_YEAR=rec_year,
    REC_CITY=rec_city,
    REC_COUNTRY=rec_country,
    EPISODE_HEADLINE=episode_headline,
    EPISODE_DESCRIPTION=episode_descr,
    GUEST_INFO=guest_info,
    GUEST_NAME=guest_name,
    GUEST_TWITTER=guest_twitter,
    GUEST_LINKEDIN=guest_linkedin,
    GUEST_WEB=guest_www,
    EPISODE_LINKS=episode_links)

st.subheader('YouTube Description')
st.write(
    filled.replace('\n', '<br>').replace('*', '\*'),
    unsafe_allow_html=True
)