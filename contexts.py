import pickle
cache = {}
def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        pickled = pickle.dumps([m, [0], [c]])
        cached = cache.get(pickled)
        if cached:
            determinant += cached
        else:
            det = ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
            determinant += det
            cache[pickled] = det
        # print(f'{c} of {len(m)}: determined.')
    return determinant

def getMatrixInverse(m):
    print(m, type(m), 'inverse', len(m))
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        print(f'{r} of {len(m)}')
        cofactorRow = []
        for c in range(len(m)):
            pickled = pickle.dumps([m, [r], [c]])
            cached = cache.get(pickled)
            if cached:
                print('Cached Here too')
                cofactorRow.append(cached)
            else:
                minor = getMatrixMinor(m,r,c)
                det = ((-1)**(r+c)) * getMatrixDeternminant(minor)
                cofactorRow.append(det)
                cache[pickled] = det
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    print(type(cofactors))
    cofactors = list(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors