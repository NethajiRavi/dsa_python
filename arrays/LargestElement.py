class LargetElement:

  def get_largest_element(self,element: list[int]) -> int:
    return max(element)

if __name__ == "__main__":
  nums = [2, 5, 1, 9, 3]
  obj = LargetElement()
  output =  obj.get_largest_element(nums)
  print(output) 