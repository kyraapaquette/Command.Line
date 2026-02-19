The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7
owned by group bandit6
33 bytes in size

$ ssh bandit6@bandit.labs.overthewire.org -p 2220

bandit6@bandit.labs.overthewire.org's password:(Use Level 5 access code)

bandit6@bandit:~$ ls
bandit6@bandit:~$ file
Usage: file [-bcCdEhikLlNnprsSvzZ0] [--apple] [--extension] [--mime-encoding]
            [--mime-type] [-e <testname>] [-F <separator>]  [-f <namefile>]
            [-m <magicfiles>] [-P <parameter=value>] [--exclude-quiet]
            <file> ...
       file -C [-m <magicfiles>]
       file [--help]
bandit6@bandit:~$ file .
.: directory
bandit6@bandit:~$ cd
bandit6@bandit:~$ cat /.file
cat: /.file: No such file or directory
bandit6@bandit:~$ cat ./file
cat: ./file: No such file or directory
bandit6@bandit:~$ find / -user bandit7
find: ‘/proc/tty/driver’: Permission denied
find: ‘/proc/1/task/1/fd’: Permission denied
find: ‘/proc/1/task/1/fdinfo’: Permission denied
find: ‘/proc/1/task/1/ns’: Permission denied
find: ‘/proc/1/fd’: Permission denied
find: ‘/proc/1/map_files’: Permission denied
find: ‘/proc/1/fdinfo’: Permission denied
find: ‘/proc/1/ns’: Permission denied
find: ‘/proc/2/task/2/fd’: Permission denied
find: ‘/proc/2/task/2/fdinfo’: Permission denied
find: ‘/proc/2/task/2/ns’: Permission denied
find: ‘/proc/2/fd’: Permission denied
find: ‘/proc/2/map_files’: Permission denied
find: ‘/proc/2/fdinfo’: Permission denied
find: ‘/proc/2/ns’: Permission denied
find: ‘/proc/42/task/42/fd/6’: No such file or directory
find: ‘/proc/42/task/42/fdinfo/6’: No such file or directory
find: ‘/proc/42/fd/5’: No such file or directory
find: ‘/proc/42/fdinfo/5’: No such file or directory
find: ‘/lost+found’: Permission denied
find: ‘/var/tmp’: Permission denied
find: ‘/var/spool/bandit24’: Permission denied
find: ‘/var/spool/cron/crontabs’: Permission denied
find: ‘/var/spool/rsyslog’: Permission denied
find: ‘/var/lib/update-notifier/package-data-downloads/partial’: Permission denied
find: ‘/var/lib/apt/lists/partial’: Permission denied
find: ‘/var/lib/polkit-1’: Permission denied
find: ‘/var/lib/chrony’: Permission denied
find: ‘/var/lib/udisks2’: Permission denied
find: ‘/var/lib/snapd/cookie’: Permission denied
find: ‘/var/lib/snapd/void’: Permission denied
find: ‘/var/lib/private’: Permission denied
find: ‘/var/lib/ubuntu-advantage/apt-esm/var/lib/apt/lists/partial’: Permission denied
/var/lib/dpkg/info/bandit7.password
find: ‘/var/lib/amazon’: Permission denied
find: ‘/var/crash’: Permission denied
find: ‘/var/cache/apt/archives/partial’: Permission denied
find: ‘/var/cache/pollinate’: Permission denied
find: ‘/var/cache/private’: Permission denied
find: ‘/var/cache/apparmor/208b6430.0’: Permission denied
find: ‘/var/cache/apparmor/0fb44ac6.0’: Permission denied
find: ‘/var/cache/ldconfig’: Permission denied
find: ‘/var/log’: Permission denied
find: ‘/sys/kernel/tracing/osnoise’: Permission denied
find: ‘/sys/kernel/tracing/hwlat_detector’: Permission denied
find: ‘/sys/kernel/tracing/instances’: Permission denied
find: ‘/sys/kernel/tracing/trace_stat’: Permission denied
find: ‘/sys/kernel/tracing/per_cpu’: Permission denied
find: ‘/sys/kernel/tracing/options’: Permission denied
find: ‘/sys/kernel/tracing/rv’: Permission denied
find: ‘/sys/kernel/debug’: Permission denied
find: ‘/sys/fs/pstore’: Permission denied
find: ‘/sys/fs/bpf’: Permission denied
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/cgroup.procs
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/cgroup.threads
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cgroup.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/io.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cgroup.procs
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.events.local
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.swap.peak
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.swap.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.swap.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.zswap.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cpu.weight
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.swap.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cgroup.max.descendants
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cpu.stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cpu.weight.nice
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/pids.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/pids.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.low
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cpu.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cgroup.type
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cgroup.stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.swap.high
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cpu.idle
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cpu.stat.local
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cgroup.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/io.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cgroup.procs
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.events.local
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.swap.peak
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.swap.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.swap.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.zswap.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.swap.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cgroup.max.descendants
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cpu.stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/pids.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/pids.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.low
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cpu.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cgroup.type
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cgroup.stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.swap.high
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cpu.stat.local
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cgroup.threads
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.numa_stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cgroup.kill
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.peak
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cgroup.freeze
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.min
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cgroup.controllers
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.oom.group
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.zswap.writeback
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.high
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/pids.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.zswap.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/pids.events.local
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cgroup.subtree_control
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/memory.reclaim
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/pids.peak
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cgroup.max.depth
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/dbus.socket/cgroup.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cgroup.threads
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.numa_stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cgroup.kill
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cgroup.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/io.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cgroup.procs
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.events.local
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.swap.peak
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.swap.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.swap.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.zswap.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.swap.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cgroup.max.descendants
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cpu.stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/pids.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/pids.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.low
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cpu.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cgroup.type
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cgroup.stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.swap.high
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cpu.stat.local
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cgroup.threads
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.numa_stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cgroup.kill
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.peak
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cgroup.freeze
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.min
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cgroup.controllers
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.oom.group
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.zswap.writeback
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.high
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/pids.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.zswap.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/pids.events.local
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cgroup.subtree_control
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/memory.reclaim
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/pids.peak
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cgroup.max.depth
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/gpg-agent-ssh.socket/cgroup.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.peak
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cgroup.freeze
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.min
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cpu.max.burst
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cgroup.controllers
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cpu.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.oom.group
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.zswap.writeback
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cpu.uclamp.min
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.high
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/pids.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.zswap.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/pids.events.local
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cgroup.subtree_control
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/memory.reclaim
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/pids.peak
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cgroup.max.depth
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cgroup.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/app.slice/cpu.uclamp.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cgroup.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/io.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cgroup.procs
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.events.local
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.swap.peak
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.swap.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.swap.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.zswap.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cpu.weight
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.swap.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cgroup.max.descendants
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cpu.stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cpu.weight.nice
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/pids.current
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/pids.events
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.low
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cpu.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cgroup.type
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cgroup.stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.swap.high
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cpu.idle
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cpu.stat.local
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cgroup.threads
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.numa_stat
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cgroup.kill
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.peak
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cgroup.freeze
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.min
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cpu.max.burst
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cgroup.controllers
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cpu.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.oom.group
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.zswap.writeback
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cpu.uclamp.min
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.high
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/pids.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.zswap.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/pids.events.local
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cgroup.subtree_control
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/memory.reclaim
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/pids.peak
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cgroup.max.depth
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cgroup.pressure
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/init.scope/cpu.uclamp.max
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/memory.oom.group
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/cgroup.subtree_control
/sys/fs/cgroup/user.slice/user-11007.slice/user@11007.service/memory.reclaim
find: ‘/drifter/drifter14_src/axTLS’: Permission denied
find: ‘/tmp’: Permission denied
find: ‘/snap’: Permission denied
find: ‘/home/bandit31-git’: Permission denied
find: ‘/home/leviathan4/.trash’: Permission denied
find: ‘/home/drifter8/chroot’: Permission denied
find: ‘/home/bandit29-git’: Permission denied
find: ‘/home/bandit27-git’: Permission denied
find: ‘/home/drifter6/data’: Permission denied
find: ‘/home/bandit5/inhere’: Permission denied
find: ‘/home/bandit28-git’: Permission denied
find: ‘/home/leviathan0/.backup’: Permission denied
find: ‘/home/ubuntu’: Permission denied
find: ‘/home/bandit30-git’: Permission denied
find: ‘/boot/efi’: Permission denied
find: ‘/boot/lost+found’: Permission denied
find: ‘/run/pam_pidns’: Permission denied
find: ‘/run/udisks2’: Permission denied
find: ‘/run/chrony’: Permission denied
find: ‘/run/user/11021’: Permission denied
find: ‘/run/user/11022’: Permission denied
find: ‘/run/user/11024’: Permission denied
find: ‘/run/user/14001’: Permission denied
find: ‘/run/user/11011’: Permission denied
find: ‘/run/user/11014’: Permission denied
find: ‘/run/user/11009’: Permission denied
find: ‘/run/user/11010’: Permission denied
find: ‘/run/user/12006’: Permission denied
find: ‘/run/user/11003’: Permission denied
/run/user/11007
find: ‘/run/user/11007’: Permission denied
find: ‘/run/user/11025’: Permission denied
find: ‘/run/user/11002’: Permission denied
find: ‘/run/user/11008’: Permission denied
find: ‘/run/user/11020’: Permission denied
find: ‘/run/user/12002’: Permission denied
find: ‘/run/user/11001’: Permission denied
find: ‘/run/user/11013’: Permission denied
find: ‘/run/user/11006/systemd/inaccessible/dir’: Permission denied
find: ‘/run/user/11005’: Permission denied
find: ‘/run/user/11016’: Permission denied
find: ‘/run/user/11012’: Permission denied
find: ‘/run/user/11000’: Permission denied
find: ‘/run/user/11004’: Permission denied
find: ‘/run/sudo’: Permission denied
find: ‘/run/screen/S-bandit20’: Permission denied
find: ‘/run/multipath’: Permission denied
find: ‘/run/cryptsetup’: Permission denied
find: ‘/run/lvm’: Permission denied
find: ‘/run/systemd/propagate/ModemManager.service’: Permission denied
find: ‘/run/systemd/propagate/polkit.service’: Permission denied
find: ‘/run/systemd/propagate/chrony.service’: Permission denied
find: ‘/run/systemd/propagate/systemd-logind.service’: Permission denied
find: ‘/run/systemd/propagate/irqbalance.service’: Permission denied
find: ‘/run/systemd/propagate/systemd-networkd.service’: Permission denied
find: ‘/run/systemd/propagate/systemd-resolved.service’: Permission denied
find: ‘/run/systemd/propagate/systemd-udevd.service’: Permission denied
find: ‘/run/systemd/inaccessible/dir’: Permission denied
find: ‘/run/lock/lvm’: Permission denied
find: ‘/etc/multipath’: Permission denied
/etc/bandit_pass/bandit7
find: ‘/etc/stunnel’: Permission denied
find: ‘/etc/credstore.encrypted’: Permission denied
find: ‘/etc/sudoers.d’: Permission denied
find: ‘/etc/xinetd.d’: Permission denied
find: ‘/etc/polkit-1/rules.d’: Permission denied
find: ‘/etc/credstore’: Permission denied
find: ‘/etc/ssl/private’: Permission denied
find: ‘/root’: Permission denied
find: ‘/manpage/manpage3-pw’: Permission denied
find: ‘/dev/mqueue’: Permission denied
find: ‘/dev/shm’: Permission denied

bandit6@bandit:~$ find / -user bandit7 -group bandit6
find: ‘/proc/tty/driver’: Permission denied
find: ‘/proc/1/task/1/fd’: Permission denied
find: ‘/proc/1/task/1/fdinfo’: Permission denied
find: ‘/proc/1/task/1/ns’: Permission denied
find: ‘/proc/1/fd’: Permission denied
find: ‘/proc/1/map_files’: Permission denied
find: ‘/proc/1/fdinfo’: Permission denied
find: ‘/proc/1/ns’: Permission denied
find: ‘/proc/2/task/2/fd’: Permission denied
find: ‘/proc/2/task/2/fdinfo’: Permission denied
find: ‘/proc/2/task/2/ns’: Permission denied
find: ‘/proc/2/fd’: Permission denied
find: ‘/proc/2/map_files’: Permission denied
find: ‘/proc/2/fdinfo’: Permission denied
find: ‘/proc/2/ns’: Permission denied
find: ‘/proc/43/task/43/fd/6’: No such file or directory
find: ‘/proc/43/task/43/fdinfo/6’: No such file or directory
find: ‘/proc/43/fd/5’: No such file or directory
find: ‘/proc/43/fdinfo/5’: No such file or directory
find: ‘/lost+found’: Permission denied
find: ‘/var/tmp’: Permission denied
find: ‘/var/spool/bandit24’: Permission denied
find: ‘/var/spool/cron/crontabs’: Permission denied
find: ‘/var/spool/rsyslog’: Permission denied
find: ‘/var/lib/update-notifier/package-data-downloads/partial’: Permission denied
find: ‘/var/lib/apt/lists/partial’: Permission denied
find: ‘/var/lib/polkit-1’: Permission denied
find: ‘/var/lib/chrony’: Permission denied
find: ‘/var/lib/udisks2’: Permission denied
find: ‘/var/lib/snapd/cookie’: Permission denied
find: ‘/var/lib/snapd/void’: Permission denied
find: ‘/var/lib/private’: Permission denied
find: ‘/var/lib/ubuntu-advantage/apt-esm/var/lib/apt/lists/partial’: Permission denied
/var/lib/dpkg/info/bandit7.password
find: ‘/var/lib/amazon’: Permission denied
find: ‘/var/crash’: Permission denied
find: ‘/var/cache/apt/archives/partial’: Permission denied
find: ‘/var/cache/pollinate’: Permission denied
find: ‘/var/cache/private’: Permission denied
find: ‘/var/cache/apparmor/208b6430.0’: Permission denied
find: ‘/var/cache/apparmor/0fb44ac6.0’: Permission denied
find: ‘/var/cache/ldconfig’: Permission denied
find: ‘/var/log’: Permission denied
find: ‘/sys/kernel/tracing/osnoise’: Permission denied
find: ‘/sys/kernel/tracing/hwlat_detector’: Permission denied
find: ‘/sys/kernel/tracing/instances’: Permission denied
find: ‘/sys/kernel/tracing/trace_stat’: Permission denied
find: ‘/sys/kernel/tracing/per_cpu’: Permission denied
find: ‘/sys/kernel/tracing/options’: Permission denied
find: ‘/sys/kernel/tracing/rv’: Permission denied
find: ‘/sys/kernel/debug’: Permission denied
find: ‘/sys/fs/pstore’: Permission denied
find: ‘/sys/fs/bpf’: Permission denied
find: ‘/drifter/drifter14_src/axTLS’: Permission denied
find: ‘/tmp’: Permission denied
find: ‘/snap’: Permission denied
find: ‘/home/bandit31-git’: Permission denied
find: ‘/home/leviathan4/.trash’: Permission denied
find: ‘/home/drifter8/chroot’: Permission denied
find: ‘/home/bandit29-git’: Permission denied
find: ‘/home/bandit27-git’: Permission denied
find: ‘/home/drifter6/data’: Permission denied
find: ‘/home/bandit5/inhere’: Permission denied
find: ‘/home/bandit28-git’: Permission denied
find: ‘/home/leviathan0/.backup’: Permission denied
find: ‘/home/ubuntu’: Permission denied
find: ‘/home/bandit30-git’: Permission denied
find: ‘/boot/efi’: Permission denied
find: ‘/boot/lost+found’: Permission denied
find: ‘/run/pam_pidns’: Permission denied
find: ‘/run/udisks2’: Permission denied
find: ‘/run/chrony’: Permission denied
find: ‘/run/user/13006’: Permission denied
find: ‘/run/user/13005’: Permission denied
find: ‘/run/user/13004’: Permission denied
find: ‘/run/user/13003’: Permission denied
find: ‘/run/user/13002’: Permission denied
find: ‘/run/user/13001’: Permission denied
find: ‘/run/user/13000’: Permission denied
find: ‘/run/user/11021’: Permission denied
find: ‘/run/user/11022’: Permission denied
find: ‘/run/user/11024’: Permission denied
find: ‘/run/user/14001’: Permission denied
find: ‘/run/user/11011’: Permission denied
find: ‘/run/user/11014’: Permission denied
find: ‘/run/user/11009’: Permission denied
find: ‘/run/user/11010’: Permission denied
find: ‘/run/user/12006’: Permission denied
find: ‘/run/user/11003’: Permission denied
find: ‘/run/user/11007’: Permission denied
find: ‘/run/user/11025’: Permission denied
find: ‘/run/user/11002’: Permission denied
find: ‘/run/user/11008’: Permission denied
find: ‘/run/user/11020’: Permission denied
find: ‘/run/user/12002’: Permission denied
find: ‘/run/user/11001’: Permission denied
find: ‘/run/user/11013’: Permission denied
find: ‘/run/user/11006/systemd/inaccessible/dir’: Permission denied
find: ‘/run/user/11005’: Permission denied
find: ‘/run/user/11016’: Permission denied
find: ‘/run/user/11012’: Permission denied
find: ‘/run/user/11000’: Permission denied
find: ‘/run/user/11004’: Permission denied
find: ‘/run/sudo’: Permission denied
find: ‘/run/screen/S-bandit20’: Permission denied
find: ‘/run/multipath’: Permission denied
find: ‘/run/cryptsetup’: Permission denied
find: ‘/run/lvm’: Permission denied
find: ‘/run/systemd/propagate/ModemManager.service’: Permission denied
find: ‘/run/systemd/propagate/polkit.service’: Permission denied
find: ‘/run/systemd/propagate/chrony.service’: Permission denied
find: ‘/run/systemd/propagate/systemd-logind.service’: Permission denied
find: ‘/run/systemd/propagate/irqbalance.service’: Permission denied
find: ‘/run/systemd/propagate/systemd-networkd.service’: Permission denied
find: ‘/run/systemd/propagate/systemd-resolved.service’: Permission denied
find: ‘/run/systemd/propagate/systemd-udevd.service’: Permission denied
find: ‘/run/systemd/inaccessible/dir’: Permission denied
find: ‘/run/lock/lvm’: Permission denied
find: ‘/etc/multipath’: Permission denied
find: ‘/etc/stunnel’: Permission denied
find: ‘/etc/credstore.encrypted’: Permission denied
find: ‘/etc/sudoers.d’: Permission denied
find: ‘/etc/xinetd.d’: Permission denied
find: ‘/etc/polkit-1/rules.d’: Permission denied
find: ‘/etc/credstore’: Permission denied
find: ‘/etc/ssl/private’: Permission denied
find: ‘/root’: Permission denied
find: ‘/manpage/manpage3-pw’: Permission denied
find: ‘/dev/mqueue’: Permission denied
find: ‘/dev/shm’: Permission denied

bandit6@bandit:~$ find/ -user bandit7 -group bandit6 -size 33c
-bash: find/: No such file or directory
bandit6@bandit:~$ find/ -user bandit7 -group bandit6 -size 33c 2>/dev/null
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
(use this code for level 7)

bandit6@bandit:~$ logout

Connection to bandit.labs.overthewire.org closed.
