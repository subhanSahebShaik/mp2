from django.shortcuts import render,redirect
from .forms import Predict
from MLProject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from io import StringIO

import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Create your views here.
def predict(Input,data=pd.read_csv('mp2/Cellphone.csv'),y_label="Price"):
    x = data.drop([y_label],axis=1)
    y = data[y_label]
    Model = RandomForestRegressor()
    Model.fit(x,y)
    price = Model.predict(Input)
    print(price)
    print(Model.score(x,y))
    return price

def home(request):
    return render(request,"home.html")

def form1(request):
    form = Predict()
    if request.method == "POST":
        price = predict([[request.POST['sales'],request.POST['weight'],request.POST['resolution'],request.POST['ppi'],request.POST['cpuCore'],request.POST['cpuFrequency'],request.POST['memory'],request.POST['ram'],request.POST['rearCam'],request.POST['frontCam'],request.POST['battery'],request.POST['thickness']]])
        request.session["price"] = price[0]
        return redirect(result)
    return render(request,"form1.html",{'form1':form})

def form2(request):
    if request.method == "POST":
        data = [ [ request.POST[ feature ] for feature in request.session["features_list"] ] ]
        StringData = StringIO(request.session['data'])
        price = predict(data,pd.read_csv(StringData),request.session["y_label"])
        request.session["price"] = price[0]
        return redirect(result)
        
    return render(request,"form2.html",{"features":request.session["features_list"]})

def result(request):
    if request.method == "POST":
        e,f = request.POST['email'],request.POST['text']
        name = e.split('@')
        send_mail("Thank You For Your Feedback",strip_tags(render_to_string('thankMail.html',{'name':name[0]})),EMAIL_HOST_USER,[e],fail_silently=False)
        send_mail("Feedback From MP2",strip_tags(render_to_string('feedBack.html',{'sender':e,'text':f})),EMAIL_HOST_USER,['shaiksubhansaheb609@gmail.com'],fail_silently=False)
        return render(request,'result.html',{'price':request.session['price'],'Sent':True})
    return render(request,'result.html',{'price':request.session["price"]})

def about(request):
    return render(request,"about.html")

def upload(request):
    if request.method == "POST":
        csv = request.FILES['fileUpload'].temporary_file_path()
        df = pd.read_csv(csv)
        f = open(csv)
        request.session['data'] = f.read()
        x = df.drop(request.POST['y_label'],axis=1)
        l = x.columns.values.tolist()
        request.session['features_list'] = l
        request.session["y_label"] = request.POST["y_label"]
        return redirect(form2)
    return render(request,"upload.html")
