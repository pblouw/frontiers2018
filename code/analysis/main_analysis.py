import numpy as np

from bootstrap import sample, mean, bootstrapci

# counts for each Likert option from .csv files
con_1 = 263
con_2 = 68
con_3 = 22
con_4 = 19
con_5 = 6

neut_1 = 13
neut_2 = 29
neut_3 = 100
neut_4 = 176
neut_5 = 81

true_1 = 4
true_2 = 15
true_3 = 26
true_4 = 133
true_5 = 224

mod_1 = 50
mod_2 = 41
mod_3 = 46
mod_4 = 124
mod_5 = 121

# create arrays of recorded Likert values from all conditions
con_data = np.concatenate((5 * np.ones(con_5),
                           4 * np.ones(con_4),
                           3 * np.ones(con_3),
                           2 * np.ones(con_2),
                           1 * np.ones(con_1)))

neut_data = np.concatenate((5 * np.ones(neut_5),
                            4 * np.ones(neut_4),
                            3 * np.ones(neut_3),
                            2 * np.ones(neut_2),
                            1 * np.ones(neut_1)))

true_data = np.concatenate((5 * np.ones(true_5),
                            4 * np.ones(true_4),
                            3 * np.ones(true_3),
                            2 * np.ones(true_2),
                            1 * np.ones(true_1)))

mod_data = np.concatenate((5 * np.ones(mod_5),
                           4 * np.ones(mod_4),
                           3 * np.ones(mod_3),
                           2 * np.ones(mod_2),
                           1 * np.ones(mod_1)))

true_mean = mean(true_data)
true_ci = bootstrapci(true_data, mean)
print('')
print('Entailment')
print('Mean Rating: ', true_mean)
print('95% CIs: ', (true_ci[1] - true_ci[0]) / 2)
print(true_ci)

neut_mean = mean(neut_data)
neut_ci = bootstrapci(neut_data, mean)
print('')
print('Neutral')
print('Mean Rating: ', neut_mean)
print('95% CIs: ', (neut_ci[1] - neut_ci[0]) / 2)
print(neut_ci)

con_mean = mean(con_data)
con_ci = bootstrapci(con_data, mean)
print('')
print('Contradiction')
print('Mean Rating: ', con_mean)
print('95% CIs: ', (con_ci[1] - con_ci[0]) / 2)
print(con_ci)

mod_mean = mean(mod_data)
mod_ci = bootstrapci(mod_data, mean)
print('')
print('Model')
print('Mean Rating: ', mod_mean)
print('95% CIs: ', (mod_ci[1] - mod_ci[0]) / 2)
print(mod_ci)

true_std = np.std(true_data)
mod_std = np.std(mod_data)
neut_std = np.std(neut_data)

true_cohens = (mod_mean - true_mean) / np.sqrt((true_std**2 + mod_std**2) / 2)
print('Cohens d - True / Model: ', true_cohens)
print('Effect size: ', true_cohens / np.sqrt(true_cohens**2 + 4))
print('')


neut_cohens = (mod_mean - neut_mean) / np.sqrt((neut_std**2 + mod_std**2) / 2)
print('Cohens d - Neutral / Model: ', neut_cohens)
print('Effect size: ', neut_cohens / np.sqrt(neut_cohens**2 + 4))
print('')
