# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:40:42 2021

@author: tapas.tiwari
"""

import streamlit as st
import numpy as np
import pandas as pd

st.title('Mondelez Simulator')
df = pd.DataFrame({
  'first column': ['Top','Bottom','Right', 'Left'],
  'second column': [10, 20, 30, 40]
})

#df
option = st.selectbox(
    'Where is your image',
     df['first column'])

'Image placed at:',option
