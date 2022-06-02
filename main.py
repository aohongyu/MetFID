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

    # TODO: for testing (CASMI mass)
    # num_list = ["{0:03}".format(i) for i in range(1, 209)]
    # for i in num_list:
    #     f = open('casmi_test_mass2d-kat-16/Challenge-' + i + '.txt', 'w')  # change file path here
    #     path = 'casmi_test/Challenge-' + i + '.txt'
    #     msms_dict = mdp.read_data_file(path)
    #     binned_vec = mdp.binning(msms_dict)
    #     predicted_fp = prediction.predict_fingerprint(binned_vec)
    #     compound_dict = rc.retrieve_compound('mass', predicted_fp, '_files/MassDB.csv', 20, msms_dict['precursor'])
    #     f.write(rc.visualize_compound_dict(compound_dict))
    #     f.close()

    # TODO: for testing (CASMI formula)
    # formula_list = []
    # df = pd.read_csv('casmi_test/casmi2016_official_w_formula.csv')
    # for ind in df.index:
    #     formula_list.append(df['Formula'][ind].lstrip().rstrip())
    #
    # num_list = ["{0:03}".format(i) for i in range(1, 209)]
    # # num_list = ["{0:03}".format(i) for i in range(35, 209)]
    # for i in num_list:
    #     f = open('casmi_test_formula-8/Challenge-' + i + '.txt', 'w')  # change file path here
    #     path = 'casmi_test/Challenge-' + i + '.txt'
    #     msms_dict = mdp.read_data_file(path)
    #     binned_vec = mdp.binning(msms_dict)
    #     predicted_fp = prediction.predict_fingerprint(binned_vec)
    #     compound_dict = rc.retrieve_compound('mass', predicted_fp, '_files/MassDB.csv', 20, msms_dict['precursor'])
    #
    #     for name_inchi in list(compound_dict):
    #         try:
    #             # omics_craft database
    #             formula = df.loc[df['Inchikey'] == name_inchi[1]]["Formula"].iloc[0]
    #             # print("get formula from database")
    #         except:
    #             # pubchempy
    #             try:
    #                 formula = pubchempy.get_compounds(identifier=name_inchi[1], namespace="inchikey")[0].molecular_formula
    #             except IndexError:
    #                 print('error No.', i, name_inchi)
    #                 continue
    #
    #         if formula != formula_list[int(i) - 1]:
    #             del compound_dict[name_inchi]
    #
    #     f.write(rc.visualize_compound_dict(compound_dict))
    #     f.close()

    # TODO: for other users
    # msms_dict = mdp.read_data_file('_files/testing_compound.txt')
    # inchikey_dict = mdp.get_binned('_files/inchikey_list.txt')
    # msms_dict_scale = mdp.scaling(msms_dict)
    # binned_vec = mdp.binning(msms_dict_scale)
    # predicted_fp = prediction.predict_fingerprint(binned_vec)
    # inchikey_score = rc.get_inchikey_score(inchikey_dict, predicted_fp)
    # rc.visualize_compound_dict(inchikey_score, False)
