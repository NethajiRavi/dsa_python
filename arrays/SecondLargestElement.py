class SecondLargestElement:

  def get_seccond_larget_element(self,element:list[int]):
    largest = second = float('-inf')
    print(f"infinte{largest}")
    for i in element:
      if i > largest:
        second = largest
        largest = i
      elif i > second and i != largest:
        second = i
    return second

if __name__ == "__main__":
  ele =  [12, 35, 1, 10, 34, 1]
  obj = SecondLargestElement()
  output =  obj.get_seccond_larget_element(ele)
  print(output)