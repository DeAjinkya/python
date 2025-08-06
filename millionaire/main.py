questions = [
    ["1. What is an operating system?","interface between the hardware and application programs","collection of programs that manages hardware resources","system service provider to the application programs","all of the mentioned", 4],
    ["2. What is the main function of the command interpreter","to provide the interface between the API and application program","to handle the files in the operating system","to get and execute the next user-specified command","none of the mentioned",3],
    ["3. In Operating Systems, which of the following is/are CPU scheduling algorithms?","Priority","Round Robin","Shortest Job First","All of the mentioned",4],
    ["4. To access the services of the operating system, the interface is provided by the ___________","Library","System calls","Assembly instructions","API",2],
    ["5. CPU scheduling is the basis of ___________","multiprogramming operating systems","larger memory sized systems","multiprocessor systems","none of the mentioned",1]
]

i = 0
sum = 0
prizes = [100,200,300,400,500]

for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    # check the answer is correct or not
    a = int(input("enter u answer 1 for a, 2 for b, c for 3, d for 4\n"))

    if question[5] == a:
        print("correct answer")
    else:
        print(f"incorrect answer, right answer is {question[5]}")
        print("better luck next time")
        break

    sum += prizes[i]
    print(f"u won {sum}")
    i += 1