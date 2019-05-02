import sys
import re
from tkinter import *
from bisect import bisect_left


class MyApplication:

    def __init__(self, master):
        master.title("Welcome to LikeGeeks app")
        master.minsize(600, 300)

        self.tc_frame = LabelFrame(root, text='From TeamCity')
        self.tc_frame.pack(ipadx=10, ipady=10, padx=10, pady=10, fill=X)

        self.inner_tc_frame_1 = Frame(self.tc_frame)
        self.inner_tc_frame_1.pack(side=TOP)

        Label(self.inner_tc_frame_1, text='TestRail Ids').pack()
        self.text_ids = Text(self.inner_tc_frame_1, width=60, height=4, wrap=WORD)
        self.text_ids.pack()

        Label(self.inner_tc_frame_1, text='TestRail Parameters').pack()
        self.text_params = Text(self.inner_tc_frame_1, width=60, height=4, wrap=WORD)
        self.text_params.pack()

        self.inner_tc_frame_2 = Frame(self.tc_frame)
        self.inner_tc_frame_2.pack(side=RIGHT)

        self.new_frame = LabelFrame(root, text='New Parameters')
        self.new_frame.pack(ipadx=10, ipady=10, padx=10, pady=10, fill=X)

        Label(self.new_frame, text='New values').pack()
        self.text_new = Text(self.new_frame, width=60, height=5, wrap=WORD)
        self.text_new.pack()

        self.button_generate = Button(master, text='Generate params', command=self.generate_params)
        self.button_generate.pack()
        self.button_clear = Button(master, text='Clear all', command=self.clear_all_fields)
        self.button_clear.pack()

    def clear_all_fields(self):
        self.text_ids.delete('1.0', END)
        self.text_params.delete('1.0', END)
        self.text_new.delete('1.0', END)

    def find_missing(self, int_array, min_val=False, max_val=False):
        if len(int_array) == 0:
            return list(range(min_val, max_val + 1))

        int_array = sorted(int_array)
        first_in_int_array = int_array[0]
        last_in_int_array = int_array[len(int_array) - 1]

        if not min_val:
            min_val = first_in_int_array

        if not max_val:
            max_val = last_in_int_array
        result = []

        if min_val < first_in_int_array:
            int_array.insert(0, min_val)
            result.append(min_val)

        if max_val > last_in_int_array:
            int_array.insert(len(int_array), max_val)
            result.append(max_val)

        try:
            min_pos = int_array.index(min_val)

        except Exception as e:
            result.append(min_val)
            min_pos = bisect_left(int_array, min_val)
            int_array.insert(min_pos, min_val)

        try:
            max_pos = int_array.index(max_val)
        except Exception as e:
            result.append(max_val)
            max_pos = bisect_left(int_array, max_val)
            int_array.insert(max_pos, max_val)

        for i in range(min_pos, max_pos):
            difference = int_array[i + 1] - int_array[i]
            if difference != 1 and difference != 0:
                result += range(int_array[i] + 1, int_array[i + 1])

        result.sort()
        return result

    def generate_params(self):
        all_ids = re.findall(r'\d+', self.text_ids.get(index1=1))
        all_labels = re.findall(r'label\_\d+', self.text_params.get(index1=0, index2=END))
        all_datas = re.findall(r'data\_\d+', self.text_params.get(index1=0, index2=END))
        all_data_ids = re.findall(r'[\'|\"](\d+)[\'|\"]', self.text_params.get(index1=0, index2=END))

        if len(all_labels) != len(all_datas):
            raise Exception(
                'Len of two lists is different: all_labels=%d, all_datas=%d'.format(len(all_labels), len(all_datas)))

        numbers = [int(label.split('_')[1]) for label in all_labels]
        missed_numbers = self.find_missing(numbers, min_val=1, max_val=max(numbers))

        new_settings = []
        new_ids = []
        for test_name, test_id in tuple(self.text_new.get(index1=0, index2=END)):
            try:
                free_number = missed_numbers.pop(0)
            except IndexError:
                free_number = max(numbers) + 1
                numbers.append(free_number)

            if test_id not in all_data_ids:
                new_settings.append("label_%d='%s' data_%d='%s'" % (free_number, test_name, free_number, test_id))
            else:
                print('-------------- ' + test_id + ' - ' + test_name + ' -------------')

            if test_id not in all_ids:
                new_ids.append(test_id)

        new_ids_str = ' '.join(new_ids)
        print('-------------- GOT = ' + str(len(new_values)) + '; EDDED = ' + str(len(new_ids)) + ' --------------')
        print(selected_ids + ' ' + new_ids_str)

        new_settings_str = ' '.join(new_settings)
        print(
            '-------------- GOT = ' + str(len(new_values)) + '; EDDED = ' + str(len(new_settings)) + ' --------------')
        print(settings + ' ' + new_settings_str)

        print('--------------------------------------------------------------------------------------------------')


if __name__ == '__main__':
    root = Tk()

    window = MyApplication(root)

    root.mainloop()
