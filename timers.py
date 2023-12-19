import machine

class downTimers():
    downCnters = dict() # general purpose timer field, will be counted down til zero
    def __init__(self):
        downTimers.gpt = freeTimer("downTimerField", 10, downTimers.downCnt)
        downTimers.gpt.start()
        
    def downCnt(self):     
        for key, value in downTimers.downCnters.items():
            if downTimers.downCnters[key]:
                downTimers.downCnters[key] -= 1
                
class freeTimer():
    id = 0
    
    def __init__(self, name, period, callback):
        print(f"Timer <{name}> initialized with ID = {self.id} ...")
        self.timer_id = freeTimer.id
        freeTimer.id += 1
        self.timer = machine.Timer(self.timer_id)
        self.period = period
        self.callback = callback
        self.name = name        

    def start(self):
        print(f"starting timer <{self.name}>")
        self.timer.init(period=self.period, mode=machine.Timer.PERIODIC, callback=self.callback)

    def stop(self):
        print(f"stopping timer <{self.name}>")
        self.timer.deinit()
        
