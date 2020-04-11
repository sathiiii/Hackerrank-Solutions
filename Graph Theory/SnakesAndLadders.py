class Record(object):
    def __init__(self, curr = 0, steps = 0):
        self.curr = curr
        self.steps = steps

def quickestWayUp(jumps):
    visited = [False] * 100
    visited[0] = True
    queue = [Record()]
    rec = Record()
    while queue:
        rec = queue.pop(0)
        u = rec.curr
        if u == 99:
            return rec.steps
        v = u + 1
        while v <= u + 6 and v < 100:
            if not visited[v]:
                visited[v] = True
                a = Record()
                a.steps = rec.steps + 1
                a.curr = v if jumps[v] == -1 else jumps[v]
                queue.append(a)
            v += 1
    return -1
