import random 

class SplitData:
    def __init__(self, data, train_ratio, test_ratio, shuffel):
        self.data = data
        self.train_ratio = train_ratio 
        self.test_ratio = test_ratio 
        self.shuffel = shuffel

    def split_data(self):
        if self.shuffel == True:
            random.shuffle(self.data)
        split_index = int(len(self.data)* (1- self.train_ratio))
        train_data = self.data[split_index:]
        test_data = self.data[:split_index]
        print(f"Train data: {len(train_data)} ----- Test data: {len(test_data)}")
        return train_data, test_data 

data_1 = [ i for i in range(50)] # list type 
split = SplitData(data_1, 0.7, 0.3, True)
split.split_data()