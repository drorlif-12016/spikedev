# Run via
#  sudo ampy --port <your-dev-here> run ./demo/tank/advanced-driving-base.py
import hub
import math
from spikedev.motor import MotorSpeedPercent, SpikeLargeMotor, SpikeMediumMotor
from spikedev.sensor import ColorSensor
from spikedev.tank import MoveDifferential
from spikedev.unit import DistanceInches, DistanceStuds
from spikedev.wheel import SpikeLargeWheel

adb = MoveDifferential(
   left_motor_port=hub.port.A,
   right_motor_port=hub.port.E,
   wheel_class=SpikeLargeWheel,
   wheel_distance=DistanceStuds(19),
   motor_class=SpikeLargeMotor
)
adb.rear_motor = SpikeMediumMotor(hub.port.C)
adb.front_motor = SpikeMediumMotor(hub.port.D)
adb.left_color_sensor = ColorSensor(hub.port.B)
adb.right_color_sensor = ColorSensor(hub.port.F)

adb.turn_right(90, MotorSpeedPercent(20))
adb.run_for_distance(DistanceInches(12), MotorSpeedPercent(50))
adb.run_arc_right(DistanceInches(8), DistanceInches(8) * math.pi, MotorSpeedPercent(20))