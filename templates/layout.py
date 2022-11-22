#!/usr/bin/env python
# coding: utf-8

# In[1]:


# to open/create a new html file in the write mode
f = open('layout.html', 'w')

# the html code which will go in the file index.html
html_template = """<html>

<html>
<head>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    
    
    <link
      rel="canonical"
      href="{{ url_for(request.endpoint, **request.view_args) }}"
    />

    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"
    />

    <style>
      

      body {
        width: 100%;
        min-height: 100%;
        background-color: LightCyan;
        font-family: %%SVG;
        font-size: 1.5em;
      }    
    img {
       
        width: 250px;
     }     
      .content {
        width: 50%;
        margin: 60px auto;
        text-align: center;
      }
      .predict-form {
        max-width: 500px;
        margin: 0 auto;

      }
      .cityscape-img {
        width: 50%;
        aspect-ratio: 2;
      }
    </style>

    <title>Semantic Segmentation API</title>
  </head>
  <body>
    <main class="content">{% block content %}{% endblock %}</main>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  </body>
</html>
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()


# In[ ]:





# In[ ]:




