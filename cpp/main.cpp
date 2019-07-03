#include <stdint.h>
#include <string>
#include <memory>                       // for shared_ptr<>
#include <iostream>
#include <deque>
#include <map>
#include <algorithm>                    // for lower_bound()
#include <iterator>                     // for next() and prev()
#include <fstream>
using namespace std;
 
#include "Sequence.hh"
#include "LCS.h"

// Check program parameters and print usage
void check_n_print_usage(string exe, int argc) {
  exe = exe.substr(exe.rfind('/') + 1);
  string usage = "Usage:\n\t";
  usage += exe; usage += "\n";
  usage += "\t\t file1.fa file2.fa";

  // get length of file
  cin.seekg(0,ios::end);
  int cin_length = cin.tellg();
  cin.seekg(0,ios::beg);

  if (argc < 3 && cin_length <= 0) {
    cerr<<usage<<endl;
    exit(1);
  }
};

int main(int argc,char *argv[])
{
    // input
    check_n_print_usage(argv[0], argc);

    // two input files
    string fn1 = argv[1];
    string fn2 = argv[2];
    // cout << "fn1 = " << fn1 << " , fn2 = " << fn2 << endl;
    //
    Sequence *seq1 = NULL, *seq2 = NULL;
    seq1  = Sequence::parseSequences(fn1);
    seq2  = Sequence::parseSequences(fn2);
    cout << "seq1 = " << seq1->sequence() << endl;
    cout << "seq2 = " << seq2->sequence() << endl;
    // LCS
    LCS lcs;
    auto s = lcs.Correspondence(seq1->sequence(), seq2->sequence());
    cout << "LCS = " << s << endl;
}