import re

import msms_data_process as mdp
import prediction
import retrieve_compund as rc


def read_and_predict(file_name):
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
        compound_dict = rc.retrieve_compound('mass', predicted_fp, '_files/MassDB.csv', msms_dict['rt'], 20, msms_dict['precursor'])
        # compound_dict = rc.retrieve_compound('formula', predicted_fp, '_files/MassDB.csv', 20, inchikey='UWPJYQYRSWYIGZ-UHFFFAOYSA-N')

        if msms_dict['mode'] == 'positive':  # restore to original mass
            real_mass = msms_dict['precursor'] + 1.007276
        else:
            real_mass = msms_dict['precursor'] - 1.007276

        with open('_files/prediction_output.txt', 'a') as result:
            result.write(title_list.pop(0) + '\n')
            result.write(rc.visualize_compound_dict(compound_dict, real_mass) + '\n')


if __name__ == '__main__':
    read_and_predict('_files/testing_compound.txt')
