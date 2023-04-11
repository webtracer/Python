import week_one_dist

# d = week_one_dist.distance(3, 5, -1, 2)
# print(d)


def postfix_math(a,b,c,d,e,f,g):
    """

    :param a:
    :param b:
    :param c:
    :param d:
    :param e:
    :param f:
    :return:
    """
    #postfix_result = abc-d/e*+fg^+
    infix_result = a+(b-c)/d*e+f^g

    #print(f"Postfix: {postfix_result}")
    print(f"Infix: {infix_result}")


postfix_math(1.0,2.0,3.0,4.0,5.0,6.0,2.0)