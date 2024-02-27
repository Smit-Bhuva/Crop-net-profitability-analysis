import Calc
import Data
import Hort
import Food
import Cash
from matplotlib import pyplot as plt


Yield = Data.Y.copy()

print("Welcome!")

print("Select two crops which you want to compare(1 to 12) : \n"
      "1. Banana\n"
      "2. Potato\n"
      "3. Onion\n"
      "4. Ginger\n"
      "5. Rice\n"
      "6. Wheat\n"
      "7. Maize\n"
      "8. Bajra\n"
      "9. Tobacco\n"
      "10. Groundnut\n"
      "11. Cotton\n"
      "12. Sesame\n")

l = input("Enter the numbers of crop from above having space between (E.g. : 1 2) : ")
l = l.split(" ")
l2 = int(l[0])
l3 = int(l[1])

crop1 = Data.crops[l2-1]
crop2 = Data.crops[l3-1]

area = float(input("Enter your farm area in acre : "))

print("\nDo you want to use our data or you want to enter your data manually ?\n"
      "1. No, Use database data\n"
      "2. Yes, Enter data manually\n")

c = input("Enter your choice from above(1/2) : ")

choice = ("1", "2")

if c == choice[1]:
    print("You will need to enter following data per acre\n")

    # input cost
    inp_c = input("Input cost of both crops(seed+fertilizer+pesticide), put space between both number : ")
    x1 = inp_c.split(" ")
    x2 = int(x1[0])
    x3 = int(x1[1])

    # Inter-culture cost
    int_c = input("Inter-culture and tillage cost of both crops(including sowing), put space between both number : ")
    y1 = int_c.split(" ")
    y2 = int(y1[0])
    y3 = int(y1[1])

    # Irrigation cost
    irr = input("Input irrigation cost, put space between both number : ")
    z1 = irr.split(" ")
    z2 = int(z1[0])
    z3 = int(z1[1])

    # Harvesting cost
    har = input("Input harvesting cost, put space between both number : ")
    p1 = har.split(" ")
    p2 = int(p1[0])
    p3 = int(p1[1])

    # Other costs
    ot = input(" Input other remaining expenses than above entered costs for the crop, put space between both number : ")
    q1 = ot.split(" ")
    q2 = int(q1[0])
    q3 = int(q1[1])

    # Total cost per acre
    cr1 = x2+y2+z2+p2+q2
    cr2 = x3+y3+z3+p3+q3

    # crop 1
    avg_rt = float(Calc.avg_return(crop1))
    yt = Calc.return_per_acre(Yield[l2-1], avg_rt)
    print("Total cultivation cost of {} is {} per acre.\n".format(crop1, cr1))
    print("Average market price of {} is {} per Quintal\n".format(crop1, avg_rt))

    print("Hence, You will get Return per acre of {}".format(yt),
          "for {} crop.\n".format(crop1))

    print("And your net profit for {} crop will be {} per acre.\n".format(crop1, (yt-avg_rt)))

    print("Net profit for your total farm area is {}\n".format((yt-avg_rt)*area))

    # crop 2
    avg_rt2 = float(Calc.avg_return(crop2))
    yt2 = Calc.return_per_acre(Yield[l3 - 1], avg_rt2)
    print("Total cultivation cost of {} is {} per acre.\n".format(crop2, cr2))
    print("Average market price of {} is {} per Quintal\n".format(crop2, avg_rt2))

    print("Hence, You will get Return per acre of {}".format(yt2),
          "for {} crop.\n".format(crop2))

    print("And your net profit for {} crop will be {} per acre.\n".format(crop2, (yt2 - avg_rt2)))

    print("Net profit for your total farm area is {}\n".format((yt2 - avg_rt2) * area))


else:
    # Crop 1
    avg_rt3 = float(Calc.avg_return(crop1))
    yt3 = Calc.return_per_acre(Yield[l2-1], avg_rt3)
    print("Input cost of {} is {}\n".format(crop1, Data.Input_costs[l2-1]),
          "Tillage & Inter-culture cost of {} is {}\n".format(crop1, Data.Tillage_Interculture_cost[l2-1]),
          "Irrigation cost of {} is {}\n".format(crop1, Data.Irrigation_cost[l2-1]),
          "Harvesting cost of {} is {}\n".format(crop1, Data.Harvesting_Cost[l2-1]),
          "Other costs of {} is {}\n".format(crop1, Data.Other_costs[l2-1]))

    print("Hence, Total cultivation cost of {} is {} per acre.\n".format(crop1, Data.total_cost_list[l2-1]))

    print("\nAverage market price of {} is {} per Quintal\n".format(crop1, Calc.avg_return(crop1)))

    print("Hence, You will get Return per acre of {}".format(yt3),
          "for {} crop.\n".format(crop1))

    print("And your net profit for {} crop will be {} per acre.\n".format(crop1, (yt3 - avg_rt3)))

    print("Net profit for your total farm area is {}\n".format((yt3 - avg_rt3) * area))


    # Crop 2
    avg_rt4 = float(Calc.avg_return(crop2))
    yt4 = Calc.return_per_acre(Yield[l3 - 1], avg_rt4)
    print("Input cost of {} is {}\n".format(crop2, Data.Input_costs[l3 - 1]),
          "Tillage & Inter-culture cost of {} is {}\n".format(crop2, Data.Tillage_Interculture_cost[l3 - 1]),
          "Irrigation cost of {} is {}\n".format(crop2, Data.Irrigation_cost[l3 - 1]),
          "Harvesting cost of {} is {}\n".format(crop2, Data.Harvesting_Cost[l3 - 1]),
          "Other costs of {} is {}\n".format(crop2, Data.Other_costs[l3 - 1]))

    print("Hence, Total cultivation cost of {} is {} per acre.\n".format(crop2, Data.total_cost_list[l3-1]))

    print("\nAverage market price of {} is {} per Quintal\n".format(crop2, Calc.avg_return(crop2)))

    print("Hence, You will get Return per acre of {}".format(yt4),
          "for {} crop.\n".format(crop2))

    print("And your net profit for {} crop will be {} per acre.\n".format(crop2, (yt4 - avg_rt4)))

    print("Net profit for your total farm area is {}\n".format((yt4 - avg_rt4) * area))


# Visualization

# Plot for user input crops
avg_mar_pr = [Hort.banana_list, Hort.potato_list, Hort.onion_list, Hort.ginger_list,
              Food.year1, Food.year2, Food.year3, Food.year4,
              Cash.Tobacco_list, Cash.Groundnut_list, Cash.Cotton_list, Cash.Sesame_list]

x = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
y1 = avg_mar_pr[l2-1]
y2 = avg_mar_pr[l3-1]

plt.plot(x, y1, label="{}".format(crop1))
plt.plot(x, y2, label="{}".format(crop2))

plt.legend()
plt.xlabel("Years")
plt.ylabel("Average Market Prices")

plt.title("Price comparison for both crops")

plt.show()

# Plot for all crops
s1 = avg_mar_pr[0]
s2 = avg_mar_pr[1]
s3 = avg_mar_pr[2]
s4 = avg_mar_pr[3]
s5 = avg_mar_pr[4]
s6 = avg_mar_pr[5]
s7 = avg_mar_pr[6]
s8 = avg_mar_pr[7]
s9 = avg_mar_pr[8]
s10 = avg_mar_pr[9]
s11 = avg_mar_pr[10]
s12 = avg_mar_pr[11]

plt.plot(x, s1, label="Banana")
plt.plot(x, s2, label="Potato")
plt.plot(x, s3, label="Onion")
plt.plot(x, s4, label="Ginger")
plt.plot(x, s5, label="Rice")
plt.plot(x, s6, label="Wheat")
plt.plot(x, s7, label="Maize")
plt.plot(x, s8, label="Bajra")
plt.plot(x, s9, label="Tobacco")
plt.plot(x, s10, label="Groundnut")
plt.plot(x, s11, label="Cotton")
plt.plot(x, s12, label="Sesame")

plt.legend(loc='upper left', ncol=3)
plt.xlabel("Years")
plt.ylabel("Average Market Prices")

plt.title("Price trend for all crops")

plt.show()
