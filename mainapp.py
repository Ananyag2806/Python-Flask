from flask import Flask, make_response, json,request,jsonify, render_template
from joblib import load
from flask_cors import CORS, cross_origin
model=load(r'E:\Python Flask\support_vector_machine')
app=Flask(__name__, template_folder='templates')
cors=CORS(app)
app.config['CORS_HEADERS']='Content-Type'
@app.route('/',methods=['GET', 'POST'])
@cross_origin()
def basic():
   
    if request.method=='POST':
        data=request.get_json()
        print(jsonify(data))
        X_test=[x for x in data.values()]
        y_pred=model.predict([X_test])
        return make_response(jsonify({'predicted_value':str(y_pred[0])}))
    
    else:
        return render_template("front end new.html")
        # return jsonify({'error':'no data'})

    

    


if __name__=='__main__':
    app.run(debug=True)

