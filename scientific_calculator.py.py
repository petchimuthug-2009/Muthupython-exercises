print('WELCOME,enter the continues values according to BODMAS rule')
import math

q1 = 1
q = []
p1 = 0

while True:
    x = input(
        'enter the (num), if you operate with previous ans enter(ans), '
        'if you want seperate function value enter (fun):'
    )

    if x == '':
        print('end')
        break

    if x == 'num':
        a = eval(input('enter the number:'))
        c = input(
            'enter the operator[+,-,*,/,root(),POWER()]:'
        )

        if type(a) is type(q1):
            b = int(input('enter the num if incase of / b must be >=1:'))

            if c == '+':
                a1 = a + b
                q.append(a1)
                print(a1)

            if c == '-':
                a2 = a - b
                q.append(a2)
                print(a2)

            if c == '*':
                a3 = a * b
                q.append(a3)
                print(a3)

            if c == '/':
                a4 = a / b
                q.append(a4)
                print(a4)

            if c == 'root()':
                a51 = input('+ve or -ve root:')

                if a51 == '+ve':
                    a25 = int(input('enter the root value :'))
                    a511 = float(a ** (1 / a25))
                    print(a511)
                    q.append(float(a511))

                if a51 == '-ve':
                    a512 = int(input('enter the root value :'))
                    a52 = float(a ** (1 / a512))
                    a522 = float(1 / a52)
                    print(float(a522))
                    q.append(a522)

            if c == 'POWER()':
                df = input(
                    'enter the power type i.e +ve or -ve, exp(),log():'
                )

                if df == '+ve':
                    df1 = eval(input('enter the power value :'))
                    a61 = float(a ** df1)
                    print(a61)
                    q.append(a61)

                if df == '-ve':
                    df2 = eval(input('enter the value'))
                    a62 = float(a ** df2)
                    a621 = float(1 / a62)
                    print(a621)
                    q.append(a621)

    if x == 'fun':
        y1 = input('enter the fun [exp(),log(),sin(),cos(),tan()]:')

        if y1 == 'exp()':
            q2 = input(
                'positive or negative power(+ or -),log() :'
            )

            if q2 == '+':
                r2 = int(
                    input(
                        'if positive power enter the exp power '
                        'what you want for e.g(1/2 means e^1/2) or skip:'
                    )
                )
                f2 = float(math.exp(r2))
                print(f2)
                q.append(f2)

            if q2 == '-':
                r3 = eval(
                    input(
                        'if negative power enter the exp power '
                        'what you want for e.g(1/2 means e^1/2) or skip:'
                    )
                )
                f3 = float(math.exp(-r3))
                print(f3)
                q.append(f3)

            if q2 == 'log()':
                d344 = eval(input('enter the log value:'))
                d345 = math.log(d344)
                d346 = math.exp(d345)
                print(d346)
                q.append(d346)

        if y1 == 'log()':
            r11 = eval(input('enter the value:'))
            f4 = float(math.log(r11))
            print(f4)
            q.append(f4)

        if y1 == 'sin()':
            t69 = eval(input('enter the value(degree):'))
            t67=t69*22/(7*180)
            t68 = float(math.sin(t67))
            print(t68)
            q.append(t68)

        if y1 == 'cos()':
            j69 = eval(input('enter the value(degree):'))
            j67=j69*22/(7*180)
            j68 = float(math.cos(j67))
            print(j68)
            q.append(j68)

        if y1 == 'tan()':
            p67 = eval(input('enter the value(degree):'))
            l67 = float(math.tan(p67))
            p68 = float(math.tan(l67))
                
            print(p68)
            q.append(p68)

    if x == 'ans':
        v1 = [float(i) for i in q]
        a = v1[-1]
        k = input('enter the operater (+,-,*,/,root(),POWER()):')
        h1 = input('num,fun:')

        if h1 == 'num':
            b = int(input('enter the num if incase of / b must be >=1:'))

            if k == '+':
                a1 = a + b
                q.pop(0)
                q.append(a1)
                print(a1)

            if k == '-':
                a2 = a - b
                q.pop(0)
                q.append(a2)
                print(a2)

            if k == '*':
                a3 = a * b
                q.pop(0)
                q.append(a3)
                print(a3)

            if k == '/':
                a4 = a / b
                q.pop(0)
                q.append(a4)
                print(a4)

            if k == 'root()':
                a51 = input('+ve or -ve root:')

                if a51 == '+ve':
                    a25 = int(input('enter the root value :'))
                    a511 = float(a ** (1 / a25))
                    print(a511)
                    q.pop(0)
                    q.append(float(a511))

                if a51 == '-ve':
                    a512 = int(input('enter the root value :'))
                    a52 = float(a ** (1 / a512))
                    a522 = float(1 / a52)
                    print(float(a522))
                    q.pop(0)
                    q.append(a522)

            if k == 'POWER()':
                df = input(
                    'enter the power type i.e +ve or -ve, exp(),log():'
                )

                if df == '+ve':
                    df1 = eval(input('enter the power value :'))
                    a61 = float(a ** df1)
                    print(a61)
                    q.pop(0)
                    q.append(a61)

                if df == '-ve':
                    df2 = eval(input('enter the value'))
                    a62 = float(a ** df2)
                    a621 = float(1 / a62)
                    print(a621)
                    q.pop(0)
                    q.append(a621)

        if h1 == 'fun':
            y1 = input('enter the fun [exp(),log()]:')

            if y1 == 'exp()':
                q2 = input(
                    'positive or negative power(+ or -),log() :'
                )

                if q2 == '+':
                    r2 = int(
                        input(
                            'if positive power enter the exp power '
                            'what you want for e.g(1/2 means e^1/2) or skip:'
                        )
                    )
                    f2 = float(math.exp(r2))
                    print(f2)
                    q.pop(0)
                    q.append(f2)

                if q2 == '-':
                    r3 = eval(
                        input(
                            'if negative power enter the exp power '
                            'what you want for e.g(1/2 means e^1/2) or skip:'
                        )
                    )
                    f3 = float(math.exp(-r3))
                    print(f3)
                    q.pop(0)
                    q.append(f3)

                if q2 == 'log()':
                    d344 = eval(input('enter the log value:'))
                    d345 = math.log(d344)
                    d346 = math.exp(d345)
                    print(d346)
                    q.pop(0)
                    q.append(d346)

            if y1 == 'log()':
                r11 = eval(input('enter the value:'))
                f4 = float(math.log(r11))
                print(f4)
                q.pop(0)
                q.append(f4)

            if y1 == 'sin()':
                t69 = eval(input('enter the value(degree):'))
                t67=t69*22/(7*180)
                t68 = float(math.sin(t67))
                print(t68)
                q.append(t68)

            if y1 == 'cos()':
                j69 = eval(input('enter the value(degree):'))
                j67=j69*22/(7*180)
                j68 = float(math.cos(j67))
                print(j68)
                q.append(j68)

            if y1 == 'tan()':
                p67 = eval(input('enter the value(degree):'))
                l67=p67*22/(7*180)
                p68 = float(math.tan(l67))
                print(p68)
                q.append(p68)
