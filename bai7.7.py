tien_muon_doi = int(input("Nhap so tien muon doi: "))
print(f"So tien muon doi: {tien_muon_doi}")
so_to_1 = tien_muon_doi//500000
tien_con_lai = tien_muon_doi%500000
print(f"So to 500000: {so_to_1}")
so_to_2 = tien_muon_doi//200000
tien_con_lai = tien_muon_doi%200000
print(f"So to 200000: {so_to_2}")
so_to_3 = tien_muon_doi//100000
tien_con_lai = tien_muon_doi%100000
print(f"So to 100000: {so_to_3}")
so_to_4 = tien_muon_doi//50000
tien_con_lai = tien_muon_doi%50000
print(f"So to 50000: {so_to_4}")
print(f"So tien con lai: {tien_con_lai}")