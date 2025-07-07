#[any max consec] นับเลขให้หนูหน่อยสิ;-;

#longest subsequence

""" จงเขียนโปรแกรมที่รับจำนวนเต็มจากผู้ใช้จนกว่าจะพบเลข 0 เมื่อรับข้อมูลจนครบแล้วโปรแกรมจะรายงานเลขที่ถูกใส่มาซ้ำติดต่อกันโดยไม่มีเลขตัวอื่นกั้น ติดต่อกันยาวที่สุดกี่ครั้งและเลขดังกล่าวมีค่าเท่าใด
  สำหรับโปรแกรมนี้ผลลัพธ์มี 2 บรรทัดโดยผลลัพธ์ในบรรทัดแรกจะระบุจำนวนตัวเลขที่ซ้ำติดต่อกันมากสุด ส่วนบรรทัดที่สองระบุว่าเลขนั้นคือเลขใดในกรณีที่มีหลายตัวให้รายงานเฉพาะตัวเลขตัวแรก
"""

seq = []
status = True 
while status:
    nums = int(input())
    if nums == 0:
        status = False
        continue
    seq.append(nums)


if len(seq) != 0:
    longest_sub = (1, seq[0])
    current_nums = (1, seq[0])
    for i in seq[1:]:
        if i == current_nums[1]:
            current_nums = current_nums[0] + 1, current_nums[1]
            if longest_sub[0] < current_nums[0]:
                longest_sub = current_nums
        else:   
            current_nums = 1, i

else:
    print("Sequence is empty")

print(f"{longest_sub[0]}\n{longest_sub[1]}")