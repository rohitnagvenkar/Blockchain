import subprocess
username = 'rohit'
password = 'password12345678'
host = 'http://3.17.183.98:14166/'

command = '''curl --user ''' + username + ':' + password + ''' --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getbalance", "params": ["", 6] }' -H 'content-type: text/plain;' ''' + host
p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
print(out)
