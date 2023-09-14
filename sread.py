labels = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]

def sreader (encoded_num):
	real_x = 0
	for x in range(0,100):
		tested_max = 2**x
		if (encoded_num+1)%(tested_max)==0 and 2**real_x < tested_max:
			real_x = x
			
	real_y = 0
	for y in range(0,100):
		if ((encoded_num+1)/(2**real_x))==((2*y+1)):
			real_y = y
			break
	return real_x,real_y


def encode_s_list (prog):
	res = []
	max_prime = 0
	primes = [x for x in range(2,prog+1) if all(x % y != 0 for y in range(2, x))]

	for n in primes:
		if prog%n == 0 and n > max_prime:
			max_prime = n
	
	limit = list(filter(lambda x: x <= max_prime, primes))

	for n in limit:
		how_many = 0
		while prog%n == 0:
			how_many += 1
			prog = prog/n
		res.append(how_many)
	return res
	
def commends (x,argument_num) : 
		arguments = ["Y","X1","Z1","X2","Z2","X3","Z3","X4","Z4","X5","Z5","X6","Z6","X7"]

		if x == 0:
			return arguments[argument_num] + " <- " + arguments[argument_num]
		elif x == 1: 
			return arguments[argument_num] + " <- " + arguments[argument_num] + " + 1",
		elif x == 2: 
			return arguments[argument_num] + " <- " + arguments[argument_num] + " - 1",
		else: 
			return "goto " + labels[x-3]		
	
def main ():				
	encoded_num = int(input("Enter encoded commend: "))

	enc_list = encode_s_list(encoded_num)

	for i in enc_list:
		if(i == 0):
			continue
		res = sreader(i)
		left = res[0]
		right = sreader(res[1])
		commend = right[0]
		argument_num = right[1]
		print("[",labels[left-1] if left > 0 else "","]" ,commends(commend,argument_num))

main()

