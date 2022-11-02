from Lib import MyLib


class OrderStatistics(object):
    """ generated source for class OrderStatistics """
    a = []
    t = MyLib()

    def __init__(self):
        """ generated source for method __init__ """
        self.t = MyLib()

    def makeDataUnique(self, u, v, n):
        """ generated source for method makeDataUnique """
        #  create array a with unique elements
        self.a = t.createArrayUnique(u, v, n)

    def heapSort(self):
        """ generated source for method heapSort """
        # Create min HEAP from the array a
        i = 0
        s = int()
        f = int()
        x = int()
        n = int()
        r = int()
        n = a.length
        r = 0
        #  create array a with unique elements
        # Create min HEAP from the array a
        while i < n:
            #  create array a with unique elements
            # Create min HEAP from the array a
            x = a[i]  # Store value a[i] in x
            s = i  # s is the son
            # f=(s-1)/2 is the father
            while s > 0 and x < a[(s - 1) / 2]:
                self.a[s] = a[(s - 1) / 2]  # son = father
                s = (s - 1) / 2
            self.a[s] = x  # s is the new index of x
            i += 1
        # END OF MAKING MIN HEAP

        while i > 0:
            x = a[i], self.a[i] = a[0]
            f = 0
            s = 2 * f + 1
            # s is the left son of f
            if s + 1 < i and self.a[s] > a[s + 1]:
                s = s + 1
            # if there is right son and this less than left son the right son is selected
            while s < i and x > a[s]:
                self.a[f] = a[s]  # replace father with son value
                f = s
                # continue to move to son
                s = 2 * f + 1
                if s + 1 < i and self.a[s] > a[s + 1]:
                    s = s + 1
            self.a[f] = x
            # f is the new place of x = a[i]
            i -= 1
        # s is the left son of f
        # if there is right son and this less than left son the right son is selected
        # replace father with son value
        # continue to move to son
        # f is the new place of x = a[i]

    def swap(self, a, i, k):
        """ generated source for method swap """
        #  Swap element at position i with element at position k
        x = int()
        x = a[i]
        a[i] = a[k]
        a[k] = x

    def partitionRand(self, low, up):
        """ generated source for method partitionRand """
        #  return pivot index
        pivot = int()
        pivotval = int()
        i = int()
        j = int()
        i = t.rand(low, up)
        self.swap(self.a, i, low)
        pivotval = a[low]
        # Select a[low] as pivot value
        i = low
        j = up
        while i < j:
            while self.a[i] <= pivotval and i < up:
                i += 1  # a[i]>pivotval
            while self.a[j] > pivotval:
                j -= 1  # a[j]<=pivotval
            if i < j:
                self.swap(self.a, i, j)
        self.swap(self.a, low, j)
        #  put pivot value to pivot index place
        pivot = j
        return (pivot)

    # @overloaded
    def quickSort(self, low, up):
        """ generated source for method quickSort """
        pivot = int()
        if low >= up:
            return
        pivot = partitionRand(low, up)
        self.quickSort(low, pivot - 1)
        self.quickSort(pivot + 1, up)

    # -----------------------------------------------------
    # @quickSort.register(object)
    def quickSort_0(self):
        """ generated source for method quickSort_0 """
        n = self.a.length
        self.quickSort(0, n - 1)

    # =======================================================================================    
    def orderSta_heap(self, k):
        """ generated source for method orderSta_heap """
        # Create min HEAP from the array a
        i = int()
        s = int()
        f = int()
        j = int()
        x = int()
        n = int()
        r = int()
        n = a.length
        r = 0
        while i < n:
            x = a[i]  # Store value a[i] in x
            s = i  # s is the son
            # f=(s-1)/2 is the father
            while s > 0 and x < a[(s - 1) / 2]:
                self.a[s] = a[(s - 1) / 2]  # son = father
                s = (s - 1) / 2
            self.a[s] = x  # s is the new index of x
            i += 1
        # END OF MAKING MIN HEAP
        j = 0
        while i > 0:
            x = a[i]
            self.a[i] = a[0]
            j += 1
            if j == k:
                return (self.a[i])  # The k-the root removed => this is the k-th order statistics too
            f = 0
            s = 2 * f + 1  # s is the left son of f
            if s + 1 < i and self.a[s] > a[s + 1]:
                s = s + 1  # if there is right son and this less than left son the right son is selected
            while s < i and x > a[s]:
                self.a[f] = a[s]  # replace father with son value
                f = s  # continue to move to son
                s = 2 * f + 1
                if s + 1 < i and self.a[s] > a[s + 1]:
                    s = s + 1
            self.a[f] = x  # f is the new place of x = a[i]
            i -= 1
        return (-1)

    # =======================================================================================    
    def orderSta_quick(self, low, up, k):
        """ generated source for method orderSta_quick """
        pivot = int()
        i = int()
        if low == up:
            return (self.a[low])
        pivot = self.partitionRand(low, up)
        if pivot == k:
            return (self.a[k])
        if k < pivot:
            return (self.orderSta_quick(low, pivot - 1, k))
        else:
            return (self.orderSta_quick(pivot, up, k))

    def test_heapSort(self):
        """ generated source for method test_heapSort """
        self.makeDataUnique(0, 100, 20)
        self.t.display(self.a)
        self.heapSort()
        print("The list after sorting:")
        self.t.display(self.a)

    def test_quickSort(self):
        """ generated source for method test_quickSort """
        self.makeDataUnique(0, 1000, 20)
        self.t.display(self.a)
        self.quickSort()
        print("The list after sorting:")
        self.t.display(self.a)

    def test_OS_heap(self):
        """ generated source for method test_OS_heap """
        self.makeDataUnique(0, 1000, 20)
        k = 5
        self.t.display(self.a)
        q = self.orderSta_heap(k)
        print("The " + k + "th order statistics is " + q)
        self.t.selectSort(self.a)
        self.t.display(self.a)

    def test_OS_quick(self):
        """ generated source for method test_OS_quick """
        self.makeDataUnique(0, 1000, 20)
        k = 5
        self.t.display(self.a)
        n = self.a.length
        q = self.orderSta_quick(0, n - 1, k)
        print("The " + k + "th order statistics is " + q)
        self.t.selectSort(self.a)
        self.t.display(self.a)
