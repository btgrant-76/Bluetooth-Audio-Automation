import sys
import os

# Input constants
DISCONNECT = "Disconnect"
CONNECT = "Connect"
BOSE = "briPhones"
AUDIO_ENGINE = "AudioEngine"
TOZO = "TOZO"

AUDIO_DEVICES = {
    TOZO: "15-16-02-13-52-4f",
    AUDIO_ENGINE: "01-29-b5-22-3c-c9",
    BOSE: "28-11-a5-44-62-88",
    # "TOZO-T12 blue": "47-05-02-14-38-4b",  these really don't get used with the laptop
}

# TOZO can connect while briPhones are connected & while AudioEngine are connected
# AudioEngine don't seem to have any trouble connecting when any others are connected
INPUTS = {
    CONNECT + " " + BOSE: [DISCONNECT + " " + AUDIO_ENGINE],  # AudioEngine needs to be fdisconnected for briPhones to connect
    CONNECT + " " + AUDIO_ENGINE: [],
    CONNECT + " " + TOZO: [],
    DISCONNECT + " " + BOSE: [],
    DISCONNECT + " " + AUDIO_ENGINE: [],
    DISCONNECT + " " + TOZO: [],
}


def main(command):
    commands = INPUTS[command]
    commands.append(command)

    for cmd in commands:
        splits = cmd.split()
        option = "--" + splits[0].lower()
        device_address = AUDIO_DEVICES[splits[1]]

        sys_cmd = "/usr/local/bin/BluetoothConnector " + option + " " + device_address

        res = os.system(sys_cmd)
        print("command '" + sys_cmd + "' finished with code " + str(res))


if __name__ == '__main__':
    arg = sys.argv[1]
    print("input: " + arg)

    if arg not in INPUTS.keys():
        print("Invalid input '" + arg + "'")
        input_delimiter = "\n\t- "
        print("Valid input options:  " + input_delimiter + input_delimiter.join(INPUTS.keys()))
        sys.exit(-1)
    else:
        main(arg)
        # connect_cmd = "/usr/local/bin/BluetoothConnector --connect 28-11-a5-44-62-88"
        # disconnect_cmd = "/usr/local/bin/BluetoothConnector --disconnect 28-11-a5-44-62-88"
        # res = os.system(disconnect_cmd)
        # res = os.system(connect_cmd)
        # print(res)
