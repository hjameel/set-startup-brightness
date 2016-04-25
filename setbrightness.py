#!/usr/bin/env python3

import dbus

BRIGHTNESS = 60

def set_brightness(brightness):
    session_bus = dbus.SessionBus()
    proxy = session_bus.get_object(
            "org.gnome.SettingsDaemon", "/org/gnome/SettingsDaemon/Power")
    power_setting_interface = dbus.Interface(
            proxy, dbus_interface='org.gnome.SettingsDaemon.Power.Screen')

    power_setting_interface.SetPercentage(brightness)

if __name__ == "__main__":
    set_brightness(BRIGHTNESS)
