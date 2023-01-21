
furniture = ["Chair", "Table", "Drawer", "Stool", "Rack", "Bed","HeadBoard", "Sofa_bed", "Chess_table", "Tv_table"]

gadget = ["Mobile", "Television", "Charger", "Power_bank", "Laptop", "Earphone", "Ear_bud", "Watch", "Calculator", "Camera"]

#Replacing
for i in range(len(furniture)):
    furniture[i] = gadget[i]
print(furniture)

#printing furniture using for loop
for i in furniture:
    print(i)

#printing gadget using for loop
for i in gadget:
    print(i)



#Sort in descending order
furniture.sort(reverse=True)
print(furniture)

#Delete middle two items
del furniture[4]
del furniture[5]
print(furniture)

#college lists in ontario

college = ["Lambton college", "Humber college", "Seneca college", "George Brown college", "Mahawk college", "Georgian college", "St Clair college"
           "Sheridan College", "Conestoga college", "Loyalist college"]

#merging two list
mergerd_list = gadget+college
print(mergerd_list)