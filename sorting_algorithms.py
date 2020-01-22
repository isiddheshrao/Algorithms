import sys
import random
import matplotlib.pyplot as plt
import time

#Merge Sort Omega(nlogn) Algorithm, 
class Merge:
    # define mergesort function and get mid point of input list
    def mergesort(self, input_list):
        if len(input_list)>1:
            mid = len(input_list)//2
            #based on mid point, make two sublists, right an left
            right_list = input_list[mid:]
            left_list = input_list[:mid]

            # call merge sort again until there is just one element in both sub lists
            self.mergesort(left_list)
            self.mergesort(right_list)


            # merging two small sorted list into larger sorted list
            i = 0
            j = 0
            k = 0
            #comparing left list element with right list element
            while i< len(left_list) and j < len(right_list):
                if left_list[i] <= right_list[j]:
                    input_list[k] = left_list[i]
                    i +=1
                else:
                    input_list[k] = right_list[j]
                    j +=1
                k +=1

            while i < len(left_list):
                input_list[k] = left_list[i]
                i+=1
                k+=1
            
            while j < len(right_list):
                input_list[k]=right_list[j]
                j+=1
                k+=1
        
        print("Sorting Via Merge Sort ", input_list)

# Heap Sort Omega(nlogn), O(nlogn)
class Heap: 
    def heapsort(self, input_list):
        #rearrange list into list representation of heap
        self.build_max_heap(input_list)
        #swap first with last element of heap
        for i in range(len(input_list)-1, 0, -1):
            print("Sorting via Heap Sort: ", input_list)
            input_list[0], input_list[i] = input_list[i], input_list[0]
            #new heap to have size one less than its previous size and call max_heapify with index = 0 to make this new heap satisfy the heap property
            self.max_heapify(input_list, index = 0, size= i)
        print("Your Sorted List via Heap Sort is", input_list)
    
    def parent(self, i):
        #index as argument and return index of parent
        return (i - 1) // 2

    def left(self, i):
        #index as argument and return index of left child
        return 2*i + 1

    def right(self, i):
        #index as argument and return index of right child
        return 2*i + 2

    def build_max_heap(self, input_list):
        #list as argument and rearrange to form max heap
        length = len(input_list)
        start = self.parent(length-1)
        #calling max_heapify on each parent node starting from the last parent node and working towards the root
        while start >= 0:
            self.max_heapify(input_list, index = start, size = length)
            start -= 1

    def max_heapify(self, input_list, index, size):
        # index as argument and modifies the heap structure at and below the node at this index to make it satisfy the heap property
        l = self.left(index)
        r = self.right(index)
        if (l < size and input_list[l] > input_list[index]):
            largest = l
        else:
            largest = index
        if (r < size and input_list[r] > input_list[largest]):
            largest = r
        if largest != index:
            input_list[largest], input_list[index] = input_list[index], input_list[largest]
            self.max_heapify(input_list, largest, size)


#Insertion Sort Omega(n), O(n^2)
class Insertion:
    def insertionsort(self, input_list):
        #for every element in input_list
        for i in range(1, len(input_list)):
            current_ele = input_list[i]
            pos = i - 1

            while pos >= 0 and current_ele < input_list[pos]:
                #comparing and swapping done here
                input_list[pos + 1] = input_list[pos]
                pos -= 1
                print(input_list)

            input_list[pos + 1] = current_ele
        
        print("Your Sorted List Via Insertion Sort is: ", input_list)

# Quick Sort using median 3- Omega(nlogn) Algorithm , O(n^2)
class Quick:

    def median(self, left, middle, right):
        #calculating median of 3
        if ( left - middle) * (right - left) >= 0:
            return left
        elif (middle - left) * (right - middle) >= 0:
            return middle
        else:
            return right

    def partition_median(self, input_list, left_list, right_list):
        left = input_list[left_list]
        right = input_list[right_list-1]
        length = right_list - left_list
        #getting middle by getting floor value
        if length % 2 == 0:
            middle = input_list[left_list + length//2 - 1]
        else:
            middle = input_list[left_list + length//2]

        # getting pivot element by median of three
        pivot = self.median(left, right, middle)
        # getting pivot index
        pivotindex = input_list.index(pivot) 
        input_list[pivotindex] = input_list[left_list]
        input_list[left_list] = pivot
        i = left_list + 1
        # comparing with respect to pivot element
        for j in range(left_list + 1, right_list):
            if input_list[j] < pivot:
                temp = input_list[j]
                input_list[j] = input_list[i]
                input_list[i] = temp
                i += 1
        leftendval = input_list[left_list]
        input_list[left_list] = input_list[i-1]
        input_list[i-1] = leftendval
        return i - 1
    
    def quicksort(self, input_list, left_index, right_index):
        print("Sorting via quick Sort: ", input_list)
        #updating pivot and returning sorted list
        if left_index < right_index:
            newpivotindex = self.partition_median(input_list, left_index, right_index)
            self.quicksort(input_list, left_index, newpivotindex)
            self.quicksort(input_list, newpivotindex + 1, right_index)
        return input_list

    

# Bubble Sort Omega(n^2), O(n^2)
class Bubble:
    def bubblesort(self, input_list):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(input_list)-1):
                # Comparision and Swapping done here
                if input_list[i]>input_list[i+1]:
                    print("Sorting via Bubble Sort: ", input_list)
                    input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                    swapped = True
        return input_list

def generate_randoms(n):
    #generating random integers in range 1-10,000 based on input size n
    input_list = [random.randint(1, 10000) for i in range(n)]
    return input_list

def get_user_input(n):
    print("Enter elements for your list: ")
    # enter list elements
    for i in range(0, n):
        elements = int(input())
        input_list.append(elements)
    return input_list

def compare_algorithms():
    # randomly generates list of different 
    # sizes and calls all sorting funtions 
    element1 = list() 
    time1 = list()
    element2 = list()
    time2 = list()
    element3 = list()
    time3 = list()
    element4 = list()
    time4 = list()
    element5 = list()
    time5 = list()

    for i in range(1,100):  
        # generate some integers 
        a = [random.randint(1, 1000) for _ in range(i)]
        start1 = time.clock() 
        msort.mergesort(a)
        end1 = time.clock()
        element1.append(len(a)) 
        time1.append(end1-start1)

        a1 = [random.randint(1, 1000) for _ in range(i)]
        start2 = time.clock()
        isort.insertionsort(a1)
        end2 = time.clock() 
        element2.append(len(a1)) 
        time2.append(end2-start2)

        a2 = [random.randint(1, 1000) for _ in range(i)]
        start3 = time.clock()
        bsort.bubblesort(a2)
        end3 = time.clock() 
        element3.append(len(a2)) 
        time3.append(end3-start3)

        a3 = [random.randint(1, 1000) for _ in range(i)]
        start4 = time.clock()
        hsort.heapsort(a3)
        end4 = time.clock() 
        element4.append(len(a3)) 
        time4.append(end4-start4)

        a4 = [random.randint(1, 1000) for _ in range(i)]
        start5 = time.clock()
        qsort.quicksort(a4, 0, len(a4))
        end5 = time.clock() 
        element5.append(len(a4)) 
        time5.append(end5-start5) 
  
    plt.xlabel('List Length Size') 
    plt.ylabel('Time [s]') 
    plt.plot(element1, time1, label ='Merge Sort')
    plt.plot(element2, time2, label ='Insertion Sort')
    plt.plot(element3, time3, label ='Bubble Sort')
    plt.plot(element4, time4, label ='Heap Sort')
    plt.plot(element5, time5,  label ='Quick Sort') 
    plt.grid() 
    plt.legend() 
    plt.show()

if __name__=="__main__":
    msort = Merge()
    qsort = Quick()
    isort = Insertion()
    hsort = Heap()
    bsort = Bubble()
    input_list = []
    choice = input("Please enter your choice of sorting algorithm (Enter 'Merge'/'Heap'/'Quick'/'Insertion'/'Bubble'): ")
    choice = choice.lower()
    if choice == "merge":
        #Enter input size of list.
        n = int(input("Enter size of list to be sorted: "))
        random_choice = input("Do you want to randomly generate numbers (Enter Y/N): ")
        random_choice = random_choice.lower()
        if random_choice == 'y':
            input_list = generate_randoms(n)
            print("Your Input List is: ", input_list)
            msort.mergesort(input_list)
            print("Sorted List via Merge Sort is: ", input_list)
            tot_time = time.process_time()
            print("Total Execution Time: ", tot_time)
            plot_choice = input("Do you want to see Time vs List Size Graph? (Y/N): ")
            plot_choice = plot_choice.lower()
            if plot_choice == 'y':
                # randomly generates list of different 
                # sizes and call MergeSort funtion 
                elements = list() 
                times = list() 
                for i in range(1, n):  
                    # generate some integers 
                    a = [random.randint(1, 1000) for _ in range(i)]
                    start = time.clock() 
                    msort.mergesort(a) 
                    end = time.clock() 
                    elements.append(len(a)) 
                    times.append(end-start) 
  
                plt.xlabel('List Length Size') 
                plt.ylabel('Time [s]') 
                plt.plot(elements, times, label ='Merge Sort') 
                plt.grid() 
                plt.legend() 
                plt.show()
            else:
                sys.exit()
        elif random_choice == 'n':
            input_list = get_user_input(n)
            print("Your Input List is: ", input_list)
            msort.mergesort(input_list)
            tot_time = time.process_time()
            print("Total Execution Time: ", tot_time)

    elif choice == "bubble":
        #Enter input size of list.
        n = int(input("Enter size of list to be sorted: "))
        random_choice = input("Do you want to randomly generate numbers (Enter Y/N): ")
        random_choice = random_choice.lower()
        if random_choice == 'y':
            input_list = generate_randoms(n)
            print("Your Input List is: ", input_list)
            output = bsort.bubblesort(input_list)
            print("Your Sorted List via Bubble Sort is: ", output)
            tot_time = time.process_time()
            print("Total Execution Time: ", tot_time)
            plot_choice = input("Do you want to see Time vs List Size Graph? (Y/N): ")
            plot_choice = plot_choice.lower()
            if plot_choice == 'y':
                # randomly generates list of different 
                # sizes and call BubbleSort funtion 
                elements = list() 
                times = list() 
                for i in range(1, n):  
                    # generate some integers 
                    a = [random.randint(1, 1000) for _ in range(i)]
                    start = time.clock() 
                    bsort.bubblesort(a) 
                    end = time.clock() 
                    elements.append(len(a)) 
                    times.append(end-start) 
  
                plt.xlabel('List Length Size') 
                plt.ylabel('Time [s]') 
                plt.plot(elements, times, label ='Bubble Sort') 
                plt.grid() 
                plt.legend() 
                plt.show()
            else:
                sys.exit()
        elif random_choice == 'n':
            input_list = get_user_input(n)
            print("Your Input List is: ", input_list)
            output = bsort.bubblesort(input_list)
            print("Your Sorted List via Bubble Sort is: ", output)
            tot_time = time.process_time()
            print("Total Execution Time: ", tot_time)

    elif choice == "insertion":
        #Enter input size of list.
        n = int(input("Enter size of list to be sorted: "))
        random_choice = input("Do you want to randomly generate numbers (Enter Y/N): ")
        random_choice = random_choice.lower()
        if random_choice == 'y':
            input_list = generate_randoms(n)
            print("Your Input List is: ", input_list)
            isort.insertionsort(input_list)
            tot_time = time.process_time()
            print("Total Execution Time: ", tot_time)
            plot_choice = input("Do you want to see Time vs List Size Graph? (Y/N): ")
            plot_choice = plot_choice.lower()
            if plot_choice == 'y':
                # randomly generates list of different 
                # sizes and call InsertionSort funtion 
                elements = list() 
                times = list() 
                for i in range(1, n):  
                    # generate some integers 
                    a = [random.randint(1, 1000) for _ in range(i)]
                    start = time.clock() 
                    isort.insertionsort(a) 
                    end = time.clock() 
                    elements.append(len(a)) 
                    times.append(end-start) 
  
                plt.xlabel('List Length Size') 
                plt.ylabel('Time [s]') 
                plt.plot(elements, times, label ='Insertion Sort') 
                plt.grid() 
                plt.legend() 
                plt.show()
            else:
                sys.exit()
        elif random_choice == 'n':
            input_list = get_user_input(n)
            print("Your Input List is: ", input_list)
            isort.insertionsort(input_list)
            tot_time = time.process_time()
            print("Total Execution Time: ", tot_time)

    elif choice == "heap":
        #Enter input size of list.
        n = int(input("Enter size of list to be sorted: "))
        random_choice = input("Do you want to randomly generate numbers (Enter Y/N): ")
        random_choice = random_choice.lower()
        if random_choice == 'y':
            input_list = generate_randoms(n)
            print("Your Input List is: ", input_list)
            hsort.heapsort(input_list)
            tot_time = time.process_time()
            print("Total Execution Time: ", tot_time)
            plot_choice = input("Do you want to see Time vs List Size Graph? (Y/N): ")
            plot_choice = plot_choice.lower()
            if plot_choice == 'y':
                # randomly generates list of different 
                # sizes and call HeapSort funtion 
                elements = list() 
                times = list() 
                for i in range(1, n):  
                    # generate some integers 
                    a = [random.randint(1, 1000) for _ in range(i)]
                    start = time.clock() 
                    hsort.heapsort(a) 
                    end = time.clock() 
                    elements.append(len(a)) 
                    times.append(end-start) 
  
                plt.xlabel('List Length Size') 
                plt.ylabel('Time [s]') 
                plt.plot(elements, times, label ='Heap Sort') 
                plt.grid() 
                plt.legend() 
                plt.show()
            else:
                sys.exit()
        elif random_choice == 'n':
            input_list = get_user_input(n)
            print("Your Input List is: ", input_list)
            hsort.heapsort(input_list)
            tot_time = time.process_time()
            print("Total Execution Time: ", tot_time)

    elif choice == "quick":
        #Enter input size of list.
        n = int(input("Enter size of list to be sorted: "))
        random_choice = input("Do you want to randomly generate numbers (Enter Y/N): ")
        random_choice = random_choice.lower()
        if random_choice == 'y':
            input_list = generate_randoms(n)
            print("Your Input List is: ", input_list)
            sorted_list = qsort.quicksort(input_list, 0, len(input_list))
            print("Your Sorted List via Quick Sort is: ", sorted_list)
            tot_time = time.process_time()
            print("Total Execution Time: ", tot_time)
            plot_choice = input("Do you want to see Time vs List Size Graph? (Y/N): ")
            plot_choice = plot_choice.lower()
            if plot_choice == 'y':
                # randomly generates list of different 
                # sizes and call QuickSort funtion 
                elements = list() 
                times = list() 
                for i in range(1, n):  
                    # generate some integers 
                    a = [random.randint(1, 1000) for _ in range(i)]
                    start = time.clock() 
                    qsort.quicksort(a, 0, len(a)) 
                    end = time.clock() 
                    elements.append(len(a)) 
                    times.append(end-start) 
  
                plt.xlabel('List Length Size') 
                plt.ylabel('Time [s]') 
                plt.plot(elements, times, label ='Quick Sort') 
                plt.grid() 
                plt.legend() 
                plt.show()
            else:
                sys.exit()
        elif random_choice == 'n':
            input_list = get_user_input(n)
            print("Your Input List is: ", input_list)
            sorted_list = qsort.quicksort(input_list, 0, len(input_list))
            print("Your Sorted List via Quick Sort is: ", sorted_list)
            tot_time = time.process_time()
            print("Total Execution Time: ", tot_time)
    
    else:
        compare_choice = input("Do you want to see time vs list size graph for all algorithms? (Y/N): ")
        compare_choice = compare_choice.lower()
        if compare_choice == 'y':
            print("Comparing all algorithms and plotting Tims vs List Size Graph")
            compare_algorithms()
        else:
            sys.exit()