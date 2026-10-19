class LinearSearch:
    def findTheElement(self, element: list[int], target: int) -> int:
        for index, value in enumerate(element):
            print(index, value)

        for i, val in enumerate(element):
            if val == target:
                return i   # return index instead of value
        return -1

if __name__ == "__main__":
    elem = [10, 20, 30, 40, 50]
    target = 30
    obj = LinearSearch()
    output = obj.findTheElement(elem, target)
    print("Result index:", output)
