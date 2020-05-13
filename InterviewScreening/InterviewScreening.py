

applicant_dict ={'Anna ': {'experience': 2, 'languages': ['Python', 'Java', 'Ruby', 'C++'],
                          'project_supervision': False},
                 'Ben ': {'experience': 5, 'languages': ['Python', 'Java', 'Perl', 'Kotlin'],
                          'project_supervision': False},
                 'Calvin ': {'experience': 3, 'languages': ['C', 'Python', 'Scala', 'C++'],
                            'project_supervision': True},
                 'Andrew ': {'experience': 4, 'languages': ['C#', 'Java', 'C', 'Scala'] ,
                          'project_supervision': False},
                 'Bella ' : {'experience': 6, 'languages': ['PHP', 'JavaScript', 'Java', 'C++'] ,
                          'project_supervision': True},

                 }

min_experience = 4
required_languages = ['Python', 'Java']
for name, cv_dict in applicant_dict.items():
    if(cv_dict['experience'] >= min_experience) and \
    (set(required_languages).issubset(set(cv_dict['languages'])) or \
            cv_dict['project_supervision']):
        print(name + 'passes the screening. Congratulations !!!!')
