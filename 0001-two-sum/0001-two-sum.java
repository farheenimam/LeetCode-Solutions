    class Solution {
        public static int[] twoSum(int[] nums, int target) {
            int sum = 0, prevIndex, index1 = 0, index2 = 0;
            for (int i = 0 ; i < nums.length; i ++){
                for(int j = i+1; j < nums.length; j++){
                    if (nums[i] + nums[j] == target){
                        return new int[]{i,j};
                    }
                } 
            }
    
            return new int[]{};
        }
        public static void main(String[] args){
            Scanner s = new Scanner(System.in);
            int target = s.nextInt();
            int size = s.nextInt();
            int nums[] = new int[size];
            for (int i = 0; i < size; i++){
                nums[i] = s.nextInt();
            }

            System.out.println(Solution.twoSum(nums, target));
        }
    }