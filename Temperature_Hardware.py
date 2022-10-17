# FRANCESCO GERRATANA 2022 | Use OpenHardwareMonitorLib  to read Temperature sensors
import clr
import os


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
    handle.HDDEnabled = True
    handle.FanControllerEnabled = True

    handle.Open()

    return handle


def catch_temp_sensor(sensor):
    if sensor.Value is not None:

        if str(sensor.SensorType) == str('Temperature'):
            print(" ", sensor.Hardware.HardwareType, sensor.Hardware.Name, sensor.Index, sensor.Name, sensor.Value,
                  sensor.Identifier)


def scan_hardware(handle):
    print("\n FRANCESCO GERRATANA 2022 | Use OpenHardwareMonitorLib  to read Temperature sensors \n \n Mainboard ",
          handle.Hardware[0].Name, "\n")

    for i in handle.Hardware:
        i.Update()
        #print('Debug', i.HardwareType, i.Name)
        for sensor in i.Sensors:
            catch_temp_sensor(sensor)
            #print('-Debug', sensor.Name, sensor.Value, sensor.Identifier)

    handle.Close()


if __name__ == "__main__":
    scan_hardware(init_openhardwaremonitor())
