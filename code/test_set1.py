from nose import with_setup
def setup():
  print 'Setup Set 1'

def test_1():
  print 'Set 1 Test 1'

def test_1point5():
  print 'Set 1 Test 1.5'
  print 10/0
  print 'End of test 1.5'

def forcefail():
  print 'Forcing an error...'
  print 10/0

@with_setup(forcefail)
def test_2():
  print 'Set 1 Test 2'

def teardown():
  print 'Closedown Set 1'
