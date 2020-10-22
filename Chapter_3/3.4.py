gest_list = [ 'Qiushi', 'Zhendong', 'peikang', 'nanchi' ]
print(gest_list)

not_come = gest_list.pop()
print(gest_list)
print(not_come.title() + " can not come.")
print(gest_list[0].title() + "来吃翔！")
print(gest_list[1].title() + "来吃翔！")
print(gest_list[2].title() + "来吃翔！")

gest_list.append('kakasu')
gest_list.append('miyuki')
gest_list.insert(0, 'fukuyama')
print(gest_list)
print('I found a larger table so I can invite them, I am glad')


print('Sorry I can only invite 2 persons.')
not_invi = gest_list.pop()
print('Sorry ' + not_invi + ", I can't invite you this time. ")
not_invi = gest_list.pop()
print('Sorry ' + not_invi + ", I can't invite you this time. ")
not_invi = gest_list.pop(0)
print('Sorry ' + not_invi + ", I can't invite you this time. ")
print("Hey " + gest_list[0] + " you are still invited!")
print("Hey " + gest_list[1] + " you are still invited!")
print("Hey " + gest_list[2] + " you are still invited!")

del gest_list[0]
del gest_list[0]
del gest_list[0]
print(gest_list)