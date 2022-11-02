import random
from calendar import Calendar


class MyLib(object):
    """ generated source for class MyLib """
    r = random.Random()

    def __init__(self):
        """ generated source for method __init__ """
        self.r = random.Random()

    def rand(self, u, v):
        """ generated source for method rand """
        if u > v:
            return (-1)
        x = u + self.r.nextInt(v - u + 1)
        return (x)

    def createArray(self, u, v, n):
        """ generated source for method createArray """
        a = [None] * n
        i = 0
        while i < n:
            i += 1
        return (a)

    def createArrayUnique(self, u, v, n):
        """ generated source for method createArrayUnique """
        h = HashSet()
        i = int()
        k = int()
        while i < n:
            k = self.rand(u, v)
            h.add(k)
            i += 1
        m = len(h)
        a = [None] * m
        g = h.iterator()
        i = 0
        __i_0 = i
        i += 1
        while g.hasNext():
            k = int(g.next())
            a[__i_0] = k
        return (a)

    def display(self, a):
        """ generated source for method display """
        n = int()
        m = int()
        i = int()
        n = a.length
        if n < 50:
            m = n
        else:
            m = 50
            print("\nList of first " + m + " elements of the array are:")
        while i < m:
            i += 1
        print

    def saveFile(self, fname, a):
        """ generated source for method saveFile """
        f = RandomAccessFile()
        try:
            f = RandomAccessFile(fname, "rw")
            while i < a.length:
                i += 1
            f.close()
        except Exception as e:
            pass

    def saveTextFile(self, fname, a):
        """ generated source for method saveTextFile """
        f = RandomAccessFile()
        i = int()
        j = 0
        try:
            f = RandomAccessFile(fname, "rw")
            while i < a.length:
                f.writeBytes(" " + a[i])
                j += 1
                if j % 10 == 0:
                    f.writeBytes("\r\n")
                i += 1
            f.close()
        except Exception as e:
            pass

    def loadFile(self, fname):
        """ generated source for method loadFile """
        f = RandomAccessFile()
        t = ArrayList()
        k = int()
        i = int()
        n = int()
        try:
            f = RandomAccessFile(fname, "r")
            while True:
                k = f.readInt()
                if k == -1:
                    break
                t.add(k)
            f.close()
        except Exception as e:
            pass
        n = len(t)
        a = [None] * n
        while i < n:
            i += 1
        return (a)

    def loadTextFile(self, fname):
        """ generated source for method loadTextFile """
        f = RandomAccessFile()
        t = ArrayList()
        s = str()
        k = int()
        i = int()
        n = int()
        u = []
        x = str()
        try:
            f = RandomAccessFile(fname, "r")
            while True:
                s = f.readLine()
                if s == None:
                    break
                u = s.split("[ ]+")
                while i < u.length:
                    x = u[i].trim()
                    if x == "":
                        continue
                    k = Integer.parseInt(x)
                    t.add(k)
                    i += 1
            f.close()
        except Exception as e:
            pass
        n = len(t)
        a = [None] * n
        while i < n:
            i += 1
        return (a)

    def selectSort(self, a):
        """ generated source for method selectSort """
        i = int()
        j = int()
        k = int()
        x = int()
        n = int()
        n = a.length
        while i < n - 1:
            k = i
            x = a[i]
            while j < n:
                if a[j] < x:
                    x = a[j]
                    k = j
                j += 1
            if i != k:
                x = a[i]
                a[i] = a[k]
                a[k] = x
            i += 1

    def testRunningTime(self):
        """ generated source for method testRunningTime """
        n = int()
        M = int()
        t = Calendar()
        t1 = long()
        t2 = long()
        s = Scanner(System.in_)
        print("Enter the size of the array: ", )
        n = s.nextInt()
        s.nextLine()
        M = 5 * n
        a = self.createArray(0, M, n)
        self.display(a)
        t = Calendar.getInstance()
        t1 = t.getTimeInMillis()
        self.selectSort(a)
        t = Calendar.getInstance()
        t2 = t.getTimeInMillis()
        self.display(a)
        print("Selection sort running time in milli seconds = " + (t2 - t1))
        print()
