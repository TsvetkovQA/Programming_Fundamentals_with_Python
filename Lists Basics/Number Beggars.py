integers_str = input()
beggars_count = int(input())

integers = [int(num) for num in integers_str.split(", ")]

beggars_sums = [0] * beggars_count

for i, num in enumerate(integers):
    beggar_index = i % beggars_count
    beggars_sums[beggar_index] += num

result_list = beggars_sums

print(result_list)
