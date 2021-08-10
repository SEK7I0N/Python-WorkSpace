def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        Flag = False
        
        pointer_num = 0
        pointer_zeros = 0
        len_of_nums = len(nums)
        while pointer_num < len_of_nums and pointer_zeros< len_of_nums:    
            print(pointer_num,"  ",pointer_zeros)
            if nums[pointer_num] == 0:
                pointer_num +=1
                continue
            if nums[pointer_zeros] != 0:
                pointer_zeros +=1
                continue
            if pointer_num > pointer_zeros:
                
                temp = nums[pointer_num]
                nums[pointer_num] = nums[pointer_zeros] 
                nums[pointer_zeros] = temp
            else:
                pointer_num+=1

number_list = [0,1,2,0,3,0,01,0,2130,]

print(moveZeroes(number_list))