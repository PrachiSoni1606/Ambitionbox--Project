from flask import Flask ,render_template,request
import pandas as pd

app=Flask(__name__)




@app.route("/")
def home():
    df=pd.read_csv("all cities data.csv")
    unique_loc = df["LOCATION"].unique().tolist()
    unique_field = df["FIELD"].unique().tolist()
    unique_ratings = df["RATINGS"].unique().tolist()
    return render_template("index.html",loc = unique_loc , field = unique_field, rating= unique_ratings)



@app.route("/sub" , methods=["POST","GET"])
def submit():
    import pandas as pd
    import os
    if request.method=="POST":
        view=request.form.get("view")
        location=request.form.get("Location")
        field=request.form.get("Field")
        rating=request.form.get("Rating")
        print(location,field,rating,sep="\n")
        df=pd.read_csv("all cities data.csv")
        data = df[(df["LOCATION"]==location) & (df["FIELD"]==field) ]
        if view=="table":
            
        
        
            print(data)
            column=data.columns.tolist()
            print(column)
            rows=data.to_dict(orient="records")


            return render_template("data.html",rows=rows,column=column)  

        elif view == "visual":
            
            import matplotlib
            matplotlib.use('agg')
            import matplotlib.pyplot as plt
            plt.figure()
            df=data.sort_values(by="RATINGS",ascending=False).head(10)
            plt.hist(data["RATINGS"])
            plt.title("RATING DISTRIBUTION")
            plt.xlabel("Rating")
            plt.ylabel("Frequency")

            plt.savefig("static/graph1.png")
            plt.close()

            # graph2
            plt.figure()
            d=data.head(10)
            plt.scatter(d["REVIEW"],d["JOB"],color="red")
            plt.colorbar()
            
            plt.title(" REVIEWS VS JOBS ")
            plt.xticks(d["REVIEW"],rotation=45)
            plt.yticks(d["JOB"],rotation=45)
            plt.xlabel("Reviews")
            plt.ylabel("jobs")
            
            plt.savefig("static/graph2.png")
            plt.close()

            #   graph 3

            plt.figure()
            df=data.sort_values(by="RATINGS",ascending=False).head(5)
            plt.pie(df["RATINGS"],labels=df["COMPANY NAME"],autopct='%1.1f%%')
            plt.title("Top 5 Companies Rating Share")
            plt.savefig("static/graph3.png")
            plt.close()




            
            return render_template("graph.html")

           
            
        
        

        




app.run(debug=True,port = 5502) 



