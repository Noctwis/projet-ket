#!/usr/bin/env python
# coding: utf-8

# In[1]:


# to open/create a new html file in the write mode
f = open('index.html', 'w')

# the html code which will go in the file index.html
html_template = """<html>

<html>
<head>
{% extends 'layout.html' %} {% block content %}
 <!-- Make it compatible to mobile devices -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">


<div class="predict-form">
  <h1 style="color:Darkblue;" class="mb-3"> Semantic segmentation</h1> 
  <!-- Add an image -->
  <img src="https://www.cityscapes-dataset.com/wordpress/wp-content/uploads/2015/07/zuerich00.png">
  <br>
  <form class="form-floating" method="get">
    <div class="row">
      <div class="col-auto">
        <label for="inputImageID" style="color:Darkblue;" class="col-form-label">select your image :</label>
      </div>
      <div class="col-auto">
        <input
          name="image_id"
          type="text"
          class="form-control"
          id="inputImageID"
          aria-describedby="imageIDHelp"
          
          value="{{ image_id }}"
        />
      </div>
      <div class="col-auto">
        <button type="submit" class="btn btn-primary">Submit</button>
      </div>
    </div>
    <div class="row">
        <div id="imageIDHelp" class="form-text">
          
        </div>
    </div>
  </form>
</div>


<hr />

<div class="text-center">
  <div class="row">
    <figure class="figure row">
      <img
        class="img-thumbnail cityscape-img"
        src="data:image/png;base64,{{ original_img_str }}"
      />
      <figcaption class="figure-caption" >Image</figcaption>
    </figure>

    <figure class="figure row">
      <img
        class="img-thumbnail cityscape-img"
        src="data:image/png;base64,{{ labels_img_str }}"
      />
      <figcaption class="figure-caption">True label</figcaption>
    </figure>

    <figure class="figure row">
      <img
        class="img-thumbnail cityscape-img"
        src="data:image/png;base64,{{ categories_img_str }}"
      />
      <figcaption class="figure-caption">Predicted label</figcaption>
    </figure>
  </div>
</div>

{% endblock %}
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()


# In[ ]:





# In[ ]:




