import subprocess
print("If you just got this device and didn't reboot it, you should reboot it now, some bypasses can hide themselves before you reboot.")
input("Press enter to continue ")
p1 = subprocess.Popen(["cmd", "/C", "lib\ideviceactivation.exe state"], stdout = subprocess.PIPE)
statusphone = p1.communicate()[0]
if statusphone == b'ActivationState: Activated\r\n':
    print("Device doesn't seem bypassed")
elif statusphone == b'ActivationState: Unactivated\r\n':
    print("Device seems bypassed (or is on the setup screen?)")
elif statusphone == b'ActivationState: FactoryActivation\r\n':
    print("Device seems bypassed")
elif statusphone == b'No device found, is it plugged in?\r\n':
    print("Device doesn't seem to be connected")
else:
    print("Error occured, please report this to the developer")
input("Press enter to exit")
