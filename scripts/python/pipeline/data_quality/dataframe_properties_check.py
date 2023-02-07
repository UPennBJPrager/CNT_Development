# Standard library import
import os
import sys

# Add submodule repository tools to the current opath
testpath = '../../../../unit_tests'
if testpath not in sys.path:
    sys.path.append(testpath)

# User library import
import array_unit_tests as AUT 

def main(DF,N,M=-1,dtype='float64',verbose=True):
    """
    Ensure dataframe properties are correct. Main function runs all checks.

    Parameters
    ----------
    DF : Pandas dataframe
        Dataframe contain ieeg data. SamplesxChannel format.
    N : Integer
        Number of channels expected.
    M : Integer, optional
        Number of expected samples. Set to -1 to skip this check. The default is -1.
    dtype : String, optional
        Expected datatype for the dataframe entries.
    verbose : TYPE, optional
        Print test results to stdout. The default is True.

    Returns
    -------
    Boolean flag.

    """
    
    # Run through all tests
    CLS = AUT.TestArrayProperties(DF,verbose)
    CLS.test_dim(M,N)
    CLS.test_type(dtype)
    CLS.test_inf()
    CLS.test_nan()

if __name__ == '__main__':
    main()