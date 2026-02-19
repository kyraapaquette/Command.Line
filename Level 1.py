$ ssh bandit1@bandit.labs.overthewire.org -p 2220

bandit1@bandit.labs.overthewire.org's password: (From Level 0)


bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat -
ls
ls
cd -
cd -
^C
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cd -
-bash: cd: OLDPWD not set
bandit1@bandit:~$ -
-: command not found
bandit1@bandit:~$
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ passwd
Changing password for bandit1.
Current password:

passwd: Authentication token manipulation error
passwd: password unchanged
bandit1@bandit:~$
bandit1@bandit:~$ cd ~
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ ls -all
total 24
-rw-r-----   1 bandit2 bandit1   33 Oct 14 09:26 -
drwxr-xr-x   2 root    root    4096 Oct 14 09:26 .
drwxr-xr-x 150 root    root    4096 Oct 14 09:29 ..
-rw-r--r--   1 root    root     220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root    root    3851 Oct 14 09:19 .bashrc
-rw-r--r--   1 root    root     807 Mar 31  2024 .profile
bandit1@bandit:~$ cd ..
bandit1@bandit:/home$ ls
bandit0   bandit24      bandit5    drifter12    formulaone6  manpage1  narnia0  utumno6   vortex21
bandit1   bandit25      bandit6    drifter13    krypton1     manpage2  narnia1  utumno7   vortex22
bandit10  bandit26      bandit7    drifter14    krypton2     manpage3  narnia2  utumno8   vortex23
bandit11  bandit27      bandit8    drifter15    krypton3     manpage4  narnia3  vortex0   vortex24
bandit12  bandit27-git  bandit9    drifter2     krypton4     manpage5  narnia4  vortex1   vortex25
bandit13  bandit28      behemoth0  drifter3     krypton5     manpage6  narnia5  vortex10  vortex3
bandit14  bandit28-git  behemoth1  drifter4     krypton6     manpage7  narnia6  vortex11  vortex4
bandit15  bandit29      behemoth2  drifter5     krypton7     maze0     narnia7  vortex12  vortex5
bandit16  bandit29-git  behemoth3  drifter6     leviathan0   maze1     narnia8  vortex13  vortex6
bandit17  bandit3       behemoth4  drifter7     leviathan1   maze2     narnia9  vortex14  vortex7
bandit18  bandit30      behemoth5  drifter8     leviathan2   maze3     ubuntu   vortex15  vortex8
bandit19  bandit30-git  behemoth6  drifter9     leviathan3   maze4     utumno0  vortex16  vortex9
bandit2   bandit31      behemoth7  formulaone0  leviathan4   maze5     utumno1  vortex17
bandit20  bandit31-git  behemoth8  formulaone1  leviathan5   maze6     utumno2  vortex18
bandit21  bandit32      drifter0   formulaone2  leviathan6   maze7     utumno3  vortex19
bandit22  bandit33      drifter1   formulaone3  leviathan7   maze8     utumno4  vortex2
bandit23  bandit4       drifter10  formulaone5  manpage0     maze9     utumno5  vortex20
bandit1@bandit:/home$ bandit1
Command 'bandit1' not found, did you mean:
  command 'bandit' from snap bandit (1.8.6)
  command 'bandit' from deb python3-bandit (1.6.2-3)
See 'snap info <snapname>' for additional versions.
bandit1@bandit:/home$ bash bandit1
bandit1: bandit1: Is a directory
bandit1@bandit:/home$ -
-: command not found
bandit1@bandit:/home$ cat bandit1
cat: bandit1: Is a directory
bandit1@bandit:/home$ grep
Usage: grep [OPTION]... PATTERNS [FILE]...
Try 'grep --help' for more information.
bandit1@bandit:/home$ grep bandit1


^C
bandit1@bandit:/home$ ls
bandit0   bandit24      bandit5    drifter12    formulaone6  manpage1  narnia0  utumno6   vortex21
bandit1   bandit25      bandit6    drifter13    krypton1     manpage2  narnia1  utumno7   vortex22
bandit10  bandit26      bandit7    drifter14    krypton2     manpage3  narnia2  utumno8   vortex23
bandit11  bandit27      bandit8    drifter15    krypton3     manpage4  narnia3  vortex0   vortex24
bandit12  bandit27-git  bandit9    drifter2     krypton4     manpage5  narnia4  vortex1   vortex25
bandit13  bandit28      behemoth0  drifter3     krypton5     manpage6  narnia5  vortex10  vortex3
bandit14  bandit28-git  behemoth1  drifter4     krypton6     manpage7  narnia6  vortex11  vortex4
bandit15  bandit29      behemoth2  drifter5     krypton7     maze0     narnia7  vortex12  vortex5
bandit16  bandit29-git  behemoth3  drifter6     leviathan0   maze1     narnia8  vortex13  vortex6
bandit17  bandit3       behemoth4  drifter7     leviathan1   maze2     narnia9  vortex14  vortex7
bandit18  bandit30      behemoth5  drifter8     leviathan2   maze3     ubuntu   vortex15  vortex8
bandit19  bandit30-git  behemoth6  drifter9     leviathan3   maze4     utumno0  vortex16  vortex9
bandit2   bandit31      behemoth7  formulaone0  leviathan4   maze5     utumno1  vortex17
bandit20  bandit31-git  behemoth8  formulaone1  leviathan5   maze6     utumno2  vortex18
bandit21  bandit32      drifter0   formulaone2  leviathan6   maze7     utumno3  vortex19
bandit22  bandit33      drifter1   formulaone3  leviathan7   maze8     utumno4  vortex2
bandit23  bandit4       drifter10  formulaone5  manpage0     maze9     utumno5  vortex20
bandit1@bandit:/home$ file bandit1
bandit1: directory
bandit1@bandit:/home$ cd bandit1
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ file -
^C
bandit1@bandit:~$ cat -
^C
bandit1@bandit:~$ find password -
find: ‘password’: No such file or directory
-
bandit1@bandit:~$ bash -
bandit1@bandit:~$ cat ---
cat: unrecognized option '---'
Try 'cat --help' for more information.
bandit1@bandit:~$ cat -- -
^C
bandit1@bandit:~$ cat -.txt
cat: invalid option -- '.'
Try 'cat --help' for more information.
bandit1@bandit:~$ cat --.txt
cat: unrecognized option '--.txt'
Try 'cat --help' for more information.
bandit1@bandit:~$ cat -- -.txt
cat: -.txt: No such file or directory
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cd -
/home
bandit1@bandit:/home$ ls
bandit0   bandit24      bandit5    drifter12    formulaone6  manpage1  narnia0  utumno6   vortex21
bandit1   bandit25      bandit6    drifter13    krypton1     manpage2  narnia1  utumno7   vortex22
bandit10  bandit26      bandit7    drifter14    krypton2     manpage3  narnia2  utumno8   vortex23
bandit11  bandit27      bandit8    drifter15    krypton3     manpage4  narnia3  vortex0   vortex24
bandit12  bandit27-git  bandit9    drifter2     krypton4     manpage5  narnia4  vortex1   vortex25
bandit13  bandit28      behemoth0  drifter3     krypton5     manpage6  narnia5  vortex10  vortex3
bandit14  bandit28-git  behemoth1  drifter4     krypton6     manpage7  narnia6  vortex11  vortex4
bandit15  bandit29      behemoth2  drifter5     krypton7     maze0     narnia7  vortex12  vortex5
bandit16  bandit29-git  behemoth3  drifter6     leviathan0   maze1     narnia8  vortex13  vortex6
bandit17  bandit3       behemoth4  drifter7     leviathan1   maze2     narnia9  vortex14  vortex7
bandit18  bandit30      behemoth5  drifter8     leviathan2   maze3     ubuntu   vortex15  vortex8
bandit19  bandit30-git  behemoth6  drifter9     leviathan3   maze4     utumno0  vortex16  vortex9
bandit2   bandit31      behemoth7  formulaone0  leviathan4   maze5     utumno1  vortex17
bandit20  bandit31-git  behemoth8  formulaone1  leviathan5   maze6     utumno2  vortex18
bandit21  bandit32      drifter0   formulaone2  leviathan6   maze7     utumno3  vortex19
bandit22  bandit33      drifter1   formulaone3  leviathan7   maze8     utumno4  vortex2
bandit23  bandit4       drifter10  formulaone5  manpage0     maze9     utumno5  vortex20
bandit1@bandit:/home$ cd bandit1
bandit1@bandit:~$ cat -git.txt
cat: invalid option -- 'g'
Try 'cat --help' for more information.
bandit1@bandit:~$ cat -- -git.txt
cat: -git.txt: No such file or directory
bandit1@bandit:~$ cat ./-
(use for level 2 access)

bandit1@bandit:~$ logout
