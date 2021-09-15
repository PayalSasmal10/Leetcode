def reverse(strg):
    if len(strg) <=1:
        return strg
    print(strg[len(strg)-1])
    return strg[len(strg)-1]+ reverse(strg[0:len(strg)-1])



print(reverse("Twitter"))






# strg[4] + reverse("paya") l -> layap
#     strg[3]+ reverse("pay") a + yap - > ayap
#         strg[2] + reverse("pa") y +ap -> yap
#           strg[1] + reverse("p") a + p ->ap
#               strg[0] + reverse ("p") ->p



