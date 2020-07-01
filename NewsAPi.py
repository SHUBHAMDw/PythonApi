from flask import Flask,jsonify
import  requests
import json
app=Flask(__name__)

@app.route('/newsrequst',methods=['GET'])
def hello():
    url='http://newsapi.org/v2/everything?q=covid&from=2020-06-30&sortBy=publishedAt&apiKey=d2c48ff2e0f54ae9b748476f9efa9161'
    response = requests.get(url)
    jsonres=response.json()
    ifresponse.status_code==)
    data=jsonres['articles']
    #data=data[0]
    lis=[]
    for item in data:
        newnews={
        'author':item['author'],
        'description':item['description'],
        'title':item['title']
        }
        lis.append(newnews)
    print(lis[0])

    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)