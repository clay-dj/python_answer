class Solution:
    # 参数nums1：整数数组
    # 参数nums2：整数数组
    def nextGreaterElement(self, nums_one, num_second):
        answer = {}
        stack = []
        for x in num_second:
            while stack and stack[-1] < x:
                answer[stack[-1]] = x
                del stack[-1]
            stack.append(x)
        for x in stack:
            answer[x] = -1
        return [answer[x] for x in nums_one]


if __name__ == '__main__':
    s = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print("输入1：", nums1)
    print("输入2：", nums2)
    print("输出3", s.nextGreaterElement(nums1, nums2))
