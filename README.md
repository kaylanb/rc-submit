# rc-submit
submit a job to a cluster remotely


AWS
-------------

Create account/log-in
EC2



StarCluster
--------------


http://star.mit.edu/cluster/docs/latest/quickstart.html


$ sudo easy_install StarCluster
$ starcluster help
$ pico ~/.starcluster/config

make sure not to have trailing comments in any of the enabled config lines

AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
	NAME > Security Credentials > Access Keys (Ignore IAM warning)

AWS_USER_ID
	NAME > My Account (Account ID)

AWS_REGION_NAME, AWS_REGION_HOST


starcluster createkey mykey -o ~/.ssh/starcluster.rsa

[key mykey]
KEY_LOCATION=~/.ssh/starcluster.rsa


$ starcluster start smallcluster
$ starcluster sshmaster smallcluster
$ starcluster stop smallcluster
$ starcluster terminate smallcluster


TODO
---------------

- how to monitor jobs
- python interface to creating/editing starcluster configurations
- things other than python
