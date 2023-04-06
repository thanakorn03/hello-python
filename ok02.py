import random

number = random.randint(1, 100)
guess_count = 0
guess_limit = 6

print("ยินดีต้อนรับสู่เกมทายตัวเลข!")
print(f"กรุณาเดาตัวเลขที่อยู่ระหว่าง 1 ถึง 100 ภายใน {guess_limit} ครั้ง")

while guess_count < guess_limit:
    guess = int(input("ทายตัวเลขของคุณ: "))
    guess_count += 1
    
    if guess < number:
        print("ตัวเลขของคุณต่ำเกินไป!")
    elif guess > number:
        print("ตัวเลขของคุณสูงเกินไป!")
    else:
        print(f"ยินดีด้วย! คุณทายตัวเลข {number} ถูกต้องในครั้งที่ {guess_count}!")
        break
else:
    print(f"เสียใจด้วย! คุณไม่สามารถทายตัวเลข {number} ในจำนวนครั้งที่กำหนดได้")