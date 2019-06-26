# ML-Model-Web-Application
The basic approach was to take the famous dataset with Boston House Prices, create a simpel (far from perfect) model, put it in a Docker container and make it available through AWS Elastic Beanstalk where you can put in values through an HTML-form and get instant predictions.
<br>
Can be accessed via: http://leijtenss-hacktid.eu-west-1.elasticbeanstalk.com/
<br><br>
Dataset: https://scikit-learn.org/stable/datasets/index.html#boston-dataset
<br><br>
Requirements:
<br>
* Flask==1.0.2
* itsdangerous==1.1.0
* Jinja2==2.10.1
* MarkupSafe==1.1.1
* simplejson==3.16.0
* Werkzeug==0.15.2
* numpy==1.16.4
* pandas==0.24.2
* scikit-learn==0.21.1
* scipy==1.0.0
* requests==2.22.0
* gunicorn==19.9.0
