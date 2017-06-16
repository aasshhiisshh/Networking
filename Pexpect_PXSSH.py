import pexpect
from pexpect import pxssh


class ssh:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()
    
    # Establish the connection
    def connect(self):
        try:
	    global s
            s = pexpect.spawn('ssh '+self.user+'@'+self.host)
            s.expect_exact('password:')
	    s.sendline(self.password)
        except Exception as E:
            print "Exception ",E
            print "[-] Error Connecting"
    # Send the command in one session
    def execute_command(self, cmd, pas=None):
	global s
	self.robot_env.log_to_console(self.host)	
	s.expect_exact("@undercloud ~]$ ")
        s.sendline(cmd)
	if pas != None:
	    s.expect_exact("Password: ")
	    s.sendline(pas)
        print s.before,s.after
	try:
            s.expect([],timeout=30)
	except pexpect.EOF:
    	    print "It is inside EOF"
	except pexpect.TIMEOUT:
            print "It is inside timeout"

# Put your output and see the Result
Client = ssh(host, user, password)
Client.execute_command()


