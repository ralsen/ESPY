import machine

class TI():
    id = 0
    def __init__(self, name, period, callback):
        print(f"Timer {name} initialized with ID = {self.id} ...")
        self.timer_id = TI.id
        TI.id += 1
        self.timer = machine.Timer(self.timer_id)
        self.period = period
        self.callback = callback
        self.name = name        

    def start(self):
        print(f"starting timer {self.name}")
        self.timer.init(period=self.period, mode=machine.Timer.PERIODIC, callback=self.callback)

    def stop(self):
        print(f"stopping timer {self.name}")
        self.timer.deinit()