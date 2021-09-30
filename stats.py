# stats class 
class stats:
    def __init__(self, number_list, n):
        self.n = n
        self.number_list = number_list
        self.sorted_list = sorted(self.number_list)
        self.counter_dict = {}

    def mean(self):
        mean = sum(self.number_list)/n
        return mean
    
    def median(self):
        if n%2 != 0:
            median = self.sorted_list[int(len(self.sorted_list)/2)]
        else:
            middle_1 = self.sorted_list[int(len(self.sorted_list)/2)]
            middle_2 = self.sorted_list[int(len(self.sorted_list)/2) - 1]
            median = (middle_1 + middle_2) / 2

        return median
    
    def mode(self):
        for item in self.sorted_list:
            if (item in self.counter_dict): 
                self.counter_dict[item] += 1
            else:
                self.counter_dict[item] = 1
            
        max_value = max(self.counter_dict.values())
        if max_value == 1:
            mode = min(self.sorted_list)
        else:
            most_frequent = [k for k,v in self.counter_dict.items() if v == max(self.counter_dict.values())]
            mode = min(most_frequent)
        return mode    

n = 10
ar = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060, 51135, 14216, 51135]

st = stats(n=n, number_list=ar)
st.mean()
st.median()
st.mode()