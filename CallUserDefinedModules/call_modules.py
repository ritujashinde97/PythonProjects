import operate_list as ol
import handle_numbers as hn

my_number_list = [2,3,4,5,2,9,4,8]
my_name_list = ['Rituja','Ashutosh','Chaitali', 'Sonali','Austin', 'Reshma', 'Ishwari','Dakshata']

ol.delete_name(my_name_list,'Dakshata')
print(my_name_list)

ol.add_names(my_name_list,'Isha',2)
print(my_name_list)

my_sum = hn.add_number(my_number_list,1,5)
print(my_sum)

my_average = hn.get_mean(my_number_list,1,5)
print(my_average)