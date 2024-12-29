def calculate_median(sample_data, size):
    # for i in range(size):
    #     print(i)
    val = (size + 1) / 2
    decimal_val = val - int(val)
    if type(val) == float and decimal_val != 0.0:
        first_val = int(val)
        
        return (sample_data[first_val-1] + sample_data[first_val]) / 2
    else:
        val = int((size + 1) / 2)
        return sample_data[val-1]
    
sample_data = []
size = int(input("Enter the total size of sample: "))
print("Enter the data samples: ")
for _ in range(size):
    sample_data.append(int(input()))

sample_data.sort()
calculated_median = calculate_median(sample_data, size)
print("\nOutput:")
print(f"Data sample: {sample_data}")
print(f"Median: {calculated_median}")