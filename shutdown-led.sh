#! /bin/sh

### BEGIN INIT INFO
# Provides:          listen-for-shutdown.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# If you want a command to always run, put it here
# Si quieres que un comando siempre se ejecute, ponlo aqui

# Carry out specific functions when asked to by the system
# Realizar funciones especificas cuando el sistema lo solicite
case "$1" in
  start)
    echo "Arrancando shutdown-led.py"
    /usr/local/bin/shutdown-led.py &
    ;;
  stop)
    echo "Parando shutdown-led.py"
    pkill -f /usr/local/bin/shutdown-led.py
    ;;
  *)
    echo "Usar: /etc/init.d/shutdown-led.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
