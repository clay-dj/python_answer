class Solution:
    def mergeSortArray(self, first_list, second_list):
        new_list = []
        point_one = 0
        point_two = 0
        while point_one < len(first_list) - 1 or point_two < len(second_list) - 1:
            if first_list[point_one] > second_list[point_two]:  # 如果上面的数比下面的大，则把下面的元素append到空列表中，下面列表的指针往后移动一位
                new_list.append(second_list[point_two])
                point_two += 1
            else:  # 如果没有则反之
                new_list.append(first_list[point_one])
                point_one += 1
        if point_one < len(first_list):
            new_list.append(first_list[point_one])
        if point_two < len(second_list):
            new_list.append(second_list[point_two])

        return new_list


if __name__ == '__main__':
    list_one = [1, 2, 4]
    list_two = [1, 3, 6]
    solution = Solution()
    merge_list = solution.mergeSortArray(list_one, list_two)
    print(merge_list)
