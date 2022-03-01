def gen_chart_title(file_name):
    file_name_list = file_name.split('/')
    file_name = file_name_list[-1]
    cup_core, ue_per_tti, ue_nums = file_name.replace('.txt', '').split('-')[0:3]
    print(cup_core, ue_per_tti, ue_nums)



text = '0225/frank/2-4-32.txt'
gen_chart_title(text)