class Solution:
    def maxArea(self, heights: list[int]) -> int:
        front = 0
        back = len(heights) - 1
        maxArea = 0

        while front < back:
            dims = [heights[front], heights[back]]
            width = back - front
            currentArea = min(dims) * width
            maxArea = max(maxArea, currentArea)

            if heights[front] < heights[back]:
                front += 1
            elif heights[front] > heights[back]:
                back -= 1
            else:
                temp_front = front + 1
                temp_back = back - 1

                front_area = min(heights[temp_front], heights[back]) * (
                    back - temp_front
                )
                back_area = min(heights[front], heights[temp_back]) * (
                    temp_back - front
                )

                if front_area > back_area:
                    front = temp_front
                else:
                    back = temp_back
        return maxArea
