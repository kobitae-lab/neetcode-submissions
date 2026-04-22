class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target and matrix[mid][-1] >= target:
                return binarySearch(matrix[mid], target)
            else:
                left = mid + 1
        return False


def binarySearch(lon, target):
    left = 0
    right = len(lon) - 1

    while left <= right:
        mid = (left + right) // 2

        if lon[mid] == target:
            return True
        elif lon[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False