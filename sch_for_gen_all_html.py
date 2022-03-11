import os
import time

start_time = time.time()
COLUMN_NAME = 'NUM_TIMES'


def gen_htmls():
    log_files = list()
    root_dir = 'cpu_profile'
    for root, dirs, files in os.walk('cpu_profile'):
        for file in files:
            if root_dir == 'cpu_profile':
                if '2plus1_cores' in os.path.join(root, file):
                    log_files.append(os.path.join(root, file))
            else:
                if '2-' not in file:
                    log_files.append(os.path.join(root, file))

    if COLUMN_NAME != 'NUM_TIMES':
        event_types = ['task_profile_info_ss_rt_task',
                       'task_profile_info_ss_nrt_task',
                       'queue_profile_info_ss_rt_task',
                       'queue_profile_info_ss_nrt_task']
    else:
        event_types = ['task_profile_info_ss_rt_task',
                       'task_profile_info_ss_nrt_task']

    for log_file in log_files:
        for event_type in event_types:
            os.system(f'python main.py --option {event_type} --f {log_file} --column_name {COLUMN_NAME}')


if __name__ == '__main__':
    gen_htmls()
    print((time.time() - start_time))
