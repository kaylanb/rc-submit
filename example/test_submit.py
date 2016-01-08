import rcsubmit
import time

sc = rcsubmit.StarCluster("smallcluster")
submission = rcsubmit.Submission(sc, 'qsub', 'test_mpi.pbs', 'test_mpi.py')
submission.run()
time.sleep(5)

sc.pull_files(['hello_world.out'])
