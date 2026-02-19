$ ssh bandit2@bandit.labs.overthewire.org -p 2220

bandit2@bandit.labs.overthewire.org's password:(From level 1)

bandit2@bandit:~$ dir
--spaces in this filename--
bandit2@bandit:~$ cat spaces\ in\ this\filename
cat: 'spaces in thisfilename': No such file or directory
bandit2@bandit:~$ cat spaces\ in\ this\ filename
cat: 'spaces in this filename': No such file or directory
bandit2@bandit:~$ ls
--spaces in this filename--
bandit2@bandit:~$ cat -- -spaces in this filename
cat: -spaces: No such file or directory
cat: in: No such file or directory
cat: this: No such file or directory
cat: filename: No such file or directory
bandit2@bandit:~$ ls
--spaces in this filename--
bandit2@bandit:~$ cat /. --spaces in this filename--
cat: unrecognized option '--spaces'
Try 'cat --help' for more information.
bandit2@bandit:~$ cd
bandit2@bandit:~$ ;s
-bash: syntax error near unexpected token `;'
bandit2@bandit:~$ ls
--spaces in this filename--
bandit2@bandit:~$ dir
--spaces in this filename--
bandit2@bandit:~$ cd --spaces in this filename--
-bash: cd: --: invalid option
cd: usage: cd [-L|[-P [-e]] [-@]] [dir]
bandit2@bandit:~$ cd spaces\ in\ this\ filename
-bash: cd: spaces in this filename: No such file or directory
bandit2@bandit:~$ cat spaces\in \this\ filename
cat: spacesin: No such file or directory
cat: 'this filename': No such file or directory
bandit2@bandit:~$ dir spaces\ in\ this\ filename
dir: cannot access 'spaces in this filename': No such file or directory
bandit2@bandit:~$ ls
--spaces in this filename--
bandit2@bandit:~$ cat "spaces in this filename"
cat: 'spaces in this filename': No such file or directory
bandit2@bandit:~$ cat spaces\in\this\filename
cat: spacesinthisfilename: No such file or directory
bandit2@bandit:~$ cat ./"--spaces in this filename--"
(use for level 3 access)

bandit2@bandit:~$ logout

Connection to bandit.labs.overthewire.org closed.
