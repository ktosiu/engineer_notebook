Services
========

To setup daemons to run at boot time or be able to easily start/stop
them, we need to the init system. Create a file in ``/etc/init.d`` like
the one below:

::

    # /etc/init.d/netscan
    #

    # Some things that run always
    DAEMON_USER=root
    DIR=/home/pi/github/netscan
    DAEMON_NAME=netscan
    SERVER_NAME=simple_server
    DAEMON=$DIR/$DAEMON_NAME.py
    SERVER=$DIR/$SERVER_NAME.py
    PIDFILE=/var/run/$DAEMON_NAME.pid
    SERVER_PIDFILE=/var/run/$SERVER_NAME.pid

    . /lib/lsb/init-functions

    # Carry out specific functions when asked to by the system
    case "$1" in
      start)
        echo "Starting netscan"
        log_daemon_msg "Starting system $DAEMON_NAME daemon"
        start-stop-daemon --start --background --pidfile $PIDFILE --make-pidfile --u
    ser $DAEMON_USER --chuid $DAEMON_USER --startas $DAEMON
        start-stop-daemon --start --background --pidfile $SERVER_PIDFILE --make-pidf
    ile --user pi --chuid pi --startas $SERVER
        log_end_msg $?
        ;;
      stop)
        log_daemon_msg "Stopping system $DAEMON_NAME daemon"
        start-stop-daemon --stop --pidfile $PIDFILE --retry 10
        start-stop-daemon --stop --pidfile $SERVER_PIDFILE --retry 10
        log_end_msg $?
        ;;
      status)
        status_of_proc $SERVER_NAME $SERVER && status_of_proc $DAEMON_NAME $DAEMON &
    & exit 0 || exit $?
        ;;
      *)
        echo "Usage: /etc/init.d/netscan {start|status|stop}"
        exit 1
        ;;
    esac

    exit 0

Another example:

::

    # /etc/init.d/nodesjs
    #

    # Some things that run always
    DAEMON_USER=root
    DIR=/usr/local/bin
    DAEMON_NAME=http-server
    DAEMON=$DIR/$DAEMON_NAME   
    PIDFILE=/var/run/$DAEMON_NAME.pid
    DAEMON_full="$DAEMON -- /mnt/usbdrive -p 9000 -s"

    . /lib/lsb/init-functions

    # Carry out specific functions when asked to by the system
    case "$1" in
      start)
            echo "Starting Nodejs HTTP Server for movies"
            echo $DAEMON_full
            log_daemon_msg "Starting system $DAEMON_NAME daemon"
            start-stop-daemon --start --background --pidfile $PIDFILE --make-pidfile --user $DAEMON_USER --chuid $DAEMON_USER --startas $DAEMON_full 
            log_end_msg $?
            ;;
      stop)
            log_daemon_msg "Stopping system $DAEMON_NAME daemon"
            start-stop-daemon --stop --pidfile $PIDFILE --retry 10
            log_end_msg $?
            ;;
      status)
            status_of_proc status_of_proc $DAEMON_NAME $DAEMON && exit 0 || exit $?
            ;;
      *)
            echo "Usage: /etc/init.d/nodejs-movies {start|status|stop}"
            exit 1
            ;;
    esac

    exit 0

Change the permissions with:

::

    chmod 755 /etc/init.d/netscan

Add the service to the proper run levels:

::

    update-rc.d netscan defaults

References
----------

-  `thegeekstuff <http://www.thegeekstuff.com/2012/03/lsbinit-script/>`__
-  `debian-administration.org <https://www.debian-administration.org/article/28/Making_scripts_run_at_boot_time_with_Debian>`__
