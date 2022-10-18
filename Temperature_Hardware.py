# FRANCESCO GERRATANA 2022 | Use LibreHardwareMonitorLib to read Temperature sensors
import clr
import os
from tabulate import tabulate


def init_librehardwaremonitor():
    # Without path dll
    # noinspection PyUnresolvedReferences
    # clr.AddReference('LibreHardwareMonitorLib')

    # Use path dll
    cwd = os.getcwd()
    clr.AddReference(cwd + '\\LibreHardwareMonitorLib.dll')
    clr.AddReference(cwd + '\\HidSharp.dll')

    from LibreHardwareMonitor import Hardware

    handle = Hardware.Computer()
    handle.IsCpuEnabled = True
    handle.IsGpuEnabled = True
    handle.IsMemoryEnabled = True
    handle.IsMotherboardEnabled = True
    handle.IsControllerEnabled = True
    handle.IsNetworkEnabled = True
    handle.IsStorageEnabled = True

    handle.Open()

    return handle


def scan_hardware(handle):
    headers = ["Hardware Name","Temperature","Identifier"] 
    hw = [] 
    print("\n FRANCESCO GERRATANA 2022 | Use LibreHardwareMonitorLib  to read Temperature sensors","\n")
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
    scan_hardware(init_librehardwaremonitor())
