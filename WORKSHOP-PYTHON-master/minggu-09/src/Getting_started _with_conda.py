##Creating Virtual Environments##
import sys
sys.path
# output :['', 'D:\\MiniConda\\python310.zip', 'D:\\MiniConda\\DLLs', 'D:\\MiniConda\\lib', 'D:\\MiniConda', 'C:\\Users\\Afriyanda\\AppData\\Roaming\\Python\\Python310\\site-packages', 'D:\\MiniConda\\lib\\site-packages'] 

##Managing Packages with pip##
python -m pip show requests
#output : 
# Name: requests
# Version: 2.28.1
# Summary: Python HTTP for Humans.
# Home-page: https://requests.readthedocs.io
# Author: Kenneth Reitz
# Author-email: me@kennethreitz.org
# License: Apache 2.0
# Location: d:\miniconda\lib\site-packages
# Requires: certifi, charset-normalizer, idna, urllib3
# Required-by: conda, conda_package_streaming

####
conda info --envs
# output : 
# snakes                   C:\Users\Afriyanda\.conda\envs\snakes
# snowflakes               C:\Users\Afriyanda\.conda\envs\snowflakes
#                          C:\Users\Afriyanda\miniconda3
# base                  *  D:\MiniConda