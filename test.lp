\* Studentski_dom *\
Minimize
Funkcija_cilja: - Mjesecna_nabavna_cijena_hrane + Mjesecni_profit_menze
 - Rezije - Ukupan_trosak_karata - Ukupan_trosak_na_place_radnika
 - Ukupan_trosak_subvencije + Zarada_doma_od_stanarine
Subject To
Budzet: - Mjesecna_nabavna_cijena_hrane + Mjesecni_profit_menze - Rezije
 - Ukupan_trosak_karata - Ukupan_trosak_na_place_radnika
 - Ukupan_trosak_subvencije + Zarada_doma_od_stanarine = 0
Cijena_režija: Rezije = 0
Maksimalan_kapacitet_doma: Maksimalan_kapacitet_doma <= 0
Maksimalan_trošak_na_plaæe_radnika: Ukupan_trosak_na_place_radnika <= 0
Maksimalni_mjeseèni_nabavni_trošak_menze: Mjesecna_nabavna_cijena_hrane <= 0
Minimalan_mjeseèni_trošak_na_prijevoz: Ukupan_trosak_karata >= 0
Minimalni_mjesecni_profit_menze: Mjesecni_profit_menze >= 0
Minimalni_trošak_na_subvencije: Ukupan_trosak_subvencije >= 0
Zarada_od_stanarine: Zarada_doma_od_stanarine = 0
Bounds
 Maksimalan_kapacitet_doma free
 Mjesecna_nabavna_cijena_hrane free
 Mjesecni_profit_menze free
 Rezije free
 Ukupan_trosak_karata free
 Ukupan_trosak_na_place_radnika free
 Ukupan_trosak_subvencije free
 Zarada_doma_od_stanarine free
End
