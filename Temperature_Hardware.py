# FRANCESCO GERRATANA 2022 | Use OpenHardwareMonitorLib to read Temperature sensors
import clr
import os
from tabulate import tabulate


def init_openhardwaremonitor():
    # Without path dll
    # noinspection PyUnresolvedReferences
    # clr.AddReference('OpenHardwareMonitorLib')

    # Use path dll
    cwd = os.getcwd()
    clr.AddReference(cwd + '\\OpenHardwareMonitorLib.dll')

    from OpenHardwareMonitor import Hardware

    handle = Hardware.Computer()
    handle.MainboardEnabled = True
    handle.CPUEnabled = True
    handle.RAMEnabled = True
    handle.GPUEnabled = True
    handle.HDDEnabled = True #<--- if enabled GPU Temp Lost

    handle.Open()

    return handle


def scan_hardware(handle):
    headers = ["Hardware Name","Temperature","Identifier"] 
    hw = [] 
    print("\n FRANCESCO GERRATANA 2022 | Use OpenHardwareMonitorLib  to read Temperature sensors","\n")
    hw.append([str(handle.Hardware[0].Name),"",""]) 
    for i in handle.Hardware:
        i.Update()
        for sensor in i.Sensors: 
            if str(sensor.SensorType) == str('Temperature'):
                hw.append([str(sensor.Hardware.Name +' '+ sensor.Name),str(sensor.Value),str(sensor.Identifier)]) 
    handle.Close()
    table = tabulate(hw, headers, tablefmt="fancy_grid")

    print(table)


if __name__ == "__main__":
    scan_hardware(init_openhardwaremonitor())
