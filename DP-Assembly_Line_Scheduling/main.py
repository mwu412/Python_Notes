
class AMR_routing:
    def __init__(self, cp, waiting, cross, enter, exit):
        self.num_cp = len(cp[0])
        t0 = [0 for i in range(self.num_cp)]
        t1 = [0 for i in range(self.num_cp)]

        t0[0] = waiting[0][0] * cp[0][0]
        t1[0] = waiting[1][0] * cp[1][0] 

        for i in range(1, self.num_cp):
            t0[i] = min(t0[i-1] + waiting[0][i] * cp[0][i],
                        t1[i-1] + cross[1][i] + waiting[0][i] * cp[0][i])
            t1[i] = min(t1[i-1] + waiting[1][i] * cp[1][i],
                        t0[i-1] + cross[0][i] + waiting[1][i] * cp[1][i])

        
