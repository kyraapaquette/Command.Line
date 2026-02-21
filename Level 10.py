The password for the next level is stored in the file data.txt, which contains base64 encoded data
    
PS C:\Users\paque\Git\.git\Command.Line> ssh bandit10@bandit.labs.overthewire.org -p 2220

bandit10@bandit.labs.overthewire.org's password:(use access code from level 9)

bandit10@bandit:~$ base64 data.txt
VkdobElIQmhjM04zYjNKa0lHbHpJR1IwVWpFM00yWmFTMkl3VWxKelJFWlRSM05uTWxKWGJuQk9W
bW96Y1ZKeUNnPT0K
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ base64 -d data.txt
The password is (use this to acceess level 11)

bandit10@bandit:~$ logout

Connection to bandit.labs.overthewire.org closed.