import os , random

for i in range(10):
    d = str(i) + 'days ago'
    rand = random.randrange(9, 12)
    with open('test.txt','a') as file:
        file.write(d+'\n')
    os.system('git add test.txt')
    os.system('git commit --date=" 2023-'+str(rand)+'-'+d+'" -m 1')
os.system('git push -u origin main')
