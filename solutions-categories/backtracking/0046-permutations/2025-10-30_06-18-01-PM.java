class Solution {
    public List<List<Integer>> permute(int[] nums) {
        boolean[] used = new boolean[nums.length];
        List<List<Integer>> out = new ArrayList<>();
        backtrack(nums, new ArrayList<>(), used, out);
        return out;
    };

    private void backtrack(int[] nums, List<Integer> path, boolean[] used, List<List<Integer>> out) {
        if (path.size() == nums.length) {
            out.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            path.add(nums[i]);
            backtrack(nums, path, used, out);
            path.remove(path.size() - 1);
            used[i] = false;
        }
    }
}
