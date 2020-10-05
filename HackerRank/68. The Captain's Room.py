# Author Aman Shekhar

k = int(input())
room_number_list = list(map(int,input().split()))
room_number_set = set(room_number_list)
room_number_list_sum = sum(room_number_list)
room_number_set_sum = sum(room_number_set) * k
diff = room_number_set_sum - room_number_list_sum
for i in room_number_set:
    if diff == ((k-1)*i):
        print(i)
        break