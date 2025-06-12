student_data = {'id1':
    {'name':['sara'],
     'class':['v'],
     'subject_integration':['english,math,scince']
    },
    'id2':
    {'name':['David'],
     'class':['v'],
     'subject_integration':['english,math,scince']
    },
    'id3':
    {'name':['sara'],
     'class':['v'],
     'subject_integration':['english,math,scince']
    },
    'id4':
    {'name':['surya'],
     'class':['v'],
     'subject_integration':['english,math,scince']
    },
}
result={}
for key,value in student_data.items():
    if value not in result.values ():
     result [key]=value
print(result) 