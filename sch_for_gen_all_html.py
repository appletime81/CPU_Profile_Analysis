import os


def gen_htmls():
    log_files = list()
    for root, dirs, files in os.walk('0225'):
        for file in files:
            log_files.append(os.path.join(root, file))

    event_types = ['task_profile_info_ss_rt_task',
                   'task_profile_info_ss_nrt_task',
                   'queue_profile_info_ss_rt_task',
                   'queue_profile_info_ss_nrt_task']

    for log_file in log_files:
        for event_type in event_types:
            os.system(f'python main.py --option {event_type} --f {log_file}')


if __name__ == '__main__':
    gen_htmls()
