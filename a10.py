#H3: Non-whites are paid less (i.e, race bias).

white_salaries    = cleaned_salaries[cleaned_salaries['race'] == 'white']
black_salaries    = cleaned_salaries[cleaned_salaries['race'] == 'black']
hispanic_salaries = cleaned_salaries[cleaned_salaries['race'] == 'hispanic']
other_salaries    = cleaned_salaries[cleaned_salaries['race'] == 'other']

white_salary_stats_dict =    {'median':  np.median(white_salaries['earn']), \
                              'average': np.average(white_salaries['earn'])}
black_salary_stats_dict =    {'median':  np.median(black_salaries['earn']), \
                              'average': np.average(black_salaries['earn'])}
hispanic_salary_stats_dict = {'median':  np.median(hispanic_salaries['earn']), \
                              'average': np.average(hispanic_salaries['earn'])}
other_salary_stats_dict =    {'median':  np.median(other_salaries['earn']), \
                              'average': np.average(other_salaries['earn'])}
salary_stats_dict =          {'white':    white_salary_stats_dict, \
                              'black':    black_salary_stats_dict, \
                              'hispanic': hispanic_salary_stats_dict, \
                              'other':    other_salary_stats_dict}
white_ed_stats_dict =    {'median':   np.median(white_salaries['ed']), \
                          'average':  np.average(white_salaries['ed'])}
black_ed_stats_dict =    {'median':   np.median(black_salaries['ed']), \
                          'average':  np.average(black_salaries['ed'])}
hispanic_ed_stats_dict = {'median':   np.median(hispanic_salaries['ed']), \
                          'average':  np.average(hispanic_salaries['ed'])}
other_ed_stats_dict =    {'median':   np.median(other_salaries['ed']), \
                          'average':  np.average(other_salaries['ed'])}
salary_ed_dict =         {'white':    white_ed_stats_dict, \
                          'black':    black_ed_stats_dict, \
                          'hispanic': hispanic_ed_stats_dict, \
                          'other':    other_ed_stats_dict}


print("           Median Salary   Median Years of Education")
print("White      ${:.0f}          {:.0f}".format(salary_stats_dict['white']['median'], \
                                                  salary_ed_dict['white']['median']))
print("Black      ${:.0f}          {:.0f}".format(salary_stats_dict['black']['median'], \
                                                  salary_ed_dict['black']['median']))
print("Hispanic   ${:.0f}          {:.0f}".format(salary_stats_dict['hispanic']['median'], \
                                                  salary_ed_dict['hispanic']['median']))
print("Other      ${:.0f}          {:.0f}".format(salary_stats_dict['other']['median'], \
                                                  salary_ed_dict['other']['median']))

print("-"*50)
print("           Average salary  Average education")
print("White      ${:.0f}          {:.0f}".format(salary_stats_dict['white']['average'], \
                                                 salary_ed_dict['white']['average']))
print("Black      ${:.0f}          {:.0f}".format(salary_stats_dict['black']['average'], \
                                                 salary_ed_dict['black']['average']))
print("Hispanic   ${:.0f}          {:.0f}".format(salary_stats_dict['hispanic']['average'], \
                                                 salary_ed_dict['hispanic']['average']))
print("Other      ${:.0f}          {:.0f}".format(salary_stats_dict['other']['average'], \
                                                 salary_ed_dict['other']['average']))

#now check by years of education
white_salary_stats_by_years_dict =     {'12': np.median(white_salaries[white_salaries['ed'] == 12]['earn']), \
                                        '13': np.median(white_salaries[white_salaries['ed'] == 13]['earn']), \
                                        '14': np.median(white_salaries[white_salaries['ed'] == 14]['earn']), \
                                        '15': np.median(white_salaries[white_salaries['ed'] == 15]['earn']), \
                                        '16': np.median(white_salaries[white_salaries['ed'] == 16]['earn']), \
                                        '17': np.median(white_salaries[white_salaries['ed'] == 17]['earn']), \
                                        '18': np.median(white_salaries[white_salaries['ed'] == 18]['earn'])}
non_white_salary_stats_by_years_dict = {'12': np.median(non_white_salaries[non_white_salaries['ed'] == 12]['earn']), \
                                        '13': np.median(non_white_salaries[non_white_salaries['ed'] == 13]['earn']), \
                                        '14': np.median(non_white_salaries[non_white_salaries['ed'] == 14]['earn']), \
                                        '15': np.median(non_white_salaries[non_white_salaries['ed'] == 15]['earn']), \
                                        '16': np.median(non_white_salaries[non_white_salaries['ed'] == 16]['earn']), \
                                        '17': np.median(non_white_salaries[non_white_salaries['ed'] == 17]['earn']), \
                                        '18': np.median(non_white_salaries[non_white_salaries['ed'] == 18]['earn'])}

#combine dictionaries
salary_stats_by_years_dict = {'white':     white_salary_stats_by_years_dict, \
                              'non_white': non_white_salary_stats_by_years_dict}

print('-'*50)
print('Years of ed.    12     13     14     15     16     17     18')
print('White           ', end='')
for key in salary_stats_by_years_dict['white']:
    print('{:.0f}  '.format(salary_stats_by_years_dict['white'][key]), end='')
print('\n', end='')
print('Non-white       ', end='')
for key in salary_stats_by_years_dict['non_white']:
    print('{:.0f}  '.format(salary_stats_by_years_dict['non_white'][key]), end='')