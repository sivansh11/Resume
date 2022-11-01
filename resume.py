import streamlit as st
import os

with open(os.getcwd() + '/assets/main.css') as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


'# Sivansh Gupta'
'''
Pursuing computer science engeenering from IPU (Indraprastha University), currently in year 3.\\
Machine Learning enthusiast\\
Email: sivanshgupta2002@gmail.com
'''
'---'

'# Socials'
col1, col2 = st.columns(2)
with col1:
    '### [GitHub](https://github.com/sivansh11)'
with col2:
    '### [LinkedIn](https://www.linkedin.com/in/sivansh-gupta-b50565192)'
'---'


'# Qualifications'
'''
- 2020: \\
    Passed Grade 12 from Hillwoods Academy (Preet Vihar) with 91%
- 2021-2022: \\
    Practical Machine Learning Course from Techstack Institute Saket 
- 2020-2024 (still pursuing): \\
    Pursuing Computer Science Engeenering from IPU ADGITM (Dr. Akhilesh Das Gupta Institute of Technology & Management) 
'''
'---'


'# Skills'
col1, col2, col3 = st.columns(3)

with col1:
    '**Python**'
with col2:
    '**C/C++**'
with col3:
    '**Deep/Machine Learning**'
