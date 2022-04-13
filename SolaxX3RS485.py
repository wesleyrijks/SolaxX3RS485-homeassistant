from pymodbus.client.sync import ModbusSerialClient
from pymodbus.constants import Defaults
import json

Defaults.UnitId = 1

def join_msb_lsb(msb, lsb):
    return (msb << 16) | lsb

class SolaxX3RS485(object):

    ##
    # Create a new class to fetch data from the Modbus interface of Solax inverters
    def __init__(self, port, baudrate, parity, stopbits, timeout):
        self.port = port
        self.client = ModbusSerialClient(method="rtu", port=self.port, baudrate=baudrate, parity=parity,
                                         stopbits=stopbits, timeout=timeout)

    def fetch(self, completionCallback):
        result = self.client.read_input_registers(0X400, 53)
        
        self.vals = {}
        self.vals['Pv1 input voltage'] = result.getRegister(0) / 10
        self.vals['Pv2 input voltage'] = result.getRegister(1) / 10
        self.vals['Pv1 input current'] = result.getRegister(2) / 10
        self.vals['Pv2 input current'] = result.getRegister(3) / 10
        self.vals['Grid Voltage Phase 1'] = result.getRegister(4) / 10
        self.vals['Grid Voltage Phase 2'] = result.getRegister(5) / 10
        self.vals['Grid Voltage Phase 3'] = result.getRegister(6) / 10
        self.vals['Grid Frequency Phase 1'] = result.getRegister(7) / 100
        self.vals['Grid Frequency Phase 2'] = result.getRegister(8) / 100
        self.vals['Grid Frequency Phase 3'] = result.getRegister(9) / 100
        self.vals['Output Current Phase 1'] = result.getRegister(10) / 10
        self.vals['Output Current Phase 2'] = result.getRegister(11) / 10
        self.vals['Output Current Phase 3'] = result.getRegister(12) / 10
        self.vals['Temperature'] = result.getRegister(13)
        self.vals['Inverter Power'] = result.getRegister(14)
        self.vals['RunMode'] = result.getRegister(15)
        self.vals['Output Power Phase 1'] = result.getRegister(16)
        self.vals['Output Power Phase 2'] = result.getRegister(17)
        self.vals['Output Power Phase 3'] = result.getRegister(18)
        self.vals['Total DC Power'] = result.getRegister(19)
        self.vals['PV1 DC Power'] = result.getRegister(20)
        self.vals['PV2 DC Power'] = result.getRegister(21)
        self.vals['Fault value of Phase 1 Voltage'] = result.getRegister(22) / 10
        self.vals['Fault value of Phase 2 Voltage'] = result.getRegister(23) / 10
        self.vals['Fault value of Phase 3 Voltage'] = result.getRegister(24) / 10
        self.vals['Fault value of Phase 1 Frequency'] = result.getRegister(25) / 100
        self.vals['Fault value of Phase 2 Frequency'] = result.getRegister(26) / 100
        self.vals['Fault value of Phase 3 Frequency'] = result.getRegister(27) / 100
        self.vals['Fault value of Phase 1 DCI'] = result.getRegister(28) / 1000
        self.vals['Fault value of Phase 2 DCI'] = result.getRegister(29) / 1000
        self.vals['Fault value of Phase 3 DCI'] = result.getRegister(30) / 1000
        self.vals['Fault value of PV1 Voltage'] = result.getRegister(31) / 10
        self.vals['Fault value of PV2 Voltage'] = result.getRegister(32) / 10
        self.vals['Fault value of Temperature'] = result.getRegister(33)
        self.vals['Fault value of GFCI'] = result.getRegister(34) / 1000
        self.vals['Total Yield'] = join_msb_lsb(result.getRegister(36), result.getRegister(35)) / 1000
        self.vals['Yield Today'] = join_msb_lsb(result.getRegister(38), result.getRegister(37)) / 1000
        
        print(json.dumps(self.vals))
        
        
        
