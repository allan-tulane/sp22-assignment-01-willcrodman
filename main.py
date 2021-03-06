"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1:
      return x

    else:
      ra, rb = foo(x-1), foo(x-2)
      return ra, rb

def longest_run(mylist, key):

    count = 0
    max_count = 0

    for i in mylist:
      if i == key:
        count += 1
        if count > max_count: 
          max_count = count
      else:
        count = 0

    return count

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))

def longest_run_recursive(mylist, key):
  def merge(r1, r2):

    if r1.is_entire_range == False and r2.is_entire_range == False:    
      l = r1.left_size
      r = r2.right_size
      if r1.is_entire_range: l += r2.left_size
      if r2.is_entire_range: r += r1.right_size
      return Result(l, r, max((r1.right_size + r2.left_size), r1.longest_size, r2.longest_size), False) 
    else:
      t = r1.longest_size + r1.longest_size
      return Result(t, t, t, True)
      
  if len(mylist) == 1:
      if mylist[0] == key:            
          return Result(1, 1, 1, True)
      else:
          return Result(0, 0, 0, False)

  r1 = longest_run_recursive(mylist[:len(mylist)//2], key)
  r2 = longest_run_recursive(mylist[len(mylist)//2:], key)
  return merge(r1, r2)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12).longest_size == 3
