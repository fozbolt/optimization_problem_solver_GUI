import tkinter as tk
from pulp import *

fields = ('Broj studenata u domu', 'Broj subvencioniranih studenata', 'Broj studenata u menzi(dnevno)', 'Iznos pojedine subvencije',
          'Iznos pojedine stanarine', 'Broj obroka dnevno (po studentu)', 'Prodajna cijena obroka', 'Dani u mjesecu' , 'Cijena režija' , 'Cijena karte' ,
          'Postotak plaćenog prijevoza' , 'Nabavna cijena obroka (prosječna)' , 'Broj radnika' , 'Plaća radnika', 'Budzet')




def makeForm(root, fields):
    entries = {}
    #u komenarima su potrebni elementi kako bi naše ulazne varijable unaprijed bile popunjene, a trenutno je svaka ulazna varijabla stavljena na =0
    #popunjenaForma = [ 136, 200, 1000, 200, 750, 2, 40, 30, 10000, 150, 0.25, 20, 20, 5000, 500000,]
    #i=0

    for field in fields:
        #print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=27, text=field + ": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")  # popunjenaForma[i]
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=5,
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                 expand=tk.YES,
                 fill=tk.X)
        entries[field] = ent
        #i = i+1


    return entries





def lp(entries, child):
    #entries => inputs

    x1 = LpVariable("Zarada_doma_od_stanarine", None, None, LpContinuous)

    x2 = LpVariable("Mjesecni_profit_menze", None, None, LpContinuous)

    x3 = LpVariable("Ukupan_trosak_subvencije", None, None, LpContinuous)

    x4 = LpVariable("Rezije", None, None, LpContinuous)

    x5 = LpVariable("Ukupan_trosak_karata", None, None, LpContinuous)

    x6 = LpVariable("Mjesecna_nabavna_cijena_hrane", None, None, LpContinuous)

    x7 = LpVariable("Ukupan_trosak_na_place_radnika", None, None, LpContinuous)

    x8 = LpVariable("Maksimalan kapacitet doma", None, None, LpContinuous)

    prob = LpProblem("Studentski_dom", LpMinimize)

    prob += ((x1 + x2) - (x3 + x4 + x5 + x6 + x7)), "Funkcija_cilja"
    prob += ((x1 + x2 + (float(entries['Budzet'].get()))) - (x3 + x4 + x5 + x6 + x7)) == 0 , "Budzet"   # ((x1 + x2 +) - (x3 + x4 + x5 + x6 + x7)) >=  (float(entries['Budzet'].get())) ->> trošak ne smije biti veći od budžeta
    prob += x1 == (float(entries['Broj studenata u domu'].get())) * (float(entries['Iznos pojedine stanarine'].get())),  "Zarada od stanarine"
    prob += x2 >= ((float(entries['Broj obroka dnevno (po studentu)'].get())) * (float(entries['Dani u mjesecu'].get())) * (float(entries['Prodajna cijena obroka'].get())) * (float(entries['Broj studenata u menzi(dnevno)'].get()))) * 0.2,  "Minimalni mjesecni profit menze"
    prob += x3 >= (float(entries['Broj subvencioniranih studenata'].get())) * (float(entries['Iznos pojedine subvencije'].get())), "Minimalni trošak na subvencije"
    prob += x4 == (float(entries['Cijena režija'].get())), "Cijena režija"
    prob += x5 >= ((float(entries['Cijena karte'].get())) * (float(entries['Broj subvencioniranih studenata'].get()))) *(float(entries['Postotak plaćenog prijevoza'].get())),  "Minimalan mjesečni trošak na prijevoz"
    prob += x6 <= (float(entries['Dani u mjesecu'].get())) * (float(entries['Broj obroka dnevno (po studentu)'].get()))* (float(entries['Nabavna cijena obroka (prosječna)'].get())) * (float(entries['Broj studenata u menzi(dnevno)'].get())), "Maksimalni mjesečni nabavni trošak menze"  # uz uvjet da se svako jelo proda
    prob += x7 <= (float(entries['Broj radnika'].get())) * (float(entries['Plaća radnika'].get())),  "Maksimalan trošak na plaće radnika"
    prob += x8 <= (float(entries['Broj studenata u domu'].get())),   "Maksimalan kapacitet doma"



    prob.writeLP("test.lp")
    prob.solve()
    #print("Status:", LpStatus[prob.status])


    #izlazi / rješenje u novom prozoru

    row = tk.Frame(child)
    lab = tk.Label(row, width=27, text=" Status :  ", anchor='w')
    ent = tk.Entry(row)
    ent.insert(0, LpStatus[prob.status])
    row.pack(side=tk.TOP,
             fill=tk.X,
             padx=5,
             pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT,
             expand=tk.YES,
             fill=tk.X)

    for v in prob.variables():
        #print(v.name, "=", v.varValue)
        row = tk.Frame(child)
        lab = tk.Label(row, width=27, text=v.name + ": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, v.varValue)
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=5,
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                 expand=tk.YES,
                 fill=tk.X)

    row = tk.Frame(child)
    lab = tk.Label(row, width=27, text="Potroseno budzeta:  ", anchor='w')
    ent = tk.Entry(row)
    ent.insert(0,  value(prob.objective))
    row.pack(side=tk.TOP,
             fill=tk.X,
             padx=5,
             pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT,
             expand=tk.YES,
             fill=tk.X)

    #print(" Potroseno od budzeta : ", value(prob.objective))

def delete_inputs(inputs):
        pass   #nije dovrseno


def window(inputs):

    # izvor: https://pythonprogramming.altervista.org/tkinter-open-a-new-window-and-just-one/
    global child

    try:
        if child.state() == "normal": child.focus()
    except:
        child = tk.Toplevel()
        child.geometry("300x350")
        lp(inputs, child)  #Poziv funkcije za optimizaciju
        tk.Button(child, text="Quit", command=child.destroy).pack(fill=tk.BOTH, pady=(15,0))




if __name__ == '__main__':
    root = tk.Tk()
    root.title("Optimizer 3000")
    inputs = makeForm(root, fields) #kreiramo formu za ulazne varijable ...

    b1 = tk.Button(root, text='Solve', command=(lambda i=inputs: window(i)))
    b1.pack(side=tk.LEFT, padx=(75,5), pady=5)

    b2 = tk.Button(root, text='Delete inputs', command=(lambda i=inputs: delete_inputs(i)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()