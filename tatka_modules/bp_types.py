# bp_types.py
# Data types for BackProj

class Trigger():
    def __init__(self,
                 eventid=None,list_picks=None,
                 x=None, y=None, z=None,
                 i=None, j=None, k=None,
                 max_grid=None,
                 beg_win=None, end_win=None,
                 center_win=None):
        self.eventid = None
        self.list_picks = []
        self.x = x
        self.y = y
        self.z = z
        self.i = i
        self.j = j
        self.k = k
        self.max_grid = max_grid
        self.beg_win = beg_win
        self.end_win = end_win
        self.center_win = center_win
        self.lat = None
        self.lon = None
        self.origin_time = None
        

    def __str__(self):
        s = '%s ' % self.eventid
        s += 'X %s ' % self.x
        s += 'Y %s ' % self.y
        s += 'Z %s ' % self.z
        s += 'MaxStack %.3f ' % (self.max_grid)
        s += 'BEG %s ' % self.beg_win
        s += 'END %s ' % self.end_win
        if (self.lat is not None and
            self.lon is not None):
            s += ' LAT %.2f LON %.2f' % (self.lat, self.lon)
        if (self.origin_time is not None):
            s += ' T_ORIG %s' % (self.origin_time)
        return s
    
    def add_picks(self, x):
        self.list_picks.append(x)
    
class Pick():
    def __init__(self,
                 eventid=None,station=None,
                 arrival_type=None):
        
        self.eventid = eventid
        self.station = station
        self.arrival_type = arrival_type
        self.theor_time = []
        self.pick_time = []

    def __str__(self):
        s = ''
        for sta,tt,pt in zip(self.station,self.theor_time,self.pick_time):
            s += ' sta %s ' % sta
            s += ' Ph %s ' % self.arrival_type
            s += ' TT %.2f ' % tt
            s += ' PT %.2f ' % pt
            s += '\n'
        return s
