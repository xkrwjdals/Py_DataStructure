# import stack as st
import calculator as cal

# odd = st.Stack()
# even = st.Stack()
# for i in range(10):
#     if i%2==0 : even.push(i)
#     else: odd.push(i)
#
# print('Even stack push 5 times:', even.top)
# print('Odd stack push 5 times:', odd.top)

infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
Postfix1 = cal.Infix2Postfix(infix1)
Postfix2 = cal.Infix2Postfix(infix2)

print(infix1, '의 후위표기 \n', Postfix1)
print('계산결과 : ', cal.evalPostfix(Postfix1))

print(infix2, '의 후위표기 \n', Postfix2)
print('계산결과 : ', cal.evalPostfix(Postfix2))

