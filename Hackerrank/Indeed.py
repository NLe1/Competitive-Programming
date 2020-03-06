users, jobs = {}, {}

def handle_add(type, user_id, job_id):
    #check if user_id in the exists in database
    #create a dictionary associated with user_id
    if user_id not in users:
        users[user_id] = {}

    #check if the user already have existing steps associated with job_id
    #if not create a queue of steps type
    if job_id not in users[user_id]:
        users[user_id][job_id] = []

    users[user_id][job_id].append(type)

    #add user_id to record of job applicants
    #check if exists job or not
    if job_id not in jobs:
        jobs[job_id] = set()

    #add user_id to collections associated with job_id
    jobs[job_id].add(user_id)

def handle_query(user_id):
    #check if user_id in the users
    if user_id in users:
        #check if exists next step
        if len(users[user_id]) > 0:
            print("Next steps for user {}:".format(user_id))
            for job_id in sorted(users[user_id].keys()):
                print("    {} {}".format(job_id, users[user_id][job_id][0]))
        else:
            print("No result")
    else:
        print("No result")

def handle_complete(user_id, job_id):
    #check if the input is valid by checking if user_id exists and
    #checking if that user have job_id or not
    if user_id in users:
        if job_id in users[user_id]:
            next_step = users[user_id][job_id].pop(0)

            #if there is no more steps, delete the job_id from the users
            #and delete the user from the jobs
            if len(users[user_id][job_id]) == 0:
                del users[user_id][job_id]
                jobs[job_id].remove(user_id)
            print("User {} completed {} for job {}".format(user_id, next_step, job_id))
        else:
            print("No result")
    else:
        print("No result")


def handle_expire(job_id):
    #check if job_id exists
    if job_id in jobs:
        for user_id in list(set(jobs[job_id])):
            # delete all the steps associated with job_id and user_id
            del users[user_id][job_id]
        # delete the job_id from the jobs
        del jobs[job_id]


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for _ in range(n):
    queries = input().rstrip().split()
    operation = queries[0]

    if operation == "ADD":
        handle_add(queries[1], queries[2], queries[3])
    elif operation == "QUERY":
        handle_query(queries[1])
    elif operation == "COMPLETE":
        handle_complete(queries[1], queries[2])
    else:
        handle_expire(queries[1])



