def calculate_mean(sample_data, size):
    sum = 0
    for i in range(size):
        sum += sample_data[i]
    return sum/size

sample_data = []
size = int(input("Enter the total size of sample: "))
print("Enter the data samples: ")
for _ in range(size):
    sample_data.append(int(input()))

calculated_mean = calculate_mean(sample_data, size)
print(f"\nData sample: {sample_data}")
print(f"\nMean: {calculated_mean:.3f}")