import machine

"""class downTimers():
    downCnter = dict() # general purpose timer field, will be counted down til zero
    def __init__(self):
        downTimers.gpt = freeTimer("downTimerField", 10, downTimers.downCnt)
        downTimers.gpt.start()
        
    def downCnt(self):     
        for key, value in downTimers.downCnter.items():
            if downTimers.downCnter[key]:
                downTimers.downCnter[key] -= 1
                
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
        print(f"starting timer <{self.name}> with {self.period}ms")
        self.timer.init(period=self.period, mode=machine.Timer.PERIODIC, callback=self.callback)

    def stop(self):
        print(f"stopping timer <{self.name}>")
        self.timer.deinit()
"""        
__id = 0
class Timers():
    timers = {}
    def __init__(self):
        print(f"Timer class initialized.")
        Timers.timers = {}   
        
    def append(self, name, period, callback):
        global __id
        print(f"Timer <{name}> initialized with ID = {__id} ...")
        Timers.timers[name] = dict()
        Timers.timers[name]['id'] = __id
        Timers.timers[name]['instance'] = machine.Timer(id)
        Timers.timers[name]['name'] = name
        if callback == 'downTimer':
            Timers.timers[name]['callback'] = self.downCnt
            Timers.timers[name]['downCnt'] = period
            period = 10
        else:
            Timers.timers[name]['callback'] = callback
            Timers.timers[name]['period'] = period
            Timers.timers[name]['downCnt'] = -1
        Timers.timers[name]['instance'].init(period=period, mode=machine.Timer.PERIODIC, callback=callback)
        __id += 1
        return Timers.timers[name]
       
    def stop(self, timer):    
        print(f"stopping timer <{timer['name']}>")
        timer['instance'].deinit()

    def start(self,timer):
        print(f"starting timer <{self.name}> with {self.period}ms")
        timer['instance'].init(period=timer['period'], mode=machine.Timer.PERIODIC, callback=timer['callback'])

    def downCnt(self):
        if Timers.timers[self.id]['downCnt']:
           Timers.timers[self.id]['downCnt'] -= 1
        