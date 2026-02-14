class Quize():
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer
        

        

question_list=[
    "What is the full form of ABC? \n  a.Apple ball cow \n  b.abstract base class \n  c.NOne \n  d.error",
    "which is dictionary? \n  a.dict \n  b.str \n  c.list  \n  d.None ",
    "Dry in coding? \n  a.error  \n  b.bug \n  c.dont repeat yourself \n  d.both"
]  
     
  
quize_list=[    
        Quize(question_list[0],"b"),
        Quize(question_list[1],"a"),
        Quize(question_list[2],"c")

]

def show(quize_list):
    score=0
    for i in quize_list: #i=Quize(question_list[0],"b")
        user=input(f"{i.question}\n :") #b
        
        if user == i.answer:
            score+=1
        # else:
        #     print(f"wrong answer your correct answer {i.answer}")
    print(f"your total score is {score}/{len(question_list)}")
            
        
show(quize_list)