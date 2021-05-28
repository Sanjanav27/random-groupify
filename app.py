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
    clone_arr=[]
    for name in name_arr:
        clone_arr.append(name)
    grpsize=request.form["grp-size"]

    length=len(name_arr)
    div=int(length/int(grpsize))
    rem=int(length%int(grpsize))
    name_pair=[]
    while name_arr!=[]:
        try:
            for i in range(0,div):
                dummy=[]
                for j in range(0,int(grpsize)):
                    dummy.append(random.choice(name_arr))
                    s=str(dummy[j])
                    name_arr.remove(s)
                name_pair.append(dummy) 
        except:
            t=[]
            cur=[]
            for pair in name_pair:
                for name in pair:
                    cur.append(name)
            for ori in clone_arr:
                if(ori not in cur):
                    t.append(ori)
            name_pair.append(t)

        
    return render_template("group.html",name_pair=name_pair,grpsize=int(grpsize))


if __name__=='__main__':
    app.run()


