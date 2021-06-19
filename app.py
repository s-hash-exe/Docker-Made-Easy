from flask import Flask, render_template, request
import subprocess as sp

app = Flask("myapp")
@app.route("/")
def homepage():
    return render_template("index.html");

@app.route("/start")
def start():
    (ret, data) = sp.getstatusoutput("systemctl start docker")
    data = "I am running."
    return render_template("success.html", substitute=data)

@app.route("/available")
def available():
    (ret, data) = sp.getstatusoutput("docker images")
    return render_template("success.html", substitute=data)
    
@app.route("/stop")
def stop():
    (ret, data) = sp.getstatusoutput("systemctl stop docker")
    data = "Engine has been stopped."
    return render_template("success.html", substitute=data)
    
@app.route("/active")
def active():
    (ret, data) = sp.getstatusoutput("docker ps")
    return render_template("success.html", substitute=data)
    
    
@app.route("/all")
def all():
    (ret, data) = sp.getstatusoutput("docker ps -a")
    return render_template("success.html", substitute=data)
    
@app.route("/terminateAll")
def terminateAll():
    (ret, data) = sp.getstatusoutput("docker rm -f $(docker ps -aq)")
    return render_template("success.html", substitute=data)
 

@app.route("/pull")
def pull():
    name = request.args.get("name")
    (ret, data) = sp.getstatusoutput("docker pull {}".format(name))
    return render_template("success.html", substitute=data)
        
    
@app.route("/inspect")
def inspect():
    name = request.args.get("name")
    (ret, data) = sp.getstatusoutput("docker container inspect {}".format(name))
    return render_template("success.html", substitute=data)
    
    
@app.route("/terminate")
def terminate():
    name = request.args.get("name")
    (ret, data) = sp.getstatusoutput("docker rm -f {}".format(name))
    return render_template("success.html", substitute=data)
    
@app.route("/launch")
def launch():
    name = request.args.get("name")
    image = request.args.get("image")
    net = request.args.get("network")
    (ret, data) = sp.getstatusoutput("docker run -dit --name {} --network {} {}".format(name, net, image))
    if ret==0:
        data1="Container has been launched. \n Container ID is \n{}".format(data)
    return render_template("success.html", substitute=data1)
    
@app.route("/customize")
def customize():
    name = request.args.get("name")
    image = request.args.get("image")
    tag = request.args.get("tag")
    (ret, data) = sp.getstatusoutput("docker commit {} {}:{}".format(name, image, tag))
    return render_template("success.html", substitute=data)
    
@app.route("/execute ")
def execute():
    name = request.args.get("name")
    prog = request.args.get("program")
    (ret, data) = sp.getstatusoutput("docker exec {} {}".format(name, prog))
    return render_template("success.html", substitute=data)
        
@app.route("/continue")
def ccontinue():
    return render_template("index.html");
    

   
    
  
    
app.run(host="0.0.0.0", port=1434, debug=True)





