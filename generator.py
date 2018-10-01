import os, sys
import random
class Generate(object):
    def __init__(self):
        self.column_list = []
        self.type_list = []
        self.value_list = {}
        self.delimeter = ','
        pass
    def load_preset(self, path='./columns'):
        for root, dir, files in os.walk(path):
            for file in files:
                path_file = path+'/'+file
                self.column_list.append(path_file)
                self.value_list[path_file] = list()
                f = open(path_file, 'r')
                f_ = f.read()
                self.type_list.append(f_.split('\n')[0])
                for value in f_.split("\n")[1:]:
                    if value != "":
                        self.value_list[path_file].append(value)
                f.close()
    def gen_record(self):
        record = ""
        try:
            for col in self.column_list:
                record += self.value_list[col][random.randint(0,len(self.value_list[col]) - 1)]
                record += self.delimeter
            record = record[:-1]
            self.constraint(record)
        except ValueError as err:
            return False, ""
        return True, record
    def data_gen(self, record_count=100, output_path="output/data{}.csv".format(1)):
        count = 0
        f = open(output_path, 'a')
        while count < record_count:
            result, record = self.gen_record()
            if result:
                count+=1
                f.write(record+'\n')
        f.close()
    
    
    def constraint(self, record):
        values = record.split(self.delimeter)
        if False:
            raise ValueError
if __name__ == '__main__':
    gen = Generate()
    gen.load_preset()
    gen.data_gen()
