# standard compile options for the c++ executable
FLAGS = -fPIC

# the python interface through swig
PYTHONI = -I/usr/include/python3.6/
PYTHONL = -Xlinker -export-dynamic

# default super-target
all: 
	g++ -fPIC -c GRN.cpp -o GRN.o
	swig -c++ -python -o GRN_wrap.cxx GRN.i 
	g++ $(FLAGS) $(PYTHONI) -c GRN_wrap.cxx -o GRN_wrap.o
	g++ $(PYTHONL) $(LIBFLAGS) -shared GRN.o GRN_wrap.o -o _GRN.so
