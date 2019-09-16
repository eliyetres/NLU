from tdm.lib.device import DddDevice, DeviceWHQuery, DeviceAction


class TimeDevice(DddDevice):
    def __init__(self):
        self.reset()

    def reset(self):
        self._time_hour = 00
        self._time_minute = 00
        self._alarm_hour = 00
        self._alarm_minute = 00
        self._alarm_is_set = False

    class current_time(DeviceWHQuery):
        def perform(self):
            time = '"%02d:%02d"' % (self.device._time_hour, self.device._time_minute)
            return [time]

    class selected_alarm_time(DeviceWHQuery):
        def perform(self):
            options = ["eight", "eight_thirty", "nine"]
            return options

    class current_alarm(DeviceWHQuery):
        def perform(self):
            if self.device._alarm_is_set == False:
                alarm_time = "alarm_off"
                return [alarm_time]
            else:
                alarm_time = "%02d:%02d" % (self.device._alarm_hour, self.device._alarm_minute)
                if alarm_time == str("08:00"):
                    return ["eight"]
                elif alarm_time == "08:30":
                    return ["eight_thirty"]
                elif alarm_time == "09:00":
                    return ["nine"]
                else:
                    return ["alarm_off"]

    class SetTime(DeviceAction):
        def perform(self, hour, minute):
            self.device._time_hour = hour
            self.device._time_minute = minute
            return True

    class SetAlarm(DeviceAction):
        def perform(self, selected_alarm_time):
            if selected_alarm_time == "eight":
                self.device._alarm_hour = 8
                self.device._alarm_minute = 0
            elif selected_alarm_time == "eight_thirty":
                self.device._alarm_hour = 8
                self.device._alarm_minute = 30
            elif selected_alarm_time == "nine":
                self.device._alarm_hour = 9
                self.device._alarm_minute = 0
            self.device._alarm_is_set = True
            return True
