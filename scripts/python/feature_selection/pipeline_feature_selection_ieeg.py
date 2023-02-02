# Add submodule repository tools to the current opath
import sys
sys.path.append('../../../CNT_research_tools/python/tools')

# User requested tools for feature selection
import bandpower as BP
import line_length as LL

def main(ieeg_obj,samp_freq,features=None,channels=None,bp_freq_min=60,bp_freq_max=120):
    """
    Create a dictionary with feature selection for ieeg data. 

    Parameters
    ----------
    iieeg_obj : array or dataframe structure
        Placeholder until example workflow is available.
    features : list, optional
        Feature selection. Currently available:
            LL = Line Length,
            BP = Band Power
        The default is None. If None, all features. Case Sensitive.
    channels : list, optional
        Channels to analyze.
        The default is None. If None, all channels.

    Returns
    -------
    Dictionary with requested features.

    """
    
    # Initialize variables
    feature_dict = {}
    if channels == None:
        channel_list = ieeg_obj.columns
    else:
        channel_list = channels
    if features == None:
        feature_list = ['LL','BP']
    else:
        feature_list = features
    
    # Work through by feature than by channel request
    if 'LL' in feature_list:
        feature_dict['LL'] = {}
        for ichannel in channel_list:
            feature_dict['LL'][ichannel] = LL.line_length(ieeg_obj[ichannel].values)
    if 'BP' in feature_list:
        feature_dict['BP'] = {}
        for ichannel in channel_list:
            feature_dict['BP'][ichannel] = BP.bandpower(ieeg_obj[ichannel].values,samp_freq,[bp_freq_min,bp_freq_max])    
    return feature_dict

if __name__ == '__main__':
    
    main()