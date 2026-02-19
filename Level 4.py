The password for the next level is stored in the only human-readable file in the inhere directory. 

$ ssh bandit4@bandit.labs.overthewire.org -p 2220

bandit4@bandit.labs.overthewire.org's password: (use from Level 3)

bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ cd inhere
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ cat .
cat: .: Is a directory
bandit4@bandit:~/inhere$ ls file^[[2~
ls: cannot access 'file'$'\033''[2~': No such file or directory
bandit4@bandit:~/inhere$ ls file00
ls: cannot access 'file00': No such file or directory
bandit4@bandit:~/inhere$ file
Usage: file [-bcCdEhikLlNnprsSvzZ0] [--apple] [--extension] [--mime-encoding]
            [--mime-type] [-e <testname>] [-F <separator>]  [-f <namefile>]
            [-m <magicfiles>] [-P <parameter=value>] [--exclude-quiet]
            <file> ...
       file -C [-m <magicfiles>]
       file [--help]
bandit4@bandit:~/inhere$ file00
file00: command not found
bandit4@bandit:~/inhere$ cd
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ file inhere
inhere: directory
bandit4@bandit:~$ file ls
ls: cannot open `ls' (No such file or directory)
bandit4@bandit:~$ cat -a
cat: invalid option -- 'a'
Try 'cat --help' for more information.
bandit4@bandit:~$ find
.
./.bash_logout
./inhere
./inhere/-file02
./inhere/-file04
./inhere/-file08
./inhere/-file00
./inhere/-file07
./inhere/-file06
./inhere/-file01
./inhere/-file03
./inhere/-file05
./inhere/-file09
./.bashrc
./.profile
bandit4@bandit:~$ cat ./inhere/-file02
ZnSN:4H▒▒▒'MЗey▒.▒-W▒ =bandit4@bandit:~$ .
-bash: .: filename argument required
.: usage: . filename [arguments]
bandit4@bandit:~$ cat ./inhere/-file04
%Mr3ca烺S_▒▒▒rbandit4@bandit:~$ ..
..: command not found
bandit4@bandit:~$ cat ./inhere/-file08
▒6▒
   }|&ڧa▒C▒9▒̸n▒q▒dM'όwbandit4@bandit:~$ ..
..: command not found
bandit4@bandit:~$ file00
file00: command not found
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ cd inhere
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ cat -a
cat: invalid option -- 'a'
Try 'cat --help' for more information.
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ cat ./*
6);/:ˋd▒Jhp▒r▒▒}k'▒vj7-(c\;d3_~r:#罘▒b2ZnSN:4H▒▒▒'MЗey▒.▒-W▒ =C▒▒▒▒▒z鈸1[;ҭ
hWu8;޿▒lFPIm&䙰▒▒|3=˸B▒▒▒▒S▒/Y["#4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
6
 }|&ڧa▒C▒9▒̸n▒q▒dM'όw=▒[h+|:[▒P
                              ▒]K1*~wbandit4@bandit:~/inhere$ ..
..: command not found
bandit4@bandit:~/inhere$ cat *
cat: invalid option -- 'f'
Try 'cat --help' for more information.
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
(use for access to Level 5)

bandit4@bandit:~/inhere$ logout

Connection to bandit.labs.overthewire.org closed.