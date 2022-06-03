import re

import msms_data_process as mdp
import prediction
import retrieve_compund as rc


def read_and_predict(file_name):
    """
    Given a MS/MS data file which contains the first element in the file
    represents the precursor m/z, retention time(in minutes), and ion mode.
    The remaining are m/z and intensity pairs. Outputs the predictions in a
    text file.
    :param file_name: file path for msms data
    :return: None
    """
    with open(file_name) as msms_file:
        msms_data = msms_file.read()

    processed_msms = re.split('#', msms_data)[1:]  # split file by keyword '#'
    title_list = ['#' + i.split('\n')[0] for i in processed_msms]

    for i in processed_msms:
        msms_list = i.split('\n')[1:-1]
        msms_dict = mdp.data_process(msms_list)
        msms_dict_scale = mdp.scaling(msms_dict)
        binned_vec = mdp.binning(msms_dict_scale)
        predicted_fp = prediction.predict_fingerprint(binned_vec)
        compound_dict = rc.retrieve_compound('mass', predicted_fp, '_files/MassDB.csv', 20, msms_dict['precursor'])
        # compound_dict = rc.retrieve_compound('formula', predicted_fp, '_files/MassDB.csv', 20, inchikey='UWPJYQYRSWYIGZ-UHFFFAOYSA-N')

        output_file = file_name.split('.')[0] + '_prediction.txt'
        with open(output_file, 'a') as result:
            result.write(title_list.pop(0) + '\n')
            result.write(rc.visualize_compound_dict(compound_dict) + '\n')
