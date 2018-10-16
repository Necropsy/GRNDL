%module GRN
%{
  #include "GRN.hpp"
  #include <iostream>
  #include <math.h>
  #include <omp.h>
  #include <set>
  #include <string>
%}
%include std_string.i
%include "std_set.i"
namespace std {
   %template(StringSet) set<string>;
}
%include "GRN.hpp"
