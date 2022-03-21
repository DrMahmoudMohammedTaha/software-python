import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print("Doing stuff...")

    s.enter(5, 1, do_something, (sc,))

s.enter(5, 1, do_something, (s,))
s.run()