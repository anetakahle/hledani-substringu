# Kód:


string_ = "BARBARARB"
substring_ = "BARB"
dict_ = {}
dict2_ = {}


#pridame char:[indices] do dict_
for i in range(len(substring_)):
    if substring_[i] not in dict_.keys():
        dict_[substring_[i]] = [i]
    else:
        dict_[substring_[i]] += [i]

#prochazime seqenci, podivame se vzdy, za kolik nejvyse to muzeme napojit koncu
#prochazime indices pozadu, abychom nenavazovali na neco, co jsme prave pridali

for char in string_:
    if char in dict_:
        for pos in reversed(dict_[char]):
            if pos-1 in dict2_:
                if pos not in dict2_:
                    dict2_[pos] = dict2_[pos-1]
                else:
                    dict2_[pos] += dict2_[pos-1]
            if pos == 0:
                if pos not in dict2_:
                    dict2_[pos] = 1
                else:
                    dict2_[pos] += 1

print(dict2_[len(substring_)-1])




# Časová složitost:
# V prvním cyklu O(len(substring_))
# V druhém cyklu O(len(string_)*len(substring_))
