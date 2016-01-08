
import rcsubmit

sc = rcsubmit.StarCluster("smallcluster")

# Simple ssh command example
#sc.ssh('echo "hello world" > test')

# Copying files and running remote script
sc.push_files(['./test.sh'])
sc.ssh('cd {} && sh test.sh'.format(sc.remote_dir))
sc.pull_files(['hello_world.out'])

# Using scheduler
# submission = rcsubmit.Submission(sc, 'qsub', 'job.pbs', 'script.py', 'test.dat', 'test1.dat')

