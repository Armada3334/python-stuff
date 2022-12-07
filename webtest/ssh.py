# ssh.py

import paramiko
from flask import Blueprint, request

bp = Blueprint('ssh', __name__)

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect('150.136.248.163', username='armada', password='Armada2002307!')

@bp.route('/ssh', methods=['POST'])
def ssh():
  # Execute the user's input on the remote machine
  stdin, stdout, stderr = ssh.exec_command(request.data)

  # Return the output to be displayed in the terminal
  return stdout.read()
