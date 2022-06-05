import matplotlib 
import matplotlib.pyplot as plt
def main():
    rainfall = [102.6,83.1,72.9,53.1,31.1,8.4,6.9,5.2,7.1,37.2,62.3,98.4]
    x_coords = [10,20,30,40,50,60,70,80,90,100,110,120]
    y_coords = rainfall
    plt.title("Monthly Rainfall")
    plt.xlabel("Month")
    plt.ylabel("Rainfall-kg/m^3")
    plt.xticks([10,20,30,40,50,60,70,80,90,100,110,120],
               ["Jan","Feb","Mar","Apr","May","June","july","Aug","Sep","Oct","Nov","Dec"])
    plt.bar(x_coords,y_coords,5)
    plt.show()
main()
