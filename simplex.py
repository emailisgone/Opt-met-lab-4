from imports import np

class SimplexSolver:
    def __init__(self, c, A, b):
        self.numVars = len(c)
        self.numConstr = len(b)
        self.origC = c.copy()
        self.c = c
        self.A = A
        self.b = b
        self.table = self.createInitTable()
        self.base = list(range(self.numVars, self.numVars + self.numConstr))

    def createInitTable(self):
        numSlack = self.numConstr
        totalVars = self.numVars + numSlack
        
        table = np.zeros((self.numConstr + 1, totalVars + 1))
        
        table[:-1, :self.numVars] = self.A 
        table[:-1, self.numVars:totalVars] = np.eye(numSlack) 
        table[:-1, -1] = self.b 
        
        table[-1, :self.numVars] = self.c
        
        return table

    def solve(self):
        self.solveOptimal()
        return self.getSolv()

    def solveOptimal(self):
        maxIter = 1000
        iter = 0
        
        while iter<maxIter:
            pivotCol = self.getEnterVar()
            if pivotCol is None:
                break
            
            pivotRow = self.getDepartVar(pivotCol)
            if pivotRow is None:
                raise Exception("Pivot row error.")
            
            self.base[pivotRow] = pivotCol
            
            self.pivot(pivotRow, pivotCol)
            iter += 1
        
        if iter == maxIter:
            raise Exception("[DEBUG] Maximum iterations reached.")
        
        return -self.table[-1, -1]

    def getEnterVar(self):              
        objectRow = self.table[-1, :-1]
        minVal = np.min(objectRow)
        
        if minVal>=-1e-6:
            return None
            
        return np.argmin(objectRow)   

    def getDepartVar(self, pivotCol):               
        ratios = []
        rhsCol = self.table[:-1, -1]
        pivotColVal = self.table[:-1, pivotCol]
        
        for i in range(len(rhsCol)):
            if pivotColVal[i]<=1e-6:
                ratios.append(float('inf'))
            else:
                ratio = rhsCol[i]/pivotColVal[i]
                if ratio<0:
                    ratios.append(float('inf'))
                else:
                    ratios.append(ratio)
        
        if min(ratios) == float('inf'):
            return None
            
        return np.argmin(ratios)

    def pivot(self, pivotRow, pivotCol):
        pivot = self.table[pivotRow, pivotCol]
        self.table[pivotRow] = self.table[pivotRow]/pivot
        
        for i in range(len(self.table)):
            if i!=pivotRow:
                factor = self.table[i, pivotCol]
                self.table[i] = self.table[i]-factor*self.table[pivotRow]

    def getSolv(self):
        solution = np.zeros(self.numVars)
        
        for i, var in enumerate(self.base):
            if var<self.numVars:  
                solution[var] = max(0, self.table[i, -1])
        
        objVal = np.dot(self.origC, solution)
        
        return {
            'x': solution,
            'objective': objVal,  
            'table': self.table
        }
