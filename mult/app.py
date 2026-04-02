from flask import Flask, request, jsonify
import socket  # <-- Isso é essencial para a Questão 1 e 2!

app = Flask(__name__)

@app.route('/mult')
def multiply():
    try:
        op1 = float(request.args.get('op1', 0))
        op2 = float(request.args.get('op2', 0))
        res = op1 * op2
        return jsonify({
            "resultado": res,
            "container_id": socket.gethostname() 
        })
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)