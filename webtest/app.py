# app.py

from flask import Flask, request
import ssh

app = Flask(__name__)
app.register_blueprint(ssh.bp)

if __name__ == '__main__':
  app.run()
