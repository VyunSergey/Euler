from Point2D import Point2D


class LatticePath2D(object):
    def __init__(self, pth):
        self.path = pth

    def __str__(self):
        _str = "{ "
        for _elem in self.path:
            _str += str(_elem) + ", "
        _str = _str[:-2] + " }"
        return _str

    def copy(self):
        return LatticePath2D(self.path.copy())

    def valid(self):
        for index in range(len(self.path)-1):
            if self.path[index].end_point != self.path[index+1].start_point:
                return False
        return True

    def first_element(self):
        return self.path[0]

    def last_element(self):
        return self.path[len(self.path) - 1]

    def add_element_left(self):
        self.path.append(self.last_element().copy().left())
        return self

    def add_element_right(self):
        self.path.append(self.last_element().copy().right())
        return self

    def add_element_up(self):
        self.path.append(self.last_element().copy().up())
        return self

    def add_element_down(self):
        self.path.append(self.last_element().copy().down())
        return self


def make_all_paths(
        srt_pt: Point2D,
        fsh_pt: Point2D,
        lttc_pth: LatticePath2D,
        pths: []):
    if srt_pt == fsh_pt:
        return
    _start_pt = lttc_pth.first_element()
    _finish_pt = lttc_pth.last_element()

    if _start_pt == srt_pt and _finish_pt == fsh_pt:
        pths.append(lttc_pth)
        return
    if _start_pt.slight_lt(srt_pt) or _finish_pt.slight_gt(fsh_pt):
        return
    make_all_paths(srt_pt, fsh_pt, lttc_pth.copy().add_element_right(), pths)
    make_all_paths(srt_pt, fsh_pt, lttc_pth.copy().add_element_up(), pths)
    return


def x_ort_point2d(fst_pt: Point2D, snd_pt: Point2D):
    return fst_pt.x - snd_pt.x


def y_ort_point2d(fst_pt: Point2D, snd_pt: Point2D):
    return fst_pt.y - snd_pt.y


def dist_point2d(fst_pt: Point2D, snd_pt: Point2D):
    return min(abs(x_ort_point2d(fst_pt, snd_pt)), abs(y_ort_point2d(fst_pt, snd_pt)))


def lattice_paths_count(srt_pt: Point2D, fsh_pt: Point2D):
    if dist_point2d(srt_pt, fsh_pt) < 3 \
            or abs(x_ort_point2d(srt_pt, fsh_pt)) < 3 \
            or abs(y_ort_point2d(srt_pt, fsh_pt)) < 3:
        pth = [srt_pt]
        lattice_path = LatticePath2D(pth)
        arr_lattice_paths = []
        make_all_paths(srt_pt, fsh_pt, lattice_path, arr_lattice_paths)
        return len(arr_lattice_paths)
    else:
        left_pt = fsh_pt.copy().left().left()
        middle_pt = fsh_pt.copy().left().down()
        down_pt = fsh_pt.copy().down().down()
        if left_pt.slight_lt(srt_pt) \
                or middle_pt.slight_lt(srt_pt) \
                or down_pt.slight_lt(srt_pt):
            return 0
        res = lattice_paths_count(start_pt, left_pt)
        res += 2 * lattice_paths_count(start_pt, middle_pt)
        res += lattice_paths_count(start_pt, down_pt)
        return res


def f(n, m):
    if n == 0 and m == 0:
        return 0
    if (n == 0 and m > 0) or (m == 0 and n > 0):
        return 1
    if n == 1:
        return m + 1
    if m == 1:
        return n + 1
    if n > m:
        return f(m, n)
    return f(n - 2, m) + 2 * f(n - 1, m - 1) + f(n, m - 2)


if __name__ == '__main__':
    all_lattice_paths = []
    start_pt = Point2D(0, 0)
    finish_pt = Point2D(15, 15)
    ph = [start_pt]
    lt_ph = LatticePath2D(ph)

    # make_all_paths(start_pt, finish_pt, lt_ph, all_lattice_paths)
    # # for elem in all_lattice_paths:
    # #     print('Final path:', elem, sep='\n')
    # print('Printing Final Paths COUNT:', len(all_lattice_paths))
    # print('New Final Paths COUNT:', lattice_paths_count(start_pt, finish_pt))

    for ind in range(26):
        print('f(', ind, ', ', ind, ') =', f(ind, ind))


def test():
    a = [[0, 1,  1,  1,   1,   1,   1],
         [1, 2,  3,  4,   5,   6,   7],
         [1, 3,  6, 10,  15,  21,  28],
         [1, 4, 10, 20,  35,  56,  84],
         [1, 5, 15, 35,  70, 126, 210],
         [1, 6, 21, 56, 126, 252, 462],
         [1, 7, 28, 84, 210, 462, 924]
         ]

    for i in range(7):
        for j in range(7):
            print('Point({}, {}): len ='.format(i, j),
                  lattice_paths_count(Point2D(0, 0), Point2D(i, j)),
                  'Correct len = ', a[i][j])
