The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

human-readable
1033 bytes in size
not executable

$ ssh bandit5@bandit.labs.overthewire.org -p 2220

bandit5@bandit.labs.overthewire.org's password: (use Level 4 Access Code)

bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ cd inhere
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
bandit5@bandit:~/inhere$ file /.*
/.*: cannot open `/.*' (No such file or directory)
bandit5@bandit:~/inhere$ file ./*
./maybehere00: directory
./maybehere01: directory
./maybehere02: directory
./maybehere03: directory
./maybehere04: directory
./maybehere05: directory
./maybehere06: directory
./maybehere07: directory
./maybehere08: directory
./maybehere09: directory
./maybehere10: directory
./maybehere11: directory
./maybehere12: directory
./maybehere13: directory
./maybehere14: directory
./maybehere15: directory
./maybehere16: directory
./maybehere17: directory
./maybehere18: directory
./maybehere19: directory
bandit5@bandit:~/inhere$ find ./*
./maybehere00
./maybehere00/.file1
./maybehere00/.file2
./maybehere00/.file3
./maybehere00/-file1
./maybehere00/spaces file3
./maybehere00/spaces file2
./maybehere00/-file2
./maybehere00/spaces file1
./maybehere00/-file3
./maybehere01
./maybehere01/.file1
./maybehere01/.file2
./maybehere01/.file3
./maybehere01/-file1
./maybehere01/spaces file3
./maybehere01/spaces file2
./maybehere01/-file2
./maybehere01/spaces file1
./maybehere01/-file3
./maybehere02
./maybehere02/.file1
./maybehere02/.file2
./maybehere02/.file3
./maybehere02/-file1
./maybehere02/spaces file3
./maybehere02/spaces file2
./maybehere02/-file2
./maybehere02/spaces file1
./maybehere02/-file3
./maybehere03
./maybehere03/.file1
./maybehere03/.file2
./maybehere03/.file3
./maybehere03/-file1
./maybehere03/spaces file3
./maybehere03/spaces file2
./maybehere03/-file2
./maybehere03/spaces file1
./maybehere03/-file3
./maybehere04
./maybehere04/.file1
./maybehere04/.file2
./maybehere04/.file3
./maybehere04/-file1
./maybehere04/spaces file3
./maybehere04/spaces file2
./maybehere04/-file2
./maybehere04/spaces file1
./maybehere04/-file3
./maybehere05
./maybehere05/.file1
./maybehere05/.file2
./maybehere05/.file3
./maybehere05/-file1
./maybehere05/spaces file3
./maybehere05/spaces file2
./maybehere05/-file2
./maybehere05/spaces file1
./maybehere05/-file3
./maybehere06
./maybehere06/.file1
./maybehere06/.file2
./maybehere06/.file3
./maybehere06/-file1
./maybehere06/spaces file3
./maybehere06/spaces file2
./maybehere06/-file2
./maybehere06/spaces file1
./maybehere06/-file3
./maybehere07
./maybehere07/.file1
./maybehere07/.file2
./maybehere07/.file3
./maybehere07/-file1
./maybehere07/spaces file3
./maybehere07/spaces file2
./maybehere07/-file2
./maybehere07/spaces file1
./maybehere07/-file3
./maybehere08
./maybehere08/.file1
./maybehere08/.file2
./maybehere08/.file3
./maybehere08/-file1
./maybehere08/spaces file3
./maybehere08/spaces file2
./maybehere08/-file2
./maybehere08/spaces file1
./maybehere08/-file3
./maybehere09
./maybehere09/.file1
./maybehere09/.file2
./maybehere09/.file3
./maybehere09/-file1
./maybehere09/spaces file3
./maybehere09/spaces file2
./maybehere09/-file2
./maybehere09/spaces file1
./maybehere09/-file3
./maybehere10
./maybehere10/.file1
./maybehere10/.file2
./maybehere10/.file3
./maybehere10/-file1
./maybehere10/spaces file3
./maybehere10/spaces file2
./maybehere10/-file2
./maybehere10/spaces file1
./maybehere10/-file3
./maybehere11
./maybehere11/.file1
./maybehere11/.file2
./maybehere11/.file3
./maybehere11/-file1
./maybehere11/spaces file3
./maybehere11/spaces file2
./maybehere11/-file2
./maybehere11/spaces file1
./maybehere11/-file3
./maybehere12
./maybehere12/.file1
./maybehere12/.file2
./maybehere12/.file3
./maybehere12/-file1
./maybehere12/spaces file3
./maybehere12/spaces file2
./maybehere12/-file2
./maybehere12/spaces file1
./maybehere12/-file3
./maybehere13
./maybehere13/.file1
./maybehere13/.file2
./maybehere13/.file3
./maybehere13/-file1
./maybehere13/spaces file3
./maybehere13/spaces file2
./maybehere13/-file2
./maybehere13/spaces file1
./maybehere13/-file3
./maybehere14
./maybehere14/.file1
./maybehere14/.file2
./maybehere14/.file3
./maybehere14/-file1
./maybehere14/spaces file3
./maybehere14/spaces file2
./maybehere14/-file2
./maybehere14/spaces file1
./maybehere14/-file3
./maybehere15
./maybehere15/.file1
./maybehere15/.file2
./maybehere15/.file3
./maybehere15/-file1
./maybehere15/spaces file3
./maybehere15/spaces file2
./maybehere15/-file2
./maybehere15/spaces file1
./maybehere15/-file3
./maybehere16
./maybehere16/.file1
./maybehere16/.file2
./maybehere16/.file3
./maybehere16/-file1
./maybehere16/spaces file3
./maybehere16/spaces file2
./maybehere16/-file2
./maybehere16/spaces file1
./maybehere16/-file3
./maybehere17
./maybehere17/.file1
./maybehere17/.file2
./maybehere17/.file3
./maybehere17/-file1
./maybehere17/spaces file3
./maybehere17/spaces file2
./maybehere17/-file2
./maybehere17/spaces file1
./maybehere17/-file3
./maybehere18
./maybehere18/.file1
./maybehere18/.file2
./maybehere18/.file3
./maybehere18/-file1
./maybehere18/spaces file3
./maybehere18/spaces file2
./maybehere18/-file2
./maybehere18/spaces file1
./maybehere18/-file3
./maybehere19
./maybehere19/.file1
./maybehere19/.file2
./maybehere19/.file3
./maybehere19/-file1
./maybehere19/spaces file3
./maybehere19/spaces file2
./maybehere19/-file2
./maybehere19/spaces file1
./maybehere19/-file3
bandit5@bandit:~/inhere$ du ./*
68      ./maybehere00
76      ./maybehere01
64      ./maybehere02
76      ./maybehere03
56      ./maybehere04
60      ./maybehere05
60      ./maybehere06
52      ./maybehere07
52      ./maybehere08
72      ./maybehere09
52      ./maybehere10
68      ./maybehere11
68      ./maybehere12
60      ./maybehere13
56      ./maybehere14
60      ./maybehere15
76      ./maybehere16
68      ./maybehere17
64      ./maybehere18
72      ./maybehere19
bandit5@bandit:~/inhere$ find . -type f -readbale -size 1033c ! -executable
find: unknown predicate `-readbale'
bandit5@bandit:~/inhere$ find . -type f -readable -size 1033c ! -executable
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
(use this to access Level 6)

bandit5@bandit:~/inhere$ logout

Connection to bandit.labs.overthewire.org closed.

