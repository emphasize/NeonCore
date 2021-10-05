from mycroft.lock import Lock
from mycroft.util import wait_for_exit_signal, reset_sigint_handler
from neon_core.messagebus.service import NeonBusService
from neon_core.skills.service import NeonSkillService
from time import sleep

reset_sigint_handler()
# Create PID file, prevent multiple instances of this service
# TODO should also detect old services Locks
lock = Lock("NeonCore")

# launch websocket listener
bus = NeonBusService(daemonic=True)
bus.start()

# launch skills service
skills = NeonSkillService()
skills.start()

wait_for_exit_signal()

skills.shutdown()
bus.shutdown()
