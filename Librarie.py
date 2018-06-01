import os
lib = ['Requests','Scrapy','wxPython','Pillow','SQLAlchemy','BeautifulSoup','NumPy','SciPy','matplotlib','Pygame','Pyglet','pyQT','pyGtk','Scapy','pywin32','nltk','nose','SymPy','IPython','Pandas','Seaborn','Bokeh','plotly','Theano','OpenCv','PyAutoGUI','Pygame','Selenium','Faker']
for i in range(0,len(lib)):
 cmd = "pip3 install "+lib[i]
 returned_value = os.system(cmd)
 print(returned_value)
