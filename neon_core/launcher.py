from mycroft.messagebus.load_config import load_message_bus_config
from mycroft.util import wait_for_exit_signal, reset_sigint_handler
from neon_core.messagebus.service import create_websocket_app
from neon_core.skills.service import NeonSkillService
from neon_core.messagebus.service import NeonBusService

reset_sigint_handler()
# Create PID file, prevent multiple instances of this service
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