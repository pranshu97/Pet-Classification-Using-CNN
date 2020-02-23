from flask import *  
import os
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("index.html")  

@app.route('/success', methods = ['POST'])  
def success():  
    app.config['UPLOAD_FOLDER'] = 'E:/PROJECTS/Dog-vs-Cat/images/test'
    if request.method == 'POST':  
        f = request.files['file']  
        f.filename = 'new.jpg'
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return redirect('/predict')  
        # return render_template("success.html", name = f.filename) 

@app.route('/predict')
def predict():
    import predict
    if predict.prediction():
    	return render_template("dog.html")
    return render_template("cat.html")

if __name__ == '__main__':  
    app.run(debug = False) 