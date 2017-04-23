import os
import sys
from flask import Flask
from flask import request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "<center><h2>Insert Tamil Text</h2><br/><form method = \"post\" id=\"tamilinputform\"><textarea form=\"tamilinputform\" name=\"tamilinput\" cols=\"80\" rows=\"20\"></textarea><br/><input type=\"submit\" /></form></ceter>";
    else:
        tamilinput=request.form['tamilinput']
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        print("%s"%(tamilinput))
        open("/tmp/%s.txt"%(timestamp), "w").write(tamilinput.encode('utf8'))
        #        cwd = os.path.dirname(os.readlink(sys.argv[0]))
        #        os.system(cwd + "/../../src/flite_hts_tamil -m " + cwd + "../../asserts/naveen_tamil.htsvoice -o " + timestamp + ".wav")
        os.remove("/tmp/%s.txt"%(timestamp))
        #        return app.send_static_file(timestamp + ".wav")
        return "helloworld"

if __name__ == "__main__":
    app.run("0.0.0.0", 8888)
