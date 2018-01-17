import numpy as np

from bootstrap import mean, bootstrapci

# counts for each Likert option from .csv files
con_1 = 55
con_2 = 20
con_3 = 8
con_4 = 1
con_5 = 0

true_1 = 0
true_2 = 3
true_3 = 8
true_4 = 29
true_5 = 46

mod_1 = 70
mod_2 = 56
mod_3 = 39
mod_4 = 117
mod_5 = 88

# create arrays of recorded Likert values from all conditions
con_data = np.concatenate((5 * np.ones(con_5),
                           4 * np.ones(con_4),
                           3 * np.ones(con_3),
                           2 * np.ones(con_2),
                           1 * np.ones(con_1)))

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
print('')
print('True STD: ', true_std)
print('Model STD: ', mod_std)

true_cohens = (mod_mean - true_mean) / np.sqrt((true_std**2 + mod_std**2) / 2)
print('Cohens d - True / Model: ', true_cohens)
print('Effect size: ', true_cohens / np.sqrt(true_cohens**2 + 4))
print('')
