from flask import Flask,render_template
from app import views
from flask import redirect, url_for
app = Flask(__name__)
app.add_url_rule("/base",'base',views.base)
app.add_url_rule("/",'index',views.index)
app.add_url_rule("/faceapp",'faceapp',views.faceapp)
app.add_url_rule("/faceapp/gender",'gender',views.gender,methods=['GET','POST'])

if __name__ == "__main__":
    app.run(debug=True)



