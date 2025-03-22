class Solution(object):
    def maxStudentsOnBench(self, students):
        """
        :type students: List[List[int]]
        :rtype: int
        """
    
        bench_dict = {}

        # Populate the bench_dict with student data
        for student_id, bench_id in students:
            if bench_id not in bench_dict:
                bench_dict[bench_id] = set()  # Initialize set if bench_id not exists
            bench_dict[bench_id].add(student_id)

        # Check if the dictionary is empty
        if not bench_dict:
            return 0  # Return 0 if there are no students or benches

        # Find the maximum number of unique students on any bench
        max_students = max(len(bench) for bench in bench_dict.values())

        return max_students


    