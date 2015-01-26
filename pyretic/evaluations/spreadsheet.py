import sys
import os

def create_spreadsheet(fname, outname, limit = None):
    f = open(outname, 'w')
    exp_paths = []
    for exp in os.listdir(fname):
        try:
            exp = "%03d" % int(exp)
        except:
            pass
        exp_paths.append(exp)
    exp_paths.sort()
    '''exp_paths = []
    for i in range(30, 75, 5):
        #exp_paths.append("%d-%d" % (i, i))
        exp_paths.append("%d" % (i))
    '''
    #exp_paths = ["all", "edge_unification", "cache", "partition", "integration", "default_disjoint"]
    for exp in exp_paths:
        try:
            exp = str(int(exp))
            if (limit is not None) and (int(exp) < limit):
                continue
        except:
            pass

        
        exp_path = os.path.join(fname, os.path.join(exp, 'excel_report.txt'))
        if os.path.exists(exp_path):
            g = open(exp_path, 'r')
            f.write(g.readline())
            g.close()
        

    f.close()

if __name__ == "__main__":
    limit = None
    if len(sys.argv) > 3:
        limit = sys.argv[3]
    create_spreadsheet(sys.argv[1], sys.argv[2], int(limit))    
