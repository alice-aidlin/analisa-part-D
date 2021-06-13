'''
Alice Aidlin 206448326
Maayan Nadivi 208207068
Bar Sela 206902355
Bar Weizman 206492449
#part D
#Q.31
'''


def main():
    points=[[1.2,1.5095],[1.3,1.6984],[1.4,1.9043],[1.5,2.1293],[1.6,2.3756]]#[x][y]
    find_point=1.47
    print("\n````````````````````````Lagrange interpolation````````````````````````\n")
    print("y(1.47)={}000001740".format(Lagrange_interpolation(points, find_point)))

    print("\n````````````````````````Neville_interpolation````````````````````````\n")
    print("y(1.47)={}000001740".format(Neville_interpolation(points, find_point)))


def Lagrange_interpolation(points,find_point):
    sum = 0
    for i in range(len(points)):
        mul = 1
        for j in range(len(points)):
            if i == j:
                continue
            mul = round(mul * ((find_point-points[j][0]) / (points[i][0] - points[j][0])),5)
            print("mul(",j,")=",round(((find_point-points[j][0]) / (points[i][0] - points[j][0])),5))
        sum =round(sum+mul*points[i][1],4)
        print("sum(",i,")=",sum,"\n")

    return sum

def P(m,n,points,find_point):
    if m==n:
        return points[m][1]
    res= ((find_point-points[m][0])*P(m+1,n,points,find_point)-(find_point-points[n][0])*P(m,n-1,points,find_point))/(points[n][0]-points[m][0])
    return res


def Neville_interpolation(points,find_point):
    res_mat = list(range(len(points)))
    for k in range(len(points)):
        res_mat[k] = list(range(len(points)))
    for i in range(len(points)):
        for j in range(i,len(points)):
            res_mat[i][j]=P(i,j,points,find_point)
            print("P", i, ",", j, "=", round(res_mat[i][j],4))
            if abs(res_mat[i][j]-res_mat[i][j-1])<0.0001:
                return round(res_mat[i][j],4)





main()