
import rcsubmit

sc = rcsubmit.StarCluster("smallcluster")
sc.ssh('echo "hello world" > test')
