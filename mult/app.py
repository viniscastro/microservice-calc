from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

@app.route('/mult')
def multiply():
    op1 = float(request.args.get('op1', 0))
    op2 = float(request.args.get('op2', 0))
    resultado = op1 * op2
    
    return jsonify({
        "operacao": "multiplicacao",
        "resultado": resultado,
        "container_id": socket.gethostname() # Identifica qual container respondeu
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)