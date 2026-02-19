The password for the next level is stored in a hidden file in the inhere directory.
        
$ ssh bandit3@bandit.labs.overthewire.org -p 2220

bandit3@bandit.labs.overthewire.org's password:(use from Level 2)

bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ file inhere
inhere: directory
bandit3@bandit:~$ find inhere
inhere
inhere/...Hiding-From-You
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ cat ./inhere
cat: ./inhere: No such file or directory
bandit3@bandit:~/inhere$ cat ./"inhere/...Hiding-From-You"
cat: ./inhere/...Hiding-From-You: No such file or directory
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ find in here
find: ‘in’: No such file or directory
find: ‘here’: No such file or directory
bandit3@bandit:~/inhere$ find inhere
find: ‘inhere’: No such file or directory
bandit3@bandit:~/inhere$ cat ./
cat: ./: Is a directory
bandit3@bandit:~/inhere$ cat /.
cat: /.: Is a directory
bandit3@bandit:~/inhere$ cat /."Hiding-From-You"
cat: /.Hiding-From-You: No such file or directory
bandit3@bandit:~/inhere$ file
Usage: file [-bcCdEhikLlNnprsSvzZ0] [--apple] [--extension] [--mime-encoding]
            [--mime-type] [-e <testname>] [-F <separator>]  [-f <namefile>]
            [-m <magicfiles>] [-P <parameter=value>] [--exclude-quiet]
            <file> ...
       file -C [-m <magicfiles>]
       file [--help]
bandit3@bandit:~/inhere$ cat file
cat: file: No such file or directory
bandit3@bandit:~/inhere$ cat .
cat: .: Is a directory
bandit3@bandit:~/inhere$ cd bandit3
-bash: cd: bandit3: No such file or directory
bandit3@bandit:~/inhere$ cd
bandit3@bandit:~$ cat /."inhere/...Hiding-From-You"
cat: /.inhere/...Hiding-From-You: No such file or directory
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -a
.  ..  ...Hiding-From-You
bandit3@bandit:~/inhere$ cat .hidden
cat: .hidden: No such file or directory
bandit3@bandit:~/inhere$ cat .Hiding-From-You
cat: .Hiding-From-You: No such file or directory
bandit3@bandit:~/inhere$ cat ...Hiding-From-You
(Use for level 4 access)

bandit3@bandit:~/inhere$ logout

Connection to bandit.labs.overthewire.org closed.
