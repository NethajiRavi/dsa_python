class maximumConsecutiveOnes:

  def get_length_maximum_consecutive_one(self,elements: list[int]) -> int: 
    one_count = 0
    max_elemnet = 0
    for i in elements:
      if i == 1:
        one_count +=1;
      else:
        max_elemnet = max(one_count,max_elemnet)
        one_count =0;    
    return one_count


if __name__ == "__main__":
  nums = [1, 1, 0, 1, 1, 1]
  obj = maximumConsecutiveOnes()
  out_put =  obj.get_length_maximum_consecutive_one(nums)
  print(out_put)
