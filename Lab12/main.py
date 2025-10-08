unsorted_list : list[any] = [2,1,3,5,8,7]


class Bubble_Sort:
    def __init__(self , unsorted_list : list[any]):
        self.unsorted_list : list[any] = unsorted_list

    
    def sort(self) -> list[any]:
        unsorted_list = self.unsorted_list
        print("Current Data {}".format(unsorted_list))
        for i in range(len(unsorted_list)):
            for j in range(len(unsorted_list) , i+1 , -1):
                if unsorted_list[j-1] < unsorted_list[j-2]:
                    tmp = unsorted_list[j-2]
                    tmp2 = unsorted_list[j-1]
                    unsorted_list[j-1] = tmp
                    unsorted_list[j-2] = tmp2
            print("After {} round {}".format(i , unsorted_list))
        self.unsorted_list = unsorted_list 


    def display(self) -> list[any]: return self.unsorted_list




bubble = Bubble_Sort(unsorted_list)
bubble.sort()
bubble.display()