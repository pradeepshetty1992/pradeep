import pexpect


class Upgrade:
    def __init__(self):
        pass
    
    
    def ssh_adsp(self):
        username = "smxmgr"
        ip = "10.234.121.250"
        conn_str = 'ssh ' + username + "@" + ip + " -p " + str(22)
        spawn = pexpect.spawn(conn_str)
        spawn.expect('assword:', timeout=30)
        spawn.sendline("smxmgr")
        spawn.expect(['->', pexpect.EOF, pexpect.TIMEOUT], timeout=20)
        spawn.sendline("letmeout")
        spawn.expect('$')
        output2 = spawn.read_nonblocking(size=10000)
        print(output2)
        spawn.sendline("ls")
        #import pdb; pdb.set_trace()
        output2 = spawn.read_nonblocking(size=10000)
        spawn.expect('$')
        spawn.sendline("cd /usr/local/tmp")
        spawn.expect('$')
        print("Copying the Buid~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        spawn.sendline("scp qa@10.233.84.33:/usr/local/QA/AD-service-SM7-10.2.0-03.tar .")
        spawn.expect('assword:', timeout=30)
        spawn.sendline("QAl0gin")
        spawn.expect('\$', timeout=200)
        spawn.sendline("WIPSadmin")
        spawn.expect(['->', pexpect.EOF, pexpect.TIMEOUT], timeout=10)
        spawn.sendline("servmod")
        spawn.expect(['->', pexpect.EOF, pexpect.TIMEOUT], timeout=100)
        spawn.sendcontrol("m")
        spawn.expect(['->', pexpect.EOF, pexpect.TIMEOUT], timeout=100)
        spawn.sendline("8")
        spawn.expect([':', pexpect.EOF, pexpect.TIMEOUT], timeout=100)
        spawn.sendline("yes")
        print("Upgrading Build Start ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #spawn.expect([' ', pexpect.EOF, pexpect.TIMEOUT], timeout=100)
        #spawn.sendline("Q")
        spawn.expect([':', pexpect.EOF, pexpect.TIMEOUT], timeout=700)
        print(spawn.before)
        print(spawn.readlines())
        spawn.sendcontrol("m")
        spawn.close()

obj = Upgrade()
obj.ssh_adsp()
