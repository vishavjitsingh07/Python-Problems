import numpy as np
class Solution():
    def minCost(self, colors, N):
        colors = np.array(colors).T
        r, g, b = colors[0], colors[1], colors[2]
        cr, cg, cb = r[0], g[0], b[0]
        for i in range(1, N):
            cr, cg, cb = r[i] + min(cb, cg), g[i] + min(cr, cb), b[i] + min(cr, cg)
        return min(cr, cg, cb)
