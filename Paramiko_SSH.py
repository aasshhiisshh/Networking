#Third Party Package
import paramiko
from paramiko import *

class ssh:
    def __init__(self, HOSTNAME, PORT, USERNAME, PASSWORD, command):
        self.HOSTNAME = HOSTNAME
        self.PORT = PORT
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
	self.command = command

    def ssh_execute(self):
        try:
            # Establish Connection
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.HOSTNAME, self.PORT, self.USERNAME, self.PASSWORD)
            # Establish session
            transport = self.client.get_transport()
            session = transport.open_session()
            session.setblocking(0)
            session.get_pty()
            session.invoke_shell()
            # Stdin/out/error Create
            (stdin, stdout, stderr) = self.client.exec_command(self.command)
            print "\nSTDOUT:",stdout.read()
            print "\nSTDERR:",stderr.read()
            #session ,self.client ,True
        except paramiko.ssh_exception.AuthenticationException as msg:
            print 'Check the Credentials First.',msg

# Put your output here and see the result
client = ssh(HOSTNAME, PORT, USERNAME, PASSWORD, command)
client.ssh_execute()
