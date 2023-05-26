from flask import Flask 
 
FAI=Flask(__name__)
@FAI.route('/wish/<na>/')
def wish(na):
    return f'Hello,Hai Are You {na}'
if __name__=='__main__':
    FAI.run(debug=True,port=5001,host='192.168.0.123')