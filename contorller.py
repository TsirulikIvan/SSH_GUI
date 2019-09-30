import paramiko

def Testing_local_network():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    file = open('computers.txt', 'r')
    for line in file:
        ip = line[-14::]
        print('Computer number {}'.format(ip))
        try:
            client.connect(hostname=ip, username="leninadm",
            password="12345", port=22)
        except Exception as err:
            print("Can`t connect! " + str(err))
        finally:
            client.close()

Testing_local_network() 

host = '192.168.88.24'
user = 'leninadm'
secret = '12345'
port = 22


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
run = True


while (run == True):
    cmd = input('Enter command:\n')
    stdin, stdout, stderr = client.exec_command(cmd)
    data = stdout.read() + stderr.read()
    print(type(data))
    print(data.decode('utf-8'))
    if (cmd == 'exit'):
        run = False
        print('Good bye!')
client.close()
