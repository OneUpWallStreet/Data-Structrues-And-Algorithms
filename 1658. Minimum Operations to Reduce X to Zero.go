package main

import (
	"fmt"
	"strconv"
)

var cache map[string]int
var x_val int

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func minOfResults(r1, r2 int) int {
	if r1 == -1 && r2 == -1 {
		return -1
	} else if r1 == -1 {
		return r2
	} else if r2 == -1 {
		return r1
	} else {
		return min(r1, r2)
	}
}

func didFindInCache(key string) bool {
	_, didFind := cache[key]
	return didFind
}

func createKeyFromValues(i, j, x int) string {
	return strconv.Itoa(i) + "*" + strconv.Itoa(j) + "*" + strconv.Itoa(x)
}

func recursiveOperations(nums []int, xLeft, i, j, operationCount int) int {

	if didFindInCache(createKeyFromValues(i, j, x_val)) {
		return cache[createKeyFromValues(i, j, x_val)]
	} else if xLeft == 0 {
		return operationCount
	} else if xLeft < 0 {
		return -1
	}

	operationCount++

	if i <= j {
		res := minOfResults(recursiveOperations(nums, xLeft-nums[i], i+1, j, operationCount), recursiveOperations(nums, xLeft-nums[j], i, j-1, operationCount))
		cache[createKeyFromValues(i, j, x_val)] = res
		return res
	}

	return -1
}

func minOperations(nums []int, x int) int {
	cache = map[string]int{}
	x_val = x
	return recursiveOperations(nums, x, 0, len(nums)-1, 0)
}

func main() {

	input := []int{9094, 8070, 2920, 5358, 6366, 2950, 6596, 1403, 2409, 1399, 3229, 4019, 8228, 9584, 462, 7530, 4179, 9198, 8706, 290, 6569, 8891, 5932, 4024, 6372, 7059, 898, 5257, 4310, 7342, 8614, 3961, 5932, 3364, 2954, 4861, 2948, 6931, 5056, 8927, 9468, 9459, 7257, 7844, 4623, 5006, 733, 9792, 247, 1259, 9895, 2474, 3398, 7476, 1785, 8682, 6306, 2446, 5591, 8575, 4781, 6247, 8113, 3327, 2880, 9054, 6736, 3310, 64, 1524, 3387, 7229, 7466, 2736, 5855, 4207, 3461, 1764, 9626, 9737, 1456, 4027, 9852, 8110, 5900, 2433, 5307, 8266, 5194, 7336, 8772, 1078, 3137, 8962, 4877, 384, 5557, 9881, 651, 6568, 6702, 3706, 8671, 7623, 7477, 5874, 4954, 4200, 7937, 9125, 3854, 3453, 6023, 5483, 9908, 6222, 4521, 3687, 5470, 264, 7722, 8036, 6576, 8539, 4197, 8455, 7343, 1705, 823, 9409, 1275, 9527, 5772, 8277, 5953, 2824, 2703, 6979, 1439, 7445, 6863, 526, 2252, 2523, 2727, 1669, 9751, 7731, 1003, 1467, 7414, 9040, 5611, 5617, 5391, 8600, 4551, 3477, 1479, 8665, 2947, 2629, 5246, 6726, 6671, 5338, 4428, 5473, 8469, 9989, 2544, 4704, 4041, 4533, 139, 5167, 3801, 5940, 4521, 756, 7933, 9960, 7613, 6384, 7486, 4707, 9098, 1012, 3587, 5343, 4628, 6554, 8190, 5531, 2266, 9710, 7088, 4491, 1885, 7731, 8491, 576, 3246, 8329, 416, 9966, 1142, 5424, 1337, 9736, 3486, 7253, 869, 6916, 3498, 7630, 5631, 9222, 2671, 2235, 5860, 6198, 2546, 8231, 79, 938, 5009, 5844, 9940, 8833, 101, 4638, 5828, 3136, 39, 1603, 2803, 1982, 3090, 8041, 8738, 4125, 1340, 4779, 3685, 7174, 5856, 5149, 1041, 7069, 8869, 218, 549, 7423, 8009, 4766, 5092, 5721, 4269, 8991, 2440, 3020, 26, 4992, 3971, 5170, 4421, 586, 4935, 8608, 4994, 946, 4971, 9423, 8208, 7962, 135, 3327, 977, 8965, 9003, 1610, 1529, 6223, 216, 7063, 3831, 7759, 9631, 6585, 8085, 8265, 7880, 2628, 1988, 8475, 8371, 6167, 6290, 4943, 2311, 3123, 2649, 7556, 6616, 6054, 6976, 7802, 7677, 6578, 187, 5081, 9320, 4498, 1651, 5284, 652, 5328, 9743, 2394, 5114, 8015, 5545, 926, 2422, 3596, 7850, 1821, 8720, 6807, 2439, 1395, 6666, 5881, 7173, 7284, 2529, 8113, 5562, 552, 9904, 5644, 9801, 2160, 1865, 6432, 7342, 5688, 4809, 3690, 7778, 5204, 2637, 8206, 9331, 1777, 6441, 8546, 7193, 972, 1762, 9297, 9873, 676, 4041, 6528, 7293, 9343, 6471, 6313, 3200, 8172, 4819, 4414, 7247, 5624, 771, 5202, 153, 1366, 2700, 164, 326, 7733, 2719, 7422, 6335, 5481, 7836, 872, 1385, 3847, 6829, 3215, 1057, 6015, 8903, 9022, 2211, 7958, 5473, 2434, 2217, 4354, 1835, 1351, 9396, 2388, 7528, 3596, 2710, 7357, 6147, 4676, 9804, 6771, 9735, 4200, 9958, 7945, 8998, 9615, 854, 2491, 6983, 8974, 4827, 4399, 8624, 5291, 1526, 2995, 7222, 4242, 706, 4439, 6759, 7026, 7151, 1881, 3922, 3773, 3730, 7596, 977, 4197, 1547, 6079, 7603, 4886, 8384, 2855, 2621, 5400, 5046, 2068, 859, 5297, 5383, 3499, 716, 9947, 4731, 7193, 4031, 3351, 827, 6897, 7559, 4691, 8750, 8634, 5115, 4381, 5537, 845, 8151, 5499, 7088, 5653, 2347, 5436, 744, 4075, 6827, 1280, 3526, 3615, 9728, 8021, 2449, 9838, 5001, 9689, 1798, 4961, 3881, 2420, 5937, 9645, 514, 5252, 5191, 8465, 8420, 2493, 9334, 6391, 9195, 3851, 513, 1746, 1622, 1158, 8304, 7437, 3239, 255, 2965, 5191, 4076, 9265, 4258, 4545, 1114, 4655, 6843, 271, 2340, 4950, 1974, 4280, 1009, 8251, 6119, 2835, 2971, 2462, 6104, 2599, 6726, 7863, 2056, 3150, 3406, 2353, 4921, 9293, 60, 9139, 6774, 1002, 2956, 6490, 3587, 9661, 6949, 561, 1528, 2814, 8130, 1299, 8460, 7050, 2929, 994, 1949, 7104, 1193, 5837, 7333, 1230, 6984, 9784, 9416, 2335, 3855, 7523, 4941, 4823, 6171, 9537, 279, 5292, 8974, 870, 9481, 8102, 3622, 1203, 5503, 6892, 2518, 8036, 7723, 4942, 9805, 1879, 9377, 7321, 3458, 1506, 9972, 5628, 6557, 9390, 537, 1030, 5246, 9124, 4651, 984, 5356, 1141, 6992, 4098, 1013, 2404, 5618, 6195, 5347, 1343, 8869, 5180, 7674, 2384, 6445, 8732, 5309, 5952, 5713, 9963, 9753, 4652, 1024, 492, 3659, 1861, 6054, 2394, 4114, 6879, 3927, 4738, 4090, 1054, 8550, 7016, 5112, 6045, 5984, 4109, 71, 2933, 1060, 8635, 3370, 3038, 7201, 582, 6379, 3800, 5827, 3741, 7659, 4592, 2076, 2596, 4915, 9736, 6936, 3075, 966, 3675, 3878, 9032, 4494, 2116, 1563, 7837, 7366, 1002, 849, 6843, 1034, 9071, 1245, 4326, 5329, 9277, 8233, 1680, 8051, 7856, 5679, 3809, 7129, 3598, 2163, 6939, 2796, 2790, 9718, 50, 4534, 6417, 9367, 8891, 7879, 5978, 5659, 2269, 6845, 4763, 2952, 5882, 3356, 7655, 9462, 5417, 2327, 5532, 4153, 5585, 4506, 862, 8633, 4740, 5339, 3417, 3559, 2878, 9269, 4884, 5831, 9046, 4942, 2379, 1184, 7284, 2351, 4260, 8609, 6486, 9222, 2064, 5453, 5752, 8619, 4780, 289, 8427, 3544, 3242, 6013, 2871, 5261, 2980, 4547, 9782, 874, 5710, 7870, 4193, 6237, 9414}
	x := 510247308

	answer := minOperations(input, x)
	fmt.Println(answer)

}
