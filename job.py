def JobSequencing(jobs): 
    n = len(jobs) 
    for i in range(n): 
        for j in range(0, n - i - 1): 
            if jobs[j][2] < jobs[j + 1][2]: 
                jobs[j], jobs[j + 1] = jobs[j + 1], jobs[j] 
    
    maxdeadline = max(jobs, key=lambda x: x[1])[1] 
    selected_jobs = [-1] * maxdeadline 
    profit_jobs=[0] * maxdeadline 
    totalprofit = 0 
    
    for job in jobs: 
        j,deadline, profit = job[0], job[1], job[2] 
        # Find the latest available time slot for this job 
        for i in range(deadline - 1, -1, -1): 
            if selected_jobs[i] == -1: 
                selected_jobs[i] , profit_jobs[i] = j , profit 
                break
             
    totalprofit =sum(profit_jobs) 
    print(f"Job Sequence {selected_jobs} with profits {profit_jobs}") 
    print(f"Total Profit is {totalprofit}") 



#Main Progranj 
job_list=[] 
n=int(input("Enter the number of jobs :")) 
for i in range(n): 
    deadline=int(input(f"Enter the deadline for job {i+1} :")) 
    profit=int(input(f"Enter the profit for job {i+1} :")) 
                                                                            
    j=[i+1,deadline,profit] 
    job_list.append(j) 

print(f"Given set of jobs are {job_list}")
JobSequencing(job_list) 