import os

rootdir="."

studentids=["RCA0201NSZ", "RCA0202JIZ", "RCA0203NMZ", "RCA0204ZUR", "RCA0205HDV", "RCA0206AKB", "RCA0207RVY", "RCA0208ZAK", "RCA0209ZNK", "RCA0210GNU", "RCA0211ZXU", "RCA0212RKE", "RCA0213KKA", "RCA0214KTL", "RCA0215HDC", "RCA0216EBG", "RCA0217NVS", "RCA0218NKA", "RCA0219SJH", "RCA0220KYT", "RCA0221DMU", "RCA0222SIT", "RCA0223UTZ", "RCA0224AXZ", "RCA0225DYY", "RCA0226LDV", "RCA0227XIJ", "RCA0228MWW", "RCA0229WBR", "RCA0230BLW", "RCA0231RBI", "RCA0232LUJ", "RCA0233EAM", "RCA0234MGD", "RCA0235YGN", "RCA0236VGD", "RCA0237MBR", "RCA0238CWM", "RCA0239HRZ", "RCA0240TKU", "RCA0241RBM", "RCA0242YUV", "RCA0243HGY", "RCA0244DYI", "RCA0245PVK", "RCA0246HGK", "RCA0247BJW", "RCA0248GPB", "RCA0249PII", "RCA0250HTR", "RCA0251SKX", "RCA0252BUT", "RCA0253VCB", "RCA0254IRL", "RCA0255LYI", "RCA0256JIW", "RCA0257AIZ", "RCA0258DDA", "RCA0259TEE", "RCA0260EZE"]
studentnames=["Igirimpuhwe Aime", "Biziyaremye Henriette", "Burigo Aldo Jabes", "Bwiza Nina ", "Byiringiro Saad", "Dabagire Valens", "Dufitumukiza Emmanuel", "Dukunde Irakoze Acele Happy", "Dushime Grace Fidele", "Dushime Bill Benon", "Dushimimana Sandrine", "Gashugi Muhimpundu Adeline", "Gikundiro Larissa Teta", "Girishya Fiat Bruno", "Igihozo Marie Colombe", "Ihozo Marie Honnette", "Imanzi Yannick Kenny", "Impano Alliance", "Ineza Naillah", "Ineza Ange Michaella", "Ineza Jost Chance", "Iradukunda Clarisse", "Iradukunda Verite", "Irategeka Neza Bruce", "Ishimwe Teta Lena", "Isite Yves", "Itetero Ariane ", "Kalisa Belyse", "Kamala Fidele", "Karera Marvin", "Kayigire Ngabire Kethia", "Kayitare Audax", "Kunda Mugisha sarah", "Mfitumukiza Peter", "Mizero Eloi", "Mpano Christian", "Mudahemuka Manzi", "Muhire Patrick", "Muhoza Olivier Ivan", "Munganyinka Shakira ga", "Mutegetsi Prince", "Mwizera Amen Gisele", "Niyigena Tresor", "Niyigena Yves", "Nkubito Pacis", "Nshuti Jabes", "Ntagungira Ali Rashid", "Rugero Beulla", "Rutayisire Ange Belard", "Rwagapfizi Igor Roggy", "SETH ABIJURU", "Shumbusho David", "Shumbusho Ishimwe Anglebert", "Singizwa Nick", "Teta Butera Nelly", "Turinumugisha Souvenir", "Umuhoza Esther", "Umutoniwabo Hasbiyallah", "Uwamungu Gasaro Marie Leila", "Uwenayo Alain Pacifique"]
studentemails=["igaime@rca.ac.rw", "hopebiziyaremye@gmail.com", "burigoj2@gmail.com", "ninamyles2020@gmail.com", "byiringirosaad@gmail.com", "valensdabagire@gmail.com", "dufitumukizaemmanuel0@gmail.com", "acele4444@gmail.com", "gngrace10@gmail.com", "DushimeBillBenon@gmail.com", "sanrdushimimana@gmail.com", "aderlinecarmella@gmail.com", "tetalarissa69@gmail.com", "fiatbruno10@gmail.com", "igihozocolombe2003@gmail.com", "ihozohonnette12@gmail.com", "yanniimanzi@rca.ac.rw", "alliekook03@gmail.com", "NAILLAINEZA@gmail.com", "michaellaineza13@gmail.com", "jinezachance@gmail.com", "ciradukundaa@gmail.com", "veriteiradukunda14@gmail.com", "nezabruce@gmail.com", "tetalenaa@gmail.com", "yvesisite@gmail.com", "arianeitetero@gmail.com", "kalisabelyseteta", "0781792484", "kareramarvin14@gmail.com", "ketsukj@gmail.com", "kayitareauda@gmail.com", "mugishakundasarah@gmail.com", "mfitep6@gmail.com", "eloimizero324@gmail.com", "mpanoc6@gmail.com", "mudahemukamanzi@yahoo.com", "pmuhire@rca.ac.rw", "moikalasa12@gmail.com", "munganyinkashakira@.com", "0727190899", "mamengisele@gmail.com", "niyigenatreasure@gmail.com", "nives@rca.ac.rw", "pacisnkubito@gmail.com", "nshutij7", "ntagungiraali@gmail.com", "beullarugero7@gmail.com", "angebelard@gmail.com", "rwagapfiziroggy@gmail.com", "abiheloaf@gmail.com", "Davidshumbusho10@gmail.com", "anglebertsh@gmail.com", "singizwanick19@gmail.com", "buteranelly@gmail.com", "turinumuugishasouvenirgmail.com", "umuesther@yahoo.com", "shanessa@gmail.com", "gasaroleila2018@gmail.com", "uwenayoallain@gmail.com"]

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        student_folder = subdir.replace("./","").upper()
        filepath = subdir + os.sep + file
        if file.startswith("ntw-cat1.txt"):
            f=open(filepath)
            f1=open("answers-y2-networks-2021~2022-term1-cat1.txt","a")
            f1.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            f1.write("\n")
            f1.write(student_folder)
            f1.write("\n")
            for k in range(len(studentids)):
                if studentids[k]==student_folder:
                    f1.write(studentnames[k])
            f1.write("\n")
            f1.write("Marks:/10 ......")
            f1.write("\n\n")
            for line in f.readlines():
                f1.write(line)
            f1.write("\n")
            f.close()
            f1.close()
