#!/usr/bin/python3

from twisted.internet import task, reactor
from SolaxX3RS485 import SolaxX3RS485

def outputActions(vals):
    global outputs
    if outputs is None:
        return

def inputActions(inputs):
    for input in inputs:
        input.fetch(outputActions)


SolaxRS485Meters = []
SolaxRS485Meters.append(SolaxX3RS485("/dev/ttyUSB0", 9600, "N", 1, 1))

looperSolaxRS485 = task.LoopingCall(inputActions, SolaxRS485Meters)
looperSolaxRS485.start(5)

reactor.run()