''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import math
def checkPrime(number):
    #print(number)
    #math.floor(math.sqrt(number))
    #number//2
    possibleDivisor = math.floor(math.sqrt(number))
    for num in range(2,possibleDivisor+1):
        if number%num == 0:
            return False
    return True


def main():

 # Write code here 
    N = int(input())
    L = []
    R = []
    for _ in range(N):
        left, right = input().split()
        L.append(int(left))
        R.append(int(right))

    for set_of_numbers in range(N):
        difference = -1
        value_in_left = L[set_of_numbers]
        value_in_right = R[set_of_numbers]
        left_flag = False
        right_flag = False
        left_temp = 0
        right_temp = 0
        while value_in_left <= value_in_right:
            if checkPrime(value_in_left) and left_flag == False:
                left_flag = True
                left_temp=value_in_left
            if checkPrime(value_in_right) and right_flag == False:
                right_flag = True
                right_temp=value_in_right
            #print(left_temp,right_temp)
            value_in_left+=1
            value_in_right-=1
        if right_flag and left_flag:
            difference = right_temp - left_temp
        elif right_flag or left_flag:
            difference = 0
        print(difference)
main()

1