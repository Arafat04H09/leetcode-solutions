class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        ans = 0
        for num_boxes, units_per_box in boxTypes:
            if truckSize <= 0:
                break  

            boxes_to_load = min(num_boxes, truckSize)
            ans += boxes_to_load * units_per_box
            truckSize -= boxes_to_load

        return ans