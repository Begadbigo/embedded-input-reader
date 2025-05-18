import machine
import time
from utime import sleep

ButtonCount = 3
LedCount = 9
InputCount = 4

ButtonStartId = 16
Led_GPIO_Start = 7
last_button_time_stamp = 0
KeyPress = []

# Extract the numeric pin id from the passed in Pin instance
def PinId(pin):
    return int(str(pin)[8:11].rstrip(","))

def interrupt_callback(pin):
    global last_button_time_stamp

    cur_button_ts = time.ticks_ms()
    button_press_delta = cur_button_ts - last_button_time_stamp
    if button_press_delta > 200:
        last_button_time_stamp = cur_button_ts
        KeyPress.append(pin)
        # Call the PinId method to get the numeric pin value
        print(f'key press: {PinId(pin) - ButtonStartId}')

def main():
    global KeyPress
    global last_button_time_stamp
    PASSCODE_LENGTH = 0

    s0 = machine.Pin(27, machine.Pin.OUT)
    s1 = machine.Pin(28, machine.Pin.OUT)
    mux_in = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)

    buttons = []
    for btn_idx in range(0, ButtonCount):
        buttons.append(machine.Pin(ButtonStartId + btn_idx, machine.Pin.IN, machine.Pin.PULL_DOWN))
        buttons[-1].irq(trigger=machine.Pin.IRQ_FALLING, handler=interrupt_callback)

    PASS_CODE = [buttons[1], buttons[0], buttons[2]]
    PASSCODE_LENGTH = len(PASS_CODE)

    out_pins = []
    for out_id in range(0, LedCount):
        out_pins.append(machine.Pin(Led_GPIO_Start + out_id, machine.Pin.OUT))

    last_dev = -1
    while True:
        binary_code = 0
        for selector_val in range(InputCount):
            s0.value(selector_val % 2)
            s1.value(selector_val // 2)
            sleep(0.02)
            binary_code += (pow(2, selector_val) * mux_in.value())

        if last_dev != binary_code:
            last_dev = binary_code
            print(f'selected output: {last_dev}')
        sleep(0.2)

        if len(KeyPress) >= PASSCODE_LENGTH:
            if KeyPress[:PASSCODE_LENGTH] == PASS_CODE:
                print('correct passcode')
                if binary_code < LedCount:
                    print(f'toggling: {binary_code}')
                    out_pins[binary_code].toggle()
                else:
                    print(f'invalid output: {binary_code}, ' + \
                    f'valid range: 0-{len(out_pins) - 1}, doing nothing')
            else:
                print('wrong passcode')
            print('')
            KeyPress = KeyPress[PASSCODE_LENGTH:]

if __name__ == "__main__":
    main()
