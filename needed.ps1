try {
    python3 -m pip install --upgrade pip
    pip3 install argparse pytermgui npyscreen paramiko
}
catch {
    exit(1)
}