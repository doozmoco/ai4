flask code 
from flask import Flask,request,jsonify 

app=Flask(name)


@app.route('/api/messages',methods=['POST'])
def receive_message():
    #get the JSON data from the request
    data=request.json
    message=data.get('message','')
    print(f"Received mesaage:{message}")

    return jsonify({"status":"Message received!"})


if _name=='main_':
    app.run(host='0.0.0.0',port=5000)
