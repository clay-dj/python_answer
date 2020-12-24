class Solution:

    def reverseInteger(self, number):
        a = int(number // 100)
        b = int(number % 100 // 10)
        c = int(number % 10)

        new_num = 100 * c + 10 * b + a
        return new_num


if __name__ == '__main__':
    num = input("输入一个三位数:")
    solution = Solution()
    new_num = solution.reverseInteger(int(num))
    print("新生成的数是:%s" % new_num)
