from flask import Flask,render_template,request
import random


app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def main():       
    return render_template("pplcount.html")

@app.route("/pplcount",methods=["POST","GET"])
def pplcount(): 
    namesize=request.form["name-size"]
    nsize=int(namesize)      
    return render_template("index.html",nsize=nsize)

@app.route("/group2/<nsize>",methods=["POST","GET"])
def group2(nsize):
    name_arr=[]
    for i in range(0,int(nsize)):
        a=f"name-{i}"

        name_arr.append(request.form[a])
    grpsize=request.form["grp-size"]

    length=len(name_arr)
    rem=int(length/int(grpsize))
    name_pair=[]


    while name_arr!=[]:
        try:
            for i in range(0,rem):
                dummy=[]
                for j in range(0,int(grpsize)):
                    dummy.append(random.choice(name_arr))
                    s=str(dummy[j])
                    name_arr.remove(s)
                name_pair.append(dummy) 
        except ValueError:
            a=random.choices(name_arr,k=1)
            print(a)
            for i in a:
                name_arr.remove(i) 
        
    return render_template("group.html",name_pair=name_pair,grpsize=int(grpsize))


if __name__=='__main__':
    app.run()


