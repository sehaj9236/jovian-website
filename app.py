from flask import Flask,render_template,jsonify
app=Flask(__name__)
list_job=[{"job_post":"software engineer",
       "company":"TechCorp",
       "location":"Remote"
      }, 
     {"job_post":"Graphic designer",
      "company":"DesignCo",
      "location":"New York"
       },
     {"job_post":"Frontend Engineer",
      "company":"TechCorp",
      "location":"Bangalore"
       }]
@app.route('/')

def jovian_home():
  return render_template('home.html',list_job=list_job)
@app.route('/api/jobs')
def list_jobs():  
  return jsonify(list_job)
if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)
  