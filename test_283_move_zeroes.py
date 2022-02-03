import code_283_move_zeroes as c1

def test_base_case():
    s = c1.Solution()
    arr = [0,1,0,3,12]
    s.moveZeroes(arr)
    assert arr == [1,3,12,0,0]