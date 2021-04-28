from flask import Flask, render_template, request
#from jinja2 import Template
  
#recentGradeList = recentHighs(monthlyPBs)
#print(recentGradeList)    

#pbList = maxGrades(monthlyPBs)
#print(pbList)

#execfile("styles.py")

#{"date": row[1],"url": row[0],"latitude": row[2],"longitude": row[3]}

app = Flask(__name__) #this is to make a "full-fledged" Flask application. The __name__ variable refers to the NAME OF THE CURRENT FILE. this line tells Flask to turn the current file into a Flask web application that will listen for browser requests

#next line tells Flask, what are my "routes". What are routes? URLs
#Python decorators apply one function to another. 
# Tip: You can use multiple decorators on the same function, one per line, depending on how many different routes you want to map to the same function.
#by default the methods list is "GET", if you want POST or anything else you have to include it in this list

#the if structure allows you to use the same route, so multiple pages get rendered on the same route. neater but also some other functionality is based on having it be the same route
@app.route("/")
def index():
    return render_template("index.html")
    
default='https://www.mountainproject.com/user/200166625/patrick-cheng/ticks'

@app.route("/analysis", methods = ['POST'])
def analysis():    
    url = request.args.get("url",default)
    # execfile('getTicks.py') shortcircuited due to MP throttling
    execfile('shortcut.py')
    execfile('PBanalysis.py')
    execfile('styles.py')

    recentGradeList = recentHighs(monthlyPBs)
    highGradeList = maxGrades(monthlyPBs)

    # at this state tickdf is loaded into memory
    # need to activate plots by inserting changing html with javascript on button press now
    # on button press: no need for new page... activate javascript

    gradefreqs = tickdf.loc[tickdf['gradekey']!=0,'gradekey'].value_counts().sort_index(ascending=False)
    grades = gradefreqs.index.tolist()
    freqs = gradefreqs.values.tolist()
    print(grades)
    print(freqs)

    return render_template('landing.html', datefill = datefill, recentGradeList = recentGradeList, highGradeList = highGradeList, allcounts = allcounts, alllabels = alllabels, grades = grades, freqs = freqs)

# take the plots one at a time (line, pie, pyramid which isn't done yet)
# what did line require? 



 
#@app.route("/styles", methods = ['POST'])
# def styles():
    #return render_template('styles.html', allcounts = allcounts, alllabels = alllabels, tencounts = tencounts, tenlabels = tenlabels, elecounts = elecounts, elelabels = elelabels, twelvecounts = twelvecounts, twelvelabels = twelvelabels)

    #the "request" library that you imported at the start gives you access to the HTTP request and any parameters in it. the way to use it is request.args.get("variable name"). Flask will parse the URL for the variable name and return it for use in index.html with Jinja syntax {{ name }}
    #use request.form.get("variable name") for POST. args for GET
    # GET /search?name=Brian HTTP/1.1    