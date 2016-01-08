from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
f = open('/home/blah_todo/hello_world.out', 'a')
f.write("hello world from process {}".format(rank))
f.close()