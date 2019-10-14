import paramiko



def Searching_right_port():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for i in range(0,2049):
        ip = '192.168.88.37'
        print('Port {0} \n'.format(i))
        #passw = input('Enter pass\n')
        try:
            client.connect(hostname=ip, username="leninadm",
            password="liblen19", port=i)
            stdin, stdout, stderr = client.exec_command('w')
            data = stdout.read() + stderr.read()
            print(data.decode('utf-8'))
        except Exception as err:
            print("Can`t connect! " + str(err) + '\n')
        finally:
            client.close()
        print("--------------------------------------\n")


def Testing_local_network():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    n = 0
    for i in range(31,39):
        ip = '192.168.88.' + str(i)
        number_pc = str(i - 30)
        print('Computer number {0} ip {1}: \n'.format(number_pc, ip))
        #passw = input('Enter pass\n')
        try:
            client.connect(hostname=ip, username="leninadm",
            password="liblen19", port=738)
            stdin, stdout, stderr = client.exec_command('ifconfig')
            data = stdout.read() + stderr.read()
            msg = data.decode('utf-8')
            print(type(msg))
            print(msg)
            n = n + 1
            print('Number of iter {}'.format(n))
        except Exception as err:
            print("Can`t connect! " + str(err) + '\n')
        finally:
            client.close()
        print("--------------------------------------\n")
Testing_local_network()
#Searching_right_port()
