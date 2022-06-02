import msms_data_process as mdp
import prediction
import retrieve_compund as rc
import pandas as pd
import pubchempy

if __name__ == '__main__':
    # TODO: for lab members (use the database to search)
    msms_dict = mdp.read_data_file('_files/testing_compound.txt')
    msms_dict_scale = mdp.scaling(msms_dict)
    binned_vec = mdp.binning(msms_dict_scale)
    predicted_fp = prediction.predict_fingerprint(binned_vec)
    compound_dict = rc.retrieve_compound('mass', predicted_fp, '_files/MassDB.csv', 20, msms_dict['precursor'])
    # compound_dict = rc.retrieve_compound('formula', predicted_fp, '_files/MassDB.csv', 20, inchikey='UWPJYQYRSWYIGZ-UHFFFAOYSA-N')
    rc.visualize_compound_dict(compound_dict)

    # TODO: for other users
    # msms_dict = mdp.read_data_file('_files/testing_compound.txt')
    # inchikey_dict = mdp.get_binned('_files/inchikey_list.txt')
    # msms_dict_scale = mdp.scaling(msms_dict)
    # binned_vec = mdp.binning(msms_dict_scale)
    # predicted_fp = prediction.predict_fingerprint(binned_vec)
    # inchikey_score = rc.get_inchikey_score(inchikey_dict, predicted_fp)
    # rc.visualize_compound_dict(inchikey_score, False)
