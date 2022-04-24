# Bluetooth Audio Automation
A simple script designed to fit into an Automator workflow and execute [`BluetoothConnector`](https://github.com/lapfelix/BluetoothConnector) commands based on user input.

Targeting Python 2.7.16 since that's what's available through Automator's Run Shell Script Action.

## Automator Inputs
```AppleScript
{"Connect AudioEngine", "Connect briPhones", "Connect TOZO", "Disconnect AudioEngine", "Disconnect briPhones", "Disconnect TOZO"}
```

